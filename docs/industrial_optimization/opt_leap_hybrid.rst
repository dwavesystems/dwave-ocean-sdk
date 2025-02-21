.. _opt_leap_hybrid:

=============================
Leap Service's Hybrid Solvers
=============================

This section introduces the |cloud_tm|_ service's quantum-classical
:term:`hybrid` :term:`solvers <solver>` and provides references to usage
information.

.. note::
    Not all accounts have access to this type of solver.

.. _opt_leap_hybrid_supported_solvers:

Supported Solvers
=================

.. include:: ../shared/hybrid.rst
    :start-after: start_leap_intro
    :end-before: end_leap_intro

.. include:: ../shared/hybrid.rst
    :start-after: start_generally_available_solvers
    :end-before: end_generally_available_solvers

.. _opt_leap_hybrid_properties_params:

Solver Properties and Parameters
================================

The following table provides links to documentation for the properties and
parameters of the hybrid solvers in the Leap service.

.. list-table:: Hybrid Solver Properties and Parameters
    :header-rows: 1

    *   -   **Solver for Model**
        -   **Properties**
        -   **Parameters**
    *   -   :ref:`Nonlinear models <concept_models_nonlinear>`
        -   :ref:`opt_solver_nl_properties`
        -   :ref:`opt_solver_nl_parameters`
    *   -   :ref:`Constrained quadratic models <concept_models_cqm>`
        -   :ref:`opt_solver_cqm_properties`
        -   :ref:`opt_solver_cqm_parameters`
    *   -   :ref:`Constrained quadratic models <concept_models_bqm>`
        -   :ref:`opt_solver_bqm_properties`
        -   :ref:`opt_solver_bqm_parameters`
    *   -   :ref:`Nonlinear models <concept_models_dqm>`
        -   :ref:`opt_solver_dqm_properties`
        -   :ref:`opt_solver_dqm_parameters`

.. _opt_leap_hybrid_timing:

Solver Timing
=============

The table below lists the timing information returned from quantum-classical
hybrid solvers in the |cloud|_ service.

.. tabularcolumns:: |p{3cm}|p{10cm}|

.. table:: Timing Information from Hybrid Solvers

    =================== ========================================================
    Field               Meaning
    =================== ========================================================
    *run_time*          Time, in microseconds, the hybrid solver spent
                        working on the problem.
    *charge_time*       Time, in microseconds, charged to the account.\ [#]_
    *qpu_access_time*   QPU time, in microseconds, used by the hybrid
                        solver.\ [#]_
    =================== ========================================================

.. [#]
    *charge_time* and *run_time* may differ due to the time granularity
    of the solver. For example, if a hybrid solver has a time granularity
    of 0.5 sec and your submission specifies 4.7 sec, *run_time* might be 5 sec
    and *charge_time* 4.5 sec.

.. [#]
    *qpu_access_time* might be zero for submissions with short *run_time*.
    Because the QPU is a shared, remote resource, the first set of samples
    from the QPU might not be received before a short explicitly-specified
    or default *time_limit* is reached. In such cases, the hybrid solver
    respects the time limitation and returns without the QPU having a chance
    to contribute to the solution. On the large, complex problems for which
    hybrid solvers are intended, this is unlikely to occur.

You can access this information via the :ref:`dimod <index_dimod>`
:class:`~dimod.SampleSet` class, as in the example below.

>>> import dimod
>>> from dwave.system import LeapHybridSampler
...
>>> sampler = LeapHybridSampler(solver={'category': 'hybrid'})
>>> bqm = dimod.generators.ran_r(1, 300)
>>> sampleset = sampler.sample(bqm)
>>> sampleset.info     # doctest: +SKIP
{'qpu_access_time': 41990, 'charge_time': 2991424, 'run_time': 2991424}

.. _leap_hybrid_usage_charges:

Solver Usage Charges
====================

|dwave_short| charges you for time that solvers run your problems,
with rates depending on QPU usage. You can see the rate at which
your account's quota is consumed for a particular solver in the solver's
``property_quota_rate`` property; for example,
:ref:`property_nl_quota_conversion_rate` for the nonlinear solver.

You can see the time you are charged for in the responses returned for your
submitted problems. The relevant field in the response is :code:`'charge_time'`.
The example in the :ref:`opt_leap_hybrid_timing` section shows
:code:`'charge_time': 2991424'` in the returned response, meaning almost 3
seconds are being charged.

Instantiating the needed compute resources for your problem can introduce
a delay before the problem is processed. This delay tends to be small compared
to the overall solution time for large problems. The *charge_time*
does not include this delay.

Usage Examples
==============

Use a hybrid solver as you would any Ocean SDK sampler. For example,
given a 1000-variable problem formulated as a quadratic unconstrained binary
optimization (QUBO) model, :math:`Q`, you can submit it for solution
to a hybrid BQM solver as follows:

.. code-block:: python

    from dwave.system import LeapHybridSampler

    # Select a solver
    sampler = LeapHybridSampler()

    # Submit for solution
    answer = sampler.sample_qubo(Q)

You can find more usage examples here:

*   :ref:`opt_example_nl_tsp` for the nonlinear solver.
*   :ref:`opt_example_nl_cvrp` for the nonlinear solver.
*   :ref:`opt_example_cqm_binpacking` for the CQM solver.
*   :ref:`opt_example_cqm_stockselling` for the CQM solver.
*   :ref:`opt_example_bqm_structuralimbalance` for the BQM solver.
*   |dwave_short|'s GitHub repository,
    `dwave-examples <https://github.com/dwave-examples>`_\ , which includes
    Jupyter notebooks and code examples for various types of problems, such as
    the knapsack problem.
