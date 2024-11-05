.. _opt_index_cqm:

====================
 Hybrid Solvers: CQM
====================

Large optimization problems can be formulated as 
:ref:`constrained quadratic models <concept_models_cqm>`, as described 
in the :ref:`opt_model_construction_qm` section. You can then use 
the CQM hybrid :term:`solver` hosted in the |cloud_tm| service 
to find good solutions. 

.. toctree::
    :hidden:
    :maxdepth: 1

    opt_solver_cqm_properties
    opt_solver_cqm_parameters

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_solver_cqm_properties`

        Properties of the CQM solver.

    .. grid-item-card:: :ref:`opt_solver_cqm_parameters`

        Parameters of the CQM solver.

Example
=======

.. include:: ../shared/examples.rst
  :start-after: start_cqm1
  :end-before: end_cqm1
