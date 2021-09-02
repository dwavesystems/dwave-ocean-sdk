.. _cqm_sdk:

============================
Constrained Quadratic Models
============================

The constrained quadratic model (CQM) are problems of the form:

.. math::

    \begin{align}
        \text{Minimize an objective:} & \\
        & \sum_{i} a_i x_i + \sum_{i<j} b_{ij} x_i x_j + c, \\
        \text{Subject to constraints:} & \\
        & \sum_i a_i^{(c)} x_i + \sum_{i<j} b_{ij}^{(c)} x_i x_j+ c^{(c)} \le 0,
        \quad c=1, \dots, C_{\rm ineq.}, \\
        & \sum_i a_i^{(d)} x_i + \sum_{i<j} b_{ij}^{(d)} x_i x_j + c^{(d)} = 0,
        \quad d=1, \dots, C_{\rm eq.},
    \end{align}

where :math:`\{ x_i\}_{i=1, \dots, N}` can be binary or integer
variables, :math:`a_{i}, b_{ij}, c` are real values and
:math:`C_{\rm ineq.}, C_{\rm eq,}` are the number of inequality and
equality constraints respectively.

The :class:`dimod.ConstrainedQuadraticModel` class can contain this model and its
methods provide convenient utilities for working with representations
of a problem.
