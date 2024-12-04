.. _concept_samplesets:

========================
Samplesets and Solutions 
========================

:term:`sampler`\ s sample from low-energy states of a problem’s 
:term:`objective function`\ ---\ :term:`BQM` samplers sample from low-energy 
states in models such as those defined by an :term:`Ising` equation or a 
:term:`QUBO` problem---and return an iterable of samples, in order of increasing 
energy.

When a D‑Wave quantum computer solves a problem, it uses quantum phenomena such 
as superposition and tunneling to explore all possible solutions simultaneously 
and find a set of the best ones. At the end of the computation (anneal), a single 
solution is sampled from a set of good solutions, with some probability, and 
returned. Because the sampled solution is probabilistic, different solutions may 
be returned in different runs. The standard way of submitting a problem to the 
system requests many samples, not just one. This not only returns multiple 
“best” answers but also reduces the probability of settling on a suboptimal 
answer.

Some classical samplers might return non-probabilistic solutions; for example, 
the :ref:`sdk_index_dimod` :class:`~.ExactSolver` 
deterministically returns the best solution or solutions to small problems by 
calculating the result for every configuration of variable values. Such samplers 
are called solvers.

Some Ocean functions might return a single best solution; for example, some 
:ref:`sdk_index_dnx` graph algorithms return 
only the lowest-energy sample.

dimod provides a :class:`~dimod.SampleSet` class that contains, and enables you to
manipulate, samples.

For an introduction to returned solutions and samples, see
:ref:`concept_solutions`. For all supported sampleset
methods, see :ref:`sampleset`.

Example: Sampleset Returned from a Sampler
==========================================

This example creates a sample set and then demonstrates some :class:`~dimod.SampleSet`
properties and methods.

>>> bqm = dimod.generators.random.ran_r(1, 7)
>>> sampler = dimod.ExactSolver()
>>> sampleset = sampler.sample(bqm)

Print the best solution's energy.

>>> print(sampleset.first.energy)      # doctest:+SKIP
-9.0

Print the best solutions.

>>> print(sampleset.lowest())           # doctest:+SKIP
   0  1  2  3  4  5  6 energy num_oc.
0 +1 -1 +1 -1 +1 -1 -1   -9.0       1
1 +1 +1 +1 -1 +1 -1 -1   -9.0       1
...
7 -1 +1 -1 +1 -1 -1 +1   -9.0       1
['SPIN', 8 rows, 8 samples, 7 variables]

Convert to a third-party format
(`pandas <https://pandas.pydata.org/pandas-docs/stable/index.html>`_).

>>> sampleset.to_pandas_dataframe()       # doctest:+SKIP
     0  1  2  3  4  5  6  energy  num_occurrences
0   -1 -1 -1 -1 -1 -1 -1     3.0                1
1    1 -1 -1 -1 -1 -1 -1     7.0                1
2    1  1 -1 -1 -1 -1 -1     7.0                1
...

Example: Creating a Sampleset
=============================

This example creates a sample set from NumPy arrays.

>>> import numpy as np
>>> samples = np.random.randint(0, 2, (100, 10))
>>> energies = np.random.randint(-10, 0, 100)
>>> occurrences = np.random.randint(0, 50, 100)
>>> sampleset = dimod.SampleSet.from_samples(samples,
...                                          "BINARY",
...                                          energies,
...                                          num_occurrences=occurrences)

.. _concept_solutions:

=========
Solutions
=========

:term:`sampler`\ s sample from low-energy states of a problem’s 
:term:`objective function`\ ---\ :term:`BQM` samplers sample from low-energy 
states in models such as those defined by an :term:`Ising` equation or a 
:term:`QUBO` problem---and return an iterable of samples, in order of increasing 
energy.

When a D‑Wave quantum computer solves a problem, it uses quantum phenomena such 
as superposition and tunneling to explore all possible solutions simultaneously 
and find a set of the best ones. At the end of the computation (anneal), a single 
solution is sampled from a set of good solutions, with some probability, and 
returned. Because the sampled solution is probabilistic, different solutions may 
be returned in different runs. The standard way of submitting a problem to the 
system requests many samples, not just one. This not only returns multiple 
“best” answers but also reduces the probability of settling on a suboptimal 
answer.

Some classical samplers might return non-probabilistic solutions; for example, 
the :doc:`dimod <oceandocs:docs_dimod/sdk_index>` :class:`~.ExactSolver` 
deterministically returns the best solution or solutions to small problems by 
calculating the result for every configuration of variable values. Such samplers 
are called solvers.

Some Ocean functions might return a single best solution; for example, some 
:doc:`dwave-networkx <oceandocs:docs_dnx/sdk_index>` graph algorithms return 
only the lowest-energy sample.

SampleSets
----------

Ocean uses the :doc:`dimod <oceandocs:docs_dimod/sdk_index>` :class:`~dimod.SampleSet`
class to hold samples and some additional information (e.g., timing and 
:term:`minor-embedding` information from some samplers). 

As a simple example, this three-variable BQM,

.. math::

    E(\bf{s}) = - s_0 s_1 - s_0 s_2 + s_1 s_2
    \qquad\qquad s_i\in\{-1,+1\}

might be solved directly on a D-Wave quantum computer by sampling 1000 times. 
Here, the :class:`~.EmbeddingComposite` :term:`composite` maps the symbolic BQM 
to qubits on the quantum processor, which is called by the 
:class:`~.DWaveSampler` sampler:

>>> import dimod 
>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> s0, s1, s2 = dimod.Spins(['s0', 's1', 's2'])
>>> bqm = s1*s2 - s0*s1 - s0*s2   
>>> sampler = EmbeddingComposite(DWaveSampler())     
>>> sampleset = sampler.sample(bqm, num_reads=1000)                      
>>> print(sampleset)                                                     # doctest: +SKIP
  s0 s1 s2 energy num_oc. chain_.
0 -1 +1 -1   -1.0     183     0.0
1 -1 -1 +1   -1.0     141     0.0
2 -1 -1 -1   -1.0     206     0.0
3 +1 -1 +1   -1.0     162     0.0
4 +1 +1 +1   -1.0     123     0.0
5 +1 +1 -1   -1.0     185     0.0
['SPIN', 6 rows, 1000 samples, 3 variables]

The returned :class:`~dimod.SampleSet`, in this case, shows six solutions of
equal energy :math:`-1.0`. Solution :math:`s_0=-1, s_1=+1, s_2=-1` on the first 
line occurred in 183 of the 1000 samples. 

For this submission, the sampleset also contained the following additional 
information:

>>> print(sampleset.info.keys())    # doctest: +SKIP
dict_keys(['timing', 'problem_id', 'embedding_context', 'warnings'])

For example, the `timing information <https://docs.dwavesys.com/docs/latest/c_qpu_timing.html>`_ 
for the problem might look something like:

>>> print(sampleset.info["timing"])  # doctest: +SKIP
{'qpu_sampling_time': 85860.0, 
 'qpu_anneal_time_per_sample': 20.0, 
 'qpu_readout_time_per_sample': 45.32, 
 'qpu_access_time': 101619.97, 
 'qpu_access_overhead_time': 2259.03, 
 'qpu_programming_time': 15759.97, 
 'qpu_delay_time_per_sample': 20.54, 
 'total_post_processing_time': 2277.0, 
 'post_processing_overhead_time': 2277.0} 
