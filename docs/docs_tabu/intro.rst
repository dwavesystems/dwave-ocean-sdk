.. attention::

    ``dwave-neal`` is deprecated since ``dwave-ocean-sdk`` 5.4.0 in favor of
    :ref:`index_dwave_samplers` and will be removed in ``dwave-ocean-sdk`` 7.0.0.

============
Introduction
============

*Samplers* are processes that sample from low energy states of a problem’s objective function.
A binary quadratic model (BQM) sampler samples from low energy states in models such as those
defined by an Ising equation or a Quadratic Unconstrained Binary Optimization (QUBO) problem
and returns an iterable of samples, in order of increasing energy. A dimod :term:`sampler` provides
‘sample_qubo’ and ‘sample_ising’ methods as well as the generic BQM sampler method.

The :class:`~tabu.TabuSampler` sampler implements the `MST2 multistart tabu search algorithm
<https://link.springer.com/article/10.1023/B:ANOR.0000039522.58036.68>`_
for quadratic unconstrained binary optimization (QUBO) problems
with a :std:doc:`dimod <oceandocs:docs_dimod/sdk_index>` Python wrapper.

For a description of the tabu search algorithm, see `tabu search <https://en.wikipedia.org/wiki/Tabu_search>`_\ .
