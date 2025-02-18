.. _opt_index_examples_beginner:

=====================
Basic Hybrid Examples
=====================

..  toctree::
    :maxdepth: 1
    :hidden:

    opt_example_cqm_binpacking
    opt_example_cqm_stockselling
    opt_example_cqm_diet
    opt_example_nl_tsp
    opt_example_nl_cvrp

For beginners, formulating problems as `Quadratic Models`_ can be a more
intuitive introduction to solving optimization problems. `Nonlinear Models`_
may be more familiar for users with experience in non-linear programming; for
many problems, these models---if effectively formulated---are expected to enable
superior performance.

Quadratic Models
================

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_example_cqm_binpacking`
        :link: opt_example_cqm_binpacking
        :link-type: ref

        Solves a constrained problem with binary variables using the
        `Leap <https://cloud.dwavesys.com/leap/>`_ service's :term:`CQM` solver.

    .. grid-item-card:: :ref:`opt_example_cqm_stockselling`
        :link: opt_example_cqm_stockselling
        :link-type: ref

        Solves an constrained problem with integer variables using the Leap
        service's CQM solver.

    .. grid-item-card:: :ref:`opt_example_cqm_diet`
        :link: opt_example_cqm_diet
        :link-type: ref

        Solves a mixed-integer linear-programming
        (`MILP <https://en.wikipedia.org/wiki/Integer_programming>`_) problem
        using the Leap service's CQM solver.

Nonlinear Models
================

These examples solve small instances of known optimization problems using
the `Leap <https://cloud.dwavesys.com/leap/>`_ service's hybrid
:term:`nonlinear-model <nonlinear model>` solver.

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_example_nl_tsp`
        :link: opt_example_nl_tsp
        :link-type: ref

        Helps you start using the Leap service's hybrid nonlinear-model solver.

    .. grid-item-card:: :ref:`opt_example_nl_cvrp`
        :link: opt_example_nl_cvrp
        :link-type: ref

        Demonstrates more advanced usage options for solving nonlinear models.

Additional Examples
===================

For additional and more advanced examples, see the
:ref:`opt_index_examples_advanced` section.
