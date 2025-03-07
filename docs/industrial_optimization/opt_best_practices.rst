.. _opt_best_practices:

==============
Best Practices
==============

|dwave_short|'s quantum-classical hybrid solvers are designed to simplify the
incorporation of quantum computing into problem-solving applications. They make
good starting points in developing your application code, and this section
provides some usage guidance.

|dwave_short| offers two complementary approaches to quantum-classical hybrid
computing, :ref:`opt_leap_hybrid` and :ref:`opt_dwave_hybrid`.

Reformulation
=============

The :ref:`qpu_reformulating` section provides guidance on formulating your
problem as a model; some of that content applies to hybrid solvers too,
especially those that accept binary quadratic models.

.. _opt_best_practices_large_problems:

Large-Problem Construction
==========================

For large problems, attention should be given to the total number of symbols for
nonlinear models and biases for quadratic models. Generating models with huge
numbers of symbols or biases may exhaust resources such as memory on your local
machine and uploads to the Leap service may tax your connection's bandwidth.

To enable best performance of your local machine and application, consider such
points as the following:

*   Before constructing extremely large problems, verify that your local machine
    has sufficient resources (such as memory) to support possibly millions of
    biases.

*   Problems can be formulated with more performant software structures such as
    BQMs or models built from NumPy arrays rather than Python lists.

    See :ref:`dimod <index_dimod>` for examples.

*   Uploading huge problems to the Leap service can take time and may require
    significant bandwidth from your Internet link. Consider using compression
    where supported by your selected hybrid solver.

.. _opt_best_practices_runtimes:

Run Times
=========

Hybrid solvers enable you to configure the time the solver runs your problem.

For many heuristic solvers, solution quality as a function of runtime is highly
dependent on the problem being solved. Consequently, hybrid solvers can set a
default runtime that is either short and insufficient for many problems or long
and expensive for many problems. Hybrid solvers in the Leap service set as the
default runtime a minimum time based on the number of problem variables (and
possibly additional measures of the problem's complexity, such as connectivity).

**Running a hybrid solver with the default** :ref:`parameter_nl_time_limit`
**parameter does not guarantee a good solution.**

Depending on the size and complexity of your problem, there are a number of
strategies you can use for setting appropriate runtimes.

*   Use the default, see if the returned solutions are good enough for your
    needs. If not, keep doubling the runtime until good solutions are produced
    or solutions remain unchanged.

*   Set a runtime based on experiments with similar problems.

*   Set a runtime based on considerations of the context in which your
    application runs: cost, available time for processing, solution quality
    required, etc.

Further Information
===================

*   [Dwave7]_ gives a performance evaluation of the hybrid solvers in the
    `Leap <https://cloud.dwavesys.com/leap/>`_ service.
*   For documentation, see the :ref:`dwave-hybrid <index_hybrid>` section.
*   The
    `Hybrid Computing <https://github.com/dwave-examples/hybrid-computing-notebook>`_
    Jupyter Notebooks explain and demonstrate how to develop and use the
    *dwave-hybrid* hybrid solvers and development framework.
