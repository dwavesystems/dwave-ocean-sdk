.. _qpu_decomposing:

==========================
Decomposing Large Problems
==========================

part requiring no more than the number of qubits available on the QPU and,
optionally for hybrid approaches, parts suited to conventional compute
platforms. Detailed information is available in the literature and referenced
papers to guide actual implementation.

The :std:doc:`dwave-hybrid <oceandocs:docs_hybrid/sdk_index>` package
provides decomposition tools.

.. _cb_decomposing_energy_impact:

Energy-Impact Decomposing
=========================

One approach to decomposition, implemented by the
:class:`~hybrid.decomposers.EnergyImpactDecomposer` class, is to select a
subproblem of variables maximally contributing to the problem energy.

The example illustrated in :numref:`Figure %s <decomposingEnergyImpact>`
shows a large problem decomposed into smaller subproblems.

.. figure:: ../../_images/decomposing_energy_impact.png
    :align: center
    :name: decomposingEnergyImpact
    :alt: A large problem decomposed into small subproblems by highest energy.

    A problem too large to be embedded in its entirety on the QPU is
    sequentially decomposed into smaller problems, each of which can fit on the
    QPU, with variables selected by highest impact on energy.

Variables selected solely by maximal energy impact may not be directly connected
(no shared edges) and might not represent a local structure of the problem.
Configuring a mode of traversal such as breadth-first (BFS) or priority-first
selection (PFS) can capture features that represent local structures within a
problem.

.. figure:: ../../_images/decomposing_energy_impact_bfs_pfs.png
    :align: center
    :name: decomposingEnergyImpactBfsPfs
    :alt: A large problem decomposed into small subproblems by highest energy
        and mode of traversal.

    BFS starts with the node with maximal energy impact, from which its graph
    traversal proceeds to directly connected nodes, then nodes directly
    connected to those, and so on, with graph traversal ordered by node index.
    In PFS, graph traversal selects the node with highest energy impact among
    unselected nodes directly connected to any already selected node.

Example
-------

This example creates a hybrid decomposer that uses breadth-first traversal from
the variable with the largest energy impact, selecting 50 variables for each
subproblem.

>>> from hybrid.decomposers import EnergyImpactDecomposer
...
>>> decomposer = EnergyImpactDecomposer(size=50,
...                                     rolling_history=0.85,
...                                     traversal="bfs")

Further Information
-------------------

*   The :std:doc:`dwave-hybrid <oceandocs:docs_hybrid/sdk_index>` package
    explains energy-impact decomposition and shows implementation examples.
*   `Hybrid Computing Jupyter Notebooks <https://github.com/dwave-examples/hybrid-computing-notebook>`_.

.. _cb__decomposing_cutset:

Cutset Conditioning
===================

Cutset conditioning conditions on a subset of variables (the "cutset") of a
graph, leaving the remaining network as a tree with complexity that is
exponential in the cardinality (size) of the cutset.

Chose a subset :math:`\setminus A` of variables :math:`A` to fix throughout the
algorithm so that the graph of :math:`E(\vc{s}_A,\vc{s}_{\setminus A})`, where
:math:`\argmin_{\vc{s}_A} E(\vc{s}_A,\vc{s}_{\setminus A})`
is the optimal setting of :math:`\vc{s}_A` for a given
:math:`\vc{s}_{\setminus A}`,
breaks into separate components that can be solved independently:

.. math::
    \mathcal{E}(\vc{s}_{\setminus A}) = E_{\setminus A}(\vc{s}_{\setminus A}) +
    \sum_\alpha \mathcal{E}_\alpha(\vc{s}_{\setminus A})

where :math:`\vc{s}_A = \bigcup_\alpha \vc{s}_{A_\alpha}` and
:math:`\vc{s}_{A_\alpha} \cap \vc{s}_{A_{\alpha'}}=\emptyset` for
:math:`\alpha \not = \alpha'`.

Choose a cutset such that each of the remaining :math:`\min_{\vc{s}_{A_\alpha}}`
problems is small enough to be solved on the |dwave_short| QPU.

Example
-------

A small example is illustrated in :numref:`Figure %s <beforeadterconditioning>`.

.. figure:: ../../_images/primalGraph-CutSetGraph.png
    :align: center
    :name: beforeadterconditioning
    :alt: Two diagrams showing an 8 variable graph before and after cutset
        conditioning. Variables are numbered S 1 to S 8. The diagram on the left
        shows the variables connected, before conditioning. The diagram on the
        right shows the graph after it is conditioned on variable S 1 and
        therefore decomposed into 3 smaller subproblems.

    8-variable graph, before (left) and after (right) conditioning. If the graph
    is conditioned on variable :math:`s_1`, it decomposes into 3 smaller
    subproblems. The remaining variable sets
    :math:`\vc{s}_A=\{s_2,s_3\}\cup\{s_4,s_5,s_6\}\cup \{s_7,s_8\}` define three
    decoupled subproblems.


To simplify outer optimization, make the number of conditioned variables
as small as possible.

Further Information
-------------------

*   [Dec1987]_ discusses this method for improving search performance in AI
    applications.
*   [Bas2020]_ explores multiple approaches to solving benchmark problems.

.. _cb_decomposing_branch_bound:

Branch-and-Bound Algorithms
===========================

Branch-and-bound algorithms progressively condition more variables to either
:math:`s_i=-1` or :math:`s_i=1`, for spins, defining a *split* at node
:math:`s_i`. Further splits define a branching binary tree with leaves defining
the :math:`2^N` configurations where all variables are assigned values. At each
node a branch is pruned if no leaf node below it can contain the global optimum.

Example: Best Completion Estimate
---------------------------------

Branch-and-bound can benefit from using the |dwave_short| system
to terminate searches higher in the tree.

Condition sufficient variables so the remaining can be optimized by the QPU.
Instead of exploring deeper, call the QPU to estimate the best completion from
that node. As the upper bound is minimized through subsequent QPU completions,
this may in turn allow for future pruning.

.. note::
    Since the QPU solution does not come with a proof of optimality, this
    algorithm may not return a global minimum.

Example: Lower Bounds
---------------------

The |dwave_short| system can also provide tight lower-bound functions at any
node in the search tree.

Lagrangian relaxation finds these lower bounds by first dividing a node in the
graph representing variable :math:`s_i` in two (\ :math:`s_i^{(1)}` and
:math:`s_i^{(2)}`) with constraint :math:`s_i^{(1)} = s_i^{(2)}`. The original
objective :math:`E(s_i,\vc{s}_{\setminus i})` becomes
:math:`E'(s_i^{(1)}, s_i^{(2)},\vc{s}_{\setminus i})`, leaving the problem
unchanged. With sufficient divided variables to decompose :math:`E'` into
smaller independent problems the equality constraints are softened and treated
approximately:

The Lagrangian for the constrained problem is

.. math::
    L(s_i^{(1)},s_i^{(2)},\vc{s}_{\setminus i}; \lambda_i) =
    E'(s_i^{(1)},s_i^{(2)},\mathbf{s}_{\setminus i}) +
    \lambda_i(s_i^{(1) }- s_i^{(2)}).

Where :math:`\lambda_i` is a multiplier for the equality constraint. Maximizing
the dual function with respect to :math:`\lambda_i`,

.. math::
    g(\lambda_i) = \min_{s_i^{(1)},s_i^{(2)},\vc{s}_{\setminus i}}
    L(s_i^{(1)},s_i^{(2)},\vc{s}_{\setminus i}; \lambda_i),

provides the tightest possible lower bound.

Introduce enough divided variables to generate subproblems small enough to solve
on the QPU and then optimize each subproblem's dual function using a subgradient
method to provide the tightest possible lower bounds.

As an example, consider again the small 8-variable problem, shown on the left
side in :numref:`Figure %s <primalGraph-SplitGraph>`.

.. figure:: ../../_images/primalGraph-SplitGraph.png
    :align: center
    :name: primalGraph-SplitGraph
    :alt: Two diagrams showing an 8 variable graph before and after splitting
        into two separate subproblems. Variables are numbered S 1 to S 8. The
        diagram on the left shows the variables  connected, before splitting.
        The diagram on the right shows the graph after it is split on variable
        S1. The resulting two problems both include a copy of variable S1.

    8-variable graph, before (left) and after (right) splitting.

The Lagrangian relaxed version of the problem obtained by dividing variable
:math:`s_1` is shown on the right. The constraint :math:`s_1^{(1)}=s_1^{(2)}` is
treated softly giving two independent subproblems consisting of variable sets
:math:`{s_1^{(1)}, s_2, s_3, s_7, s_8}` and :math:`{s_1^{(2)}, s_4, s_5, s_6}`.
If either subproblem is still too large, it can be decomposed further either
through another variable division or through conditioning.

Further Information
-------------------

*   [Bac2018]_ provides a method for verifying the output of quantum optimizers
    with ground-state energy lower bounds; notably, each step in the process
    requires only an effort polynomial in the system size.
*   [Bor2008]_ provides a max-flow approach to improved lower bounds for
    quadratic unconstrained binary optimization (QUBO).
*   [Boy2007]_ gives a concise introduction to subgradient methods.
*   [Bru1994]_ describes applying the branch-and-bound algorithm to the job shop
    scheduling problem.
*   [Glo2017]_ discusses preprocessing rules that reduce graph size.
*   [Ham1984]_ discusses roof duality, complementation and persistency in
    quadratic 0–1 optimization.
*   [Joh2007]_ gives an alternative to subgradient optimization, which examines
    a smooth approximation to dual function.
*   [Mar2007]_ considers ways to explore the search tree, including dynamic
    variable orderings and best-first orderings.
*   [Mon2020]_ describes a quantum algorithm that can accelerate classical
    branch-and-bound algorithms.
*   [Nar2017]_ propose a decomposition method more effective than
    branch-and-bound, which is implemented for the maximum clique problem.
*   [Ron2016]_ provides a method for solving constrained quadratic binary
    problems via quantum adiabatic evolution.
*   [Ros2016]_ discusses branch-and-bound heuristics in the context of the
    |dwave_short| Chimera architecture.

.. _cb_decomposing_large_neighborhood:

Large-Neighborhood Local Search Algorithms
==========================================

Local search algorithms improve upon a candidate solution, :math:`\vc{s}^t`,
available at iteration :math:`t` by searching for better solutions within some
local neighborhood of :math:`\vc{s}^t`.

Quantum annealing can be very simply combined with local search to allow the
local search algorithm to explore much larger neighborhoods than the standard
1-bit-flip Hamming neighborhood.

For a problem of :math:`N` variables and a neighborhood around configuration
:math:`\vc{s}^t` of all states within Hamming distance :math:`d` of
:math:`\vc{s}^t`, choose one of :math:`\binom{N}{d}`, and determine the best
setting for these :math:`\vc{s}_A` variables given the fixed context of the
conditioned variables :math:`\vc{s}^{t}_{\setminus A}`. Select :math:`d` small
enough to solve on the QPU. If no improvement is found within the chosen subset,
select another.

Further Information
-------------------

*   [Ahu2000]_ describes the cyclic exchange neighborhood, a generalization of
    the two-exchange neighborhood algorithm.
*   [Glo1990]_ is a tutorial on the tabu search algorithm.
*   [Liu2005]_ presents promising results for even small neighborhoods
    of size :math:`d\le 4`.
*   [Mar2018]_ proposes a variable neighbourhood search heuristic for the
    conformational problem, the three-dimensional spatial arrangements of
    constituent atoms of molecules. 

.. _cb_decomposing_belief_propagation:

Belief Propagation
==================

The belief propagation algorithm passes messages between regions and variables
that represent beliefs about the minimal energy conditional on each possible
value of a variable. It can be used, for example, to calculate approximate, and
in some cases exact, marginal probabilities in Bayes nets.

Further Information
-------------------

*   [Bia2014]_ discusses belief propagation in the context of decomposing
    CSPs into subproblems small enough to be embedded onto the QPU.
*   [Cou2009]_ is a tutorial on the subject.
*   [Pea2008]_ describes the belief propagation algorithm.

