.. _concept_samplesets:

========================
Samplesets and Solutions
========================

:term:`Samplers <sampler>` sample from low-energy states of a problem's
:term:`objective function`---:term:`BQM` samplers sample from low-energy states
in models such as those defined by an :term:`Ising` equation or a :term:`QUBO`
problem---and return an iterable of samples, in order of increasing energy.

When a |dwave_short| quantum computer solves a problem, it uses quantum
phenomena such as superposition and tunneling to explore all possible solutions
simultaneously and find a set of the best ones. At the end of the computation
(:term:`anneal`), a single solution is sampled from a set of good solutions,
with some probability, and returned. Because the sampled solution is
probabilistic, different solutions may be returned in different runs. The
standard way of submitting a problem to the system requests many samples, not
just one. This not only returns multiple “best” answers but also reduces the
probability of settling on a suboptimal answer.

Some :ref:`classical <qpu_classical_intro>` samplers might return
non-probabilistic solutions; for example, the :ref:`dimod <index_dimod>`
package's :class:`~dimod.ExactSolver` class deterministically returns the best
solution or solutions to small problems by calculating the result for every
configuration of variable values. Such samplers are called
:term:`solvers <solver>`.

Some :ref:`Ocean <index_ocean_sdk>` software functions might return a single
best solution; for example, some :ref:`dwave-networkx <index_dnx>` tool graph
algorithms return only the lowest-energy sample.

The :ref:`dimod <index_dimod>` package provides a :class:`~dimod.SampleSet`
class that contains, and enables you to manipulate, samples. It also contains
information such as timing and :term:`minor-embedding` from some samplers.

Example: Sampleset
==================

This example creates a sampleset and then demonstrates some properties and
methods of the :class:`~dimod.SampleSet` class.

>>> import dimod
...
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

Example: Sampleset from NumPy
=============================

This example creates a sampleset from :std:doc:`NumPy <numpy:index>` arrays.

>>> import numpy as np
>>> samples = np.random.randint(0, 2, (100, 10))
>>> energies = np.random.randint(-10, 0, 100)
>>> occurrences = np.random.randint(0, 50, 100)
>>> sampleset = dimod.SampleSet.from_samples(samples,
...                                          "BINARY",
...                                          energies,
...                                          num_occurrences=occurrences)

Example: Timing Information
===========================

As a simple example, this three-variable :term:`BQM`,

.. math::

    E(\bf{s}) = - s_0 s_1 - s_0 s_2 + s_1 s_2
    \qquad\qquad s_i\in\{-1,+1\}

might be solved directly on a |dwave_short| quantum computer by sampling 1000
times. Here, the :class:`~dwave.system.composites.EmbeddingComposite`
:term:`composite` maps the symbolic BQM to qubits on the quantum processor,
which is called by the :class:`~dwave.system.samplers.DWaveSampler` sampler:

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

The returned :class:`~dimod.SampleSet` object, in this case, shows six solutions
of equal energy :math:`-1.0`. Solution :math:`s_0=-1, s_1=+1, s_2=-1` on the
first line occurred in 183 of the 1000 samples.

For this submission, the sampleset also contained the following additional
information:

>>> print(sampleset.info.keys())    # doctest: +SKIP
dict_keys(['timing', 'problem_id', 'embedding_context', 'warnings'])

For example, the :ref:`timing information <qpu_operation_timing>` for the
problem might look something like:

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
