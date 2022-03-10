.. _example_cqm_diet_reals:

=======================
Linear-Programming Diet
=======================

This example

The goal of this problem is to find the optimal number .

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



.. list-table:: Foods
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


First, define the

>>> diet= {'Food': {0: 'rice',
  1: 'tofu',
  2: 'banana',
  3: 'lentils',
  4: 'bread',
  5: 'avocado'},
 'Calories': {0: 100, 1: 140, 2: 90, 3: 150, 4: 270, 5: 300},
 'Protein': {0: 3, 1: 17, 2: 1, 3: 9, 4: 9, 5: 4},
 'Fat': {0: 1, 1: 9, 2: 0, 3: 0, 4: 3, 5: 30},
 'Carb': {0: 22, 1: 3, 2: 23, 3: 25, 4: 50, 5: 20},
 'Fiber': {0: 2, 1: 2, 2: 3, 3: 4, 4: 3, 5: 14},
 'Enjoyment': {0: 7, 1: 2, 2: 10, 3: 3, 4: 5, 5: 5},
 'Cost': {0: 2.5, 1: 4.0, 2: 1.0, 3: 1.3, 4: 0.25, 5: 2.0}}

>>> quantity = [dimod.Real(f"{name}") for name in diet["Food"].values()]

>>> def total_nutrient(quantity, nutrient):
...   return sum(q * c for q, c in zip(quantity, diet[nutrient].values()))


Instantiate a CQM.

>>> from dimod import ConstrainedQuadraticModel
>>> cqm = ConstrainedQuadraticModel()

You can now formulate an :term:`objective function` to optimize and constraints
any feasible solution must meet, and set these in your CQM.


Objective Function
------------------

The objective function to maximize

Bounds on the range of values for integer variables shrink the solution
space the solver must search, so it is helpful to set such bounds; for many
problems, you can find bounds from your knowledge of the problem. In this case,

* O


>>> from dimod import Real
>>>



>>> cqm.set_objective(-total_nutrient(quantity, "Enjoyment"))

.. note::

   As noted in the :ref:`example_cqm_binpacking` example, keep in mind that
   these "variables" are actually class :class:`dimod.QuadraticModel` objects,

   >>> price[0]
   QuadraticModel({'p_0': 1.0}, {}, 0.0, {'p_0': 'INTEGER'}, dtype='float64')

   with a single variable with the requested label, :code:`p_0` or :code:`s_0`.
   This means, for example, that multiplying these models to create a
   :code:`revenue[0]` "variable" actually creates a new quadratic model,

   >>> revenue[0]                               # doctest: +SKIP
   QuadraticModel({'s_0': 0.0, 'p_0': 0.0},
   ...            {('p_0', 's_0'): 1.0},
   ...            0.0,
   ...            {'s_0': 'INTEGER', 'p_0': 'INTEGER'}, dtype='float64')

   with a quadratic bias between :code:`p_0` and :code:`s_0`.

Constraints
-----------

The problem has the following constraints:

1. In t.

>>> cqm.add_constraint(
'Swn'


>>> len(cqm.constraints)
11

Solve the Problem by Sampling
=============================

Instantiate a :class:`~dwave.system.samplers.LeapHybridCQMSampler` class
sampler,



import dimod

quantity = [dimod.Real(f"{name}") for name in diet["Food"].values()]

def total_nutrient(quantity, nutrient):
   return sum(q * c for q, c in zip(quantity, diet[nutrient].values()))


cqm = dimod.ConstrainedQuadraticModel()

cqm.set_objective(-total_nutrient(quantity, "Enjoyment"))

required_nutrients = {"Protein": 50, "Fat": 30, "Carb": 130, "Fiber": 30}

cqm.add_constraint(total_nutrient(quantity, "Calories") <= 2000, label="Calories")

for nutrient, ammount in required_nutrients.items():
   cqm.add_constraint(total_nutrient(quantity, nutrient) >= ammount, label=nutrient)
