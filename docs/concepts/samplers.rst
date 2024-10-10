.. _concepts_samplers:

====================
Samplers and Solvers 
====================

Samplers
========

*Samplers* are processes that sample from low energy states of a problem’s :term:`objective function`. 
A BQM sampler samples from low energy states in models such as those
defined by an Ising equation or a Quadratic Unconstrained Binary Optimization (QUBO) problem
and returns an iterable of samples, in order of increasing energy.

Ocean software provides a variety of :doc:`dimod </docs_dimod/sdk_index>` samplers, which
all support ‘sample_qubo’ and ‘sample_ising’ methods as well as the generic BQM sampler method.
In addition to :class:`~dwave.system.samplers.DWaveSampler()`, classical solvers, which run on CPU or GPU, are available and
useful for developing code or on a small versions of a problem to verify code.

Hybrid Quantum-Classical Samplers
---------------------------------

Quantum-classical hybrid is the use of both classical and quantum resources to solve problems, exploiting the complementary strengths that each provides.

D-Wave's `Leap Quantum Application Environment <https://cloud.dwavesys.com/leap>`_
provides state-of-the-art hybrid solvers you can submit arbitrary BQMs to.
:std:doc:`dwave-hybrid <oceandocs:docs_hybrid/sdk_index>` provides you with a Python framework for
building a variety of flexible hybrid workflows that use quantum and classical
resources together to find good solutions to your problem.

Solvers
=======

Ocean software provides quantum, classical, and quantum-classical hybrid samplers that run either 
remotely (for example, in D-Wave’s Leap environment) or locally on your CPU. These compute resources 
are known as solvers.

.. note:: Some classical samplers actually brute-force solve small problems rather than sample, and 
   these are also referred to as “solvers”.

Composites
==========

Samplers can be composed. The `composite pattern <https://en.wikipedia.org/wiki/Composite_pattern>`_
allows layers of pre- and post-processing to be applied to binary quadratic programs without needing
to change the underlying sampler implementation. We refer to these layers as `composites`.
A composed sampler includes at least one sampler and possibly many composites.

Examples of composites are :class:`~dwave.system.composites.EmbeddingComposite()`,
which handle the mapping known as :term:`minor-embedding`,
and :class:`~dimod.reference.composites.roofduality.RoofDualityComposite()`, which 
uses `roof duality <https://en.wikipedia.org/wiki/Pseudo-Boolean_function>`_ to assign 
some variables as a pre-processing step before submitting the problem for sampling.

.. include:: ../ocean/docs_dimod/sdk_content.rst
  :start-after: start_samplers_composites
  :end-before: end_samplers_composites

The use of samplers in solving problems is described
in the following documentation:

*   :std:doc:`Solving Problems by Sampling <oceandocs:overview/samplers>`

    Describes the available types of samplers in Ocean and their use in solving :term:`BQM`\ s.

