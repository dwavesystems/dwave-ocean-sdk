.. _concept_model:

======
Models 
======

.. include:: ../shared/models
    :start-after: start_models_intro
    :end-before: end_models_intro

.. _concept_models_cqm:

Constrained Quadratic Models
============================

The constrained quadratic model (CQM) are problems of the form:

.. math::

    \begin{align}
        \text{Minimize an objective:} & \\
        & \sum_{i} a_i x_i + \sum_{i \le j} b_{ij} x_i x_j + c, \\
        \text{Subject to constraints:} & \\
        & \sum_i a_i^{(m)} x_i + \sum_{i \le j} b_{ij}^{(m)} x_i x_j+ c^{(m)} \circ 0,
        \quad m=1, \dots, M,
    \end{align}

where :math:`\{ x_i\}_{i=1, \dots, N}` can be binary\ [#]_, integer, or 
continuous\ [#]_ variables, :math:`a_{i}, b_{ij}, c` are real values,
:math:`\circ \in \{ \ge, \le, = \}` and  :math:`M` is the total number of constraints.

.. [#]
    For binary variables, the range of the quadratic-term summation is
    :math:`i < j` because :math:`x^2 = x` for binary values :math:`\{0, 1\}`
    and :math:`s^2 = 1` for spin values :math:`\{-1, 1\}`.

.. [#] 
    Real-valued variables are currently not supported in quadratic interactions. 

The :class:`dimod.ConstrainedQuadraticModel` class can contain this model and its
methods provide convenient utilities for working with representations
of a problem.

.. _concept_models_nonlinear:

Nonlinear Models
================

The nonlinear model represents a general optimization problem with an 
:term:`objective function` and/or constraints over variables of various 
types.

This model is especially suited for use with decision variables that represent 
a common logic, such as subsets of choices or permutations of ordering. For 
example, in a 
`traveling salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_ 
permutations of the variables representing cities can signify the order of the 
route being optimized and in a 
`knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ the 
variables representing items can be divided into subsets of packed and not 
packed. 

The :class:`~dwave.optimization.model.Model` class encodes this model and 
its methods provide convenient utilities for constructing such models.

.. _concept_models_quadratic:

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

* :ref:`concept_models_bqm` are unconstrained,  have binary variables, and are contained by
  the :class:`dimod.BinaryQuadraticModel` class.
* :ref:`concept_models_cqm` can be constrained,  have real, integer and binary variables,
  and are contained by the :class:`dimod.ConstrainedQuadraticModel` class.
* :ref:`concept_models_dqm` are unconstrained, have discrete variables, and are contained by
  the :class:`dimod.DiscreteQuadraticModel` class.

Ocean also provides support for :ref:`higher order models <oceandocs:higher_order>`,
which are typically reduced to quadratic for sampling.

Other Models
============

.. _concept_models_bqm:

Binary Quadratic Models 
-----------------------

The binary quadratic model (BQM) class encodes
Ising and quadratic unconstrained binary optimization (QUBO) models
used by samplers such as the D-Wave system.

The BQM equation,

.. math::

    E(\bf{v})
    = \sum_{i=1} a_i v_i
    + \sum_{i<j} b_{i,j} v_i v_j 
    + c
    \qquad\qquad v_i \in\{-1,+1\} \text{  or } \{0,1\}

can represent both. 

The :term:`Ising` model is an objective function of :math:`N` variables
:math:`s=[s_1,...,s_N]` corresponding to physical Ising spins, where :math:`h_i`
are the biases and :math:`J_{i,j}` the couplings (interactions) between spins.

.. math::

    \text{Ising:} \qquad  
    E(\bf{s})
    = \sum_{i=1} h_i s_i + 
    \sum_{i<j} J_{i,j} s_i s_j 
    \qquad\qquad s_i\in\{-1,+1\}


The :term:`QUBO` model is an objective function of :math:`N` binary variables represented
as an upper-diagonal matrix :math:`Q`, where diagonal terms are the linear coefficients
and the nonzero off-diagonal terms the quadratic coefficients.

.. math::

    \text{QUBO:} \qquad E(\bf{x})  
    =  \sum_{i\le j} x_i Q_{i,j} x_j
    \qquad\qquad x_i\in \{0,1\}

The :class:`dimod.BinaryQuadraticModel` class can contain both these models and its methods provide
convenient utilities for working with, and interworking between, the two representations
of a problem.

.. _concept_models_dqm:

Discrete Quadratic Models 
-------------------------

The discrete quadratic model (DQM) is a polynomial over *discrete* variables, 
with all terms of degree two or less, where a discrete variable represents some 
collection of distinct values, such as ``{red, green, blue, yellow}`` or 
``{3.2, 67}``, which are called the variable's *cases*.  

A discrete quadratic model may be defined as

.. math::

    H(\bf{d}) = \sum_{i} a_i(\bf{d}_i) + \sum_{i,j} b_{i,j}(\bf{d}_i,\bf{d}_j) + c

where :math:`\bf{d}_i` are the discrete variables, :math:`a_i()` and :math:`b_{i,j}()` 
are real-valued functions, and :math:`c` is a constant (offset).

You can represent any DQM with an equivalent model over **binary** variables 
by replacing each discrete variable, :math:`\bf{d}_i`, with a vector of binary 
variables using `one-hot encoding <https://en.wikipedia.org/wiki/One-hot>`_, 
where exactly one binary variable is True and all others are False: 
:math:`\sum_a x_{i,a} = 1 \quad \forall i`. 

In particular, a discrete quadratic model for :math:`N` discrete variables, 
:math:`\bf{d}_i`, each with :math:`n_i` cases, is then defined by using a 
binary variable, :math:`x_{i,u}`, to indicate whether discrete variable 
:math:`\bf{d}_i` is set to case :math:`u`. The objective function can be 
expressed by the equation:

.. math::

    E(\bf{x})
    = \sum_{i=1}^N \sum_{u=1}^{n_i} a_{i,u} x_{i,u}
    + \sum_{i=1}^N \sum_{j=i+1}^N \sum_{u=1}^{n_i} \sum_{v=1}^{n_j} b_{i,j,u,v} x_{i,u} x_{j,v}
    + c

Both representations are equivalent over the *feasible space*; that is, the 
solutions that meet the one-hot-encoding constraints. The second representation
ascribes energies both to the feasible space (satisfying constraints), and an 
infeasible space (violating constraints). The second representation is used 
by Ocean tools.

The :class:`dimod.DiscreteQuadraticModel` class can contain this model and its 
methods provide convenient utilities for working with representations
of a problem.


Where Else to Look
==================

These models and their use in solving problems on the D-Wave system is described
in the following documentation:

*   :std:doc:`Getting Started with the D-Wave System <sysdocs_gettingstarted:doc_getting_started>`

    Introduces key concepts such as objective functions, Ising models, QUBOs, and graphs, explains
    how these models are used to represent problems, and provides some simple examples.
*   :std:doc:`D-Wave Problem-Solving Handbook <sysdocs_gettingstarted:doc_handbook>`

    Provides a variety of techniques for, and examples of, reformulating problems as BQMs.
*   :std:doc:`Solving Problems on a D-Wave System <oceandocs:overview/solving_problems>`

    Describes and demonstrates the use of BQM in the context of Ocean software.

For more information on models, see the following:

*   :ref:`dwave-hybrid <sdk_index_hybrid>`

    Describes how to use reference hybrid solvers, build hybrid workflows, and your own hybrid components.
*   :std:doc:`Using Leap’s Hybrid Solvers <sysdocs_gettingstarted:doc_leap_hybrid>`

    Introduces Leap‘s quantum-classical hybrid solvers and provides references to usage information.

*   :ref:`Getting Started Demonstrations and Jupyter Notebooks <projects-Demonstrations>` 

    Provides pointers to a code-examples repository and Jupyter Notebooks, which have relevant content.  

*   Example :ref:`map_dqm`

    Shows an example of using `Leap <https://cloud.dwavesys.com/leap/>`_\ 's hybrid
    DQM solver, ``hybrid_binary_quadratic_model_version<x>``, to solve a map
    coloring problem.
*   :class:`dimod.DiscreteQuadraticModel` class documentation

    Describes the DQM class and its methods.
*   :class:`~dwave.system.samplers.LeapHybridDQMSampler` class documentation

    Describes Leap's DQM solver API.

