.. _ocean_index_get_started:

===============================
Get Started with Ocean Software
===============================

..  toctree::
    :maxdepth: 1
    :hidden:

    install
    leap_authorization
    sapi_access_basic
    sapi_access_advanced
    workflow
    stack

New to Ocean\ |TM| software? This section describes how to install the Ocean SDK
and gives an overview of using it to solve hard problems on |dwave_short_tm|
quantum computers.

.. _ocean_initial_setup:

Initial Set Up
==============

The following steps set up your development environment for Ocean:

1.  :ref:`ocean_install`

    Installation is **not needed** if you are using an IDE that implements the
    `Development Containers specification <https://containers.dev/supporting>`_
    (aka "devcontainers"), whether locally on your system (e.g., VS Code) or
    cloud-based (e.g.,
    `GitHub Codespaces <https://docs.github.com/codespaces>`_), because you can
    work in an updated Ocean environment through the
    `Ocean Docker file <https://hub.docker.com/r/dwavesys/ocean-dev>`_.

2.  :ref:`ocean_leap_authorization`

    Optionally authorize Ocean software to access your Leap\ |TM| service
    account to facilitate token management.

3.  :ref:`ocean_sapi_access_basic`

    Enable the running of problems in the Leap service, using quantum-classical
    :term:`hybrid` solvers and quantum computers.

Ocean SDK's Programming Model
=============================

Learn Ocean software's workflow and structure.

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`ocean_workflow`
        :link: ocean_workflow
        :link-type: ref

        The two main steps of solving problems on quantum computers.

    .. grid-item-card:: :ref:`ocean_stack`
        :link: ocean_stack
        :link-type: ref

        Ocean software stack graphic and description.
