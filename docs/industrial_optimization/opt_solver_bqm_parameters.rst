.. _opt_solver_bqm_parameters:

=====================
BQM Solver Parameters
=====================

This section describes the properties of quantum-classical hybrid
:ref:`binary quadratic model <concept_models_bqm>` solvers such as the Leap
service's ``hybrid_binary_quadratic_model_version2``. For the parameters
you can configure, see the :ref:`opt_solver_bqm_parameters` section.

.. _parameter_bqm_bqm:

bqm
===

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_bqm
    :end-before: end_parameter_bqm

Relevant Properties
-------------------

*   :ref:`property_bqm_maximum_number_of_variables` defines the maximum number
    of problem
    variables for hybrid solvers.
*   :ref:`property_bqm_maximum_number_of_biases` defines the maximum number of
    problem biases for hybrid solvers.
*   :ref:`property_bqm_minimum_time_limit` and 
    :ref:`property_bqm_maximum_time_limit_hrs` define the runtime duration for
    hybrid solvers.

Example
-------

This illustrative example submits a BQM created from a QUBO to a hybrid BQM solver.

>>> from dwave.system import LeapHybridBQMSampler
...
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> bqm = dimod.BQM.from_qubo(Q)
>>> sampleset = LeapHybridBQMSampler().sample(bqm)  # doctest: +SKIP


.. _parameter_bqm_h:

h
=

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_h
    :end-before: end_parameter_h

Relevant Properties
-------------------

*   :ref:`property_bqm_maximum_number_of_variables` defines the maximum number of problem
    variables for hybrid solvers.
*   :ref:`property_bqm_maximum_number_of_biases` defines the maximum number of problem
    biases for hybrid solvers.

Example
-------

This example sets linear and quadratic biases for a simple Ising problem.

>>> from dwave.system import LeapHybridBQMSampler
...
>>> h = {'a': 1, 'b': -1}
>>> J = {('a', 'b'): -1}
>>> sampleset = LeapHybridBQMSampler().sample_ising(h, J)   # doctest: +SKIP


.. _parameter_bqm_j:

J
=

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_j
    :end-before: end_parameter_j

Relevant Properties
-------------------

*   :ref:`property_bqm_maximum_number_of_variables` defines the maximum number
    of problem variables for hybrid solvers.
*   :ref:`property_bqm_maximum_number_of_biases` defines the maximum number of
    problem biases for hybrid solvers.

Example
-------

This example sets linear and quadratic biases for a simple Ising problem.

>>> from dwave.system import LeapHybridBQMSampler
...
>>> h = {'a': 1, 'b': -1}
>>> J = {('a', 'b'): -1}
>>> sampleset = LeapHybridBQMSampler().sample_ising(h, J)   # doctest: +SKIP


.. _parameter_bqm_label:

label
=====

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_label
    :end-before: end_parameter_label

Example
-------

This illustrative example sets a label on a submitted problem.

>>> from dwave.system import LeapHybridBQMSampler
...
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> bqm = dimod.BQM.from_qubo(Q)
>>> sampleset = LeapHybridBQMSampler().sample(
...     bqm,
...     label="Simple example")  # doctest: +SKIP

.. figure:: ../_images/leap_problem_label.png
    :align: center
    :name: LeapProblemLabelBqm
    :alt: Problem labels on dashboard.
    :height: 200 pt
    :width: 400 pt

    Problem labels on the dashboard.


.. _parameter_bqm_q:

Q
=

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_q
    :end-before: end_parameter_q

Relevant Properties
-------------------

*   :ref:`property_bqm_maximum_number_of_variables` defines the maximum number
    of problem variables for hybrid solvers.
*   :ref:`property_bqm_maximum_number_of_biases` defines the maximum number of
    problem biases for hybrid solvers.

Example
-------

This example submits a QUBO to a QPU solver.

>>> from dwave.system import LeapHybridBQMSampler
...
>>> Q = {(0, 0): -3, (1, 1): -1, (0, 1): 2, (2, 2): -1, (0, 2): 2}
>>> sampleset = LeapHybridBQMSampler().sample_qubo(Q) # doctest: +SKIP


.. _parameter_bqm_time_limit:

time_limit
==========

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_time_limit
    :end-before: end_parameter_time_limit

Relevant Properties
-------------------

*   :ref:`property_bqm_minimum_time_limit` defines the range of supported
    values for a given BQM.

Example
-------

This illustrative example configures a time limit of 6 seconds.

>>> from dwave.system import LeapHybridBQMSampler
...
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> sampleset = LeapHybridBQMSampler().sample_qubo(
...     Q,
...     time_limit=6) # doctest: +SKIP
   
