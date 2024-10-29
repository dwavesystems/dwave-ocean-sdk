.. _qpu_index_intro:

==================================
Get Started with Quantum Computing 
==================================

.. toctree::
    :maxdepth: 1

    qpu_qa_explained
    qpu_gm_explained
    qpu_workflow
    qpu_intro_classical
    qpu_intro_quantum_solvers
    qpu_embedding_intro
    qpu_index_intro_examples
    
Example
=======

The following code solves the known "minimum vertex cover" 
graph problem using an annealing quantum computer.   

>>> import networkx as nx
>>> import dwave_networkx as dnx
>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> s5 = nx.star_graph(4)
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> min_cover = dnx.min_vertex_cover(s5, sampler)
