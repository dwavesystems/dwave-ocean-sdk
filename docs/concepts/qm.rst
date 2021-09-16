.. _qm_sdk:

================
Quadratic Models
================

Quadratic models are polynomials with one or two variables per term. A simple
example of a quadratic model is,

.. math::

    Ax + By + Cxy

where :math:`A`, :math:`B`, and :math:`C` are constants. Single-variable
terms---:math:`Ax` and :math:`By` here---are linear with the constant biasing
the term's variable. Two-variable terms---:math:`Cxy` here---are quadratic with
a relationship between the variables.

Quantum computers solve hard problems by minimizing an objective function.
Quadratic models are useful objective functions because the quantum processing
unit (QPU) can represent binary variables as the states of the qubits and
linear and quadratic coefficients as, respectively, the physical biases and
couplings applied to these qubits. Hybrid quantum-classical samplers, which minimize
some parts of the objective function using classical heuristics and some by using
the QPU, enable the further abstraction of problem representation.

Ocean supports various quadratic models:

* :ref:`bqm_sdk` are unconstrained,  have binary variables, and are contained by
  the :class:`dimod.BinaryQuadraticModel` class.
* :ref:`cqm_sdk` can be constrained,  have integer and binary variables, and are
  contained by the :class:`dimod.ConstrainedQuadraticModel` class.
* :ref:`dqm_sdk` are unconstrained, have discrete variables, and are contained by
  the :class:`dimod.DiscreteQuadraticModel` class.

Ocean also provides support for :ref:`higher order models <oceandocs:higher_order>`,
which are typically reduced to quadratic for sampling.
