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
constraints are typically represented as :term:`penalty models <penalty model>`.

.. end_models_bqm


.. start_models_dqm

:ref:`Discrete quadratic models <concept_models_dqm>` (DQM) are unconstrained
and typically represent problems with several distinct options; for example,
which shift should employee X work, or should the state on a map be colored red,
blue, green, or yellow? The model uses variables that can represent a set of
values such as ``{red, green, blue, yellow}`` or ``{3.2, 67}``; constraints are
typically represented as :term:`penalty models <penalty model>`.

.. end_models_dqm


.. start_models_ising

.. removed examples (antenna transmit, network node fail) because this chunk is
    always with the BQM chunk so far (Mar 2025)

:term:`Ising models <Ising>` are unconstrained and typically
represent problems of decisions that could either be true or or false. The model
uses :math:`-1/1`-valued variables; constraints are typically
represented as :term:`penalty models <penalty model>`.

.. end_models_ising


.. start_models_ising_formula

The Ising model is traditionally used in statistical mechanics. In the formula
below, :math:`N` variables :math:`s=[s_1,...,s_N]` correspond to physical Ising
"spin up" (:math:`\uparrow`) and "spin down" (:math:`\downarrow`) states, which
can represent :math:`+1` and :math:`-1` values in an :term:`objective function`.

.. math::

    \text{E}(\vc s) = \sum_{i=1}^N h_i s_i +
    \sum_{i=1}^N \sum_{j=i+1}^N J_{i,j} s_i s_j
    \qquad\qquad s_i\in\{-1,+1\}

Here, the linear coefficients, :math:`h_i`, correspond to qubit biases, and
relationships between the spins (interactions: correlations or
anti-correlations), :math:`J_{i,j}`, correspond to coupling strengths.

.. end_models_ising_formula


.. start_models_qubo

.. removed examples (antenna transmit, network node fail) because this chunk is
    always with the BQM chunk so far (Mar 2025)

:term:`QUBOs <QUBO>` are unconstrained and typically represent problems of
decisions that could either be true or false. The model uses :math:`0/1`-valued
variables; constraints are typically represented as
:term:`penalty models <penalty model>`.

.. end_models_qubo


.. start_models_qubo_formula

QUBO problems are traditionally used in computer science. Variables take values
:math:`1` (TRUE) and :math:`0` (FALSE).

A QUBO problem is defined using an upper-diagonal matrix :math:`Q`, which is an
:math:`N \times N` upper-triangular matrix of real weights, and :math:`x`, a
vector of binary variables, as minimizing the function

.. math::

    f(x) = \sum_{i} {Q_{i,i}}{x_i} + \sum_{i<j} {Q_{i,j}}{x_i}{x_j}

where the diagonal terms :math:`Q_{i,i}` are the linear coefficients and the
nonzero off-diagonal terms  :math:`Q_{i,j}` are the quadratic coefficients.

This can be expressed more concisely as

.. math::

    \min_{{x} \in {\{0,1\}^n}} {x}^{T} {Q}{x}.

In scalar notation, the objective function expressed as a QUBO is as follows:

.. math::

    \text{E}_{qubo}(a_i, b_{i,j}; q_i) = \sum_{i} a_i q_i +
    \sum_{i<j} b_{i,j} q_i q_j.

.. note::
    Quadratic unconstrained binary optimization problems---QUBOs---are
    *unconstrained* in that there are no constraints on the variables other
    than those expressed in *Q*.

.. end_models_qubo_formula