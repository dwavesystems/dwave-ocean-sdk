.. _solutions_sdk:

=========
Solutions
=========

:term:`sampler`\ s sample from low-energy states of a problem’s :term:`objective function`\ ---\
:term:`BQM` samplers sample from low-energy states in models such as those defined by an 
Ising equation or a QUBO problem---and return an iterable of samples, in order of increasing energy.

When the D‑Wave quantum computer solves a problem, it uses quantum phenomena such as superposition and tunneling to explore all possible solutions simultaneously and find a set of the best ones.
At the end of the computation (anneal), a single solution is sampled from a set of good solutions, 
with some probability, and returned. Because the sampled solution 
is probabilistic, different solutions may be returned in different runs. The standard way of submitting
a problem to the system requests many samples, not just one. This not only returns multiple 
“best” answers but also reduces the probability of settling on a suboptimal answer.

Some classical samplers might return non-probabilistic solutions; for example, 
the :doc:`dimod <oceandocs:docs_dimod/sdk_index>` :class:`~.ExactSolver` deterministically 
returns the best solution or solutions to small problems by calculating the result for
every configuration of variable values. Such samplers are called solvers.

Some Ocean functions might return a single best solution; for example, some 
:doc:`dwave-networkx <oceandocs:docs_dnx/sdk_index>` graph algorithms return 
only the lowest-energy sample.

SampleSets
----------

Ocean uses the :doc:`dimod <oceandocs:docs_dimod/sdk_index>` :class:`~.SampleSet`
class to hold samples and some additional information (e.g., timing information from some 
samplers). 

For the simple example three-variable "triangular" BQM,

.. math::

    E(\bf{s}) = - s_0 s_1 - s_0 s_2 + s_1 s_2
    \qquad\qquad s_i\in\{-1,+1\}

might be solved directly on a D-Wave 2000Q system by sampling 1000 times as follows, where the 
:class:`~.EmbeddingComposite` :term:`composite` maps the symbolic BQM to 
qubits on the quantum processor, which is called by the 
:class:`~.DWaveSampler` sampler:

>>> bqm = dimod.BQM({}, {('s0', 's1'): -1, ('s0', 's2'): -1, ('s1', 's2'): 1}, 0, dimod.Vartype.SPIN)  
>>> sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))     # doctest: +SKIP
>>> sampleset = sampler.sample(bqm, num_reads=1000)                      # doctest: +SKIP
>>> print(sampleset)                                                     # doctest: +SKIP
  s0 s1 s2 energy num_oc. chain_b.
0 -1 -1 +1   -1.0     141      0.0
1 +1 +1 +1   -1.0     132      0.0
2 -1 -1 -1   -1.0     159      0.0
3 -1 +1 -1   -1.0     143 0.333333
4 +1 +1 -1   -1.0      91      0.0
5 -1 +1 -1   -1.0      86      0.0
6 +1 +1 +1   -1.0     129 0.333333
7 +1 -1 +1   -1.0     119      0.0
['SPIN', 8 rows, 1000 samples, 3 variables]

The returned :class:`~.SampleSet`, in this case, shows eight solutions of
equal energy :math:`-1.0`. Solution :math:`s_0=-1, s_1=-1, s_2=+1` occurred
in 141 of the 1000 samples. Two solutions,  shown in line 3 and 6,
were based on a broken :term:`chain` of qubits that represented one of the variables.

For this submission to a D-Wave 2000Q, the sampleset also contained the following
additional information:

>>> print(sampleset.info.keys())
dict_keys(['timing', 'problem_id', 'embedding_context', 'warnings'])

For example, the `timing information <https://docs.dwavesys.com/docs/latest/doc_timing.html>`_ 
for the problem might look something like:

>>> print(sampleset.info["timing"])
{'qpu_sampling_time': 314960, 
'qpu_anneal_time_per_sample': 20, 
'qpu_readout_time_per_sample': 274, 
'qpu_access_time': 324321, 
'qpu_access_overhead_time': 5362, 
'qpu_programming_time': 9361, 
'qpu_delay_time_per_sample': 21, 
'total_post_processing_time': 409, 
'post_processing_overhead_time': 409, 
'total_real_time': 324321, 
'run_time_chip': 314960, 
'anneal_time_per_run': 20, 
'readout_time_per_run': 274} 

 

