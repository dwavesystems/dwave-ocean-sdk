.. _opt_leap_hybrid:

=====================
Leap's Hybrid Solvers
=====================

Introduces the `Leap service <https://cloud.dwavesys.com/leap/>`_'s
quantum-classical hybrid solvers and provides references to usage information.

.. note::
    Not all accounts have access to this type of solver.

Hybrid Solvers
--------------

.. include:: ../shared/hybrid.rst
    :start-after: start_intro
    :end-before: end_intro

.. include:: ../shared/hybrid.rst
    :start-after: start_generally_available_solvers
    :end-before: end_generally_available_solvers

Solver Properties and Parameters
--------------------------------

The |doc_solver_properties|_ reference describes the solvers available
through the :term:`Solver API <SAPI>`, their properties, and the parameters
they accept with problem submissions.

Solver Timing
-------------

The table below lists the timing information returned from
quantum-classical hybrid solvers in the
`Leap service <https://cloud.dwavesys.com/leap/>`_.
You can access this information via the
`dimod <https://github.com/dwavesystems/dimod>`_
:class:`~dimod.SampleSet` class, as in the example below.

>>> import dimod
>>> from dwave.system import LeapHybridSampler
...
>>> sampler = LeapHybridSampler(solver={'category': 'hybrid'})
>>> bqm = dimod.generators.ran_r(1, 300)
>>> sampleset = sampler.sample(bqm)
>>> sampleset.info     # doctest: +SKIP
{'qpu_access_time': 41990, 'charge_time': 2991424, 'run_time': 2991424}

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

.. _leap_hybrid_usage_charges:

Solver Usage Charges
--------------------

|dwave_short| charges you for time that solvers run your problems,
with rates depending on QPU usage. You can see the rate at which
your account's quota is consumed for a particular solver in the solver's
:ref:`sysdocs:property_quota_rate` property.

You can see the time you are charged for in the responses returned for your
submitted problems. The relevant field in the response is :code:`'charge_time'`.
The example in the `Solver Timing`_ section shows :code:`'charge_time': 2991424`
in the returned response, meaning almost 3 seconds are being charged.

Instantiating the needed compute resources for your problem can introduce
a delay before the problem is processed. This delay tends to be small compared
to the overall solution time for large problems. The *charge_time*
does not include this delay.

Examples
--------

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

Further Information
-------------------

You can find more detailed information and usage examples here:

*   The |doc_cookbook|_ guide's :ref:`cb_hybrid` section.

*   Ocean software's :std:doc:`Getting Started <oceandocs:getting_started>`
    documentation examples:

    -   :std:doc:`Bin Packing <oceandocs:examples/hybrid_cqm_binpacking>` and
        :std:doc:`Stock-Sales Strategy <oceandocs:examples/hybrid_cqm_stock_selling>`
        demonstrate the hybrid CQM solver.

    -   :std:doc:`Structural Imbalance in a Social Network <oceandocs:examples/hybrid_solver_service>`
        demonstrates the hybrid BQM solver.

    -   :std:doc:`Map Coloring: Hybrid DQM Sampler <oceandocs:examples/map_dqm>`
        demonstrates the hybrid DQM solver.

*   `Hybrid Computing <https://github.com/dwave-examples/
    hybrid-computing-notebook>`_ Jupyter Notebooks.

*   |dwave_short|'s GitHub repository, `dwave-examples <https://github.com/
    dwave-examples>`_\ , which includes Jupyter notebooks and code examples
    for various types of problems, such as the knapsack problem.
