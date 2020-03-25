.. _using_qpu:

===============
Quantum Solvers
===============

Ocean's :doc:`dwave-system </docs_system/sdk_index>` tool enables
you to use a D-Wave system as a sampler. In addition to *DWaveSampler()*, the tool
provides a *EmbeddingComposite()* composite that maps unstructured problems to the graph
structure of the selected sampler, a process known as :term:`minor-embedding`.
For the AND gate of the :ref:`formulating_bqm` section, 

>>> import dimod
>>> bqm = dimod.BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0},
...                  {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0},
...                  0, 'BINARY')

the problem is defined on
alphanumeric variables :math:`x1, x2, y1`, that must be mapped to the QPU's numerically
indexed qubits.

Because of the sampler's probabilistic nature, you typically request multiple samples
for a problem; this example sets `num_reads` to 1000.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> sampleset = sampler.sample(bqm, num_reads=1000)   
>>> print(sampleset)   # doctest: +SKIP
  x1 x2 y1 energy num_oc. chain_b.
0  1  0  0    0.0     321      0.0
1  1  1  1    0.0      97      0.0
2  0  0  0    0.0     375      0.0
3  0  1  0    0.0     206      0.0
4  1  0  1    2.0       1 0.333333
['BINARY', 5 rows, 1000 samples, 3 variables]

Note that the first four samples are the valid states of the AND gate and have
lower energy than invalid state :math:`x1=1, x2=0, y1=1`.

Once you have configured a
:doc:`D-Wave Cloud Client configuration file </docs_cloud/sdk_index>` as described in
the :ref:`sapi_access` section, your default solver configuration is used when you
submit a problem without explicitly overriding it.

Several of the examples in the :ref:`gs` Example's section show how to submit problems
to D-Wave systems.
