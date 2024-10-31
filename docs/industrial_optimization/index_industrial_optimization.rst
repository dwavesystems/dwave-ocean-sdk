.. _index_industrial_optimization:

=======================
Industrial Optimization
=======================

.. toctree::
    :hidden:
    :maxdepth: 1

    opt_index_intro
    opt_index_nl
    opt_index_cqm
    opt_index_additional
    opt_index_using

.. sections-start-marker

Solve optimization problems using quantum-classical hybrid solvers in 
the Leap service's quantum cloud.

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_index_intro`

        Learn about optimizing with hybrid solvers.

    .. grid-item-card:: :ref:`opt_index_nl`

        Leap's hybrid nonlinear-program (NL) solver.

    .. grid-item-card:: :ref:`opt_index_cqm`

        Leap's hybrid constrained quadratic model (CQM) solver.

    .. grid-item-card:: :ref:`opt_index_additional`

        Additional hybrid solvers in Leap.

    .. grid-item-card:: :ref:`opt_index_using`

        Configuring hybrid parameters and usage best-practices.

.. sections-end-marker

Example
=======

The following code solves an illustrative 
`traveling-salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
using a quantum-classical hybrid solver in the |cloud_tm|_ quantum 
cloud service. 

>>> from dwave.optimization.generators import traveling_salesperson
>>> from dwave.system import LeapHybridNLSampler
...
>>> DISTANCE_MATRIX = [
...     [0, 656, 227, 578, 489],
...     [656, 0, 889, 141, 170],
...     [227, 889, 0, 773, 705],
...     [578, 141, 773, 0, 161],
...     [489, 170, 705, 161, 0]]
...
>>> model = traveling_salesperson(distance_matrix=DISTANCE_MATRIX)
>>> sampler = LeapHybridNLSampler()                  
>>> results = sampler.sample(
...     model,
...     label='SDK Examples - TSP')  	# doctest: +SKIP
