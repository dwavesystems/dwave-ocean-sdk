.. _qpu_intro_quantum_solvers:

===============
Quantum Solvers
===============

Ocean's :doc:`dwave-system </docs_system/sdk_index>` tool enables
you to use a D-Wave system as a sampler. In addition to 
:class:`~dwave.system.samplers.DWaveSampler`, the tool
provides a :class:`~dwave.system.composites.EmbeddingComposite` composite 
that maps unstructured problems to the graph
structure of the selected sampler, a process known as :term:`minor-embedding`.

For a BQM representing a Boolean AND gate (see also the :ref:`formulating_bqm` 
section) the problem is defined on alphanumeric variables :math:`in1, in2, out` 
that must be mapped to the QPU's numerically indexed qubits.

>>> from dimod.generators import and_gate
>>> bqm = and_gate('in1', 'in2', 'out')

Because of the sampler's probabilistic nature, you typically request multiple samples
for a problem; this example sets `num_reads` to 1000.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> sampleset = sampler.sample(bqm, num_reads=1000)   
>>> print(sampleset)   # doctest: +SKIP
  in1 in2 out energy num_oc. chain_.
0   1   0   0    0.0     321     0.0
1   1   1   1    0.0      97     0.0
2   0   0   0    0.0     375     0.0
3   0   1   0    0.0     206     0.0
4   1   0   1    2.0       1 0.33333
['BINARY', 5 rows, 1000 samples, 3 variables]

Note that the first four samples are the valid states of the AND gate and have
lower energy than invalid state :math:`in1=1, in2=0, out=1`.

Once you have configured a
:doc:`D-Wave Cloud Client configuration file </docs_cloud/sdk_index>` as described in
the :ref:`sapi_access` section, your default solver configuration is used when you
submit a problem without explicitly overriding it.

Several of the examples in the :ref:`gs` Example's section show how to submit problems
to D-Wave systems.
