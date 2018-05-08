.. _gs:

===============
Getting Started
===============

New to `D-Wave Systems <https://www.dwavesys.com>`_ Ocean or want an overview of
the software? This section describes how the Ocean tools fit together
to solve hard problems and gives examples of using them to solve such problems
on a D-Wave quantum computer.

Overview
========

How the Ocean tools fit together to solve problems and how to use a D-Wave system.

.. toctree::
   :maxdepth: 1

   overview/stack
   overview/dwavesys

Examples
========

The quickest way to see how Ocean tools are used, is to look at an end-to-end example.

The :ref:`not` example is the simplest: follow the example code to learn how to quickly
submit a problem to a D-Wave system. The :ref:`and` example is a step more advanced,
adding a simple chain in the :term:`minor-embedding` of the problem and a :term:`composite` layer
to the :term:`sampler`\ . Example :ref:`max_cut` uses algorithmic :term:`minor-embedding`
and some graphic functionality.

.. toctree::
   :maxdepth: 1

   examples/not
   examples/and
   examples/max_cut
   .. examples/cfd  TODO

.. _projects-Demonstrations:

Demonstrations
==============

* `circuit-fault-diagnosis-demo <https://github.com/dwavesystems/circuit-fault-diagnosis-demo>`_

  Demonstrates the use of the D-Wave system to solve circuit fault diagnosis, the problem of identifying
  a minimum-sized set of components that, if faulty, explains an observation of incorrect outputs given a
  set of inputs.

* factoring
