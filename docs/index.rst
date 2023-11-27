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

.. tab-set::

   .. tab-item:: Get Started

      .. grid:: 2
         :gutter: 2

         .. grid-item-card::  `dimod <https://docs.ocean.dwavesys.com/en/stable/docs_dimod/sdk_index.html>`_ 
         
            :abbr:`Quadratic models: BQM, CQM. (Shared API for binary quadratic 
            samplers. Provides a binary quadratic model class that contains 
            Ising and quadratic unconstrained binary optimization models used by 
            samplers such as the D-Wave system. Also provides utilities for 
            constructing new samplers and composed samplers.)`

         .. grid-item-card::  :ref:`dwave-samplers <index_dwave_samplers>` 
                        
            :abbr:`Classical algorithms for solving binary quadratic models. (A library 
            that implements the following classical algorithms as samplers for solving
            binary quadratic models:
            [Planar]: an exact solver for planar Ising problems with no linear biases.
            [Random]: a sampler that draws uniform random samples.
            [Simulated Annealing]: a probabilistic heuristic for optimization and approximate
            Boltzmann sampling well suited to finding good solutions of large problems.
            [Steepest Descent]: a discrete analogue of gradient descent, often used in
            machine learning, that quickly finds a local minimum.
            [Tabu]: a heuristic that employs local search with methods to escape local minima.
            [Tree Decomposition]: an exact solver for problems with low treewidth.)`
         
         .. grid-item-card::  :ref:`dwave-system <index_system>` 

            :abbr:`D-Wave samplers and composites. (Basic API for easily incorporating 
            the D-Wave system as a sampler in the D-Wave Ocean software stack.
            It includes DWaveSampler, a dimod sampler that accepts and passes system
            parameters such as system identification and authentication down the stack.
            It also includes several useful composites—layers of pre- and post-processing—that
            can be used with DWaveSampler to handle minor-embedding, optimize chain strength, etc.)`

         .. grid-item-card::  :ref:`dwave-hybrid <index_hybrid>` 
                        
            :abbr:`Framework for building hybrid samplers. (A general, minimal Python 
            framework for building hybrid asynchronous decomposition samplers for 
            quadratic unconstrained binary optimization (QUBO) problems.)`

   .. tab-item:: All Packages

      .. dropdown::  `dimod <https://docs.ocean.dwavesys.com/en/stable/docs_dimod/sdk_index.html>`_: Quadratic models (BQM, CQM). 

         Shared API for binary quadratic :term:`sampler`\ s. Provides a binary quadratic model (BQM) class
         that contains :term:`Ising` and quadratic unconstrained binary optimization (:term:`QUBO`) models
         used by samplers such as the D-Wave system. Also provides utilities for constructing new samplers
         and composed samplers.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dimod>`

      .. dropdown:: :ref:`dwavebinarycsp <index_csp>`: Generates BQMs from constraint satisfaction problems. 

         Library to construct a binary quadratic model from a constraint satisfaction
         problem with small constraints over binary variables.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwavebinarycsp>`

      .. dropdown:: :ref:`dwave-cloud-client <index_cloud>`: API client to D-Wave solvers. 

         Minimal implementation of the REST interface used to communicate with D-Wave
         :term:`Sampler` API (SAPI) servers.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-cloud-client>`

      .. dropdown:: :ref:`dwave-gate <index_gate>`: Package for quantum circuits. 

         A software package for constructing, modifying and running quantum circuits.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-gate>`

      .. dropdown:: :ref:`dwave-hybrid <index_hybrid>`: Framework for building hybrid solvers. 

         A general, minimal Python framework for building hybrid asynchronous decomposition
         samplers for quadratic unconstrained binary optimization (QUBO) problems.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-hybrid>`

      .. dropdown:: :ref:`dwave-inspector <index_inspector>`: Visualizer for problems submitted to quantum computers. 

         A tool for visualizing problems submitted to, and answers received from, a D-Wave
         structured solver such as an Advantage quantum computer.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-inspector>`

      .. dropdown:: :ref:`dwave-networkx <index_dnx>`: NetworkX extension. 

         Extension of NetworkX—a Python language package for exploration and analysis
         of networks and network algorithms—for users of D-Wave Systems.

         dwave-networkx provides tools for working with :term:`Chimera` and :term:`Pegasus`
         graphs and implementations of graph-theory algorithms on the D-Wave system and other
         binary quadratic model :term:`sampler`\ s.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-networkx>`

      .. dropdown:: :ref:`dwave-ocean-sdk <index>`: Ocean software development kit. 
         
         Installer for D-Wave's Ocean Tools.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-ocean-sdk>`

      .. dropdown:: :ref:`dwave-preprocessing <index_preprocessing>`: Preprocessing tools for quadratic models. 

         Library containing common preprocessing tools for quadratic models.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-preprocessing>`

      .. dropdown:: :ref:`dwave-samplers <index_dwave_samplers>`: Classical algorithms for solving binary quadratic models. 

         A library that implements the following classical algorithms as :term:`samplers<sampler>` for solving
         :term:`binary quadratic models<BQM>` (BQM):

         * Planar: an exact solver for planar Ising problems with no linear biases.
         * Random: a sampler that draws uniform random samples.
         * Simulated Annealing: a probabilistic heuristic for optimization and approximate
         Boltzmann sampling well suited to finding good solutions of large problems.
         * Steepest Descent: a discrete analogue of gradient descent, often used in
         machine learning, that quickly finds a local minimum.
         * Tabu: a heuristic that employs local search with methods to escape local minima.
         * Tree Decomposition: an exact solver for problems with low treewidth.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-samplers>`

      .. dropdown:: :ref:`dwave-system <index_system>`: D-Wave samplers and composites. 

         Basic API for easily incorporating the D-Wave system as a :term:`sampler` in the
         D-Wave Ocean software stack.

         It includes DWaveSampler, a dimod sampler that accepts and passes system
         parameters such as system identification and authentication down the stack.
         It also includes several useful composites—layers of pre- and post-processing—that
         can be used with DWaveSampler to handle :term:`minor-embedding`, optimize chain strength, etc.

         :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-system>`

      .. dropdown:: `minorminer <https://docs.ocean.dwavesys.com/en/stable/docs_minorminer/source/sdk_index.html>`_: Minor-embeds graphs. 

         A tool for finding graph :term:`minor-embedding`\ s, developed to embed :term:`Ising` problems onto quantum annealers (QA).

         While it can be used to find minors in arbitrary graphs, it is particularly geared
         towards the state of the art in QA: problem graphs of a few to a few hundred variables,
         and hardware graphs of a few thousand qubits.

         :bdg-link-primary:`code <https://github.com/dwavesystems/minorminer>`

      .. dropdown:: :ref:`penaltymodel <index_penalty>`: Maps constraints to binary quadratic models. 

         An approach to solve a constraint satisfaction problem (CSP) using an :term:`Ising`
         model or a :term:`QUBO`, is to map each individual constraint in the CSP to a ‘small’
         Ising model or QUBO.

         Includes a local cache for penalty models and a factory that generates penalty models
         using SMT solvers.

         :bdg-link-primary:`code <https://github.com/dwavesystems/penaltymodel>`

      .. dropdown:: `pyqubo <https://pyqubo.readthedocs.io/en/latest>`_: Creates quadratic models from mathematical expressions. 

         A package that helps you create QUBOs and Ising models from flexible mathematical expressions.

         :bdg-link-primary:`code <https://github.com/recruit-communications/pyqubo>`

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
