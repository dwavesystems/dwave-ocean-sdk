.. _projects:

=====
Tools
=====

D-Wave Ocean tools are documented on *Read the Docs*. Click on a link below for the
documentation for each tool (or the link in parentheses for the tool repository located
at `D-Wave on GitHub <https://github.com/dwavesystems>`_\ ).

.. list-table:: Ocean Software
   :widths: 10 120
   :header-rows: 1

   * - Tool
     - Description
   * - :std:doc:`dimod <dimod:index>` (`repo <https://github.com/dwavesystems/dimod>`_)
     - Shared API for binary quadratic :term:`sampler`\ s.

       dimod provides a binary quadratic model (BQM) class that contains :term:`Ising` and quadratic unconstrained binary optimization (:term:`QUBO`) models used by samplers such as the D-Wave system. It also provides utilities for constructing new samplers and composed samplers.
   * - :std:doc:`dwavebinarycsp <binarycsp:index>` (`repo <https://github.com/dwavesystems/dwavebinarycsp>`_)
     - Library to construct a binary quadratic model from a constraint
       satisfaction problem with small constraints over binary variables.
   * - :std:doc:`dwave-cloud-client <cloud-client:index>` (`repo <https://github.com/dwavesystems/dwave-cloud-client>`_)
     - Minimal implementation of the REST interface used to communicate with D-Wave :term:`Sampler` API (SAPI) servers.
   * - :std:doc:`dwave_neal <neal:index>` (`repo <https://github.com/dwavesystems/dwave-neal>`_\ )
     - An implementation of a simulated annealing sampler.
   * - :std:doc:`dwave_networkx <networkx:index>` (`repo <https://github.com/dwavesystems/dwave_networkx>`_\ )
     - Extension of NetworkX—a Python language package for exploration and analysis
       of networks and network algorithms—for users of D-Wave Systems.

       dwave_networkx provides tools for working with :term:`Chimera` graphs and implementations of
       graph-theory algorithms on the D-Wave system and other binary quadratic model
       :term:`sampler`\ s.
   * - dwave-ocean-sdk (`repo <https://github.com/dwavesystems/dwave-ocean-sdk>`_)
     - Installer for D-Wave's Ocean Tools.
   * - :std:doc:`dwave-system <system:index>` (`repo <https://github.com/dwavesystems/dwave-system>`_)
     - Basic API for easily incorporating the D-Wave system as a :term:`sampler` in the
       D-Wave Ocean software stack.

       It includes DWaveSampler, a dimod sampler that accepts and passes system
       parameters such as system identification and authentication down the stack.
       It also includes several useful composites—layers of pre- and post-processing—that
       can be used with DWaveSampler to handle :term:`minor-embedding`, optimize chain strength, etc.
   * - :std:doc:`penaltymodel <penaltymodel:index>` (`repo <https://github.com/dwavesystems/penaltymodel>`_)
     - An approach to solve a constraint satisfaction problem (CSP) using an
       :term:`Ising` model or a :term:`QUBO`, is to map each individual constraint
       in the CSP to a ‘small’ Ising model or QUBO.

       Includes a local cache for penalty models and a factory that generates penalty models
       using SMT solvers.
   * - :std:doc:`minorminer <minorminer:index>` (`repo <https://github.com/dwavesystems/minorminer>`_)
     - A tool for finding graph :term:`minor-embedding`\ s, developed to embed :term:`Ising` problems onto quantum annealers (QA).

       While it can be used to find minors in arbitrary graphs, it is particularly geared towards the state of
       the art in QA: problem graphs of a few to a few hundred variables, and hardware graphs of a few thousand qubits.
   * - :std:doc:`qbsolv <qbsolv:index>` (`repo <https://github.com/dwavesystems/qbsolv>`_)
     - A decomposing solver that finds a minimum value of a large quadratic unconstrained binary
       optimization (:term:`QUBO`) problem by splitting it into pieces. The pieces are solved
       using a classical solver running the tabu algorithm. qbsolv also enables configuring
       a D-Wave system as the solver.
