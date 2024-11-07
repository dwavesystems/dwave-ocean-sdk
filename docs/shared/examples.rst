
.. start_qpu1

The following code solves a random problem on a quantum computer.

>>> import dimod
>>> import dwave.system
...
>>> bqm = dimod.generators.ran_r(1, 20)
>>> sampler = dwave.system.EmbeddingComposite(dwave.system.DWaveSampler())
>>> sampleset = sampler.sample(bqm, num_reads=100)

.. end_qpu1

.. start_qpu2

The following code solves the known "minimum vertex cover" 
graph problem using an annealing quantum computer.   

>>> import networkx as nx
>>> import dwave_networkx as dnx
>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> s5 = nx.star_graph(4)
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> min_cover = dnx.min_vertex_cover(s5, sampler)

.. end_qpu2

.. start_nl1

The following code solves an illustrative 
`traveling-salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
using a quantum-classical hybrid solver in the Leap service. 

>>> from dwave.optimization.generators import traveling_salesperson
>>> from dwave.system import LeapHybridNLSampler
...
>>> DISTANCE_MATRIX = [
...     [0, 656, 227, 578, 489],
...     [656, 0, 889, 141, 170],
...     [227, 889, 0, 773, 705],
...     [578, 141, 773, 0, 161],
...     [489, 170, 705, 161, 0]]
...
>>> model = traveling_salesperson(distance_matrix=DISTANCE_MATRIX)
>>> sampler = LeapHybridNLSampler()                  
>>> results = sampler.sample(
...     model,
...     label='SDK Examples - TSP')  	# doctest: +SKIP
    
.. end_nl1


.. start_cqm1

The following code creates a constrained quadratic model (CQM) representing
a `knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ and
solves it using a quantum-classical hybrid solver in the Leap service. 

>>> from dimod.generators import random_knapsack 
>>> from dwave.system import LeapHybridCQMSampler
...
>>> cqm = random_knapsack(10)
>>> sampler = LeapHybridCQMSampler()
>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=180,
...                                label="SDK Examples - Bin Packing")  # doctest: +SKIP

.. end_cqm1
