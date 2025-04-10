.. _index_concepts:

========
Concepts
========

.. toctree::
    :hidden:

    csp
    hybrid
    models
    penalty
    samplers
    samplesets
    symbolic_math
    variables

Find concepts/terminology you are looking for here or under the
:ref:`generated_site_index`.

.. _terminology_links:

Concepts and Terminology
========================

.. glossary::

    access time
        Execution time for a single quantum machine instruction (:term:`QMI`, or
        problem).

        Learn more: :ref:`qpu_timing_breakdown_access`.

    adiabatic
        An annealing process that experiences no interference from outside
        energy sources and evolves the Hamiltonian slowly enough is called an
        *adiabatic* process.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    Advantage
        The |dwave_5kq_tm| quantum computer is the first quantum system
        designed for business and is the most powerful and connected commercial
        quantum computer in the world, with more than 5000 qubits and 35,000
        couplers. |dwave_5kq| :term:`QPUs <QPU>` are named
        :code:`Advantage_system<x.y>`, with ``x`` numbering :term:`solver`
        (|dwave_short| system) resources and ``y`` possibly incrementing on
        updates such as newer calibrations; for example, the first online QPU
        was :code:`Advantage_system1.1`.

    Advantage2
        The |adv2_tm| quantum computer is |dwave_short|'s next-generation
        :term:`QPU`, after the :term:`Advantage` quantum computer.

    anneal
    annealing

        See :term:`quantum annealing`.

    anneal offset
        Provide offsets to annealing paths, per qubit.

        Learn more:

        *   :ref:`parameter_qpu_anneal_offsets` for the solver property.
        *   :ref:`qpu_qa_anneal_offsets` for a description.

    anneal schedule
    annealing schedule
        A single, global, time-dependent bias controls the changes of energy
        scales :math:`A(s)` and :math:`B(s)` during the quantum annealing
        process.

        Learn more:

        *   :ref:`qpu_quantum_annealing_intro` for an introduction.
        *   :ref:`qpu_annealprotocol_standard`.
        *   :ref:`qpu_annealprotocol_fast`.
        *   :ref:`qpu_qa_anneal_sched` for pause, quench, and reverse anneal.
        *   :ref:`qpu_solver_properties_specific` for the schedules of each QPU,
            as spreadsheets.

    binary quadratic model
    BQM
        A collection of binary-valued variables (variables that can be assigned
        two values, for example -1, 1) with associated linear and quadratic
        biases. Sometimes referred to in other tools as a problem.

        Learn more: :ref:`concept_models_bqm`.

    chain
    chains
        One or more nodes or qubits in a target graph that represent a single
        variable in the source graph. See also :term:`embedding`.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_example_and` for an example.
        *   :ref:`qpu_embedding_guidance` for advanced information.

    chain break
    broken chain
        In chains, the qubits that form the nodes of the chain should always
        end the :term:`anneal` with the same value; when qubits in a chain take
        different values, the chain is considered broken.

        Learn more

        *   :ref:`qpu_example_and` explains broken chains.
        *   :ref:`qpu_example_inspector_graph_partitioning` uses the problem
            inspector (the :ref:`dwave-inspector <index_inspector>`) for
            viewing and dealing with broken chains.

    chain length
        The number of qubits in a :term:`Chain`.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.

    chain strength
        Magnitude of the negative quadratic bias applied between variables to
        form a chain.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_example_and` for an example.
        *   :ref:`qpu_embedding_guidance` for advanced information.

    charge_time
    charge time
        Time charged to your `Leap service <https://cloud.dwavesys.com/leap/>`_
        account.

        Learn more: :ref:`opt_leap_hybrid_timing` describes the timing
        for hybrid solvers.

    Chimera
        A D-Wave :term:`QPU` is a lattice of interconnected qubits. While some
        qubits connect to others via couplers, D-Wave QPUs are not fully
        connected. For earlier D-Wave 2000Q QPUs, the qubits interconnected in
        an architecture known as Chimera. See also :term:`Pegasus` and
        :term:`Zephyr`.

        Learn more: :ref:`qpu_topologies`.

    classical
    classical solver
        An algorithm that runs on any non-quantum
        `computer <https://en.wikipedia.org/wiki/Computer>`.

        Learn more: :ref:`qpu_classical_intro`.

    clique
    complete graph
    fully connected
        See `complete graph <https://en.wikipedia.org/wiki/Complete_graph>`_
        on Wikipedia or :ref:`dnx_clique`. A fully connected or complete
        :term:`binary quadratic model` is one that has interactions
        between all of its variables.

    combinatorial optimization
    discrete optimization
        The optimization of an :term:`objective function` defined over a set of
        discrete values such as Booleans.

    composed sampler
        Samplers that apply pre- and/or post-processing to binary quadratic
        programs without changing the underlying :term:`sampler` implementation
        by layering composite patterns on the sampler. For example, a composed
        sampler might add spin transformations when sampling from a D-Wave
        quantum computer.

        Learn more: :ref:`dimod_composites`.

    composite
        A :term:`sampler` can be composed. The
        `composite pattern <https://en.wikipedia.org/wiki/Composite_pattern>`_
        allows layers of pre- and post-processing to be applied to binary
        quadratic programs without needing to change the underlying sampler
        implementation. We refer to these layers as "composites". A composed
        sampler includes at least one sampler and possibly many composites.

        Learn more: :ref:`dimod_composites`.

    connected graph
        See `connected graph <https://xlinux.nist.gov/dads/HTML/connectedGraph.html>`_
        on the US NIST site. A connected graph has some path from any vertex
        to any other. A graph that has at least two vertices without a path
        between them is disconnected. Any :term:`Complete graph` is connected
        (but not all connected graphs are complete).

    constrained quadratic model
    CQM
        A collection of variables with associated linear and quadratic biases
        representing a problem modeled as an :term:`objective function` and
        inequality and equality constraints.

        Learn more: :ref:`concept_models_cqm`.

    constraint
    hard constraint
    soft constraint
        A constraint is a condition of an optimization problem that the solution
        must satisfy ("hard" constraint) or is preferred to satisfy ("soft"
        constraint). See
        `Constraint (mathematics) <https://en.wikipedia.org/wiki/Constraint_(mathematics)>`_.

    constraint satisfaction problem
    CSP
        A `constraint satisfaction problem (CSP) <https://en.wikipedia.org/wiki/Constraint_satisfaction_problem>`_
        requires that all the problem's variables be assigned values, out of a
        finite domain, that result in the satisfying of all constraints.

        Learn more: :ref:`concept_constraint_satisfaction_problem`.

    coupler
    couplers
        Couplers can correlate two qubits such that they tend to end up in the
        same classical state---both 0 or both 1---or in opposite states. The
        correlation between coupled qubits is controlled programmatically.

    directed acyclic graph
    DAG
        A `DAG <https://en.wikipedia.org/wiki/Directed_acyclic_graph>`_ is a
        graph whose edges are directed from one vertex to another, such that
        following the edges never forms a closed loop (you cannot return to a
        node by following any path along these directed edges). They are
        suitable for use with decision variables that represent a common logic,
        such as subsets of choices or permutations of ordering. For example, in
        a traveling salesperson problem, permutations of the variables that
        represent cities signify the order of the route being optimized.
        Likewise, for tasks in a project with dependencies, nodes represent
        tasks and directed edges show which tasks must be completed before
        others. Models constructed for D-Wave's hybrid nonlinear solver can be
        mapped to DAGs.

        Learn more: :ref:`opt_model_construction_nl`

    discrete quadratic model
    DQM
        A collection of discrete-valued variables  (variables that can be
        assigned the values specified by a set such as
        :math:`\{red, green, blue\}` or :math:`\{33, 5.7, 3,14 \}` ) with
        associated linear and quadratic biases.

        Learn more: :ref:`concept_models_dqm`.

    embed
    embedding
    minor embed
    minor-embed
    minor embedding
    minor-embedding
        Nodes and edges on the graph that represents an objective function
        translate to qubits and couplers in the QPU :term:`topology`. Each
        logical qubit, in the graph of the :term:`objective function`, may be
        represented by one or more physical qubits. The process of mapping the
        logical qubits to physical qubits is known as minor embedding.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.
        *   :ref:`qpu_topologies` on QPU topologies.
        *   :ref:`qpu_example_not`, :ref:`qpu_example_and`, and
            :ref:`qpu_example_multigate` for examples and more information.

    excited state
        States of a quantum system that have higher energy than the
        :term:`ground state`. Such states represent non-optimal solutions for
        problems represented by an :term:`objective function` and infeasible
        configurations for problems represented by a :term:`penalty model`.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    feasible state
        A state in which the values of variables do not violate any hard
        :term:`constraint`.

    flux bias
    flux-bias offset
        Flux biases can be used to refine the standard calibration and to bias
        qubits indirectly when you cannot set a bias on the qubit.

        Learn more:

        *   :ref:`parameter_qpu_flux_biases` for a description of the parameter.
        *   :ref:`qpu_error_fix_fbo` fo ran explanation of calibration
            refinement.
        *   :ref:`qpu_config_emulate_with_fbo`.

    gate model
    circuit model
        Gate-model quantum computing, also known as circuit model, implements
        compute algorithms with
        `quantum gates <https://en.wikipedia.org/wiki/Quantum_logic_gate>`_,
        analogously to the use of
        `Boolean gates <https://en.wikipedia.org/wiki/Logic_gate>`_ in classical
        computers.

        Learn more: :ref:`qpu_gate_model_intro`.

    graph
        A collection of nodes and edges. A graph can be derived from a
        :term:`model`\ : a node for each variable and an edge for each pair of
        variables with a non-zero quadratic bias.

    ground state
        The lowest-energy state of a quantum-mechanical system and the global
        minimum of a problem represented by an :term:`objective function`.

    Hamiltonian
        A classical Hamiltonian is a mathematical description of some physical
        system in terms of its energies. We can input any particular state of
        the system, and the Hamiltonian returns the energy for that state.
        For a quantum system, a Hamiltonian is a function that maps certain
        states, called *eigenstates*, to energies. Only when the system is in
        an eigenstate of the Hamiltonian is its energy well defined and called
        the *eigenenergy*. When the system is in any other state, its energy
        is uncertain.
        For D-Wave quantum computers, the Hamiltonian may be represented as

        .. math::
            :nowrap:

            \begin{equation}
                    {\cal H}_{ising} = \underbrace{\frac{A({s})}{2}
                    \left(\sum_i {\hat\sigma_{x}^{(i)}}\right)}_\text{Initial Hamiltonian}
                    + \underbrace{\frac{B({s})}{2}
                    \left(\sum_{i} h_i {\hat\sigma_{z}^{(i)}}
                    + \sum_{i>j} J_{i,j} {\hat\sigma_{z}^{(i)}}
                    {\hat\sigma_{z}^{(j)}}\right)}_\text{Final Hamiltonian}
            \end{equation}

        where :math:`{\hat\sigma_{x,z}^{(i)}}` are Pauli matrices operating on
        a qubit :math:`q_i`, and :math:`h_i` and :math:`J_{i,j}` are the qubit
        biases and coupling strengths.

        Learn more:

        *   :ref:`qpu_quantum_annealing_intro` for an introduction.
        *   :ref:`qpu_annealing` for advanced information on implementation.

    hardware graph
        The hardware graph is the physical lattice of interconnected qubits.
        See also :term:`working graph`.

        Learn more: :ref:`qpu_topologies`.

    hybrid
        Quantum-classical hybrid is the use of both classical and quantum
        resources to solve problems, exploiting the complementary strengths
        that each provides.

        Learn more:

        *   :ref:`concept_hybrid` for an introduction.
        *   :ref:`opt_index_hybrid` gets you started with hybrid samplers.
        *   :ref:`opt_index_properties_parameters` describes the supported
            hybrid solvers in the :term:`Leap service`.
        *   :ref:`opt_index_improving_solutions` describes best practices.

    ICE
    integrated control errors
        The dynamic range of :ref:`parameter_qpu_h` and :ref:`parameter_qpu_j`
        values may be limited by *integrated control errors* (ICE). The term
        *ICE* refers collectively to these sources of infidelity in problem
        representation.

        Learn more: :ref:`qpu_errors`.

    infeasible state
        A state in which the values of variables violate a :term:`constraint`.

    Ising
        .. include:: ../shared/models.rst
            :start-after: start_models_ising_formula
            :end-before: end_models_ising_formula

        Learn more:

        *   `Ising Model on Wikipedia <https://en.wikipedia.org/wiki/Ising_model>`_.
        *   :ref:`concept_models` on supported models.

    Leap
    Leap service

        Launched in 2018, the |cloud_tm| quantum cloud service from
        |dwave_short|_ brings quantum computing to the real world by providing
        real-time cloud access to D-Wave's systems.

    linear program
    linear optimization
        `Linear programming <https://en.wikipedia.org/wiki/Linear_programming>`_
        (LP) is a method to achieve the best outcome (such as maximum profit or
        lowest cost) in a mathematical model whose requirements and objective
        are represented by linear relationships. See also
        :term:`nonlinear model`.

    minimum gap
        The minimum distance between the :term:`ground state` and the first
        :term:`excited state` throughout any point in the anneal.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    model
        A collection of variables with associated biases. Sometimes referred to
        as a **problem**.

        Learn more: :ref:`concept_models`

    nonlinear model
        A collection of variables with associated biases that constitute an
        :term:`objective function` and/or constraints. Sometimes referred to as
        a **problem**. See also :term:`linear program`.

        Learn more: :ref:`concept_models_nonlinear`.

    Ocean
        Ocean\ |tm| software is a suite of tools for using
        `D-Wave Quantum Inc. <https://www.dwavesys.com>`_ quantum computers and
        :term:`hybrid` :term:`solvers <solver>`.

        Learn more: :ref:`index_ocean_sdk`.

    objective function
    objective
        A mathematical expression of the energy of a system as a function of
        its variables.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    one-hot
        For one-hot variables, the only valid values are those in which a single
        bit is 1 and the others are all zero. See
        `one-hot on Wikipedia <https://en.wikipedia.org/wiki/One-hot>`_ for
        details.

        Learn more: :ref:`qpu_reformulating_onehot_domainwall`

    Pegasus
        A D-Wave :term:`QPU` is a lattice of interconnected qubits. While some
        qubits connect to others via couplers, D-Wave QPUs are not fully
        connected. For an Advantage QPU, the qubits interconnect in an
        architecture known as Pegasus. See also :term:`Chimera` and
        :term:`Zephyr`.

        Learn more: :ref:`qpu_topologies`.

    penalty function
        An algorithm for solving constrained optimization problems. In the
        context of Ocean tools, penalty functions are typically employed to
        increase the energy level of a problem's :term:`objective function` by
        penalizing non-valid configurations. See
        `Penalty method on Wikipedia <https://en.wikipedia.org/wiki/Penalty_method>`_.

        Learn more: :ref:`concept_penalty`.

    penalty
    penalty model
        An approach to solving constraint satisfaction problems (CSP) using an
        :term:`Ising` model or a :term:`QUBO` by mapping each individual
        constraint in the CSP to a "small" Ising model or QUBO.

        Learn more: :ref:`concept_penalty`.

    postprocessing
        Postprocessing in the context of using a solver can refer to additional
        (classical) computation that improves the results at low cost; for
        example majority voting on broken :term:`chains <chain>`.

        Learn more:

        *   :ref:`qpu_config_postprocessing` for an introduction.
        *   :ref:`qpu_postprocessing` for results of postprocessing results
            returned from a quantum computer.

    preprocessing
        Preprocessing can refer to some low-cost classical computation applied
        to a problem before submitting to a solver, or as part of the solver's
        work on the problem.

        Learn more:

        *   :ref:`index_preprocessing`

    QMI
        Quantum machine instruction.

    QPU
        Quantum processing unit.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    qpu_access_time
        :term:`QPU` time used by a :term:`hybrid` solver.

        Learn more: :ref:`opt_leap_hybrid_timing` describes the timing
        for hybrid solvers.

    quadratic model
        A collection of variables with associated linear and quadratic biases.
        Sometimes referred to as a **problem**.

        Quadratic functions have one or two variables per term. A simple example
        of a quadratic function is,

        .. math::

            D = Ax + By + Cxy

        where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable
        terms---:math:`Ax` and :math:`By` here---are linear with the constant
        biasing the term's variable. Two-variable terms---:math:`Cxy` here---are
        quadratic with a relationship between the variables.

        Ocean software also provides support for
        :ref:`higher order models <dimod_higher_order_models>`, which are
        typically reduced to quadratic for sampling.

        Learn more: :ref:`concept_models_quadratic`.

    quantum annealing
    quantum annealer
        Quantum annealers are quantum computers that you initialize in a
        low-energy state and gradually introduce the parameters of a problem you
        wish to solve. The slow change makes it likely that the system ends in a
        low-energy state of the problem, which corresponds to an optimal
        solution.

        Learn more:

        *   :ref:`qpu_quantum_annealing_intro` for an introduction.
        *   :ref:`qpu_annealprotocol_standard`.
        *   :ref:`qpu_annealprotocol_fast`.
        *   :ref:`qpu_qa_anneal_sched` for pause, quench, and reverse anneal.

    quantum computing
    quantum computer

        A `quantum computer <https://en.wikipedia.org/wiki/Quantum_computing>`_
        is a computer that exploits
        `quantum mechanical <https://en.wikipedia.org/wiki/Quantum_mechanics>`_
        phenomena. Today, there are two leading candidate architectures for
        quantum computers: :ref:`gate model <qpu_gate_model_intro>` (also known
        as `circuit model <https://en.wikipedia.org/wiki/Quantum_circuit>`_) and
        :term:`quantum annealing`.

        Learn more: :ref:`qpu_quantum_annealing_intro`

    qubit
    qubits
        A qubit, short for quantum bit, is a basic unit of quantum information,
        a two-state (or two-level) quantum-mechanical system; for example, the
        spin of the electron in which the two levels can be taken as spin up and
        spin down. See
        `Qubit on Wikipedia <https://en.wikipedia.org/wiki/Qubit>`_.

    QUBO
        .. include:: ../shared/models.rst
            :start-after: start_models_qubo_formula
            :end-before: end_models_qubo_formula

        See also `QUBO on Wikipedia <https://en.wikipedia.org/wiki/Quadratic_unconstrained_binary_optimization>`_.

        Learn more: :ref:`concept_models_qubo`.

    run_time
    runtime
        Time a :term:`hybrid` solver spent working on your problem.

        Learn more:

        *   :ref:`opt_leap_hybrid_timing` describes the timing for hybrid
            solvers.
        *   :ref:`qpu_timing_runtime_limits` describes the runtime limit for a
            problem executing on a quantum computer.

    sampler
        Samplers are processes that sample from low energy states of a problem's
        objective function, which is a mathematical expression of the energy of
        a system. A binary quadratic model (:term:`BQM`) sampler samples from
        low energy states in models such as those defined by an :term:`Ising`
        equation or a :term:`QUBO` problem and returns an iterable of samples,
        in order of increasing energy.

        Samplers run---either remotely (for example, in the
        `Leap <https://cloud.dwavesys.com/leap/>`_ service) or locally on your
        CPU---on compute resources known as :term:`solvers <solver>`. (Note that
        some classical samplers actually brute-force solve small problems rather
        than sample, and these are also referred to as solvers.)

        Learn more: :ref:`concept_samplers`.

    sampleset
    samples
    solutions
        Ocean uses a :class:`~dimod.SampleSet` class to hold samples and some
        additional information.

        Learn more: :ref:`concept_samplesets`.

    SAPI
        Solver API used by clients to communicate with a :term:`solver`.

        Learn more:

        *   :ref:`ocean_sapi_access_basic`.
        *   :ref:`ocean_sapi_access_advanced`

    SAT
    satisfiability
    boolean satisfiability problem
        A problem of whether a formula's variables can be consistently replaced
        by the values TRUE or FALSE to make the formula evaluate to TRUE. See
        also :term:`CSP`.

        Learn more: `satisfiability (SAT) <https://en.wikipedia.org/wiki/Boolean_satisfiability_problem>`_

    service time
        Service time is defined as the difference between the times of the
        ingress time (arrival at :term:`SAPI`) and sampleset's egress (exit from
        the quantum computer) for each quantum machine instruction (QMI).

        Learn more: :ref:`qpu_timing_breakdown_service`.

    solver
        A resource that runs a problem. Some solvers interface to the
        :term:`QPU`; others leverage CPU and GPU resources.

        Learn more: :ref:`concept_samplers`.

    source
    source graph
        In the context of :term:`embedding`, the model or induced :term:`graph`
        that we wish to embed. Sometimes referred to as the **logical**
        graph/model.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.
        *   :ref:`qpu_topologies` on QPU topologies.

    spin-reversal transform
    gauge transform
    SRT
        Applying a spin-reversal transform can improve results by reducing the
        impact of unintended biases of coupling :math:`J_{i,j}` adding a small
        bias to qubits :math:`i` and :math:`j` due to leakage.

        Learn more: :ref:`qpu_config_srt`.

    structured sampler
        Samplers that are restricted to sampling only binary quadratic models
        defined on a specific :term:`graph`.

    subgraph
        See
        `subgraph <https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#subgraph>`_
        on Wikipedia.

    symbolic math
        :ref:`index_dimod` supports symbolic math that can simplify your
        coding of problems.

        Learn more: :ref:`concept_symbolic_math`.

    target
    target graph
        :term:`Embedding` attempts to create a target :term:`model` from a
        target :term:`graph`. The process of embedding takes a source model,
        derives the source graph, maps the source graph to the target graph,
        then derives the target model. Sometimes referred to as the
        **embedded** graph/model.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.
        *   :ref:`qpu_topologies` on QPU topologies.

    topology
    architecture
        The layout of the |dwave_short| quantum processing unit (:term:`QPU`):
        The QPU is a lattice of interconnected :term:`qubits`. While some
        qubits connect to others via :term:`couplers`, the QPU is not fully
        connected. Instead, the qubits of |dwave_short| annealing quantum
        computers interconnect in a topology such as :term:`Pegasus`.

        Learn more: :ref:`qpu_topologies`

    working graph
        In a D-Wave QPU, the set of qubits and couplers that are available for
        computation is known as the working graph. The yield of a working graph
        is typically less than 100% of qubits and couplers that are fabricated
        and physically present in the QPU. See :term:`hardware graph`.

        Learn more: :ref:`qpu_topologies`.

    Zephyr
        A D-Wave :term:`QPU` is a lattice of interconnected qubits. While some
        qubits connect to others via couplers, D-Wave QPUs are not fully
        connected. For D-Wave's next-generation QPU currently under development,
        the qubits interconnect in an architecture known as Zephyr. See also
        :term:`Pegasus` and :term:`Chimera`.

        Learn more: :ref:`qpu_topologies`.

.. _generated_site_index:

Generated Ocean Index
=====================

Search the automatically generated :ref:`Ocean site index <genindex>`.
