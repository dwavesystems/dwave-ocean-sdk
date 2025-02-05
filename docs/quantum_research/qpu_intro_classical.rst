.. _qpu_intro_classical:

=================
Classical Solvers
=================

.. todo:: update this is from sources:
	* Classical Solvers 
	  (https://docs.ocean.dwavesys.com/en/stable/overview/cpu.html)
	* dwave-samplers
	  (https://docs.ocean.dwavesys.com/en/stable/docs_samplers/index.html)


You might use a classical solver while developing your code or on a small version of
your problem to verify your code.
To solve a problem classically on your local machine, you configure a classical solver,
either one of those included in the Ocean tools or your own.

Examples
~~~~~~~~

Among several samplers provided in the :doc:`dimod </docs_dimod/sdk_index>`
tool for testing your code locally, is the :class:`~dimod.reference.samplers.ExactSolver` 
that calculates the energy of all
possible samples for a given problem. Such a sampler can solve a small three-variable
problem such as a BQM representing a Boolean AND gate (see also the 
:ref:`formulating_bqm` section) as follows:

>>> from dimod.generators import and_gate
>>> from dimod import ExactSolver
>>> bqm = and_gate('in1', 'in2', 'out')
>>> sampler = ExactSolver()
>>> sampleset = sampler.sample(bqm)    
>>> print(sampleset)       # doctest: +SKIP
  in1 in2 out energy num_oc.
0   0   0   0    0.0       1
1   1   0   0    0.0       1
3   0   1   0    0.0       1
5   1   1   1    0.0       1
2   1   1   0    2.0       1
4   0   1   1    2.0       1
6   1   0   1    2.0       1
7   0   0   1    6.0       1
['BINARY', 8 rows, 8 samples, 3 variables]

Note that the first four samples are the valid states of the AND gate and have
lower values than the second four, which represent invalid states.

If you use a classical solver running locally on your CPU, a single sample might provide
the optimal solution.

This example solves a two-variable problem using the :ref:`dwave-samplers <index_dwave_samplers>`
simulated annealing sampler. For such a small problem, :code:`num_reads=10` most likely
finds the optimal solution.

>>> from dwave.samplers import SimulatedAnnealingSampler
>>> solver = SimulatedAnnealingSampler()
>>> sampleset = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1}, num_reads=10)
>>> sampleset.first.sample["a"] == sampleset.first.sample["b"] == -1
True


.. include:: ../ocean/docs_samplers/README.rst
  :start-after: index-start-marker
  :end-before: index-end-marker
