.. _index_quantum_research:

================
Quantum Research
================

.. toctree::
    :hidden:
    :maxdepth: 1

    qpu_index_intro
    qpu_index_about
    qpu_index_using

.. sections-start-marker

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`qpu_index_intro` 
         
        Learn about quantum computers.

    .. grid-item-card:: :ref:`qpu_index_about`

        QPU architecture, properties, errors, timing, etc.

    .. grid-item-card:: :ref:`qpu_index_using`

        Configuring QPU parameters and usage best-practices.

.. sections-end-marker

Example
=======

The following code solves a random problem on a quantum computer.

import dimod
import dwave.system

bqm = dimod.generators.ran_r(1, 20)
sampler = dwave.system.EmbeddingComposite(dwave.system.DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=100)
