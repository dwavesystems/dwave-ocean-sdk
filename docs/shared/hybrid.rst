.. start_generally_available_solvers

The generally available hybrid solvers depend on your account in the Leap
service. Check your dashboard to see which hybrid solvers are available to you.

Generally available hybrid solvers currently supported include:

*   Hybrid BQM solver (e.g., ``hybrid_binary_quadratic_model_version2``)

    :ref:`Binary quadratic models <oceandocs:bqm_sdk>` (BQM) typically represent
    problems of decisions that could either be true (or yes) or false (no); for
    example, should an antenna transmit, or did a network node fail?

    These solvers accept arbitrarily structured, unconstrained problems
    formulated as BQMs, with any constraints typically represented through
    :ref:`penalty models <sysdocs:cb_techniques>`.

*   Hybrid CQM solver (e.g., ``hybrid_constrained_quadratic_model_version1``)

    :ref:`Constrained quadratic models <oceandocs:cqm_sdk>` (CQM) typically
    represent problems that might include real, integer and/or binary variables
    and one or more constraints.

    These solvers accept arbitrarily structured problems formulated as CQMs,
    with any constraints represented natively.

*   Hybrid DQM solver (e.g., ``hybrid_discrete_quadratic_model_version1``)

    :ref:`Discrete quadratic models <oceandocs:dqm_sdk>` (DQM) typically
    represent problems with several distinct options; for example, which shift
    should employee X work, or should the state on a map be colored red, blue,
    green, or yellow?

    These solvers accept arbitrarily structured, unconstrained problems
    formulated as DQMs, with any constraints typically represented through
    :ref:`penalty models <sysdocs:cb_techniques>`.

*   Hybrid nonlinear-program solver (e.g.,
    ``hybrid_nonlinear_program_version1``)

    :ref:`Nonlinear models <oceandocs:nl_model_sdk>` typically represent
    problems that might include integer and/or binary variables and one or more
    constraints. Such models are especially suited for use with decision
    variables that represent a common logic, such as subsets of choices or
    permutations of ordering. For example, in a
    `traveling salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_,
    permutations of the variables representing cities can signify the order of
    the route being optimized, and in a
    `knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_, the
    variables representing items can be divided into subsets of packed and not
    packed.

    These solvers accept arbitrarily structured problems formulated as nonlinear
    models, with any constraints represented natively.

Contact |dwave_short| at sales@dwavesys.com if your application requires scale
or performance that exceeds the currently advertised capabilities of the
generally available hybrid solvers.

.. end_generally_available_solvers


.. start_intro

The quantum-classical hybrid solvers in the Leap service are intended to solve
arbitrary application problems formulated as quadratic and nonlinear
models\ [#]_\ .

.. [#]
    Problems submitted directly to quantum computers are in the
    `binary quadratic model <https://docs.ocean.dwavesys.com/en/stable/concepts/bqm.html>`_
    (BQM) format, unconstrained with binary-valued variables and structured for
    the topology of the quantum processing unit (QPU). Hybrid solvers may accept
    arbitrarily structured quadratic models (QM) and a nonlinear model,
    constrained or unconstrained, with real, integer, and binary variables.

These solvers, which implement state-of-the-art classical algorithms together
with intelligent allocation of the quantum computer to parts of the problem
where it benefits most, are designed to accommodate even very large problems.
Hybrid solvers enable you to benefit from |dwave_short|'s deep investment in
researching, developing, optimizing, and maintaining hybrid algorithms.

.. end_intro