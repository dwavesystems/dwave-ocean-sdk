.. _index:

===================================
D-Wave Ocean Software Documentation
===================================

Ocean software is a suite of tools `D-Wave Systems <https://www.dwavesys.com>`_ provides
on the `D-Wave GitHub repository <https://github.com/dwavesystems>`_ for solving hard
problems with quantum computers.

* :ref:`gs` shows how to install and begin using Ocean tools.

* :ref:`concepts_sdk` defines and describes Ocean concepts and terminology.

.. toctree::
   :hidden:
   :maxdepth: 2

   getting_started
   concepts/index
   docs_cli
   packages
   contributing
   licenses

========
Packages
========

The Ocean SDK includes the :ref:`dwave_cli` and the following packages:

.. packages-start-marker

.. dropdown::  **dimod** --- Quadratic models: BQM, DQM. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_dimod/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dimod, "code", cls=badge-secondary fr text-white`

   Shared API for binary quadratic :term:`sampler`\ s. Provides a binary quadratic model (BQM) class
   that contains :term:`Ising` and quadratic unconstrained binary optimization (:term:`QUBO`) models
   used by samplers such as the D-Wave system. Also provides utilities for constructing new samplers
   and composed samplers.

.. dropdown:: **dwavebinarycsp** --- Generates BQMs from constraint satisfaction problems. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_binarycsp/sdk_index.html,"docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwavebinarycsp,"code", cls=badge-secondary fr text-white`

   Library to construct a binary quadratic model from a constraint satisfaction
   problem with small constraints over binary variables.

.. dropdown:: **dwave-cloud-client** --- API client to D-Wave solvers. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_cloud/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-cloud-client, "code", cls=badge-secondary fr text-white`

   Minimal implementation of the REST interface used to communicate with D-Wave
   :term:`Sampler` API (SAPI) servers.

.. dropdown:: **dwave-greedy** --- Steepest descent solver. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_greedy/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-greedy, "code", cls=badge-secondary fr text-white`

   An implementation of a steepest descent solver for binary quadratic models.

.. dropdown:: **dwave-hybrid** --- Framework for building hybrid solvers. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_hybrid/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-hybrid, "code", cls=badge-secondary fr text-white`

   A general, minimal Python framework for building hybrid asynchronous decomposition
   samplers for quadratic unconstrained binary optimization (QUBO) problems.

.. dropdown:: **dwave-inspector** --- Visualizer for problems submitted to quantum computers. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_inspector/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-inspector, "code", cls=badge-secondary fr text-white`

   A tool for visualizing problems submitted to, and answers received from, a D-Wave
   structured solver such as a D-Wave 2000Q quantum computer.

.. dropdown:: **dwave-neal** --- Simulated annealing sampler. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_neal/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-neal, "code", cls=badge-secondary fr text-white`

   An implementation of a simulated annealing sampler.

.. dropdown:: **dwave-networkx** --- NetworkX extension. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_dnx/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-networkx, "code", cls=badge-secondary fr text-white`

   Extension of NetworkX—a Python language package for exploration and analysis
   of networks and network algorithms—for users of D-Wave Systems.

   dwave-networkx provides tools for working with :term:`Chimera` and :term:`Pegasus`
   graphs and implementations of graph-theory algorithms on the D-Wave system and other
   binary quadratic model :term:`sampler`\ s.

.. dropdown:: **dwave-ocean-sdk** --- Ocean software development kit. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-ocean-sdk, "code", cls=badge-secondary fr text-white`

   Installer for D-Wave's Ocean Tools.

.. dropdown:: **dwave-preprocessing** --- Preprocessing tools for quadratic models. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_preprocessing/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-preprocessing, "code", cls=badge-secondary fr text-white`

   Library containing common preprocessing tools for quadratic models.

.. dropdown:: **dwave-system** --- D-Wave samplers and composites. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_system/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-system, "code", cls=badge-secondary fr text-white`

   Basic API for easily incorporating the D-Wave system as a :term:`sampler` in the
   D-Wave Ocean software stack.

   It includes DWaveSampler, a dimod sampler that accepts and passes system
   parameters such as system identification and authentication down the stack.
   It also includes several useful composites—layers of pre- and post-processing—that
   can be used with DWaveSampler to handle :term:`minor-embedding`, optimize chain strength, etc.

.. dropdown:: **dwave-tabu** --- Tabu sampler. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_tabu/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/dwave-tabu, "code", cls=badge-secondary fr text-white`

   An implementation of the MST2 multistart tabu search algorithm for quadratic unconstrained
   binary optimization (QUBO) problems with a dimod Python wrapper.

.. dropdown:: **minorminer** --- Minor-embeds graphs. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_minorminer/source/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/minorminer, "code", cls=badge-secondary fr text-white`

   A tool for finding graph :term:`minor-embedding`\ s, developed to embed :term:`Ising` problems onto quantum annealers (QA).

   While it can be used to find minors in arbitrary graphs, it is particularly geared
   towards the state of the art in QA: problem graphs of a few to a few hundred variables,
   and hardware graphs of a few thousand qubits.

.. dropdown:: **penaltymodel** --- Maps constraints to binary quadratic models. \
   :link-badge:`https://docs.ocean.dwavesys.com/en/stable/docs_penalty/sdk_index.html, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/penaltymodel, "code", cls=badge-secondary fr text-white`

   An approach to solve a constraint satisfaction problem (CSP) using an :term:`Ising`
   model or a :term:`QUBO`, is to map each individual constraint in the CSP to a ‘small’
   Ising model or QUBO.

   Includes a local cache for penalty models and a factory that generates penalty models
   using SMT solvers.

.. dropdown:: **pyqubo** --- Creates quadratic models from mathematical expressions. \
   :link-badge:`https://pyqubo.readthedocs.io/en/latest, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/recruit-communications/pyqubo, "code", cls=badge-secondary fr text-white`

   A package that helps you create QUBOs and Ising models from flexible mathematical expressions.

.. dropdown:: **qbsolv (deprecated)** --- Decomposing solver. \
   :link-badge:`https://docs.ocean.dwavesys.com/projects/qbsolv/en/latest/, "docs", cls=badge-primary fr text-white` \
   :link-badge:`https://github.com/dwavesystems/qbsolv, "code", cls=badge-secondary fr text-white`

   A decomposing solver that finds a minimum value of a large quadratic unconstrained binary
   optimization (:term:`QUBO`) problem by splitting it into pieces. The pieces are solved
   using a classical solver running the tabu algorithm. qbsolv also enables configuring
   a D-Wave system as the solver.

   .. include:: docs_qbsolv.rst
      :start-after: qbsolv_deprecation-start-marker
      :end-before: qbsolv_deprecation-end-marker

.. packages-end-marker

Index and D-Wave Links
======================

* :ref:`genindex`: Index for this site.

* `Leap <https://cloud.dwavesys.com/leap>`_: Sign up for Leap quantum cloud service,
  which gives you immediate, secure access to D-Wave quantum and hybrid solvers, as
  well as a wealth of information to help you get started creating quantum applications.

* `System Documentation <https://docs.dwavesys.com/docs/latest/index.html>`_: Here you will
  find information such as

  - `Getting Started  with the System <https://docs.dwavesys.com/docs/latest/doc_getting_started.html>`_---An
    introduction to D-Wave's quantum computers, their hardware and how they work.

  - `Solver Properties and Parameters <https://docs.dwavesys.com/docs/latest/doc_solver_ref.html>`_---Description
    of properties and parameters for of D-Wave's quantum computers and
    Leap's quantum-classical hybrid solvers.

  - `Problem-Solving Handbook <https://docs.dwavesys.com/docs/latest/doc_handbook.html>`_---Information
    and references on formulating problems and best practices in quantum
    computing.
