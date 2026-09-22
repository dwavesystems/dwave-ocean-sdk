.. _index_quantum_research:

================
Quantum Research
================

.. toctree::
    :hidden:
    :maxdepth: 1

    index_get_started
    index_get_started_gm
    index_about
    index_about_gm
    index_using
    index_using_gm
    index_vignettes

.. sections-start-marker

The :ref:`index_quantum_research` section shows how to use |dwave_short_tm|
quantum processing units (QPU) directly.

.. grid:: 2 2 3 3
    :gutter: 2

    .. grid-item-card:: :ref:`qpu_index_get_started`
        :img-top: /_images/rocket_icon.svg
        :link: qpu_index_get_started
        :link-type: ref

        Learn about |dwave_short| **annealing** quantum computers.

    .. grid-item-card:: :ref:`qpu_index_get_started_gm`
        :img-top: /_images/rocket_icon_inv.svg
        :link: qpu_index_get_started_gm
        :link-type: ref

        Learn about |dwave_short| **gate-model** quantum computers.

    .. grid-item-card:: :ref:`qpu_index_about`
        :img-top: /_images/hardware_icon.svg
        :link: qpu_index_about
        :link-type: ref

        Annealing QPU architecture, properties, errors, timing, etc.

    .. grid-item-card:: :ref:`qpu_index_about_gm`
        :img-top: /_images/gate_model_icon.svg
        :link: qpu_index_about_gm
        :link-type: ref

        Gate-model QPU architecture and properties.

    .. grid-item-card:: :ref:`qpu_index_using`
        :img-top: /_images/bipartite_icon.svg
        :link: qpu_index_using
        :link-type: ref

        Configuring annealing QPU parameters and usage best-practices.

    .. grid-item-card:: :ref:`qpu_index_using_gm`
        :img-top: /_images/bloch_sphere_icon.svg
        :link: qpu_index_using_gm
        :link-type: ref

        Configuring gate-model QPU parameters and usage best-practices.

    .. grid-item-card:: :ref:`qpu_index_benchmarks`
        :img-top: /_images/vignette_icon_quantum-research.svg
        :link: qpu_index_benchmarks
        :link-type: ref

        Compare performance of D-Wave's annealing quantum computers versus competing solvers.

The :ref:`index_industrial_optimization` section shows how to optimize business
problems using the |cloud_tm| service's quantum-classical :term:`hybrid`
solvers.

.. sections-end-marker

Example
=======

.. include:: ../shared/examples.rst
  :start-after: start_qpu1
  :end-before: end_qpu1

Useful Links
============

*   :ref:`ocean_sapi_access_basic` on accessing :term:`QPU`
    :term:`solvers <solver>` in the `Leap <https://cloud.dwavesys.com/leap/>`_
    service.
*   :ref:`qpu_qpu_usage_charges` on how the Leap service charges your
    account for use (also: :ref:`qpu_runtime_estimating`).
