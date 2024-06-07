.. _example_nl_tsp:

=====================
Traveling Salesperson
=====================

This example demonstrates the use of a `Leap <https://cloud.dwavesys.com/leap/>`_
hybrid :ref:`nonlinear <nl_model_sdk>` solver on the renowned 
`traveling salesperson <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_ 
optimization problem. 

The goal of this problem is, for a given a list of cities and distances 
between each pair of cities, to find the shortest possible route that visits 
each city exactly once and returns to the city of origin. 

.. figure:: ../_images/problem_tsp.png
    :name: Problem_tsp
    :alt: image
    :align: center
    :scale: 60 %

    Traveling-salesperson problem.

Example Requirements
====================

.. include:: hybrid_solver_service.rst
	  :start-after: example-requirements-start-marker
	  :end-before: example-requirements-end-marker

Solution Steps
==============

.. include:: hybrid_solver_service.rst
  :start-after: example-steps-start-marker
  :end-before: example-steps-end-marker

This example formulates this problem as a :ref:`nonlinear model <nl_model_sdk>`
and uses the :class:`~dwave.system.samplers.LeapHybridNonlinearSampler` to find good
solutions.

Formulate the Problem
=====================

First, create a matrix of distances between all pairs of the problem's 
destinations. In real-world problems, such a matrix can be generated 
from an application with access to an online map. Here a matrix of approximate 
driving distances between five Italian cities is created with the following 
index order: 0: Rome, 1: Turin, 2: Naples, 3: Milan, and 4: Genoa.

>>> DISTANCE_MATRIX = 
...     [[0, 656, 227, 578, 489],
...      [656, 0, 889, 141, 170],
...      [227, 889, 0, 773, 705],
...      [578, 141, 773, 0, 161],
...      [489, 170, 705, 161, 0]]

For example, the distance between Turin (row 1) and Milan (column 3) is about 
141 kilometers. Note that such a distance matrix is symmetric because the 
distance between Rome to Turin is the same regardless of the direction of 
travel.

This example uses one of Ocean software's model generators to instantiate a 
:class:`dwave.optimization.Model` class for a traveling-salesperson problem. 
The :class:`dwave.optimization.Model` class encodes all the information 
(:term:`objective function`, constraints, constants, and decision variables) 
relevant to your models. 

>>> from dwave.optimization.generators import traveling_salesperson
>>> model = traveling_salesperson(distance_matrix=DISTANCE_MATRIX)

For detailed information on how the traveling-salesperson problem is modelled, 
see the documentation for the 
:class:`~dwave.optimization.generators.traveling_salesperson` generator. 
The :ref:`tsp_model_formulation_general` section provides a general description 
of one such model formulation. 

Solve the Problem by Sampling
=============================

D-Wave's quantum cloud service provides cloud-based
:std:doc:`hybrid solvers <sysdocs_gettingstarted:doc_leap_hybrid>` you can
submit quadratic and nonlinear models to. These solvers, which implement 
state-of-the-art classical algorithms together with intelligent allocation 
of the quantum processing unit (QPU) to parts of the problem where it benefits 
most, are designed to accommodate even very large problems. Leap's solvers can
relieve you of the burden of any current and future development and optimization
of hybrid algorithms that best solve your problem.

Ocean software's :doc:`dwave-system </docs_system/sdk_index>`
:class:`~dwave.system.samplers.LeapHybridNonlinearSampler` class enables you to
easily incorporate Leap's hybrid nonlinear solvers into your application:

>>> from dwave.system import LeapHybridNonlinearSampler
>>> sampler = LeapHybridNonlinearSampler()                  # doctest: +SKIP

Submit the model to the selected solver. 

>>> sampler.sample(model, time_limit=5)  	# doctest: +SKIP
>>> route, = , = model.iter_decisions()         # doctest: +SKIP
>>> print(route.state(0))                       # doctest: +SKIP
[3. 0. 2. 1. 4.]   

