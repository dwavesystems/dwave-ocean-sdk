.. |models_variables_table| replace:: dummy

.. start_models_variables_table

.. list-table:: |models_variables_table|
    :header-rows: 1

    *   -   **Model**
        -   **Variables**
        -   **Ocean Class & Sampler**
    *   -   **Constrained:**
        -
        -
    *   -   :ref:`concept_models_nonlinear`
        -   Binary, integer
        -   :class:`~dwave.optimization.model.Model`,
            :class:`~dwave.system.samplers.LeapHybridNLSampler`
    *   -   :ref:`concept_models_cqm`
        -   Binary, integer, real
        -   :class:`~dimod.ConstrainedQuadraticModel`,
            :class:`~dwave.system.samplers.LeapHybridCQMSampler`
    *   -   **Unconstrained:**
        -
        -
    *   -   :ref:`concept_models_ising`
        -   Spin
        -   :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`,
            :class:`~dwave.system.samplers.DWaveSampler`
    *   -   :ref:`concept_models_qubo`
        -   Binary
        -   :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`,
            :class:`~dwave.system.samplers.DWaveSampler`
    *   -   :ref:`concept_models_bqm`
        -   Binary, spin
        -   :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`,
            :class:`~dwave.system.samplers.LeapHybridSampler`, :class:`~dwave.system.samplers.DWaveSampler`
    *   -   :ref:`concept_models_dqm`
        -   Binary, discrete
        -   :class:`~dimod.DiscreteQuadraticModel`,
            :class:`~dwave.system.samplers.LeapHybridDQMSampler`

.. end_models_variables_table


.. start_models_nonlinear

:ref:`Nonlinear models <concept_models_nonlinear>` typically represent general
optimization problems with an :term:`objective function` and/or one or more
constraints over integer and/or binary variables; the model supports constraints
natively.

This model is especially suited for use with decision variables that represent
a common logic, such as subsets of choices or permutations of ordering. For
example, in a
`traveling salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
permutations of the variables representing cities can signify the order of the
route being optimized and in a
`knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ the
variables representing items can be divided into subsets of packed and not
packed.

.. end_models_nonlinear


.. start_models_cqm

:ref:`Constrained quadratic models <concept_models_cqm>` (CQM) are typically
used for applications that optimize problems that might include binary-valued
variables (both :math:`0/1`-valued variables and :math:`-1/1`-valued variables),
integer-valued variables, and real variables (also known as
*continuous variables*); the model supports constraints natively.

.. end_models_cqm


.. start_models_bqm

:ref:`Binary quadratic models <concept_models_bqm>` (BQM) are unconstrained and
typically represent problems of decisions that could either be true (or yes) or
false (no); for example, should an antenna transmit, or did a network node fail?
The model uses :math:`0/1`-valued variables and :math:`-1/1`-valued variables;
constraints are typically represented as :ref:`penalty models <concept_penalty>`.

.. end_models_bqm


.. start_models_dqm

:ref:`Discrete quadratic models <concept_models_dqm>` (DQM) are unconstrained
and typically represent problems with several distinct options; for example,
which shift should employee X work, or should the state on a map be colored red,
blue, green, or yellow? The model uses variables that can represent a set of
values such as ``{red, green, blue, yellow}`` or ``{3.2, 67}``; constraints are
typically represented as :ref:`penalty models <concept_penalty>`.

.. end_models_dqm


.. start_models_ising

.. todo:: replace the example here

:ref:`Ising models <concept_models_ising>` are unconstrained and typically
represent problems of decisions that could either be true (or yes) or
false (no); for example, should an antenna transmit, or did a network node fail?
The model uses :math:`-1/1`-valued variables; constraints are typically
represented as :ref:`penalty models <concept_penalty>`.

.. end_models_ising


.. start_models_qubo

.. todo:: replace the example here

:ref:`QUBOs <concept_models_qubo>` are unconstrained and typically represent
problems of decisions that could either be true (or yes) or false (no); for
example, should an antenna transmit, or did a network node fail? The model uses
:math:`0/1`-valued variables; constraints are typically represented as
:ref:`penalty models <concept_penalty>`.

.. end_models_qubo