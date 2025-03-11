.. _concept_symbolic_math:

=============
Symbolic Math
=============

.. note::

    This section currently describes symbolic math used for
    :term:`quadratic models <quadratic model>` such as the constrained quadratic
    model (:term:`CQM`). For :term:`nonlinear models <nonlinear model>`, see the
    :ref:`opt_model_construction_nl` section.

The :ref:`dimod <index_dimod>` package's support for symbolic math can simplify
your coding of problems. For example, consider a problem of finding the
rectangle with the greatest area for a given perimeter, which you can formulate
mathematically as,

.. math::

    \textrm{Objective: } \quad &\max_{i,j} \quad ij

    \textrm{Constraint:} \quad &2i+2j \le 8

where the components are,

*   **Variables**: :math:`i` and :math:`j` are the lengths of two sides of the
    rectangle and the length of the perimeter is arbitrarily selected to be 8.
*   **Objective**: maximize the area, which is given by the standard geometric
    formula :math:`ij`.
*   **Constraint**: subject to not exceeding the given perimeter length; that
    is, :math:`2i+2j`, the summation of the rectangle's four sides, is
    constrained to a maximum value of 8.

The :ref:`dimod <index_dimod>` package's symbolic math enables an intuitive
coding of such problems:

>>> i, j = dimod.Integers(["i", "j"])
>>> objective = -i * j
>>> constraint = 2 * i + 2 * j <= 8
>>> print(objective.to_polystring())
-i*j
>>> print(constraint.to_polystring())
2*i + 2*j <= 8

Here variables :code:`i,j` are of type integer, perhaps representing the number
of tiles laid horizontally and vertically in creating a rectangular floor, and
the coded ``objective`` is set to negative because |dwave_short| samplers
minimize rather than maximize.

The foundation for this symbolic representation is single-variable models.

Variables as Models
===================

To symbolically represent an objective or constraint, you first need symbolic
representations of variables.

:ref:`Quadratic models <concept_models_quadratic>` with a single variable can
represent your variables; for example, if the type of variable you need is
integer:

>>> i = dimod.Integer('i')
>>> i
QuadraticModel({'i': 1.0}, {}, 0.0, {'i': 'INTEGER'}, dtype='float64')

Here, variable ``i`` is a
:class:`~dimod.quadratic.quadratic_model.QuadraticModel` class that contains one
variable with the label ``'i'``.

This works because quadratic models (QMs) have the form,

.. math::

    \sum_i a_i x_i + \sum_{i \le j} b_{i, j} x_i x_j + c

where :math:`\{ x_i\}_{i=1, \dots, N}` can be integer variables
(:math:`a_{i}, b_{ij}, c` are real values). If you set :math:`a_1=1` and all
remaining coefficients to zero, the model represents a single variable,
:math:`x_1`.

When your variable is used in a linear term of a polynomial, such as
:math:`3.75i`, the coefficient (:math:`3.75`) is represented in this same model
by the value of the linear bias on the ``'i'``--labeled variable:

>>> 3.75 * i
QuadraticModel({'i': 3.75}, {}, 0.0, {'i': 'INTEGER'}, dtype='float64')

Similarly, when your variable is in a quadratic term, such as :math:`2.2i^2`,
the coefficient (:math:`2.2`) is represented in this same model by the value of
the quadratic bias, :math:`b_{1, 1} = 2.2`:

>>> 3.75 * i + 2.2 * i * i
QuadraticModel({'i': 3.75}, {('i', 'i'): 2.2}, 0.0, {'i': 'INTEGER'}, dtype='float64')

You can see the various methods of creating such variables in the
:ref:`dimod <index_dimod>` package's
:ref:`Generators <generators_symbolic_math>` reference documentation.

Typically, you have more than a single variable, and your variables interact.

Operations on Variables
=======================

Consider a simple problem of a NOT operation between two binary variables. For
:math:`\{-1, 1\}`--valued binary variables, the NOT operation is equivalent to
multiplication of the two variables:

>>> s1, s2 = dimod.Spins(["s1", "s2"])
>>> bqm_not = s1*s2
>>> bqm_not
BinaryQuadraticModel({'s1': 0.0, 's2': 0.0}, {('s2', 's1'): 1.0}, 0.0, 'SPIN')
>>> print(dimod.ExactSolver().sample(bqm_not))
  s1 s2 energy num_oc.
1 +1 -1   -1.0       1
3 -1 +1   -1.0       1
0 -1 -1    1.0       1
2 +1 +1    1.0       1
['SPIN', 4 rows, 4 samples, 2 variables]

The symbolic multiplication between variables above executes a multiplication
between the models representing each variable. Binary quadratic models
(:term:`BQM`) are of the form:

.. math::

    \sum_{i=1} a_i v_i
    + \sum_{i<j} b_{i,j} v_i v_j
    + c
    \qquad\qquad v_i \in\{-1,+1\} \text{  or } \{0,1\}

where :math:`a_{i}, b_{ij}, c` are real values. The multiplication of two such
models, with linear terms :math:`a_1 = 1`, reduces to
:math:`\sum_{i=1} 1 v_1 * \sum_{i=1} 1 u_1 = v_1 u_1`, a multiplication of two
variables.

In this NOT example, because all the variables are the same
:class:`~dimod.Vartype` class, the :ref:`dimod <index_dimod>` package represents
each binary variable, and their multiplication, with
:class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel` objects.

>>> bqm_not.vartype is dimod.Vartype.SPIN
True

If an operation includes more than one type of variable, the representation is
always a :class:`~dimod.quadratic.quadratic_model.QuadraticModel` class and the
:class:`~dimod.Vartype` class is per variable:

>>> qm = bqm_not + 3.75 * i
>>> print(type(qm))
<class 'dimod.quadratic.quadratic_model.QuadraticModel'>
>>> qm.vartype("s1") == dimod.Vartype.SPIN
True
>>> qm.vartype("i") == dimod.Vartype.INTEGER
True

.. note::

    An important distinction is that :code:`x = dimod.Binary('x')`, for example,
    instantiates a model with a variable label ``'x'`` and not a free-floating
    variable labeled ``x``. Consequently, you can add ``x`` to another model by
    adding the two models,

    >>> x = dimod.Binary("x")
    >>> bqm = dimod.BinaryQuadraticModel('BINARY')
    >>> bqm += x

    which adds the variable labeled ``'x'`` in the single-variable BQM, ``x``,
    to model ``bqm``. You cannot add ``x`` to a model---as though it were
    variable ``'x'``---by doing :code:`bqm.add_variable(x)`.

Representing Constraints
========================

Many real-world problems include constraints. Typically constraints are either
equality or inequality, in the form of a left-hand side(``lhs``), right-hand
side (``rhs``), and the :class:`dimod.sym.Sense` (:math:`\le`, :math:`\ge`, or
:math:`==`). For example, the constraint of the rectangle problem above,

.. math::

    \textrm{s.t.} \quad 2i+2j \le P

has a ``lhs`` of :math:`2i+2j` less or equal to a ``rhs`` of a some real number
(:math:`8`):

>>> print(constraint.lhs.to_polystring(), constraint.sense.value, constraint.rhs)  # doctest:+SKIP
2*i + 2*j <= 8

You can create such an equality or inequality symbolically, and it is shown with
the model:

>>> print(type(3.75 * i <= 4))
<class 'dimod.sym.Le'>
>>> 3.75 * i <= 4
Le(QuadraticModel({'i': 3.75}, {}, 0.0, {'i': 'INTEGER'}, dtype='float64'), 4)

.. note::

    The :ref:`dimod <index_dimod>` package requires that the right-hand side of
    any equation to be a :class:`float` or an :class:`int`. For example,

    .. math::

        i + j \le ij

    can be transformed into a form supported by *dimod* by subtracting the
    right-hand side from both sides.

    .. math::

        i + j - ij \le 0

    You can then create the inequality symbolically.

    .. doctest:: python

        i, j = dimod.Integers(['i', 'j'])
        i + j - i*j <= 0

Performance
===========

The :ref:`dimod <index_dimod>` package's symbolic math is very useful for small
models used for experimenting and formulating problems. It also offers some more
performant functionality; for example, methods such as
:func:`~dimod.quadratic.IntegerArray` for creating multiple variables with
:std:doc:`NumPy <numpy:index>` arrays or :func:`~dimod.binary.quicksum` as a
replacement for the Python :func:`sum` function.

See the examples of :func:`~dimod.binary.BinaryArray`,
:func:`~dimod.quadratic.IntegerArray`, and :func:`~dimod.binary.SpinArray`
for usage.