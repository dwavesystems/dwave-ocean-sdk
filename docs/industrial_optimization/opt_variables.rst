.. _opt_variables:

=========
Variables
=========

D-Wave's samplers mostly\ [#]_ solve quadratic models of various sorts. Quadratic
models are characterized by having one or two variables per term. A simple example
of a quadratic model is,

.. math::

    D = Ax + By + Cxy

where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable
terms---:math:`Ax` and :math:`By` here---are *linear* with the constant biasing
the term's variable. Two-variable terms---:math:`Cxy` here---are *quadratic*
with a relationship between the variables.

The variables in these models may be of the following types:

*   **Binary**: :math:`v_i \in\{-1,+1\} \text{  or } \{0,1\}`, represented by
    the dimod :class:`~dimod.Vartype` classes :class:`~dimod.Vartype.BINARY` and
    :class:`~dimod.Vartype.SPIN`.

    Typically used for applications that optimize over decisions that could either
    be true (or yes) or false (no); for example,

    - Should the antenna transmit or no?
    - Did a network node experience failure?

*   **Discrete**: for example a variable that can be assigned one of the values of the
    set ``{red, green, blue, yellow}``, represented by the dimod :class:`~dimod.Vartype`
    class :class:`~dimod.Vartype.INTEGER`.

    Typically used for applications that optimize over several distinct options;
    for example,

    - Which shift should employee X work?
    - Should the state be colored red, blue, green or yellow?

*   **Integer**: represented by the dimod :class:`~dimod.Vartype` class
    :class:`~dimod.Vartype.INTEGER`.

    Typically used for applications that optimize the number of something; for
    example,

    - How many widgets should be loaded onto the truck?

*   **Real**: represented by the dimod :class:`~dimod.Vartype` class
    :class:`~dimod.Vartype.REAL`.

    Typically used for applications that optimize over an uncountable set; for
    example,

    - Where should the sensor be built?

.. [#] Ocean also provides some higher-order tools for developing and testing
    your code; for example, the :class:`~dimod.reference.samplers.ExactPolySolver`
    class.

Supported Models and Hybrid Samplers
====================================

D-Wave's quantum computers solve **binary** quadratic models;
`Leap <https://cloud.dwavesys.com/leap/>`_ :ref:`hybrid solvers <using_hybrid>` can
solve models with more varied variable types.

.. list-table:: Variable Types and Supported Models, Hybrid Samplers
    :header-rows: 1

    *   - **Variables**
        - **Models**
        - **Hybrid Samplers**
        - **Examples**
    *   - Binary
        - :class:`~dimod.binary.BinaryQuadraticModel`
        - :class:`~dwave.system.samplers.LeapHybridSampler`
        - :ref:`hss`
    *   - Binary, discrete
        - :class:`~dimod.DiscreteQuadraticModel`
        - :class:`~dwave.system.samplers.LeapHybridDQMSampler`
        - :ref:`map_dqm`
    *   - Binary, integer
        - :class:`~dimod.QuadraticModel`, :class:`~dimod.ConstrainedQuadraticModel`
        - :class:`~dwave.system.samplers.LeapHybridCQMSampler`
        - :ref:`example_cqm_binpacking`, :ref:`example_cqm_stock_selling`
    *   - Binary, integer, real
        - :class:`~dimod.ConstrainedQuadraticModel`
        - :class:`~dwave.system.samplers.LeapHybridCQMSampler`
        - :ref:`example_cqm_diet_reals`

Variable Representations and Labels
===================================

Ocean enables you to represent a variable with a quadratic model, as described in
:ref:`dimod's symbolic math <oceandocs:intro_symbolic_math>` documentation. This
makes it important to distinguish between such a variable's representation and
its label.

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

with its single variable having a specified label; e.g., :code:`x0` for the first
model in :code:`x`.

The code below adds two variables to a :class:`~dimod.ConstrainedQuadraticModel`.
The first, using the :meth:`~dimod.ConstrainedQuadraticModel.add_variable` method,
adds a variable by specifying a label, ``"b"``, and the type of required variable,
``"REAL"``. The second, using the
:meth:`~dimod.ConstrainedQuadraticModel.add_constraint_from_model` method, specifies
the variable ``i`` instantiated above as a :class:`~dimod.QuadraticModel` object.

>>> cqm = dimod.ConstrainedQuadraticModel()
>>> cqm.add_variable("b", "REAL")
'b'
>>> cqm.add_constraint_from_model(i, ">=", 2, "Min i")
'Min i'
>>> cqm.variables
Variables(['b', 'i'])
