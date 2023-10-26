.. _gs:

===============
Getting Started
===============

New to Ocean? The following sections describe how to install Ocean tools, what they are
and how they fit together, and give examples of using them to solve hard problems
on a D-Wave quantum computer.

.. _gs_initial_setup:

Initial Set Up
==============

The following steps set up your development environment for Ocean:

.. toctree::
    :maxdepth: 1
    :hidden:

    overview/install
    overview/leap_auth
    overview/sapi

1.  :ref:`install`

    Installation is **not needed** if you are using an IDE that implements the 
    `Development Containers specification <https://containers.dev/supporting>`_
    (aka "devcontainers"), whether locally on your system (e.g., VS Code) or 
    cloud-based (e.g., `GitHub Codespaces <https://docs.github.com/codespaces>`_), 
    because you can work in an updated Ocean environment through the 
    `Ocean Docker file <https://hub.docker.com/r/dwavesys/ocean>`_. 

2.  :ref:`leap_auth`

    Optionally authorize Ocean to access your Leap account to facilitate  
    token management.

3.  :ref:`sapi_access`

    Enable the running problems on D-Wave remote compute resources, including 
    quantum-classical hybrid solvers and the D-Wave quantum processing unit (QPU).

Ocean's Programming Model
=========================

Learn Ocean software's workflow for problem solving.

.. toctree::
   :maxdepth: 1

   overview/solving_problems
   overview/formulation
   overview/samplers
   overview/stack

D-Wave Compute Resources
========================

Use Ocean's :term:`sampler`\ s to solve problems on D-Wave's compute resources (:term:`solver`\ s)
or locally on your CPU.

.. toctree::
   :maxdepth: 1

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

   examples/hybrid_cqm_diet
   examples/hybrid_cqm_binpacking
   examples/hybrid_cqm_stock_selling
   examples/hybrid_solver_service
   examples/map_kerberos
   examples/map_dqm

* :ref:`example_cqm_diet_reals` solves a mixed-integer linear-programming (MILP)
  problem using a `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid :term:`CQM`
  solver.
* :ref:`example_cqm_binpacking` solves a binary constrained problem using a
  `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid :term:`CQM` solver.
* :ref:`example_cqm_stock_selling` solves an integer constrained problem using a
  Leap hybrid :term:`CQM` solver.
* :ref:`hss` solves an unconstrained problem using a
  Leap hybrid :term:`BQM` solver.
* :ref:`map_kerberos` demonstrates using an out-of-the-box Ocean hybrid solver.
* :ref:`map_dqm` solves a discrete quadratic model (:term:`DQM`) using a
  Leap hybrid DQM solver.

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

Additional Examples
===================

D-Wave's `dwave-examples <https://github.com/dwave-examples>`_ GitHub repo
contains many more code examples:

* Demos

  Typically in the form of short code examples you can open in
  a supported cloud-based IDE or copy (clone) locally and run. For example:

  * `Nurse scheduling <https://github.com/dwave-examples/nurse-scheduling>`_,
    `maze <https://github.com/dwave-examples/maze>`_,
    `circuit fault diagnosis <https://github.com/dwave-examples/circuit-fault-diagnosis>`_,
    and others provide examples of constraint-satisfaction problems.

  * `Map coloring <https://github.com/dwave-examples/map-coloring>`_,
    `job-shop scheduling <https://github.com/dwave-examples/job-shop-scheduling-cqm>`_,
    and others can complement similar examples presented here.

  * `RNA folding <https://github.com/dwave-examples/rna-folding>`_,
    `portfolio optimization <https://github.com/dwave-examples/portfolio-optimization>`_,
    and others provide prototype applications in a variety of industries.

* Jupyter Notebooks

  These examples, in a web-based interactive environment that includes documentation
  and code, are helpful for both walking beginners through the theory and practice
  of problem solving and explaining complex features. They can also serve as
  a framework in which to develop your own code. For example:

  * `Structural imbalance notebook <https://github.com/dwave-examples/structural-imbalance-notebook>`_
    can complement the :ref:`hss` example.
  * `Hybrid computing notebooks <https://github.com/dwave-examples/hybrid-computing-notebook>`_
    walk you through using and developing hybrid solvers.
  * `Pegasus notebook <https://github.com/dwave-examples/pegasus-notebook>`_,
    `reverse annealing notebook <https://github.com/dwave-examples/reverse-annealing-notebook>`_,
    and others explain features of the quantum computer.

.. _additional_tutorials:

Further Learning
================

* :std:doc:`Getting Started with the D-Wave System <sysdocs_gettingstarted:doc_getting_started>`

  This guide in the
  :std:doc:`System Documentation <sysdocs_gettingstarted:index>`
  introduces the D-Wave quantum computer, provides some key background information on
  how the system works, and explains how to construct a simple problem that the system
  can solve.

* :std:doc:`D-Wave Problem-Solving Handbook <sysdocs_gettingstarted:doc_handbook>`

  This guide provides advanced guidance on using D-Wave solvers, in particular QPU solvers.
  It lists, explains, and demonstrates techniques of problem formulation, minor-embedding,
  and configuring QPU parameters to optimize performance.

*   Package introductions

    The following Ocean packages have extended introductions:

    *   The :ref:`introduction to dimod <intro_dimod>` describes Ocean's supported
        models (e.g., BQMs), the format of returned solutions, :ref:`intro_symbolic_math`,
        and :ref:`intro_scaling`.

    *   The :ref:`introduction to dwave-cloud-client <intro_cloud>` discusses how to
        configure selection of and communications with solvers.

    *   The :ref:`introduction to dwave-hybrid <intro_hybrid>` explains how to use
        the Python framework for running and building hybrid samplers.
