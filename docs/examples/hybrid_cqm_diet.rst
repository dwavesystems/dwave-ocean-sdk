.. _example_cqm_diet_reals:

=============
Diet Planning
=============

This example solves a simple linear-programming type of problem, optimizing a
diet with requirements that can be expressed with a linear objective and constraints,
to demonstrate using a `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid
:term:`CQM` solver on a constrained problem with real-valued variables.

The goal of this problem is to optimize the enjoyment of a diet's foods while
consuming sufficient quantities of macro-nutrients but not excessive calories.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described
  in :ref:`sapi_access`.
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>` and
  :doc:`dimod </docs_dimod/sdk_index>`.

	.. include:: hybrid_solver_service.rst
	  :start-after: example-requirements-start-marker
	  :end-before: example-requirements-end-marker

Solution Steps
==============

.. include:: hybrid_solver_service.rst
  :start-after: example-steps-start-marker
  :end-before: example-steps-end-marker

This example formulates this problem as a :ref:`constrained quadratic model <cqm_sdk>`
and uses the :class:`~dwave.system.samplers.LeapHybridCQMSampler` to find good
solutions.

Formulate the Problem
=====================

The table below shows a selection of foods chosen by a dieter, with associated
(not necessarily realistic) evaluations of nutrients and cost, and ranked for
the dieter's enjoyment on a scale of one to ten.

.. list-table:: Nutrients, Cost, and Enjoyment Rankings for Available Foods
   :header-rows: 1

   * - **Food**
     - **Calories**
     - **Protein**
     - **Fat**
     - **Carbs**
     - **Fiber**
     - **Taste**
     - **Cost**
   * - Rice
     - 100
     - 3
     - 1
     - 22
     - 2
     - 7
     - 2.50
   * - Bananas
     - 90
     - 1
     - 0
     - 23
     - 3
     - 10
     - 1.0
   * - Lentils
     - 150
     - 9
     - 0
     - 25
     - 4
     - 3
     - 1.30
   * - Bread
     - 270
     - 9
     - 3
     - 50
     - 3
     - 5
     - 0.25
   * - Avocado
     - 300
     - 4
     - 3
     - 20
     - 14
     - 5
     - 2.00

The following table shows the dieter's daily requirements for a few selected
nutrients.

.. list-table:: Daily Required Nutrients
   :header-rows: 1

   * - **Nutrient**
     - **Calories**
     - **Protein**
     - **Fat**
     - **Carbs**
     - **Fiber**
   * - **Daily Requirement**
     - 2000
     - 50
     - 30
     - 130
     - 30

For simplicity, store the contents of the two tables above as dicts:

>>> foods = {
...   'Food': {0: 'rice', 1: 'tofu', 2: 'banana', 3: 'lentils', 4: 'bread', 5: 'avocado'},
...   'Calories': {0: 100, 1: 140, 2: 90, 3: 150, 4: 270, 5: 300},
...   'Protein': {0: 3, 1: 17, 2: 1, 3: 9, 4: 9, 5: 4},
...   'Fat': {0: 1, 1: 9, 2: 0, 3: 0, 4: 3, 5: 30},
...   'Carbs': {0: 22, 1: 3, 2: 23, 3: 25, 4: 50, 5: 20},
...   'Fiber': {0: 2, 1: 2, 2: 3, 3: 4, 4: 3, 5: 14},
...   'Taste': {0: 7, 1: 2, 2: 10, 3: 3, 4: 5, 5: 5},
...   'Cost': {0: 2.5, 1: 4.0, 2: 1.0, 3: 1.3, 4: 0.25, 5: 2.0}}
...
>>> min_nutrients = {"Protein": 50, "Fat": 30, "Carbs": 130, "Fiber": 30}
>>> max_calories = 2000

Instantiate a CQM.

>>> from dimod import ConstrainedQuadraticModel
>>> cqm = ConstrainedQuadraticModel()

You can now formulate an :term:`objective function` to optimize and constraints
any feasible solution must meet, and set these in your CQM.

Objective Function
------------------

The objective function to maximize enjoyment of the diet's foods while minimizing
the purchase cost.

Instantiate some real variables\ [#]_, :code:`quantities`, to select quantities
of every available food.

>>> quantities = [dimod.Real(f"{food}") for food in foods["Food"].values()]

Bounds on the range of values for non-binary variables shrink the solution
space the solver must search, so it is helpful to set such bounds; for many
problems, you can find bounds from your knowledge of the problem. In this case,

To maximize enjoyment and minimize cost is to assign values to the variable that
represents quantities of each food, :math:`q_i`, such that when multiplied by
coefficients representing the cost, :math:`c_i`, or taste, :math:`t_i`,
of each food, form the linear terms of the following summations to be optimized:

.. math::

	\min \sum_i q_i c_i

  \max \sum_i q_i t_i

To optimizes two different objectives, enjoyment and cost, requires weighing one
against the other. A simple way to do this, is to set priority weights; for example,

.. math::

	\text{objective} = \alpha \text{(objective 1)} + \beta \text{(objective 2)}

By setting, for example :math:`\alpha=2, \beta=1`, you double the priority of the
first objective compared to the second.

You can define a utility function, :code:`total_mix`, to calculate the summations
for any given category in the

>>> def total_mix(quantity, category):
...   return sum(q * c for q, c in zip(quantity, foods[category].values()))

Set the objective. Because Ocean solvers minimize objectives, to maximize enjoyment,
:code:`Taste` is multiplied by `-1` and minimized.

>>> cqm.set_objective(-total_mix(quantities, "Taste") + 60*total_mix(quantities, "Cost"))

Section ??? belows shows how the priority weight was chosen. 

.. [#]

   Always keep in mind that such "variables" are actually
   class :class:`~dimod.QuadraticModel` objects,

   >>> bin_used[0]
   BinaryQuadraticModel({'bin_used_0': 1.0}, {}, 0.0, 'BINARY')

   with a single variable with the requested label, :code:`bin_used_<j>`. This
   means, for example, that multiplying by two doubles the linear bias,

   >>> 2*bin_used[0]
   BinaryQuadraticModel({'bin_used_0': 2.0}, {}, 0.0, 'BINARY')

   multiplying two such "variables" creates a quadratic bias,

   >>> bin_used[0]*bin_used[1]          # doctest: +SKIP
   BinaryQuadraticModel({'bin_used_0': 0.0, 'bin_used_1': 0.0},
   ...                  {('bin_used_1', 'bin_used_0'): 1.0}, 0.0, 'BINARY')

   but multiplying three binary quadratic models requires a non-quadratic term
   and so :code:`bin_used[0]*bin_used[1]*bin_used[2]` cannot generate a binary
   quadratic model and results in an error.


Constraints
-----------

The problem has the following constraints:

1. Calories: no more than 2000
2. Protein: at least 50
3. Fat: at least 30
4. Carbs: at least 130
5. Fiber: at least 30

>>> for nutrient, amount in min_nutrients.items():
...   cqm.add_constraint(total_mix(quantities, nutrient) >= amount, label=nutrient)

You can access these constraints as a dict with the labels as keys:

>>> list(cqm.constraints.keys())
['Calories', 'Protein', 'Fat', 'Carbs', 'Fiber']

Solve the Problem by Sampling
=============================

Instantiate a :class:`~dwave.system.samplers.LeapHybridCQMSampler` class
sampler,

>>> from dwave.system import LeapHybridCQMSampler
>>> sampler = LeapHybridCQMSampler()

>>> sampleset = sampler.sample_cqm(cqm)

>>> print({food: round(quantity) for food, quantity in sampleset.first.sample.items()})
{'avocado': 1, 'banana': 0, 'bread': 7, 'lentils': 0, 'rice': 0, 'tofu': 0}
