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

Find concepts/terminology are looking for here or under the
:ref:`generated_site_index`.

.. _terminology_links:

Concepts and Terminology
========================

.. glossary::

    Adiabatic
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
        The |adv2_tm| is |dwave_short|'s next-generation :term:`QPU`, after the
        :term:`Advantage` quantum computer.

    Binary quadratic model
    BQM
        A collection of binary-valued variables (variables that can be assigned
        two values, for example -1, 1) with associated linear and quadratic
        biases. Sometimes referred to in other tools as a problem.

        Learn more: :ref:`concept_models_bqm`.

    Chain
    Chains
        One or more nodes or qubits in a target graph that represent a single
        variable in the source graph. See also :term:`embedding`.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_example_and` for an example.
        *   :ref:`qpu_embedding_guidance` for advanced information.

    Chain length
        The number of qubits in a :term:`Chain`.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.

    Chain strength
        Magnitude of the negative quadratic bias applied between variables to
        form a chain.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_example_and` for an example.
        *   :ref:`qpu_embedding_guidance` for advanced information.

    charge_time
        Time charged to your `Leap service <https://cloud.dwavesys.com/leap/>`_
        account.

        Learn more: :ref`opt_leap_hybrid_timing` describes the timing
        for hybrid solvers.

    Chimera
        A D-Wave :term:`QPU` is a lattice of interconnected qubits. While some
        qubits connect to others via couplers, D-Wave QPUs are not fully
        connected. For earlier D-Wave 2000Q QPUs, the qubits interconnected in
        an architecture known as Chimera. See also :term:`Pegasus` and
        :term:`Zephyr`.

        Learn more: :ref:`qpu_topologies`.

    Clique
    Complete graph
    Fully connected
        See `complete graph <https://en.wikipedia.org/wiki/Complete_graph>`_
        on Wikipedia or

        .. todo:: replace this link:

        :std:doc:`oceandocs:docs_dnx/reference/algorithms/clique`. A fully
        connected or complete :term:`binary quadratic model` is one that has
        interactions between all of its variables.

    Combinatorial optimization
    Discrete optimization
        The optimization of an :term:`objective function` defined over a set of
        discrete values such as Booleans.

    Composed sampler
        Samplers that apply pre- and/or post-processing to binary quadratic
        programs without changing the underlying :term:`sampler` implementation
        by layering composite patterns on the sampler. For example, a composed
        sampler might add spin transformations when sampling from a D-Wave
        quantum computer.

        Learn more: :ref:`quadratic_composites`.

    Composite
        A :term:`sampler` can be composed. The
        `composite pattern <https://en.wikipedia.org/wiki/Composite_pattern>`_
        allows layers of pre- and post-processing to be applied to binary
        quadratic programs without needing to change the underlying sampler
        implementation. We refer to these layers as "composites". A composed
        sampler includes at least one sampler and possibly many composites.

        Learn more: :ref:`quadratic_composites`.

    Connected graph
        See `connected graph <https://xlinux.nist.gov/dads/HTML/connectedGraph.html>`_
        on the US NIST site. A connected graph has some path from any vertex
        to any other. A graph that has at least two vertices without a path
        between them is disconnected. Any :term:`Complete graph` is connected
        (but not all connected graphs are complete).

    Constrained quadratic model
    CQM
        A collection of variables with associated linear and quadratic biases
        representing a problem modeled as an :term:`objective function` and
        inequality and equality constraints.

        Learn more: :ref:`concept_models_cqm`.

    Constraint
        A constraint is a condition of an optimization problem that the solution
        must satisfy. See
        `Constraint (mathematics) <https://en.wikipedia.org/wiki/Constraint_(mathematics)>`_.

    Constraint satisfaction problem
    CSP
        A `constraint satisfaction problem (CSP) <https://en.wikipedia.org/wiki/Constraint_satisfaction_problem>`_
        requires that all the problem's variables be assigned values, out of a
        finite domain, that result in the satisfying of all constraints.

        Learn more: :ref:`concept_constraint_satisfaction_problem`.

    Coupler
    Couplers
        Couplers can correlate two qubits such that they tend to end up in the
        same classical state---both 0 or both 1---or in opposite states. The
        correlation between coupled qubits is controlled programmatically.

    Discrete quadratic model
    DQM
        A collection of discrete-valued variables  (variables that can be
        assigned the values specified by a set such as
        :math:`\{red, green, blue\}` or :math:`\{33, 5.7, 3,14 \}` ) with
        associated linear and quadratic biases.

        Learn more: :ref:`concept_models_dqm`.

    Embed
    Embedding
    Minor embed
    Minor-embed
    Minor embedding
    Minor-embedding
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

    Excited state
        States of a quantum system that have higher energy than the
        :term:`ground state`. Such states represent non-optimal solutions for
        problems represented by an :term:`objective function` and infeasible
        configurations for problems represented by a :term:`penalty model`.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    Graph
        A collection of nodes and edges. A graph can be derived from a
        :term:`model`\ : a node for each variable and an edge for each pair of
        variables with a non-zero quadratic bias.

    Ground state
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

    Hardware graph
        The hardware graph is the physical lattice of interconnected qubits.
        See also :term:`working graph`.

        Learn more: :ref:`qpu_topologies`.

    Hybrid
        Quantum-classical hybrid is the use of both classical and quantum
        resources to solve problems, exploiting the complementary strengths
        that each provides.

        Learn more:

        *   :ref:`concept_hybrid` for an introduction.
        *   :ref:`opt_index_hybrid` gets you started with hybrid samplers.
        *   :ref:`opt_index_hybrid_solvers` describes the supported hybrid
            solvers in the :term:`Leap service`.
        *   :ref:`opt_index_using` describes best practices.

    ICE
    Integrated control errors
        The dynamic range of :ref:`param_qpu_h` and :ref:`_parameter_qpu_j`
        values may be limited by *integrated control errors* (ICE). The term
        *ICE* refers collectively to these sources of infidelity in problem
        representation.

        Learn more: :ref:`qpu_errors`.

    Ising
        Traditionally used in statistical mechanics. Variables are "spin up"
        (:math:`\uparrow`) and "spin down" (:math:`\downarrow`), states that
        correspond to :math:`+1` and :math:`-1` values. Relationships between
        the spins, represented by couplings, are correlations or
        anti-correlations. The :term:`objective function` expressed as an Ising
        model is as follows:

        .. math::
            :nowrap:

            \begin{equation}
                \text{E}_{ising}(\pmb{s}) = \sum_{i=1}^N h_i s_i +
                \sum_{i=1}^N \sum_{j=i+1}^N J_{i,j} s_i s_j
            \end{equation}

        where the linear coefficients corresponding to qubit biases
        are :math:`h_i`, and the quadratic coefficients corresponding to
        coupling strengths are :math:`J_{i,j}`.

        Learn more:

        *   `Ising Model on Wikipedia <https://en.wikipedia.org/wiki/Ising_model>`_.
        *   :ref:`concept_models` on supported models.

    Leap
    Leap service

        Launched in 2018, the |cloud_tm| quantum cloud service from
        |dwave_short|_ brings quantum computing to the real world by providing
        real-time cloud access to D-Wave's systems.

    Minimum gap
        The minimum distance between the :term:`ground state` and the first
        :term:`excited state` throughout any point in the anneal.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    Model
        A collection of variables with associated biases. Sometimes referred to
        as a **problem**.

        Learn more: :ref:`concept_models`

    Objective function
        A mathematical expression of the energy of a system as a function of
        its variables.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    One-hot
        For one-hot variables, the only valid values are those in which a single
        bit is 1 and the others are all zero. See
        `one-hot on Wikipedia <https://en.wikipedia.org/wiki/One-hot>` for
        details.

        Learn more: :ref:`qpu_reformulating_onehot_domainwall`

    Nonlinear model
        A collection of variables with associated biases that constitute an
        :term:`objective function` and/or constraints.
        Sometimes referred to as a **problem**.

        Learn more: :ref:`concept_models_nonlinear`.

    Pegasus
        A D-Wave :term:`QPU` is a lattice of interconnected qubits. While some
        qubits connect to others via couplers, D-Wave QPUs are not fully
        connected. For an Advantage QPU, the qubits interconnect in an
        architecture known as Pegasus. See also :term:`Chimera` and
        :term:`Zephyr`.

        Learn more: :ref:`qpu_topologies`.

    Penalty function
        An algorithm for solving constrained optimization problems. In the
        context of Ocean tools, penalty functions are typically employed to
        increase the energy level of a problem's :term:`objective function` by
        penalizing non-valid configurations. See
        `Penalty method on Wikipedia <https://en.wikipedia.org/wiki/Penalty_method>`_.

        Learn more: :ref:`concept_penalty`.

    Penalty
    Penalty model
        An approach to solving constraint satisfaction problems (CSP) using an
        :term:`Ising` model or a :term:`QUBO` by mapping each individual
        constraint in the CSP to a "small" Ising model or QUBO.

        Learn more: :ref:`concept_penalty`.

    QPU
        Quantum processing unit.

        Learn more: :ref:`qpu_quantum_annealing_intro`.

    qpu_access_time
        :term:`QPU` time used by a :term:`hybrid` solver.

        Learn more: :ref`opt_leap_hybrid_timing` describes the timing
        for hybrid solvers.

    Quadratic model
        A collection of variables with associated linear and quadratic biases.
        Sometimes referred to as a **problem**.

        Learn more: :ref:`concept_models_quadratic`.

    Quantum annealing
    Quantum annealer
        Quantum annealers are quantum computers that you initialize in a
        low-energy state and gradually introduce the parameters of a problem you
        wish to solve. The slow change makes it likely that the system ends in a
        low-energy state of the problem, which corresponds to an optimal
        solution.

        Learn more: ref:`qpu_quantum_annealing_intro`.

    Qubit
    Qubits
        A qubit, short for quantum bit, is a basic unit of quantum information,
        a two-state (or two-level) quantum-mechanical system; for example, the
        spin of the electron in which the two levels can be taken as spin up and
        spin down. See
        `Qubit on Wikipedia <https://en.wikipedia.org/wiki/Qubit>`_.

    QUBO
        Quadratic unconstrained binary optimization.
        QUBO problems are traditionally used in computer science. Variables
        are TRUE and FALSE, states that correspond to 1 and 0 values.
        A QUBO problem is defined using an upper-diagonal matrix :math:`Q`,
        which is an :math:`N` x :math:`N` upper-triangular matrix of real
        weights, and :math:`x`, a vector of binary variables, as minimizing the
        function

        .. math::
            :nowrap:

            \begin{equation}
                f(x) = \sum_{i} {Q_{i,i}}{x_i} + \sum_{i<j} {Q_{i,j}}{x_i}{x_j}
            \end{equation}

        where the diagonal terms :math:`Q_{i,i}` are the linear coefficients and
        the nonzero off-diagonal terms are the quadratic coefficients
        :math:`Q_{i,j}`.
        This can be expressed more concisely as

        .. math::
            :nowrap:

            \begin{equation}
                \min_{{x} \in {\{0,1\}^n}} {x}^{T} {Q}{x}.
            \end{equation}

        In scalar notation, the :term:`objective function` expressed as a QUBO
        is as follows:

        .. math::
            :nowrap:

            \begin{equation}
                \text{E}_{qubo}(a_i, b_{i,j}; q_i) = \sum_{i} a_i q_i +
                \sum_{i<j} b_{i,j} q_i q_j.
            \end{equation}

        See also `QUBO on Wikipedia <https://en.wikipedia.org/wiki/Quadratic_unconstrained_binary_optimization>`_.

        Learn more: :ref:`concept_models_qubo`.

    run_time
        Time a :term:`hybrid` solver spent working on your problem.

        Learn more: :ref`opt_leap_hybrid_timing` describes the timing
        for hybrid solvers.

    Sampler
        Samplers are processes that sample from low energy states of a problem's
        objective function, which is a mathematical expression of the energy of
        a system. A binary quadratic model (BQM) sampler samples from low energy
        states in models such as those defined by an :term:`Ising` equation or
        a :term:`QUBO` problem and returns an iterable of samples, in order of
        increasing energy.

        Learn more: :ref:`concept_samplers`.

    Sampleset
    Samples
    Solutions
        Ocean uses a :class:`~dimod.SampleSet` class to hold samples and some
        additional information.

        Learn more: :ref:`concept_samplesets`.

    SAPI
        Solver API used by clients to communicate with a :term:`solver`.

        Learn more:

        *   :ref:`ocean_sapi_access_basic`.
        *   :ref:`ocean_sapi_access_advanced`

    SAT
    Satisfiability
    Boolean satisfiability problem
        A problem of whether a formula's variables can be consistently replaced
        by the values TRUE or FALSE to make the formula evaluate to TRUE. See
        also :term:`CSP`.

        Learn more: `satisfiability (SAT) <https://en.wikipedia.org/wiki/Boolean_satisfiability_problem>`_

    Solver
        A resource that runs a problem. Some solvers interface to the
        :term:`QPU`; others leverage CPU and GPU resources.

        Learn more: :ref:`concept_samplers`.

    Source
    Source graph
        In the context of :term:`embedding`, the model or induced :term:`graph`
        that we wish to embed. Sometimes referred to as the **logical**
        graph/model.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.
        *   :ref:`qpu_topologies` on QPU topologies.

    Structured sampler
        Samplers that are restricted to sampling only binary quadratic models
        defined on a specific :term:`graph`.

    Subgraph
        See
        `subgraph <https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#subgraph>`_
        on Wikipedia.

    Symbolic Math
        :ref:`sdk_index_dimod` supports symbolic math that can simplify your
        coding of problems.

        Learn more: :ref:`concept_symbolic_math`.

    Target
    Target graph
        :term:`Embedding` attempts to create a target :term:`model` from a
        target :term:`graph`. The process of embedding takes a source model,
        derives the source graph, maps the source graph to the target graph,
        then derives the target model. Sometimes referred to as the
        **embedded** graph/model.

        Learn more:

        *   :ref:`qpu_embedding_intro` for an introduction.
        *   :ref:`qpu_embedding_guidance` for advanced information.
        *   :ref:`qpu_topologies` on QPU topologies.

    Topology
        The layout of the |dwave_short| quantum processing unit (:term:`QPU`):
        The QPU is a lattice of interconnected :term:`qubits>`. While some
        qubits connect to others via :term:`couplers`, the QPU is not fully
        connected. Instead, the qubits of |dwave_short| annealing quantum
        computers interconnect in a topology such as :term:`Pegasus`.

        Learn more: :ref:`qpu_topologies`

    Working graph
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
