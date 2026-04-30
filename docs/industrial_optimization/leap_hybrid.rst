.. _opt_leap_hybrid:

=======================
Using the Stride Solver
=======================

This section introduces the |cloud|_ service's quantum-classical :term:`hybrid`
nonlinear :term:`solver <solver>`, also known as the |nlstride_tm| (e.g.,
``hybrid_nonlinear_program_version1``) and provides usage information.

.. note::
    Not all accounts have access to this type of solver.

.. include:: ../shared/models.rst
    :start-after: start_models_nonlinear
    :end-before: end_models_nonlinear

These solvers accept arbitrarily structured problems formulated as nonlinear
models, with any constraints represented natively.

Philosophy?

Returned Solutions

Properties & Parameters

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
