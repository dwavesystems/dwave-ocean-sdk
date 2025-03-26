.. _concept_variables:

=========
Variables
=========

This section mainly relates to the :term:`quadratic models <quadratic model>`
submitted to |cloud|_ service solvers such as the :term:`hybrid` :term:`CQM`
solver.\ [#]_ For the variables in :term:`nonlinear models <nonlinear model>`,
see an introduction in the :ref:`opt_model_construction_nl` section and the
reference documentation under the :ref:`index_optimization` section.

The variables in :ref:`supported models <concept_models>` may be of the
following types.

.. |variables_table| replace:: Supported Variables

.. include:: ../shared/variables.rst
    :start-after: start_variables_table
    :end-before: end_variables_table

.. [#]

    These models are characterized by having one or two variables per term. A simple
    example of a quadratic model is,

    .. math::

        D = Ax + By + Cxy

    where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable
    terms---:math:`Ax` and :math:`By` here---are *linear* with the constant biasing
    the term's variable. Two-variable terms---:math:`Cxy` here---are *quadratic*
    with a relationship between the variables.

Variable Representations and Labels
===================================

Ocean software enables you to represent a variable with a quadratic model, as
described in the :ref:`concept_symbolic_math` section. This makes it important
to distinguish between such a variable's representation and its label.

For example, in the code below, variables :code:`a, i, j` are represented by
:class:`~dimod.QuadraticModel` objects and the ten variables in array :code:`x`
by :class:`~dimod.binary.BinaryQuadraticModel` objects:

>>> a = dimod.Real("a")
>>> i, j = dimod.Integers(["i", "j"])
>>> x = dimod.BinaryArray([f"x{i}" for i in range(10)])

Each such variable is represented by a quadratic model that has a single linear
bias of `1`,

>>> x[0]
BinaryQuadraticModel({'x0': 1.0}, {}, 0.0, 'BINARY')

with its single variable having a specified label; e.g., :code:`x0` for the
first model in :code:`x`.

The code below adds two variables to a
:class:`~dimod.ConstrainedQuadraticModel`. The first, using the
:meth:`~dimod.ConstrainedQuadraticModel.add_variable` method, adds a variable by
specifying a label, ``"b"``, and the type of required variable, ``"REAL"``. The
second, using the
:meth:`~dimod.ConstrainedQuadraticModel.add_constraint_from_model` method,
specifies the variable ``i`` instantiated above as a
:class:`~dimod.QuadraticModel` object.

>>> cqm = dimod.ConstrainedQuadraticModel()
>>> cqm.add_variable("b", "REAL")
'b'
>>> cqm.add_constraint_from_model(i, ">=", 2, "Min i")
'Min i'
>>> cqm.variables
Variables(['b', 'i'])

Related Information
===================

*   The :ref:`opt_model_construction_nl` section describes the construction of
    nonlinear models.
*   The :ref:`opt_model_construction_qm` section describes the construction of
    quadratic models.
*   :ref:`quadratic models <concept_models_quadratic>` describes supported
    models.
