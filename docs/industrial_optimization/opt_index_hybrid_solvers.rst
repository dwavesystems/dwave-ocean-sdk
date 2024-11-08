.. _opt_index_hybrid_solvers:

==============
Hybrid Solvers
==============

.. toctree::
    :hidden:
    :maxdepth: 1

    opt_solver_cqm_properties
    opt_solver_cqm_parameters
    opt_solver_nl_properties
    opt_solver_nl_parameters
    opt_solver_bqm_properties
    opt_solver_bqm_parameters
    opt_solver_dqm_properties
    opt_solver_dqm_parameters

The |cloud_tm| service provides these :term:`hybrid` :term:`solver`\ s.

CQM Solver 
===========

Large optimization problems can be formulated as 
:ref:`constrained quadratic models <concept_models_cqm>`, as described 
in the :ref:`opt_model_construction_qm` section. You can then use 
the CQM hybrid :term:`solver` hosted in the |cloud_tm| service 
to find good solutions. 

.. grid:: 3
    :gutter: 2


    .. grid-item-card:: :ref:`opt_solver_cqm_properties`


        Properties of the CQM solver.


    .. grid-item-card:: :ref:`opt_solver_cqm_parameters`

        Parameters of the CQM solver.
        
Nonlinear Solver
================

`Nonlinear programming (NLP) <https://en.wikipedia.org/wiki/Nonlinear_programming>`_ 
is the process of solving an optimization problem where some of the constraints 
are not linear equalities and/or the objective function is not a linear function. 
Such optimization problems are pervasive in business and logistics: inventory 
management, scheduling employees, equipment delivery, and many more.

Large optimization problems can be formulated as 
:ref:`nonlinear models <concept_models_nonlinear>`, as described 
in the :ref:`opt_model_construction_nl` section. You can then use 
the nonlinear hybrid :term:`solver` hosted in the |cloud_tm| service 
to find good solutions. 

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_solver_nl_properties`

        Properties of the nonlinear solver.

    .. grid-item-card:: :ref:`opt_solver_nl_parameters`

        Parameters of the nonlinear solver.

Additional Solvers
==================

BQM Solver
----------

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_solver_bqm_properties`

        Properties of the binary quadratic model (BQM) solver.

    .. grid-item-card:: :ref:`opt_solver_bqm_parameters`

        Parameters of the BQM solver.

DQM Solver
----------

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_solver_dqm_properties`

        Properties of the discrete quadratic model (DQM) solver.

    .. grid-item-card:: :ref:`opt_solver_dqm_parameters`

        Parameters of the DQM solver.

Examples
========

Nonlinear Solver
----------------

.. include:: ../shared/examples.rst
    :start-after: start_nl1
    :end-before: end_nl1

CQM Solver
----------

.. include:: ../shared/examples.rst
    :start-after: start_cqm1
    :end-before: end_cqm1
