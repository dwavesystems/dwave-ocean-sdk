.. _glossary:

========
Glossary
========

.. glossary::

      binary quadratic model
      BQM
         A collection of binary-valued variables  (variables that can be assigned two values, for example -1, 1) 
         with associated linear and quadratic biases. Sometimes referred to in other tools as a problem.

      Chimera
         The D-Wave :term:`QPU` is a lattice of interconnected qubits. While some qubits
         connect to others via couplers, the D-Wave QPU is not fully connected.
         Instead, the qubits interconnect in an architecture known as Chimera.

      Composite
          A :term:`sampler` can be composed. The
          `composite pattern <https://en.wikipedia.org/wiki/Composite_pattern>`_
          allows layers of pre- and post-processing to be applied to binary quadratic
          programs without needing to change the underlying sampler implementation.
          We refer to these layers as "composites". A composed sampler includes at least one
          sampler and possibly many composites.

      Embed
      Embedding
      Minor-embed
      Minor-embedding
         The nodes and edges on the graph that represents an objective function
         translate to the qubits and couplers in :term:`Chimera`. Each logical qubit, in
         the graph of the :term:`objective function`, may be represented by one or more
         physical qubits. The process of mapping the logical qubits to physical
         qubits is known as minor embedding.

      Hamiltonian
         A classical Hamiltonian is a mathematical description of some physical
         system in terms of its energies. We can input any particular state of
         the system, and the Hamiltonian returns the energy for that state.
         For a quantum system, a Hamiltonian is a function that maps certain states,
         called *eigenstates*, to energies. Only when the system is in an
         eigenstate of the Hamiltonian is its energy well defined and called
         the *eigenenergy*. When the system is in any other state, its energy
         is uncertain.
         For the D-Wave system, the Hamiltonian may be represented as

         .. math::
         	:nowrap:

         	\begin{equation}
         			{\cal H}_{ising} = \underbrace{\frac{A({s})}{2} \left(\sum_i {\hat\sigma_{x}^{(i)}}\right)}_\text{Initial Hamiltonian} + \underbrace{\frac{B({s})}{2} \left(\sum_{i} h_i {\hat\sigma_{z}^{(i)}} + \sum_{i>j} J_{i,j} {\hat\sigma_{z}^{(i)}} {\hat\sigma_{z}^{(j)}}\right)}_\text{Final Hamiltonian}
         	\end{equation}

         where :math:`{\hat\sigma_{x,z}^{(i)}}` are Pauli matrices operating on
         a qubit :math:`q_i`, and :math:`h_i` and :math:`J_{i,j}` are the qubit
         biases and coupling strengths.

      Ising
         Traditionally used in statistical mechanics. Variables are "spin up"
         (:math:`\uparrow`) and "spin down" (:math:`\downarrow`), states that
         correspond to :math:`+1` and :math:`-1` values. Relationships between
         the spins, represented by couplings, are correlations or anti-correlations.
         The :term:`objective function` expressed as an Ising model is as follows:

         .. math::
	          :nowrap:

	          \begin{equation}
	               \text{E}_{ising}(\pmb{s}) = \sum_{i=1}^N h_i s_i + \sum_{i=1}^N \sum_{j=i+1}^N J_{i,j} s_i s_j
	          \end{equation}

         where the linear coefficients corresponding to qubit biases
         are :math:`h_i`, and the quadratic coefficients corresponding to coupling
         strengths are :math:`J_{i,j}`.

      Minimum gap
         The minimum distance between the ground state and the first excited
         state throughout any point in the anneal.

      Objective function
         A mathematical expression of the energy of a system as a function of
         binary variables representing the qubits.

      Penalty function
         An algorithm for solving constrained optimization problems. In the context
         of Ocean tools, penalty functions are typically employed to increase the energy
         level of a problem’s :term:`objective function` by penalizing non-valid configurations.
         See `Penalty method on Wikipedia <https://en.wikipedia.org/wiki/Penalty_method>`_

      QPU
         Quantum processing unit

      QUBO
         Quadratic unconstrained binary optimization.
         QUBO problems are traditionally used in computer science. Variables
         are TRUE and FALSE, states that correspond to 1 and 0 values.
         A QUBO problem is defined using an upper-diagonal matrix :math:`Q`,
         which is an :math:`N` x :math:`N` upper-triangular matrix of real weights,
         and :math:`x`, a vector of binary variables, as minimizing the function

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
          		\text{E}_{qubo}(a_i, b_{i,j}; q_i) = \sum_{i} a_i q_i + \sum_{i<j} b_{i,j} q_i q_j.
            \end{equation}

      Sampler
         Samplers are processes that sample from low energy states of a problem's objective
         function, which is a mathematical expression of the energy of a system. A binary
         quadratic model (BQM) sampler samples from low energy states in models such as those
         defined by an :term:`Ising` equation or a :term:`QUBO` problem and returns an iterable
         of samples, in order of increasing energy.

      SAPI
         Solver API used by clients to communicate with a :term:`solver`.

      Solver
         A resource that runs a problem. Some solvers interface to the :term:`QPU`;
         others leverage CPU and GPU resources.
