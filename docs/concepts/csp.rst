.. _concept_constraint_satisfaction_problem:

===============================
Constraint Satisfaction Problem
===============================

A `constraint satisfaction problem (CSP) <https://en.wikipedia.org/wiki/Constraint_satisfaction_problem>`_
requires that all the problem's variables be assigned values, out of a finite
domain, that result in the satisfying of all constraints.

The map-coloring CSP, for example, is to assign a color to each region of a map
such that any two regions sharing a border have different colors.

.. figure:: ../_images/Problem_MapColoring.png
    :name: ProblemMapColoringCanada
    :alt: image
    :align: center
    :scale: 70 %

    Coloring a map of Canada with four colors.

The constraints for the map-coloring problem can be expressed as follows:

*   Each region is assigned one color only, of :math:`C` possible colors.
*   The color assigned to one region cannot be assigned to adjacent regions.

A finite domain CSP consists of a set of variables, a specification of the
domain of each variable, and a specification of the constraints over
combinations of the allowed values of the variables. A constraint
:math:`C_\alpha(\bf{x}_\alpha)` defined over a subset of variables
:math:`\bf{x}_\alpha` defines the set of feasible and infeasible combinations of
:math:`\bf{x}_\alpha`. The constraint :math:`C_\alpha` may be be viewed as a
predicate which evaluates to true on feasible configurations and to false on
infeasible configurations. For example, if the domains of variables
:math:`X_1,X_2,X_3` are all :math:`\{0,1,2\}`, and the constraint is
:math:`X_1+X_2<X_3` then the feasible set is
:math:`\{(0,0,1),(0,0,2),(0,1,2),(1,0,2)\}`, and all remaining combinations are
infeasible.

Binary CSPs
===========

Solving such problems as the map-coloring CSP on a :term:`sampler` such as the
|dwave_short| quantum computer necessitates that the mathematical formulation
use binary variables because the solution is implemented physically with qubits,
and so must translate to spins :math:`s_i\in\{-1,+1\}` or equivalent binary
values :math:`x_i\in \{0,1\}`. This means that in formulating the problem by
stating it mathematically, you might use unary encoding to represent the
:math:`C` colors: each region is represented by :math:`C` variables, one for
each possible color, which is set to value :math:`1` if selected, while the
remaining :math:`C-1` variables are :math:`0`.

Another example is logical circuits. Logic gates such as AND, OR, NOT, XOR etc
can be viewed as binary CSPs: the mathematically expressed relationships between
binary inputs and outputs must meet certain validity conditions. For inputs
:math:`x_1,x_2` and output :math:`y` of an AND gate, for example, the constraint
to satisfy, :math:`y=x_1x_2`, can be expressed as a set of valid configurations:
(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1), where the variable order is
:math:`(x_1, x_2, y)`.

.. table:: Boolean AND Operation
    :name: BooleanANDAsPenalty

    ===============  ============================
    :math:`x_1,x_2`  :math:`y`
    ===============  ============================
    :math:`0,0`      :math:`0`
    :math:`0,1`      :math:`0`
    :math:`1,0`      :math:`0`
    :math:`1,1`      :math:`1`
    ===============  ============================

You can use Ocean's :ref:`dwavebinarycsp <index_binarycsp>` to construct a
:term:`BQM` from a CSP. It maps each individual constraint in the CSP to a
"small" :term:`Ising` model or :term:`QUBO`, in a mapping called a
:ref:`penalty model <concept_penalty>`.

Related Information
===================

*   The :ref:`qpu_example_sat_constrained` section introduces the use of QUBOs
    to represent constraints in some simple examples.
*   The :ref:`qpu_reformulating` section provides a variety of techniques for,
    and examples of, reformulating CSPs as BQMs.
*   The :ref:`qpu_example_mapcoloring` section solves a map-coloring problem on
    a |dwave_short| quantum computer.
*   The :ref:`opt_example_dqm_map`and :ref:`opt_example_kerberos_map` sections
    formulate and solve the problem on :term:`hybrid` solvers.





