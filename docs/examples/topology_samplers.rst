.. _topology_samplers:

=================================
Working With Different Topologies
=================================

The examples shows how to construct software samplers with the same structure
as the :term:`QPU`, and how to work with :term:`embedding`\s with different
topologies.

The code examples below will use the following imports:

>>> import neal
>>> import dimod
>>> import dwave_networkx as dnx
>>> import networkx as nx
>>> import dwave.embedding
...
>>> from dwave.system import DWaveSampler, EmbeddingComposite

Creating a Chimera Sampler
--------------------------

As detailed in :ref:`using_cpu`, you might want to use a classical solver while
developing your code or writing tests. However, it is sometimes useful to
work with a software solver that behaves more like a quantum computer.

One of the key features of the quantum computer is its :term:`working graph`, which
defines the connectivity allowed by the :term:`binary quadratic model`.

To create a software solver with the same connectivity as a D-Wave 2000Q quantum computer
you first need a representation of the :term:`Chimera` graph which can be obtained
from the :doc:`dwave_networkx </docs_dnx/sdk_index>` project using the
:func:`~dwave_networkx.chimera_graph` function.

>>> C16 = dnx.chimera_graph(16)

Next, you need a software sampler. Use the
:class:`~neal.sampler.SimulatedAnnealingSampler` found in :doc:`dwave_neal </docs_neal/sdk_index>`,
though the :class:`~tabu.sampler.TabuSampler` from :doc:`dwave-tabu </docs_tabu/sdk_index>`
would work equally well.

.. dev note: we should maybe add a link to somewhere explaining the difference
.. between tabu/neal

>>> classical_sampler = neal.SimulatedAnnealingSampler()

Now, with a classical sampler and the desired graph, you can use 
:doc:`dimod </docs_dimod/sdk_index>`'s :class:`~dimod.reference.composites.structure.StructureComposite` 
to create a Chimera-structured sampler.

>>> sampler = dimod.StructureComposite(classical_sampler, C16.nodes, C16.edges)

This sampler accepts Chimera-structured problems. In this case, create an
:term:`Ising` problem.

>>> h = {v: 0.0 for v in C16.nodes}
>>> J = {(u, v): 1 for u, v in C16.edges}
>>> sampleset = sampler.sample_ising(h, J)

You can even use the sampler with the :class:`~dwave.system.composites.EmbeddingComposite`.

>>> embedding_sampler = EmbeddingComposite(sampler)

Finally, you can confirm that the sampler matches the :class:`~dwave.system.samplers.DWaveSampler`\ 's
structure. Make sure that the :term:`QPU` has the same topology you have
been simulating. Also note that the :term:`working graph` of the QPU is usually
a :term:`subgraph` of the full :term:`hardware graph`.

.. dev note: maybe in the future we want to talk about different topologies

>>> qpu_sampler = DWaveSampler(solver={'qpu': True, 'num_active_qubits__within': [2000, 2048]})
>>> QPUGraph = nx.Graph(qpu_sampler.edgelist)
>>> all(v in C16.nodes for v in QPUGraph.nodes)
True
>>> all(edge in C16.edges for edge in QPUGraph.edges)      # doctest: +SKIP
True


Creating a Pegasus Sampler
--------------------------

Another topology of interest is the :term:`Pegasus` topology.

As above, you can use the generator function :func:`dwave_networkx.pegasus_graph` found in
:doc:`dwave_networkx </docs_dnx/sdk_index>` and the
:class:`~neal.sampler.SimulatedAnnealingSampler` found in :doc:`dwave_neal </docs_neal/sdk_index>`
to construct a sampler.

>>> P6 = dnx.pegasus_graph(6)
>>> classical_sampler = neal.SimulatedAnnealingSampler()
>>> sampler = dimod.StructureComposite(classical_sampler, P6.nodes, P6.edges)

Working With Embeddings
-----------------------

The example above using the :class:`~dwave.system.composites.EmbeddingComposite`
hints that you might be interested in trying :term:`embedding` with different
topologies.

One thing you might be interested in is the :term:`chain length` when embedding
your problem. Say that you have a :term:`fully connected` problem with 40 variables
and you want to know the chain length needed to embed it on a 2048 node
:term:`Chimera` graph.

You can use :doc:`dwave-system </docs_system/sdk_index>`'s
:func:`~dwave.embedding.chimera.find_clique_embedding` function to find the
embedding and determine the maximum chain length.

>>> num_variables = 40
>>> embedding = dwave.embedding.chimera.find_clique_embedding(num_variables, 16)
>>> max(len(chain) for chain in embedding.values())
11

Similarly you can explore clique embeddings for a 40-variables fully connected
problem with a 680 node Pegasus graph using
:doc:`dwave-system </docs_system/sdk_index>`'s
:func:`~dwave.embedding.pegasus.find_clique_embedding` function

>>> num_variables = 40
>>> embedding = dwave.embedding.pegasus.find_clique_embedding(num_variables, 6)
>>> max(len(chain) for chain in embedding.values())
6
