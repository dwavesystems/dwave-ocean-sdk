.. _ocean_packages:

=======================
Reference Documentation
=======================

.. toctree::
    :hidden:
    :maxdepth: 1

    dimod — |dimod_version| <api_ref_dimod/index>
    dwavebinarycsp — deprecated <api_ref_binarycsp>
    dwave-cloud-client — |cloud_version| <api_ref_cloud/index>
    dwave-gate — |gate_version| <api_ref_gate/index>
    dwave-graphs — |graphs_version| <api_ref_graphs/index>
    dwave-hybrid — |hybrid_version| <api_ref_hybrid/index>
    dwave-inspector — |inspector_version| <api_ref_inspector/index>
    dwave-networkx — deprecated <api_ref_dnx/index>
    dwave-optimization — |optimization_version| <api_ref_optimization/index>
    dwave-preprocessing — |preprocessing_version| <api_ref_preprocessing/index>
    dwave-samplers — |samplers_version| <api_ref_samplers/index>
    dwave-system — |system_version| <api_ref_system/index>
    minorminer — |minorminer_version| <api_ref_minorminer/source/index>
    penaltymodel — deprecated <api_ref_penaltymodel/index>

.. packages-start-marker

.. dropdown::  :ref:`dimod <index_dimod>` (|dimod_version|): Quadratic models (BQM, CQM).

    Shared API for binary quadratic :term:`samplers <sampler>`. Provides a
    binary quadratic model (:term:`BQM`) class, which contains :term:`Ising` and
    quadratic unconstrained binary optimization (:term:`QUBO`) models used by
    samplers such as |dwave_short| quantum computers, and a constrained
    quadratic model (:term:`CQM`) used by :term:`hybrid` samplers. Also provides
    utilities for constructing new samplers and
    :term:`composed samplers <composed sampler>`.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dimod>`

.. dropdown:: :ref:`dwave-cloud-client <index_cloud>` (|cloud_version|): API
    client to the Leap service's solvers.

    Minimal implementation of the REST interface used to communicate with
    :term:`SAPI` servers.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-cloud-client>`

.. dropdown:: :ref:`dwave-gate <index_gate>` (|gate_version|): Package for quantum
    circuits.

    A software package for constructing, modifying and running quantum circuits.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-gate>`

.. dropdown:: :ref:`dwave-graphs <index_graphs>` (|graphs_version|): Package for
    QPU graphs.

    A package providing graphs and algorithms for working with D-Wave quantum
    computers.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-gate>`

.. dropdown:: :ref:`dwave-hybrid <index_hybrid>` (|hybrid_version|): Framework for
    building hybrid solvers.

    A general, minimal Python framework for building :term:`hybrid` asynchronous
    decomposition samplers for quadratic unconstrained binary optimization
    (:term:`QUBO`) problems.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-hybrid>`

.. dropdown:: :ref:`dwave-inspector <index_inspector>` (|inspector_version|):
    Visualizer for problems submitted to quantum computers.

    A tool for visualizing problems submitted to, and answers received from, a
    |dwave_short| structured solver such as an :term:`Advantage` quantum
    computer.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-inspector>`

.. dropdown:: :ref:`dwave-networkx <index_dnx>` (deprecated): NetworkX extension.

    Extension of :std:doc:`NetworkX <networkx:index>`---a Python language
    package for exploration and analysis of networks and network
    algorithms---for users of |dwave_short| quantum computers.

    This package provides tools for working with :term:`Pegasus` and
    :term:`Zephyr` graphs and implementations of graph-theory algorithms on
    |dwave_short| quantum computers and other binary quadratic model
    (:term:`BQM`) :term:`samplers <sampler>`.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-networkx>`

.. dropdown:: :ref:`dwave-ocean-sdk <ocean_source_code>` (|version|): Ocean
    software development kit.

    Installer for D-Wave's Ocean Tools.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-ocean-sdk>`

.. dropdown:: :ref:`dwave-optimization <index_optimization>` (|optimization_version|):
    Nonlinear models.

    API for :ref:`nonlinear models <concept_models_nonlinear>`. The package
    includes:

    *   A class for nonlinear models used by the |cloud|_ service's
        :term:`hybrid` nonlinear-program solver.
    *   Model generators for industrial optimization problems.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-optimization>`

.. dropdown:: :ref:`dwave-preprocessing <index_preprocessing>` (|preprocessing_version|):
    Preprocessing tools for quadratic models.

    Library containing common preprocessing tools for quadratic models.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-preprocessing>`

.. dropdown:: :ref:`dwave-samplers <index_samplers>` (|samplers_version|): Classical algorithms
    for solving binary quadratic models.

    A library that implements the following classical algorithms as
    :term:`samplers <sampler>` for solving binary quadratic models
    (:term:`BQM`):

    *   Planar: an exact solver for planar Ising problems with no linear biases.
    *   Random: a sampler that draws uniform random samples.
    *   Simulated Annealing: a probabilistic heuristic for optimization and
        approximate Boltzmann sampling well suited to finding good solutions of
        large problems.
    *   Steepest Descent: a discrete analogue of gradient descent, often used in
        machine learning, that quickly finds a local minimum.
    *   Tabu: a heuristic that employs local search with methods to escape local
        minima.
    *   Tree Decomposition: an exact solver for problems with low treewidth.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-samplers>`

.. dropdown:: :ref:`dwave-system <index_system>` (|system_version|): D-Wave
    samplers and composites.

    Basic API for easily incorporating the |dwave_short| quantum computer as a
    :term:`sampler` in the Ocean :ref:`software stack <ocean_stack>`.

    It includes the :class:`~dwave.system.samplers.DWaveSampler` sampler, a
    dimod sampler that accepts and passes system parameters such as system
    identification and authentication down the stack. It also includes several
    useful composites---layers of pre- and post-processing---that can be used
    with this sampler to handle :term:`minor-embedding`, optimize
    :term:`chain strength`, etc.

    :bdg-link-primary:`code <https://github.com/dwavesystems/dwave-system>`

.. dropdown:: :ref:`minorminer <index_minorminer>` (|minorminer_version|):
    Minor-embeds graphs.

    A tool for finding graph :term:`minor-embedding`, developed to embed
    :term:`Ising` problems onto :term:`quantum annealing` (QA) quantum
    computers.

    While it can be used to find minors in arbitrary graphs, it is particularly
    geared towards the state of the art in QA: problem graphs of a few to a few
    hundred variables, and hardware graphs of a few thousand qubits.

    :bdg-link-primary:`code <https://github.com/dwavesystems/minorminer>`

.. dropdown:: :ref:`penaltymodel <index_penaltymodel>` (deprecated): Maps
    constraints to binary quadratic models.

    An approach to solve a constraint satisfaction problem (:term:`CSP`) using
    an :term:`Ising` model or a :term:`QUBO`, is to map each individual
    constraint in the CSP to a "small" Ising model or QUBO.

    Includes a local cache for penalty models and a factory that generates
    penalty models using SMT solvers.

    :bdg-link-primary:`code <https://github.com/dwavesystems/penaltymodel>`

.. packages-end-marker
