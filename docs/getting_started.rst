.. _gs:

===============
Getting Started
===============

New to Ocean? The following sections describe how to install Ocean tools, what they are
and how they fit together, and give examples of using them to solve hard problems
on a D-Wave quantum computer.

Initial Set Up
==============

D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ integrated development
environment (IDE) is the fastest way to get started writing your quantum
application or just learning to use Ocean tools. This cloud-based IDE---run
in your browser---is available to all Leap accounts. It provides
reusable/disposable workspaces (developer environments pre-configured with
Ocean and other standard libraries as well as D-Wave extensions) for running
code from your own GitHub repository or a collection of code examples you can
then modify.

Alternatively, install the tools and configure for running problems on D-Wave
remote compute resources, including quantum-classical hybrid solvers and the
D-Wave quantum processing unit (QPU), or locally on your CPU.

.. toctree::
   :maxdepth: 1

   overview/install
   overview/sapi

Ocean's Programming Model
=========================

Learn Ocean software's workflow for problem solving.

.. toctree::
   :maxdepth: 1

   overview/solving_problems
   overview/stack

D-Wave Compute Resources
========================

Use Ocean's :term:`sampler`\ s to solve problems on D-Wave's compute resources (:term:`solver`\ s)
or locally on your CPU.

.. toctree::
   :maxdepth: 1

   overview/samplers
   overview/hybrid
   overview/cpu
   overview/qpu

Examples
========

See how Ocean tools are used with these end-to-end examples.

Because many large, hard problems are best approached with quantum-classical hybrid
solvers, a good place to start is with examples of the :ref:`examples_hybrid` section
and then learn how to work directly on the quantum computer with examples of the
:ref:`examples_qpu` section.

.. _examples_hybrid:

Beginner-Level Examples: Hybrid Computing
-----------------------------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/hybrid_solver_service
   examples/map_kerberos
   examples/map_dqm

* :ref:`hss` solves an arbitrary-sized problem using a `Leap <https://cloud.dwavesys.com/leap/>`_
  hybrid solver.
* :ref:`map_kerberos` demonstrates using an out-of-the-box Ocean hybrid solver.
* :ref:`map_dqm` solves a **discrete** quadratic model (:term:`DQM`) using 
  `Leap <https://cloud.dwavesys.com/leap/>`_\ 's hybrid DQM solver.

.. _examples_qpu:

Beginner-Level Examples: Using the QPU
--------------------------------------

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
   examples/hybrid1
   examples/pp_greedy

* :ref:`map_coloring` example solves a more complex constraint satisfaction problem.
* :ref:`multi_gate` looks more deeply at :term:`minor-embedding`.
* :ref:`hybrid1` builds a hybrid workflow and solver for a large graph problem.
* :ref:`pp_greedy` improves samples returned from a QPU by post-processing with a 
  classical greedy algorthim.

Advanced-Level Examples
-----------------------

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/inspector_graph_partitioning
   examples/topology_samplers

* :ref:`inspector_graph_partitioning` improves :term:`minor-embedding` on a graph partition problem.
* :ref:`topology_samplers` runs your code on software samplers with different :term:`QPU`-inspired topologies.

.. _projects-Demonstrations:

Demonstrations and Jupyter Notebooks
====================================

D-Wave's `dwave-examples <https://github.com/dwave-examples>`_ GitHub repo
contains demos, typically in the form of short code examples, you can open in
the Leap IDE or copy (clone) locally and run.

D-Wave's `Leap <https://cloud.dwavesys.com/leap>`_ Quantum Application Environment
provides a number of `Jupyter Notebooks <https://jupyter.org>`_ with detailed code examples for various types
of problems (for example, constraint satisfaction problems) and ways of using the
quantum computer (for example, hybrid computing and reverse annealing). These can also
serve as a framework in which to develop your own code.

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
