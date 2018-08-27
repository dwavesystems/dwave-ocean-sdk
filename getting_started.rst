.. _gs:

===============
Getting Started
===============

New to Ocean? The following sections describe how to install Ocean tools, what they are
and how they fit together, and give examples of using them to solve hard problems
on a D-Wave quantum computer.

Initial Set Up
==============

Install the tools and configure for running on a D-Wave system
(QPU) or locally (CPU/GPU).

.. toctree::
   :maxdepth: 1

   overview/install
   overview/dwavesys
   overview/cpu

Overview of Ocean Software
==========================

Learn how problems are formulated for solution on D-Wave systems using Ocean tools.

.. toctree::
   :maxdepth: 1

   overview/solving_problems
   overview/stack

Examples
========

See how Ocean tools are used with these end-to-end examples.

Beginner-Level Examples
-----------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/min_vertex
   examples/scheduling
   examples/not
   examples/and

* :ref:`min_vertex` solves a small graph problem.
* :ref:`scheduling` solves a small constraint satisfaction problem.
* :ref:`not` mathematically formulates a BQM for a two-variable problem.
* :ref:`and` demonstrates programming the QPU more directly (:term:`minor-embedding`).

Intermediate-Level Examples
---------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/map_coloring
   examples/multi_gate

* :ref:`map_coloring` example solves a more complex constraint satisfaction problem.
* :ref:`multi_gate` looks more deeply at :term:`minor-embedding`.

.. _projects-Demonstrations:

Demonstrations
==============

Copy (clone) open-source code to run demos of solving known problems on a D-Wave
system.

* `Circuit Fault Diagnosis <https://github.com/dwavesystems/circuit-fault-diagnosis-demo>`_

  Demonstrates the use of the D-Wave system to solve circuit fault diagnosis, the problem of identifying
  a minimum-sized set of components that, if faulty, explains an observation of incorrect outputs given a
  set of inputs.

* `Factoring <https://github.com/dwavesystems/factoring-demo>`_

  Demonstrates the use of the D-Wave system to factor numbers in an entirely new way,
  by turning a multiplication circuit into a constraint satisfaction problem that
  allows the quantum computer to compute inputs from a predefined output. Essentially,
  this means running the multiplication circuit in reverse.

* `Structural Imbalance <https://github.com/dwavesystems/structural-imbalance-demo>`_

  Demonstrates the use of the D-Wave system for analyzing the structural imbalance on
  a signed social network. This demo calculates and shows structural imbalance for
  social networks of militant organization based on data from the Stanford Militants
  Mapping Project.
