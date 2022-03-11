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
   * - Tofu
     - 140
     - 17
     - 9
     - 3
     - 2
     - 2
     - 4.0
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
     - 30
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
...   'rice': {'Calories': 100, 'Protein': 3, 'Fat': 1, 'Carbs': 22, 'Fiber': 2,
...            'Taste': 7, 'Cost': 2.5},
...   'tofu': {'Calories': 140, 'Protein': 17, 'Fat': 9, 'Carbs': 3, 'Fiber': 2,
...            'Taste': 2, 'Cost': 4.0},
...   'banana': {'Calories': 90, 'Protein': 1, 'Fat': 0, 'Carbs': 23, 'Fiber': 3,
...              'Taste': 10, 'Cost': 1.0},
...   'lentils': {'Calories': 150, 'Protein': 9, 'Fat': 0, 'Carbs': 25, 'Fiber': 4,
...               'Taste': 3, 'Cost': 1.3},
...   'bread': {'Calories': 270, 'Protein': 9, 'Fat': 3, 'Carbs': 50, 'Fiber': 3,
...             'Taste': 5, 'Cost': 0.25},
...   'avocado': {'Calories': 300, 'Protein': 4, 'Fat': 30, 'Carbs': 20, 'Fiber': 14,
...               'Taste': 5, 'Cost': 2.0}}
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

Bounds on the range of values for non-binary variables shrink the solution
space the solver must search, so it is helpful to set such bounds; for many
problems, you can find bounds from your knowledge of the problem. In this case,
no food should be assigned a quantity that exceeds :code:`max_calories` by itself.

>>> for

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

Section :ref:`Tuning the Solution` belows shows how the priority weight was chosen.

Constraints
-----------

The problem has the following constraints:

1. Calories: no more than 2000
2. Protein: at least 50
3. Fat: at least 30
4. Carbs: at least 130
5. Fiber: at least 30

>>> cqm.add_constraint(total_mix(quantities, "Calories") <= max_calories, label="Calories")
'Calories'

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
>>> feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)

>>> def print_diet(sampleset):
...    feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)
...    if len(feasible_sampleset):
...       best = feasible_sampleset.first.sample
...       print({food: round(quantity) for food, quantity in best.items()})
...       for constraint in cqm.iter_constraint_data(feasible_sampleset.first.sample):
...          print(f"{constraint.label} (nominal: {constraint.rhs_energy}): {round(constraint.lhs_energy)}")
...   else:
...      print("No good solutions found.")

>>> print_diet(sampleset)
{'avocado': 1, 'banana': 0, 'bread': 7, 'lentils': 0, 'rice': 0, 'tofu': 0}
Calories (nominal: 2000): 2000
Protein (nominal: 50): 62
Fat (nominal: 30): 42
Carbs (nominal: 130): 344
Fiber (nominal: 30): 30

You can see how successful the solution is for the optimized items:

>>> def total_item(sample, category):
...   return sum(foods[food][category] * amount for food, amount in sample.items())

>>> print(f'Total taste of {round(total_item(best, "Taste"))} at cost {round(total_item(best, "Cost"))}')
Total taste of 37 at cost 3

Tuning the Solution
===================

A simple method to attain good priority weights, is to sample each objective on
its own and use the energy of the best sample as representing its weight also in
the combined objective.

Start with enjoyment:

>>> cqm.set_objective(-total_mix(quantities, "Taste"))
>>> sampleset_taste = sampler.sample_cqm(cqm)
>>> feasible_sampleset_taste = sampleset_taste.filter(lambda row: row.is_feasible)
>>> if len(feasible_sampleset_taste):
...   print(round(feasible_sampleset_taste.first.energy))
-185

>>> print_diet(sampleset_taste)
{'avocado': 0, 'banana': 18, 'bread': 0, 'lentils': 0, 'rice': 0, 'tofu': 2}
Calories (nominal: 2000): 2000
Protein (nominal: 50): 50
Fat (nominal: 30): 30
Carbs (nominal: 130): 426
Fiber (nominal: 30): 64

>>> best_taste = feasible_sampleset_taste.first.sample
>>> print(f'Total taste of {round(total_item(best_taste, "Taste"))} at cost '
...       f'{round(total_item(best_taste, "Cost"))}')
Total taste of 185 at cost 26

You can see that this diet is high in bananas, the tastiest food, and makes up
for that food's low levels of protein and fat with tofu.

Next, for cost:

>>> cqm.set_objective(total_mix(quantities, "Cost"))
>>> sampleset_cost = sampler.sample_cqm(cqm)
>>> feasible_sampleset_cost = sampleset_cost.filter(lambda row: row.is_feasible)
>>> if len(feasible_sampleset_cost):
...   print(round(feasible_sampleset_cost.first.energy))
3

>>> print_diet(sampleset_cost)
{'avocado': 1, 'banana': 0, 'bread': 7, 'lentils': 0, 'rice': 0, 'tofu': 0}
Calories (nominal: 2000): 2000
Protein (nominal: 50): 62
Fat (nominal: 30): 42
Carbs (nominal: 130): 344
Fiber (nominal: 30): 30

>>> best_cost = feasible_sampleset_cost.first.sample
>>> print(f'Total taste of {round(total_item(best_cost, "Taste"))} at cost '
...       f'{round(total_item(best_cost, "Cost"))}')
Total taste of 37 at cost 3

This diet is ranked as less tasty than the previous but much cheaper. It relies
mainly on bread and uses avocado to add fat and fiber.

To give each a similar weighting in the combined objective, the
:ref:`Objective Function` section above multiplied the objective that minimizes
cost by a factor of :math:`185/3 \approx 60`.
