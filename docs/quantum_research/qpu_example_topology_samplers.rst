.. _qpu_example_topology_samplers:

=================================
Working With Different Topologies
=================================

The examples below show how to construct software samplers with the same structure
as the :term:`QPU`, and how to work with :term:`embedding`\s with different
topologies.

The code examples below uses the following imports:

>>> import dimod
>>> import dwave_networkx as dnx
>>> import networkx as nx
>>> import dwave.embedding
...
>>> from dwave.samplers import SimulatedAnnealingSampler
>>> from dwave.system import DWaveSampler, EmbeddingComposite

Creating a Pegasus Sampler
--------------------------

As detailed in :ref:`using_cpu`, you might want to use a classical solver while
developing your code or writing tests. However, it is sometimes useful to
work with a software solver that behaves more like a quantum computer.

One of the key features of the quantum computer is its :term:`working graph`, 
which defines the connectivity allowed by the :term:`binary quadratic model`.

To create a software solver with the same connectivity as an Advantage quantum 
computer you first need a representation of the :term:`Pegasus` graph which can 
be obtained from the :doc:`dwave_networkx </docs_dnx/sdk_index>` project using 
the :func:`~dwave_networkx.pegasus_graph` function.

>>> P16 = dnx.pegasus_graph(16)

Next, you need a software sampler and can use the 
:class:`~dwave.samplers.SimulatedAnnealingSampler`  
(:class:`~dwave.samplers.TabuSampler` works equally well).

.. dev note: we should maybe add a link to somewhere explaining the difference
.. between tabu/neal

>>> classical_sampler = SimulatedAnnealingSampler()

Now, with a classical sampler and the desired graph, you can use
:doc:`dimod </docs_dimod/sdk_index>`'s 
:class:`~dimod.reference.composites.structure.StructureComposite` to create a 
Pegasus-structured sampler.

>>> sampler = dimod.StructureComposite(classical_sampler, P16.nodes, P16.edges)

This sampler accepts Pegasus-structured problems. For example, create an
:term:`Ising` problem.

>>> h = {v: 0.0 for v in P16.nodes}
>>> J = {(u, v): 1 for u, v in P16.edges}
>>> sampleset = sampler.sample_ising(h, J)

You can even use the sampler with the :class:`~dwave.system.composites.EmbeddingComposite`.

>>> embedding_sampler = EmbeddingComposite(sampler)

Finally, you can confirm that the sampler matches the 
:class:`~dwave.system.samplers.DWaveSampler`\ 's
structure. Make sure that the :term:`QPU` has the same topology you have
been simulating. Also note that the :term:`working graph` of the QPU is usually
a :term:`subgraph` of the full :term:`hardware graph`.

.. dev note: maybe in the future we want to talk about different topologies

>>> qpu_sampler = DWaveSampler(solver=dict(topology__type='pegasus'))
>>> qpu_graph = qpu_sampler.to_networkx_graph()
>>> qpu_graph.nodes <= P16.nodes     # doctest: +SKIP
True
>>> qpu_graph.edges <= P16.edges      # doctest: +SKIP
True

Creating a Zephyr Sampler
-------------------------

Another topology of interest is the :term:`Zephyr` topology.

As above, you can use the generator function :func:`dwave_networkx.zephyr_graph` 
found in :doc:`dwave_networkx </docs_dnx/sdk_index>` and the
:class:`~dwave.samplers.SimulatedAnnealingSampler` to construct a sampler.

>>> Z3 = dnx.zephyr_graph(3)
>>> classical_sampler = SimulatedAnnealingSampler()
>>> sampler = dimod.StructureComposite(classical_sampler, Z3.nodes, Z3.edges)

Working With Embeddings
-----------------------

The example above using the :class:`~dwave.system.composites.EmbeddingComposite`
hints that you might be interested in trying :term:`embedding` with different
topologies.

One thing you might be interested in is the :term:`chain length` when embedding
your problem. For example, if you have a :term:`fully connected` problem with 40 
variables and you want to know the chain length needed to embed it on a 5000+ 
node :term:`Pegasus` graph.

You can use :doc:`dwave-system </docs_system/sdk_index>`'s
:func:`~dwave.embedding.pegasus.find_clique_embedding` function to find the
embedding and determine the maximum chain length.

>>> num_variables = 40
>>> embedding = dwave.embedding.pegasus.find_clique_embedding(num_variables, 16)
>>> max(len(chain) for chain in embedding.values())
5

Similarly you can explore clique embeddings for a 40-variables fully connected
problem with a 300+ node Zephyr graph using
:doc:`dwave-system </docs_system/sdk_index>`'s
:func:`~dwave.embedding.zephyr.find_clique_embedding` function

.. dev note: skip doctest until SDK has https://github.com/dwavesystems/dwave-system/pull/490

>>> num_variables = 40
>>> embedding = dwave.embedding.zephyr.find_clique_embedding(num_variables, 3)  # doctest: +SKIP
>>> max(len(chain) for chain in embedding.values()) # doctest: +SKIP
4
