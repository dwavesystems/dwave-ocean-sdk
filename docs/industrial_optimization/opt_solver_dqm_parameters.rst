.. _opt_solver_dqm_parameters:

=====================
DQM Solver Parameters
=====================

This section describes the properties of quantum-classical hybrid
:ref:`discrete quadratic model <concept_models_dqm>` solvers such as the Leap
service's ``hybrid_discrete_quadratic_model_version1``. For the parameters
you can configure, see the :ref:`opt_solver_dqm_parameters` section.

.. _parameter_dqm_dqm:

dqm
===

Ocean software's :class:`dimod.DiscreteQuadraticModel` class contains linear and
quadratic biases for problems formulated as
:ref:`discrete binary models <concept_models_dqm>` as well as additional
information such as variable labels.

Relevant Properties
-------------------

*   :ref:`property_dqm_maximum_number_of_variables` defines the maximum number
    of problem variables.
*   :ref:`property_dqm_maximum_number_of_biases` defines the maximum number of
    problem biases.
*   :ref:`property_dqm_minimum_time_limit` and
    :ref:`property_dqm_maximum_time_limit_hrs` define the runtime duration for
    hybrid solvers.

Example
-------

This example submits a small, illustrative problem---a game of
rock-paper-scissors---to Ocean software's
:class:`~dwave.system.samplers.LeapHybridDQMSampler`.

>>> import dimod
>>> from dwave.system import LeapHybridDQMSampler
...
>>> cases = ["rock", "paper", "scissors"]
>>> win = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
...
>>> dqm = dimod.DiscreteQuadraticModel()
>>> dqm.add_variable(3, label='my_hand')    # doctest: +IGNORE_RESULT
>>> dqm.add_variable(3, label='their_hand') # doctest: +IGNORE_RESULT
>>> for my_idx, my_case in enumerate(cases):
...    for their_idx, their_case in enumerate(cases):
...       if win[my_case] == their_case:
...          dqm.set_quadratic('my_hand', 'their_hand',
...                            {(my_idx, their_idx): -1})
...       if win[their_case] == my_case:
...          dqm.set_quadratic('my_hand', 'their_hand',
...                            {(my_idx, their_idx): 1})
...
>>> dqm_sampler = LeapHybridDQMSampler()      # doctest: +SKIP
>>> sampleset = dqm_sampler.sample_dqm(
...     dqm,
...     time_limit=10,
...     label="Rock-paper-scissors DQM example")   # doctest: +SKIP


.. _parameter_dqm_label:

label
=====

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_label
    :end-before: end_parameter_label

Example
-------

The example in the :ref:`parameter_dqm_dqm` section above sets the
:ref:`parameter_dqm_label` property.

.. figure:: ../_images/leap_problem_label.png
    :align: center
    :name: LeapProblemLabelDqm
    :alt: Problem labels on dashboard.
    :height: 200 pt
    :width: 400 pt

    Problem labels on the dashboard.


.. _parameter_dqm_time_limit:

time_limit
==========

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_time_limit
    :end-before: end_parameter_time_limit

Relevant Properties
-------------------

*   :ref:`property_dqm_minimum_time_limit` defines the range of supported values
    for a given DQM.

Example
-------

The example in the :ref:`parameter_dqm_dqm` section above sets the
:ref:`parameter_dqm_time_limit` property.
