.. _opt_index_properties_parameters:

==============================
Solver Properties & Parameters
==============================

.. toctree::
    :hidden:
    :maxdepth: 1

    solver_nl_properties
    solver_nl_parameters
    index_qm_properties_parameters

Large optimization problems can be formulated as
:ref:`nonlinear models <concept_models_nonlinear>`, as described in the
:ref:`opt_model_construction_nl` section. You can then use the hybrid nonlinear
:term:`solver` (also known as the |nlstride_tm|) hosted in the |cloud_tm|
service to find good solutions.

For the
properties and parameters of :term:`QPU` solvers, see the
:ref:`qpu_index_solver_properties` and :ref:`qpu_solver_parameters` sections.

For the
properties and parameters of
:ref:`constrained quadratic models <concept_models_cqm>` and other hybrid
solvers, see the :ref:`opt_index_qm_properties_parameters` section.


.. grid:: 2 2 3 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_solver_nl_properties`
        :link: opt_solver_nl_properties
        :link-type: ref

        Properties of the nonlinear solver.

    .. grid-item-card:: :ref:`opt_solver_nl_parameters`
        :link: opt_solver_nl_parameters
        :link-type: ref

        Parameters of the nonlinear solver.

Examples
========

.. include:: ../shared/examples.rst
    :start-after: start_nl1
    :end-before: end_nl1


