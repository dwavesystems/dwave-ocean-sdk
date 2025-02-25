.. _concept_samplers:

====================
Samplers and Solvers
====================

*Samplers* are processes that sample from low energy states of a problem's
:term:`objective function`. Ocean software provides
:ref:`quantum <qpu_intro_quantum_solvers>`,
:ref:`classical <qpu_intro_classical>`, and quantum-classical
:ref:`hybrid <opt_index_hybrid_solvers>` samplers that run either remotely (for
example, in the |cloud|_ service) or locally on your CPU. These compute
resources are known as solvers.

.. note:: Some classical samplers actually brute-force solve small problems
    rather than sample, and these are also referred to as “solvers”.

QPU and Classical Samplers
==========================

A BQM sampler samples from low-energy states in models such as those defined by
an :term:`Ising` equation or a Quadratic Unconstrained Binary Optimization
(:term:`QUBO`) problem and returns an iterable of samples, in order of
increasing energy.

:ref:`Ocean <index_ocean_sdk>` software provides a variety of
:ref:`dimod <index_dimod>` samplers, which all support ``sample_qubo`` and
``sample_ising`` methods as well as the generic ``bqm`` sampler method.

In addition to the :class:`~dwave.system.samplers.DWaveSampler()` class,
classical solvers, which run on CPUs, are available and useful for developing
code or on a small versions of a problem to verify code.

Hybrid Quantum-Classical Samplers
=================================

.. include:: ../shared/hybrid.rst
    :start-after: start_definition
    :end-before: end_definition

The |cloud|_ quantum cloud service provides state-of-the-art hybrid solvers you
can submit large-sized problems to. The :ref:`dwave-hybrid <index_hybrid>` tool
provides you with a Python framework for building a variety of flexible hybrid
workflows that use quantum and classical resources together to find good
solutions to your problem.

.. _concept_samplers_composites

Composites
==========

Samplers can be composed. The
`composite pattern <https://en.wikipedia.org/wiki/Composite_pattern>`_
allows layers of pre- and post-processing to be applied to binary quadratic
programs without needing to change the underlying sampler implementation.
These layers are referred to `composites`.
A composed sampler includes at least one sampler and possibly many composites.

Examples of composites are the
:class:`~dwave.system.composites.EmbeddingComposite()` class, which handles the
mapping known as :term:`minor-embedding`, and the
:class:`~dimod.reference.composites.roofduality.RoofDualityComposite()` class,
which uses
`roof duality <https://en.wikipedia.org/wiki/Pseudo-Boolean_function>`_ to
assign some variables as a pre-processing step before submitting the problem for
sampling.

The :ref:`dimod <index_dimod>` tool includes reference
:term:`samplers <sampler>` and :term:`composites <composite>` for processing
quadratic (and higher-order) models and refining sampling, and for testing your
code during development.

Creating Samplers
=================

.. todo:: replace the :ref:`api` anchor a links

The :ref:`dimod <index_dimod>` tool provides an :ref:`api` you can use to create
your own dimod samplers and composed samplers.

Examples
========

Using a Reference Sampler
-------------------------

To find solutions to the small four-node
`maximum cut <https://en.wikipedia.org/wiki/Maximum_cut>`_

.. todo:: fix this up once ocean packages are updated

:term:`BQM` generated in the :ref:`intro_models` section, shown again in the figure below,
you can use one of dimod's reference samplers: its
:class:`~dimod.reference.samplers.ExactSolver` test sampler, for example,
calculates the energy of all possible samples.

.. figure:: ../_images/four_node_star_graph.png
    :align: center
    :scale: 40 %
    :name: four_node_star_graph2
    :alt: Four-node star graph

    Star graph with four nodes.

>>> qubo = {(0, 0): -3, (1, 1): -1, (0, 1): 2, (2, 2): -1,
...         (0, 2): 2, (3, 3): -1, (0, 3): 2}
>>> dict_bqm = dimod.BQM.from_qubo(qubo)
>>> sampler_exact = dimod.ExactSolver()
>>> sampleset = sampler_exact.sample(dict_bqm)
>>> print(sampleset)
    0  1  2  3 energy num_oc.
1   1  0  0  0   -3.0       1
11  0  1  1  1   -3.0       1
2   1  1  0  0   -2.0       1
...
10  1  1  1  1    0.0       1
['BINARY', 16 rows, 16 samples, 4 variables]

Samplers can be composed. The
`composite pattern <https://en.wikipedia.org/wiki/Composite_pattern>`_ allows
layers of pre- and post-processing to be applied to quadratic programs for a
sampler implementation.

Using a Composed Sampler
------------------------

This example uses a composed sampler on the Boolean NOT Gate of the
:ref:`qpu_example_not` section.

The :class:`~dimod.reference.composites.structure.StructureComposite`
composite enforces the shape of the binary quadratic model. In this case we
only want to accept binary quadratic models with nodes labelled ``'x'``,
``'y'``, and ``'z'``.

>>> from dimod import ExactSolver, StructureComposite
>>> nodelist = ['x', 'y', 'z']
>>> edgelist = [('x', 'y'), ('x', 'z'), ('y', 'z')]
>>> composed_sampler = StructureComposite(ExactSolver(), nodelist, edgelist)
>>> Q = {('x', 'x'): -1, ('x', 'z'): 2, ('z', 'x'): 0, ('z', 'z'): -1}
>>> sampleset = composed_sampler.sample_qubo(Q)
>>> print(sampleset)
   x  z energy num_oc.
1  1  0   -1.0       1
3  0  1   -1.0       1
0  0  0    0.0       1
2  1  1    0.0       1
['BINARY', 4 rows, 4 samples, 2 variables]
>>> Q = {('a', 'a'): -1, ('a', 'b'): 2, ('b', 'a'): 0, ('b', 'b'): -1}
>>> try:
...     sampleset = composed_sampler.sample_qubo(Q)
... except ValueError:
...     print("incorrect structure!")
incorrect structure!

Creating a Sampler
------------------

This example creates a dimod sampler by implementing a single method (in this
example the :code:`sample_ising` method).

.. testcode::

    class LinearIsingSampler(dimod.Sampler):

        def sample_ising(self, h, J, **kwargs):
            kwargs = self.remove_unknown_kwargs(**kwargs)
            sample = linear_ising(h, J, **kwargs)  # Defined elsewhere
            energy = dimod.ising_energy(sample, h, J)
            return dimod.SampleSet.from_samples(sample, vartype=dimod.SPIN, energy=energy)

        @property
        def properties(self):
            return dict()

        @property
        def parameters(self):
            return dict()

The :class:`.Sampler` ABC provides the other sample methods "for free"
as mixins.