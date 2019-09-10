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

As detailed in :ref:`cpu`, you might want to use a classical solver while
developing your code or writing tests. However, it is sometimes useful to
work with a software solver that behaves more like a quantum computer.

One of the key features of the quantum computer is its :term:`working graph`, which
defines the connectivity allowed by the :term:`binary quadratic model`.

To create a software solver with the same connectivity as a D-Wave 2000Q quantum computer
we first need a representation of the :term:`Chimera` graph which can be obtained
from the :std:doc:`dwave_networkx <networkx:index>` project using the
:func:`~dwave_networkx.chimera_graph` function.

>>> C16 = dnx.chimera_graph(16)

Next, we need a software sampler. We will use the
:class:`neal.SimulatedAnnealingSampler` found in :std:doc:`dwave_neal <neal:index>`,
though the :class:`tabu.TabuSampler` from :std:doc:`dwave-tabu <tabu:index>`
would work equally well.

.. dev note: we should maybe add a link to somewhere explaining the difference
.. between tabu/neal

>>> classical_sampler = neal.SimulatedAnnealingSampler()

Now, with a classical sampler and the desired graph, we can use
:std:doc:`dimod <dimod:index>`'s :class:`dimod.StructuredComposite` to create
a Chimera-structured sampler.

>>> sampler = dimod.StructureComposite(classical_sampler, C16.nodes, C16.edges)

This sampler accepts Chimera-structured problems. In this case we create an
:term:`Ising` problem.

>>> h = {v: 0.0 for v in C16.nodes}
>>> J = {(u, v): 1 for u, v in C16.edges}
>>> sampleset = sampler.sample_ising(h, J)

We can even use the sampler with the :class:`dwave.system.EmbeddingComposite`

>>> embedding_sampler = EmbeddingComposite(sampler)

Finally, we can confirm that our sampler matches the :obj:`dwave.system.DWaveSampler`'s
structure. We make sure that our :term:`QPU` has the same topology we have
been simulating. Also note that the :term:`working graph` of the QPU is usually
a :term:`subgraph` of the full :term:`hardware graph`.

.. dev note: maybe in the future we want to talk about different topologies

>>> qpu_sampler = DWaveSampler(solver={'qpu': True, 'num_active_qubits__within': [2000, 2048]})
>>> QPUGraph = nx.Graph(qpu_sampler.edgelist)
>>> all(v in C16.nodes for v in QPUGraph.nodes)
True
>>> all(edge in C16.edges for edge in QPUGraph.edges)
True


Creating a Pegasus Sampler
--------------------------

Another topology of interest is the :term:`Pegasus` topology.

As above, we can use the generator function :func:`dwave_networkx.pegasus_graph` found in
:std:doc:`dwave_networkx <networkx:index>` and the
:class:`neal.SimulatedAnnealingSampler` found in :std:doc:`dwave_neal <neal:index>`
to construct a sampler.

>>> P6 = dnx.pegasus_graph(6)
>>> classical_sampler = neal.SimulatedAnnealingSampler()
>>> sampler = dimod.StructureComposite(classical_sampler, P6.nodes, P6.edges)

Working With Embeddings
-----------------------

The example above using the :class:`~dwave.system.EmbeddingComposite`
hints that we might be interested in trying :term:`embedding` with different
topologies.

One thing we might be interested in is the :term:`chain length` when embedding
our problem. Say that we have a :term:`fully connected` problem with 40 variables
and we want to know the chain length needed to embed it on a 2048 node
:term:`Chimera` graph.

We can use :std:doc:`dwave-system <system:index>`'s
:func:`~dwave.embedding.chimera.find_clique_embedding` function to find the
embedding and determine the maximum chain length.

>>> num_variables = 40
>>> embedding = dwave.embedding.chimera.find_clique_embedding(num_variables, 16)
>>> max(len(chain) for chain in embedding.values())
11

Similarly we can explore clique embeddings for a 40-variables fully connected
problem with a 680 node Pegasus graph using
:std:doc:`dwave-system <system:index>`'s
:func:`~dwave.embedding.pegasus.find_clique_embedding` function

>>> num_variables = 40
>>> embedding = dwave.embedding.pegasus.find_clique_embedding(num_variables, 6)
>>> max(len(chain) for chain in embedding.values())
6
