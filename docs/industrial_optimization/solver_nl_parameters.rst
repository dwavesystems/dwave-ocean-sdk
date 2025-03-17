.. _opt_solver_nl_parameters:

===========================
Nonlinear Solver Parameters
===========================

This section describes the parameters of quantum-classical hybrid
:ref:`nonlinear-model <concept_models_nonlinear>` solvers such as the Leap
service's ``hybrid_nonlinear_program_version1``. For the properties that
inform and restrict your use of the solver, see the
:ref:`opt_solver_nl_properties` section.

.. _parameter_nl_label:

label
=====

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_label
    :end-before: end_parameter_label

Example
-------

This example sets a label on a submitted problem.

>>> from dwave.optimization.generators import bin_packing
>>> from dwave.system import LeapHybridNLSampler
...
>>> model = bin_packing([3, 5, 1, 3], 7)
>>> results = LeapHybridNLSampler().sample(model)    # doctest: +SKIP

.. figure:: ../_images/leap_problem_label.png
    :align: center
    :name: LeapProblemLabelNl
    :alt: Problem labels on dashboard.
    :height: 200 pt
    :width: 400 pt

    Problem labels on the dashboard.


.. _parameter_nl_model:

model
=====

Ocean software's :class:`~dwave.optimization.model.Model` contains symbols
and states for problems formulated as a
:ref:`nonlinear model <concept_models_nonlinear>`.

Relevant Properties
-------------------

*   :ref:`property_nl_maximum_time_limit_hrs` defines the maximum runtime for
    problems submitted to the solver.
*   :ref:`property_nl_maximum_decision_state_size` defines the maximum size of
    all decision-variable states in a problem accepted by the solver.
*   :ref:`property_nl_maximum_number_of_nodes` defines the maximum number of
    nodes in a problem accepted by the solver.
*   :ref:`property_nl_maximum_number_of_states` defines the maximum number of
    initialized states in a problem accepted by the solver.
*   :ref:`property_nl_max_state_size` defines the maximum size of all states
    in a problem accepted by the solver.
*   :ref:`property_nl_state_size_multiplier`,
    :ref:`property_nl_num_nodes_multiplier`,
    :ref:`property_nl_num_nodes_state_size_multiplier`, and
    :ref:`property_nl_time_constant` are used in the internal estimate of the
    problem's minimum runtime.

Example
-------

This example creates a nonlinear model representing a flow-shop-scheduling
problem with processing times for two jobs, each on three machines.

>>> from dwave.optimization.generators import flow_shop_scheduling
...
>>> processing_times = [[10, 5, 7], [20, 10, 15]]
>>> model = flow_shop_scheduling(processing_times=processing_times)


.. _parameter_nl_time_limit:

time_limit
==========

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_time_limit
    :end-before: end_parameter_time_limit

.. attention::
    The Leap service's hybrid nonlinear-program solver does not prevent you
    from setting a :ref:`parameter_nl_time_limit` smaller than the minimum time
    estimated by Ocean software's
    :meth:`~dwave.system.samplers.LeapHybridNLSampler.estimated_min_time_limit`
    method in the
    :class:`sampler's <oceandocs:dwave.system.samplers.LeapHybridNLSampler>`
    class; however, runtime (and charge time) is not guaranteed to be shorter
    than the estimated time.

Relevant Properties
-------------------

*   :ref:`property_nl_state_size_multiplier`,
    :ref:`property_nl_num_nodes_multiplier`,
    :ref:`property_nl_num_nodes_state_size_multiplier`, and
    :ref:`property_nl_time_constant` are used in the internal estimate of the
    problem's minimum runtime.

Example
-------

This illustrative example configures a time limit of 6 seconds.

>>> from dwave.optimization.generators import flow_shop_scheduling
...
>>> processing_times = [[10, 5, 7], [20, 10, 15]]
>>> model = flow_shop_scheduling(processing_times=processing_times)
>>> results = LeapHybridNLSampler().sample(
...     model,
...     time_limit=6)   # doctest: +SKIP
