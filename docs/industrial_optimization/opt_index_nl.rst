.. _opt_index_nl:

==========================
 Hybrid Solvers: Nonlinear
==========================

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

.. toctree::
    :hidden:
    :maxdepth: 1

    opt_solver_nl_properties
    opt_solver_nl_parameters
    
.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_solver_nl_properties`

        Properties of the nonlinear solver.

    .. grid-item-card:: :ref:`opt_solver_nl_parameters`

        Parameters of the nonlinear solver.
        
Example
=======

.. include:: ../shared/examples.rst
  :start-after: start_nl1
  :end-before: end_nl1
