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

   examples/map_kerberos
   examples/min_vertex
   examples/scheduling
   examples/not
   examples/and

* :ref:`map_kerberos` demonstrates out-of-the-box solving of an arbitrary-sized problem.
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
   examples/hybrid1

* :ref:`map_coloring` example solves a more complex constraint satisfaction problem.
* :ref:`multi_gate` looks more deeply at :term:`minor-embedding`.
* :ref:`hybrid1` illustrates solving a large problem using both classical and quantum resources.

Advanced-Level Examples
-----------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/topology_samplers

* :ref:`topology_samplers` running your code on software with different :term:`QPU`-inspired topologies.

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

.. _additional_tutorials:

Additional Tutorials
====================

* :std:doc:`Getting Started with the D-Wave System <sysdocs_gettingstarted:doc_getting_started>`

  This guide in the
  :std:doc:`System Documentation <sysdocs_gettingstarted:index>`
  introduces the D-Wave quantum computer, provides some key background information on
  how the system works, and explains how to construct a simple problem that the system
  can solve.

* :std:doc:`D-Wave Problem-Solving Handbook <sysdocs_gettingstarted:doc_handbook>`

  This guide for more advanced users has an opening chapter of illustrative examples
  that explain the main steps of solving problems on the D-Wave system through two
  “toy” problems.

* `Leap <https://cloud.dwavesys.com/leap/>`_

  Leap includes Jupyter Notebooks that provide additional tutorial examples and a
  framework to help you develop your own code.
