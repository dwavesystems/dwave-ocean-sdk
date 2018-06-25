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

See how Ocean tools are used with these end-to-end examples that start from simple
and gradually add functionality.

Beginner-Level Examples
-----------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/not
   examples/and
   examples/max_cut

* :ref:`not` is a minimal example that solves a two-variable problem (:math:`y = \neg x`)
  by assigning one qubit per variable and finding the minimum energy.
* :ref:`and` adds the use of a simple chain in manually :term:`minor-embedding` a problem.
* :ref:`max_cut` adds algorithmic :term:`minor-embedding` and some graphic functionality.

Intermediate-Level Examples
---------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/map_coloring
   examples/multi_gate

* :ref:`map_coloring` example demonstrates algorithmic generation of penalty models and
  conversion to binary quadratic models.
* :ref:`multi_gate` compares solutions for various minor-embeddings and chains strengths.

.. _projects-Demonstrations:

Demonstrations
==============

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
