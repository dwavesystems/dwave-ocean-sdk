.. _ocean_section_intro:

===========================
Ocean Software: Get Started
===========================

New to Ocean? The following sections describe how to install Ocean tools, what they are
and how they fit together, and give examples of using them to solve hard problems
on a D-Wave quantum computer.

.. _ocean_initial_setup:

Initial Set Up
==============

The following steps set up your development environment for Ocean:

..  toctree::
    :maxdepth: 1
    :hidden:

    ocean_install
    ocean_leap_authorization
    ocean_sapi

1.  :ref:`install`

    Installation is **not needed** if you are using an IDE that implements the 
    `Development Containers specification <https://containers.dev/supporting>`_
    (aka "devcontainers"), whether locally on your system (e.g., VS Code) or 
    cloud-based (e.g., `GitHub Codespaces <https://docs.github.com/codespaces>`_), 
    because you can work in an updated Ocean environment through the 
    `Ocean Docker file <https://hub.docker.com/r/dwavesys/ocean-dev>`_. 

2.  :ref:`leap_auth`

    Optionally authorize Ocean to access your Leap account to facilitate  
    token management.

3.  :ref:`sapi_access`

    Enable the running problems on D-Wave remote compute resources, including 
    quantum-classical hybrid solvers and the D-Wave quantum processing unit (QPU).

Ocean's Programming Model
=========================

Learn Ocean software's workflow for problem solving.

..  toctree::
    :maxdepth: 1

    ocean_solving_problems
    ocean_formulation
    ocean_samplers
    ocean_stack


D-Wave Compute Resources
========================

Use Ocean's :term:`sampler`\ s to solve problems on D-Wave's compute resources (:term:`solver`\ s)
or locally on your CPU.

..  toctree::
    :maxdepth: 1

    industrial_optimization/opt_intro_hybrid.rst
    quantum_research/qpu_intro_classical.rst
    quantum_research/qpu_intro_classical.rst

Because most industrial problems (large, complex, and hard) are best approached 
with quantum-classical hybrid solvers, a good place to start is with examples of 
the :ref:`examples_hybrid` section. If you wish to learn how to work directly with 
the quantum computer, see the examples of the :ref:`examples_qpu` section.

