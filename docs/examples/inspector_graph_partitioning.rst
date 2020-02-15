.. _inspector_graph_partitioning:

===========================
Using the Problem Inspector
===========================

This example solves a `graph partitioning <https://en.wikipedia.org/wiki/Graph_partition>`_
problem to show how D-Wave's `problem inspector </docs_inspector>` tool can help
you evaluate the minor-embedding used in your problem submissions to a QPU.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described
  in :ref:`sapi_access`.
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>` and
  :doc:`dwave-inspector </docs_inspector>`.

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
and ran :code:`dwave setup`, your installation should meet these requirements.
In D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ IDE, the default workspace
meets these requirements.

Solution Steps
==============

:ref:`solving_problems` describes the process of solving problems on the quantum
computer in two steps: (1) Formulate the problem as a :term:`binary quadratic model` (BQM)
and (2) Solve the BQM with a D-wave system or classical :term:`sampler`. In this example,
a :term:`QUBO` is formulated with simple math, the problem is submitted naively to
the QPU, its minor embedding examined using the problem inspector, and the
submission improved.

A Problem Graph
===============

This example uses a synthetic problem for illustrative purposes: a NetworkX
generated graph,
`NetworkX random_geometric_graph() <https://networkx.github.io/documentation/stable/reference/generators.html#module-networkx.generators.random>`_. The problem of interest here,
which is NP-hard, is to try and find the best division of the graph's nodes into two
equal sets with a minimum number of edges between the two groups.

.. code-block:: python

    import networkx as nx

    graph_nodes = 16
    G = nx.random_geometric_graph(n=graph_nodes, radius=.55, dim=2)

.. figure:: ../_static/inspector_rand_geom_plot.png
   :name: InspectorRandGeomProblem
   :alt: image
   :align: center
   :scale: 70 %

   One arbitrary generation of the problem graph.

Formulate the Problem as a BQM
==============================

This example formulates the BQM as a QUBO using the same steps described in
detail in the `Graph Partitioning <https://github.com/dwave-examples/graph-partitioning>`_
code example of the `D-Wave Code Examples <https://github.com/dwave-examples>`_ GitHub
repository.

.. code-block:: python

    from collections import defaultdict
    from itertools import combinations

    gamma = 80

    Q = defaultdict(int)

    # Fill in Q matrix
    for u, v in G.edges:
        Q[(u,u)] += 1
        Q[(v,v)] += 1
        Q[(u,v)] += -2

    for i in G.nodes:
        Q[(i,i)] += gamma*(1-len(G.nodes))

    for i, j in combinations(G.nodes, 2):
    	Q[(i,j)] += 2*gamma

Print the maximum and minimum QUBO values:

>>> print("Maximum element is {:.2f} and minimum is {:.2f}.".format(max(Q.values(), min(Q.values())))

Submit to the Quantum Computer
==============================

.. note:: Importing the problem inspector activates for the session the capture of
   data such as problems sent to the QPU and returned responses, relevant details of
   minor-embedding, and warnings. The recommended workflow is to import it at the
   start of your coding session or at least before submitting your problem, as is
   done below.

.. code-block:: python

    import numpy as np
    from dwave.system import DWaveSampler, EmbeddingComposite

    # Import the problem inspector to begin data capture
    import dwave.inspector

    sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
    response = sampler.sample_qubo(Q, num_reads=1000)

Check the best returned answer:

>>> print("Number of nodes in one set is {}, in the other, {}. Energy is {}.".format(
           sum(response.first.sample.values()),
           graph_nodes - sum(response.first.sample.values()),
           response.first.energy))

A simple evaluation of the overall quality of the returned samples:

>>> print(np.count_nonzero(response.record.chain_break_fraction > 0.33)


Inspect the Submission
========================


.. figure:: ../_static/inspector_rand_geom_broken_chains.png
   :name: InspectorRandGeomBrokenChains
   :alt: image
   :align: center
   :scale: 70 %

   Default chain strength: solutions.

.. figure:: ../_static/inspector_rand_geom_broken_chains_target.png
   :name: InspectorRandGeomBrokenChains1
   :alt: image
   :align: center
   :scale: 70 %

   Default chain strength: broken chain.


.. figure:: ../_static/inspector_rand_geom_no_broken_chains.png
   :name: InspectorRandGeomNoBrokenChains
   :alt: image
   :align: center
   :scale: 70 %

   Default chain strength: chain_strength=100.

Solve the Problem Using Hybrid Resources
========================================

Once you have a hybrid workflow, you can run and tune it within the dwave-hybrid framework
or convert it to a `dimod` sampler.

.. code-block:: python

    # Convert to dimod sampler and run workflow
    result = hybrid.HybridSampler(workflow).sample(bqm)

While the tabu search runs locally, one or more subproblems are sent to the QPU.

>>> print("Solution: sample={}".format(result.first)) # doctest: +SKIP
Solution: sample=Sample(sample={0: -1, 1: -1, 2: -1, 3: 1, 4: -1, ... energy=-169.0, num_occurrences=1)
