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
   contributing
   licenses

.. toctree::
  :caption: Tools
  :hidden:
  :maxdepth: 1

  docs_cli

========
Packages
========

The SDK includes the :ref:`dwave_cli` and the following packages:

.. list-table:: Ocean Packages
   :widths: auto

   * - :doc:`dimod </docs_dimod/sdk_index>` (`repo <https://github.com/dwavesystems/dimod>`_)
     - Shared API for binary quadratic :term:`sampler`\ s. Provides a binary quadratic model (BQM) class 
       that contains :term:`Ising` and quadratic unconstrained binary optimization (:term:`QUBO`) models 
       used by samplers such as the D-Wave system. Also provides utilities for constructing new samplers 
       and composed samplers.
   * - :doc:`dwavebinarycsp </docs_binarycsp/sdk_index>` (`repo <https://github.com/dwavesystems/dwavebinarycsp>`_)
     - Library to construct a binary quadratic model from a constraint
       satisfaction problem with small constraints over binary variables.
   * - :doc:`dwave-cloud-client <docs_cloud/sdk_index>` (`repo <https://github.com/dwavesystems/dwave-cloud-client>`_)
     - Minimal implementation of the REST interface used to communicate with D-Wave :term:`Sampler` API (SAPI) servers.
   * - :doc:`dwave-hybrid <docs_hybrid/sdk_index>` (`repo <https://github.com/dwavesystems/dwave-hybrid>`_\ )
     - A general, minimal Python framework for building hybrid asynchronous decomposition samplers for quadratic unconstrained binary optimization (QUBO) problems.
   * - :doc:`dwave-neal <docs_neal/sdk_index>` (`repo <https://github.com/dwavesystems/dwave-neal>`_\ )
     - An implementation of a simulated annealing sampler.
   * - :doc:`dwave-networkx <docs_dnx/sdk_index>` (`repo <https://github.com/dwavesystems/dwave_networkx>`_\ )
     - Extension of NetworkX—a Python language package for exploration and analysis
       of networks and network algorithms—for users of D-Wave Systems.

       dwave-networkx provides tools for working with :term:`Chimera` graphs and implementations of
       graph-theory algorithms on the D-Wave system and other binary quadratic model
       :term:`sampler`\ s.
   * - :doc:`dwave-ocean-sdk <index>` (`repo <https://github.com/dwavesystems/dwave-ocean-sdk>`_)
     - Installer for D-Wave's Ocean Tools.
   * - :std:doc:`dwave-system <docs_system/sdk_index>` (`repo <https://github.com/dwavesystems/dwave-system>`_)
     - Basic API for easily incorporating the D-Wave system as a :term:`sampler` in the
       D-Wave Ocean software stack.

       It includes DWaveSampler, a dimod sampler that accepts and passes system
       parameters such as system identification and authentication down the stack.
       It also includes several useful composites—layers of pre- and post-processing—that
       can be used with DWaveSampler to handle :term:`minor-embedding`, optimize chain strength, etc.
   * - :doc:`dwave-tabu <docs_tabu/sdk_index>` (`repo <https://github.com/dwavesystems/dwave-tabu>`_)
     - An implementation of the MST2 multistart tabu search algorithm for quadratic unconstrained binary
       optimization (QUBO) problems with a dimod Python wrapper.
   * - :doc:`penaltymodel <docs_penalty/sdk_index>` (`repo <https://github.com/dwavesystems/penaltymodel>`_)
     - An approach to solve a constraint satisfaction problem (CSP) using an
       :term:`Ising` model or a :term:`QUBO`, is to map each individual constraint
       in the CSP to a ‘small’ Ising model or QUBO.

       Includes a local cache for penalty models and a factory that generates penalty models
       using SMT solvers.
   * - :std:doc:`minorminer <docs_minorminer/source/sdk_index>` (`repo <https://github.com/dwavesystems/minorminer>`_)
     - A tool for finding graph :term:`minor-embedding`\ s, developed to embed :term:`Ising` problems onto quantum annealers (QA).

       While it can be used to find minors in arbitrary graphs, it is particularly geared towards the state of
       the art in QA: problem graphs of a few to a few hundred variables, and hardware graphs of a few thousand qubits.
   * - :doc:`qbsolv <docs_qbsolv>` (`repo <https://github.com/dwavesystems/qbsolv>`_)
     - A decomposing solver that finds a minimum value of a large quadratic unconstrained binary
       optimization (:term:`QUBO`) problem by splitting it into pieces. The pieces are solved
       using a classical solver running the tabu algorithm. qbsolv also enables configuring
       a D-Wave system as the solver.


.. toctree::
  :hidden:
  :maxdepth: 1
 
  docs_dimod/sdk_index
  docs_binarycsp/sdk_index
  docs_cloud/sdk_index
  docs_hybrid/sdk_index
  docs_inspector
  docs_neal/sdk_index
  docs_dnx/sdk_index
  docs_system/sdk_index
  docs_tabu/sdk_index
  docs_minorminer/source/sdk_index
  docs_penalty/sdk_index
  docs_qbsolv

.. toctree::
  :caption: D-Wave
  :hidden:
  :maxdepth: 1

  D-Wave <https://www.dwavesys.com>
  Leap <https://cloud.dwavesys.com/leap/>
  D-Wave System Documentation <https://docs.dwavesys.com/docs/latest/index.html>

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
