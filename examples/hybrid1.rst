.. _hybrid1:

=====================
Many-Variable Problem
=====================

This example solves a graph problem with too many variables to fit onto the QPU.

The purpose of this example is to illustrate a hybrid solution---the combining of
classical and quantum resources---to a problem that cannot be mapped in its entirety
to the D-Wave system due to the number of its variables. Hard optimization problems
might have many variables; for example, scheduling or allocation of resources. In such cases,
quantum resources are used as an accelerator much as GPUs are for graphics.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in :ref:`dwavesys`.
* Ocean tools :std:doc:`dwave-system <system:index>`,  :std:doc:`dimod <dimod:index>`, and
  :std:doc:`dwave-hybrid <hybrid:index>`.

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
and ran :code:`dwave config create`, your installation should meet these requirements.


Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems on the quantum
computer in two steps: (1) Formulate the problem as a :term:`binary quadratic model` (BQM)
and (2) Solve the BQM with a D-wave system or classical :term:`sampler`. This example
uses :std:doc:`dwave-hybrid <hybrid:index>` to combine a tabu search on a CPU with
the submission of parts of the (large) problem to the D-Wave system.


Formulate the Problem
=====================

This example uses a synthetic problem for illustrative purposes: a NetworkX
generated graph,
`NetworkX barabasi_albert_graph() <https://networkx.github.io/documentation/stable/reference/generators.html#module-networkx.generators.random>`_\ , with random +1 or -1
couplings assigned to its edges.

.. code-block:: python

    # Represent the graph problem as a binary quadratic model
    import dimod
    import networkx as nx
    import random
    G = nx.barabasi_albert_graph(100, 3, seed=1)
    h = {v: 0. for v in G.nodes}
    J = {tuple(c): random.choice([-1, 1]) for c in G.edges}
    bqm = dimod.BQM(h, J, offset=0, vartype='SPIN')

Create a Hybrid Workflow
========================



.. code-block:: python

    # Set a workflow of tabu search in parallel to submissions to a D-Wave system
    import hybrid
    iteration = hybrid.RacingBranches(
        hybrid.InterruptableTabuSampler(),
        hybrid.EnergyImpactDecomposer(size=30, rolling=True, rolling_history=0.15)
        | hybrid.QPUSubproblemAutoEmbeddingSampler()
        | hybrid.SplatComposer()
    ) | hybrid.ArgMin()
    workflow = hybrid.LoopUntilNoImprovement(iteration, convergence=3)


Solve the Problem Using Hybrid Resources
========================================



.. code-block:: python

    # Provide some initial solution and improve it through tabu search and sampling
    init_state = hybrid.State.from_problem(bqm)
    result = workflow.run(init_state).result()

    print("Solution: sample={.samples.first}".format(final_state))
