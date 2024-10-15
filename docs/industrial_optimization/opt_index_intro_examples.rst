.. _opt_index_intro_examples:

=====================
Basic Hybrid Examples
=====================

For beginners, formulating problems as `Quadratic Models`_ can be a more 
intuitive introduction to solving optimization problems. `Nonlinear Models`_ 
may be more familiar for users with experience in non-linear programming; for 
many problems, these models---if effectively formulated---are expected to 
enable superior performance.

Quadratic Models
================

..  toctree::
    :maxdepth: 1
    :hidden:

    opt_example_cqm_diet
    opt_example_cqm_binpacking
    opt_example_cqm_stockselling

*   :ref:`opt_example_cqm_diet` solves a mixed-integer linear-programming (MILP)
    problem using a `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid :term:`CQM`
    solver.
*   :ref:`opt_example_cqm_binpacking` solves a binary constrained problem using a
    `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid :term:`CQM` solver.
*   :ref:`opt_example_cqm_stockselling` solves an integer constrained problem using a
    Leap hybrid :term:`CQM` solver.

Nonlinear Models
================

These examples solve small instances of known optimization problems using 
a `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid 
:term:`nonlinear-model <nonlinear model>` solver.

..  toctree::
    :maxdepth: 1
    :hidden:

    opt_example_nl_tsp
    opt_example_nl_cvrp

*   :ref:`opt_example_nl_tsp` helps you start using Leap's hybrid nonlinear-model solver. 

*   :ref:`opt_example_nl_cvrp` demonstrates more advanced usage options for solving
    nonlinear models.
    
Additional Examples
===================

For additional and more advanced examples, see the 
:ref:`opt_section_advanced_examples` section. 
