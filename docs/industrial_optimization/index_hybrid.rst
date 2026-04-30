.. _opt_index_hybrid:

============================
Sampling with Hybrid Solvers
============================

.. toctree::
    :hidden:
    :maxdepth: 1

    leap_hybrid
    dwave_hybrid

.. include:: ../shared/hybrid.rst
    :start-after: start_leap_intro
    :end-before: end_leap_intro

.. grid:: 2 2 3 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_leap_hybrid`
        :link: opt_leap_hybrid
        :link-type: ref

        Using the |nlstride_tm|.

    .. grid-item-card:: :ref:`opt_dwave_hybrid`
        :link: opt_dwave_hybrid
        :link-type: ref

        Other hybrid samplers.

D-Wave also provides a Python framework for building a variety of flexible
hybrid workflows. The :ref:`opt_dwave_hybrid_development_framework` section
describes this framework.

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
>>> sampler = LeapHybridSampler(solver={'category': 'hybrid'})  # doctest: +SKIP
>>> bqm = dimod.generators.ran_r(1, 300)
>>> sampleset = sampler.sample(bqm)     # doctest: +SKIP
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


Related Information
===================

*   The :ref:`Concepts: Hybrid <concept_hybrid>` section gives an overview of
    hybrid and links to related topics.
*   The :ref:`opt_example_nl_tsp` section is an example of using Leap service
    solvers.
*   The :ref:`opt_example_kerberos_map` and
    :ref:`opt_example_dwavehybrid_workflow` sections are examples of using the
    :ref:`dwave-hybrid <index_hybrid>` framework.
