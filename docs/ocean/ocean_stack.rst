.. _ocean_stack:

====================
Ocean Software Stack
====================

The :ref:`Ocean <index_ocean_sdk>` software stack provides a chain of tools that
implements the steps needed to solve your problem on a CPU, a |dwave_short|
quantum computer, or a quantum-classical :term:`hybrid` :term:`solver`. As
described in the :ref:`ocean_workflow` section, these steps include formulating
the problem in a way the :term:`solver` understands (as a
:ref:`supported model <concept_models>`) and solving the formulated problem by
submitting it to a |dwave_short| quantum computer, a
:ref:`classical sampler <qpu_intro_classical>`, or a :term:`hybrid` solver.

It's helpful to visualize the tool chain as layers of abstraction, each of which
handles one part of the solution procedure.

Abstraction Layers
==================

.. _fig_stack:

.. figure:: ../_images/ocean_stack.png
    :name: stack
    :scale: 100 %
    :alt: Overview of the software stack.
    :height: 400 pt
    :width: 400 pt

    Ocean Software Stack

The :ref:`fig_stack` graphic above divides Ocean software and its context into
the following layers of functionality:

*   Compute Resources

    The hardware on which the problem is solved. This might be a |dwave_short|
    quantum computer but it can also be the CPU of your laptop computer or one
    of the `Leap <https://cloud.dwavesys.com/leap/>`_ service's :term:`hybrid`
    solvers.
*   Samplers

    Abstraction layer of the :term:`sampler` functionality.
    :ref:`Ocean <index_ocean_sdk>` tools implement several samplers that use the
    |dwave_short| quantum computer and classical compute resources. You can use
    the Ocean tools to customize a sampler, create your own sampler, or use
    existing (classical) samplers to test your code as you develop it.
*   Sampler API

    Abstraction layer that represents the problem in a form that can access the
    selected sampler; for example, a :ref:`dimod <index_dimod>` binary quadratic
    model (:term:`BQM`) class representing your problem wrapped in a
    :term:`minor-embedding` composite that handles the mapping between your
    problem's variables and the sampler's :term:`topology`.
*   Methods

    Tools that help formulate a problem as
    :ref:`supported models <concept_models>`; for example the
    :ref:`dwave_networkx <index_dnx>`package for graph-related problems.
*   Application

    Original problem in its context ("problem space"); for example, circuit
    fault diagnosis attempts to identify failed logic gates during chip
    manufacturing.

Problem-to-Solution Tool Chain
==============================

As described in the :ref:`ocean_workflow` section, problems can be posed in a
variety of formulations; the |dwave_short| quantum computer solves binary
quadratic models (term:`BQM`) and other :term:`hybrid` solvers handle more
abstract :ref:`models <concept_models>`. :ref:`Ocean <index_ocean_sdk>` tools
assist you in converting the problem from its original form to a form native to
the solver and sending the compatible problem for solving.

This section will familiarize you with the different tools and how you can fit
them together to solve your problem.

Bottom-Up Approach
------------------

One approach to envisioning how you can map your problem-solving process to
Ocean software is to start from the bottom---the hardware doing the
computations---and work your way up the Ocean stack to see the complete picture.
This subsection shows how you might map each stage of the process to a layer of
the Ocean stack.

1.  **Compute resource**

    You will likely use some combination of both local classical resources and a
    |dwave_short| quantum computer in your work with Ocean software. When would
    you use which?

    *   CPU: For offline testing, small problems that can be solved exactly or
        heuristically in a reasonable amount of time.
    *   QPU: Hard problems or for learning how to use quantum resources to solve
        such problems.
    *   Hybrid of both QPU and CPU/GPU: Large, complex problems that need to run
        classically but may benefit from having some parts allocated to a
        quantum computer for solution.

2.  **Sampler**

    Your :term:`sampler` provides access to the compute resource that solves
    your problem.

    The table below shows some Ocean samplers and considerations for selecting
    one or another.

    .. list-table:: Ocean Samplers
        :widths: 10 20 50 40
        :header-rows: 1

        *   - Computation
            - Tool & Sampler
            - Usage
            - Notes
        *   - Classical
            - :ref:`dimod <index_dimod>`
              :class:`~dimod.reference.samplers.ExactSolver`
            - Find all states for small (<20 variables) problems.
            - For code-development testing.
        *   - Classical
            - :ref:`dimod <index_dimod>`
              :class:`~dimod.reference.samplers.random_sampler.RandomSampler`
            - Random sampler for testing.
            - For code-development testing.
        *   - Classical
            - :ref:`dimod <index_dimod>`
              :class:`~dimod.reference.samplers.simulated_annealing.SimulatedAnnealingSampler`
            - Simulated annealing sampler for testing.
            - For code-development testing.
        *   - Classical
            - :ref:`dwave-samplers <index_samplers>`
              :class:`~dwave.samplers.greedy.sampler.SteepestDescentSolver`.
            - A steepest-descent solver for binary quadratic models.
            - For post-processing and convex problems.
        *   - Classical
            - :ref:`dwave-samplers <index_samplers>`
              :class:`~dwave.samplers.sa.sampler.SimulatedAnnealingSampler`
            - Simulated annealing sampler.
            -
        *   - Quantum
            - :doc:`dwave-system <index_system>`
              :class:`~dwave.system.samplers.DWaveSampler`
            - Quick incorporation of the |dwave_short| quantum computer as a
              sampler.
            - Typically part of a composite that handles
              :term:`minor-embedding`.
        *   - Quantum
            - :doc:`dwave-system <index_system>`
              :class:`~dwave.system.samplers.DWaveCliqueSampler`
            - Quick incorporation of the |dwave_short| quantum computer as a
              sampler.
            - Handles :term:`minor-embedding` for clique
              (:term:`complete graph`) problems.
        *   - Quantum
            - :doc:`dwave-cloud-client <index_cloud>` :code:`Solver()`
            - |dwave_short| quantum computer as a sampler.\ [#]_
            - For low-level control of problem submission.
        *   - Hybrid
            - :doc:`dwave-hybrid <index_hybrid>`
              :class:`~hybrid.reference.kerberos.KerberosSampler`
            - *dimod*-compatible hybrid asynchronous decomposition sampler.
            - For problems of arbitrary structure and size.
        *   - Hybrid
            - `Leap <https://cloud.dwavesys.com/leap/>`_ service's
              :class:`~dwave.system.samplers.LeapHybridNLSampler`
            - Cloud-based quantum-classical hybrid solver.
            - For application problems formulated as
              :ref:`nonlinear models <nl_model_sdk>`.
        *   - Hybrid
            - `Leap <https://cloud.dwavesys.com/leap/>`_ service's
              :class:`~dwave.system.samplers.LeapHybridCQMSampler`
            - Cloud-based quantum-classical hybrid solver.
            - For constrained quadratic models (:term:`CQM`) of arbitrary
              structure and size.
        *   -
            - :ref:`dimod <index_dimod>` custom
            - Write a custom sampler for special cases.
            - See examples in the :ref:`dimod <index_dimod>` reference
              documentation.

.. [#] This sampler is for low-level work on communicating with SAPI and is not
    a dimod sampler.

3. **Pre- and Post-Processing**

   Samplers can be composed of `composite patterns <https://en.wikipedia.org/wiki/Composite_pattern>`_
   that layer pre- and post-processing to binary quadratic programs without changing the
   underlying sampler.

   The table below shows some Ocean composites and considerations for selecting one or another.

   .. list-table:: Ocean Composites
      :widths: 10 50 50
      :header-rows: 1

      * - Tool & Composite
        - Usage
        - Notes
      * - :doc:`dwave-system </docs_system/sdk_index>` :class:`~dwave.system.composites.EmbeddingComposite`
        - Maps unstructured problems to a structured sampler.
        - Enables quick incorporation of the D-Wave system as a sampler by handling the :term:`minor-embedding`
          to the QPU's :term:`Chimera` topology of qubits.
      * - :doc:`dwave-system </docs_system/sdk_index>` :class:`~dwave.system.composites.FixedEmbeddingComposite`
        - Maps unstructured problems to a structured sampler.
        - Uses a pre-calculated minor-embedding for improved performance.
      * - :doc:`dwave-system </docs_system/sdk_index>` :class:`~dwave.system.composites.TilingComposite`
        - Tiles small problems multiple times to a Chimera-structured sampler.
        - Enables parallel sampling for small problems.
      * - :doc:`dimod </docs_dimod/sdk_index>` :class:`~dimod.reference.composites.tracking.TrackingComposite`
        - Tracks inputs and outputs.
        - Helps with testing and debugging.
      * - :std:doc:`dwave-preprocessing <oceandocs:docs_preprocessing/sdk_index>`
          :class:`~dwave.preprocessing.composites.SpinReversalTransformComposite`
        - Applies spin reversal transform preprocessing.
        - Improves QPU results by reducing the impact of possible analog and systematic errors.
      * - :doc:`dimod </docs_dimod/sdk_index>` :class:`~dimod.reference.composites.structure.StructureComposite`
        - Creates a structured composed sampler from an unstructured sampler.
        - Maps from a problem graph (e.g., a square graph) to a sampler's graph.

   In addition to composites that provide pre- and post-processing, Ocean also provides
   stand-alone tools to handle complex or large problems. For example:

   * :doc:`minorminer </docs_minorminer/source/sdk_index>` for :term:`minor-embedding`
     might be used to improve solutions by fine tuning parameters or incorporating problem
     knowledge into the embedding.
   * :ref:`dwave-samplers <index_dwave_samplers>` provides a steepest-descent solver
     for binary quadratic models that can be run on the samples returned from solvers such
     as :class:`~dwave.system.samplers.DWaveSampler` to find local minima in the neighbourhoods
   * :doc:`dwave-hybrid </docs_hybrid/sdk_index>` splits problems too large for the QPU into
     pieces solved either via a D-Wave system or a classical solver.

4. **Map to a Supported Format**

    Typically, you formulate your problem as a binary quadratic model (BQM), which you solve
    by submitting to the sampler (with its pre- and post-processing composite layers) you
    select based on the considerations listed above.

    Ocean provides tools for formulating the BQM:

    * :doc:`dwavebinarycsp </docs_binarycsp/sdk_index>` for constraint
      satisfaction problems with small constraints over binary variables. For example, many
      problems can be posed as satisfiability problems or with Boolean logic.
    * :doc:`dwave_networkx </docs_dnx/sdk_index>` for
      implementing graph-theory algorithms of the D-Wave system. Many problems can be
      posed in a form of graphs---this tool handles the construction of BQMs for several
      standard graph algorithms such as maximum cut, cover, and coloring.

    You might formulate a BQM mathematically; see :ref:`not` for a mathematical formulation
    for a two-variable problem.

    See the :std:doc:`system documents <sysdocs_gettingstarted:index>` for more information on techniques for formulating problems
    as BQMs.

5. **Formulate**

   The first step in solving a problem is to express it in a mathematical formulation.
   For example, the :ref:`map_coloring` problem is to assign a color to each region of a map
   such that any two regions sharing a border have different colors. To begin solving
   this problem on any computer, classical or quantum, it must be concretely defined;
   an intuitive approach, for the map problem, is to think of the regions as variables
   representing the possible set of colors, the values of which must be selected from
   some numerical scheme, such as natural numbers.

   The selection function must express the problem’s constraints:

   * Each region is assigned one color only, of C possible colors.
   * The color assigned to one region cannot be assigned to adjacent regions.

   Now solving the problem means finding a permissible value for each of the variables.

   When formulating a problem for the D-Wave system, bear in mind a few considerations:

   * Mathematical formulations must use binary variables because the solution is implemented
     physically with qubits, and so must translate to spins :math:`s_i \in {−1, +1}` or
     equivalent binary values :math:`x_i \in {0, 1}`.
   * Relationships between variables must be reducible to quadratic (e.g., a QUBO)
     because the problem’s parameters are represented by qubits’ weights and couplers’
     strengths on a QPU.
   * Formulations should be sparing in its number of variables because a QPU has a
     limited number of qubits and couplers.
   * Alternative formulations may have different implications for performance.

   Ocean demo applications, which formulate known problems, include:

   * `Structural Imbalance <https://github.com/dwave-examples/structural-imbalance>`_.
   * `Circuit-Fault Diagnosis <https://github.com/dwave-examples/circuit-fault-diagnosis>`_.


Top-Down Approach
-----------------
Another approach to envisioning how you can map your problem-solving process to Ocean
software is to start from the top---your (possibly abstractly defined) problem---and
work your way down the Ocean stack.

.. list-table:: Ocean Software
   :widths: 10 120
   :header-rows: 1

   * - Step
     - Description
   * - State the Problem
     - Define your problem concretely/mathematically; for example, as a constraint satisfaction
       problem or a graph problem.
   * - Formulate as a BQM
     - Reformulate an integer problem to use binary variables, for example, or convert a
       nonquadratic (high-order) polynomial to a QUBO.

       Ocean's :doc:`dwavebinarycsp </docs_binarycsp/sdk_index>` and :doc:`dwave_networkx </docs_dnx/sdk_index>`
       can be helpful for some problems.
   * - Decompose
     - Allocate large problems to classical and quantum resources.

       Ocean's :doc:`dwave-hybrid </docs_hybrid/sdk_index>` provides a framework and building
       blocks to help you create hybrid workflows.
   * - Embed
     - Consider whether your problem has repeated elements, such as logic gates, when
       deciding what tool to use to :term:`minor-embed` your BQM on the QPU. You might
       start with fully automated embedding (using :class:`~dwave.system.composites.EmbeddingComposite` for example)
       and then seek performance improvements through :doc:`minorminer </docs_minorminer/source/sdk_index>`.
   * - Configure the QPU
     - Use spin-reversal transforms to reduce errors, for example, or examine the annealing
       with reverse anneal. See the :std:doc:`system documents <sysdocs_gettingstarted:index>` for more information of features
       that improve performance.
