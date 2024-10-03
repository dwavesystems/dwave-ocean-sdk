.. _gs_formulation:

==================================
Formulation: Objectives and Models
==================================

For quantum computing, as for classical, solving a problem requires that it
be formulated in a way the computer and its software understand.

For example, if you want your laptop to calculate the area of a $1 coin, you might
express the problem as an equation, :math:`A=\pi r^2`, that you program as
:code:`math.pi*13.245**2` in your Python terminal. For a laptop with Python software,
this formulation---a particular string of alphanumeric symbols---causes the manipulation
of bits in a CPU and memory chips that produces the correct result.

.. _gs_objectives:

Objective Functions
===================

With quantum computing, you express your problem in a form that enables solution by
minimization: an :term:`objective function`, which is a mathematical expression of the
energy of a system. If you are solving your problem on a D-Wave quantum computer,
for example, the system is the qubits of a quantum processing unit (QPU) and your
objective function represents the states of the qubits as binary variables, and
the physical biases and couplings applied to these qubits as, respectively, linear
and quadratic coefficients. By formulating an objective function such that lowest
energy states represent good solutions to your problem, you can solve your problem
by minimizing the objective function. In the case of a D-Wave quantum computer,
the QPU uses quantum annealing to seek the minimum of the energy landscape for
its qubits with the biases and couplings applied by your objective function; for
hybrid quantum-classical algorithms, some parts of the objective function are
minimized using classical heuristics and some by the QPU.

As an illustrative example, consider the equation :math:`x+1=2`. You can solve
by minimization an equivalent objective function, :math:`\min_x[2-(x+1)]^2`,
formulated by taking the square of the subtraction of one side from another.
Minimization seeks the shortest distance between the sides, which occurs at
equality (with the square eliminating negative distance).

There are many ways of mapping between a problem---chains of amino acids
forming 3D structures of folded proteins, traffic in the streets of Beijing,
circuits of binary gates---and an objective function to be solved (by sampling)
with a D-Wave system, a :term:`hybrid` solver, or locally on your CPU.
The :ref:`Getting Started examples <gs>` given here show some simple
objective functions to help you begin using Ocean tools.

For more detailed information on objective functions, how D-Wave quantum computers
minimize objective functions, and techniques for reformulating problems as
objective functions, see the
:std:doc:`System Documentation <sysdocs_gettingstarted:index>` or the training
content on the `D-Wave website <https://www.dwavesys.com/>`_.

For code examples that formulate models for various problems, see
`D-Wave's examples repo <https://github.com/dwave-examples>`_  and many example
customer applications on the `D-Wave website <https://www.dwavesys.com/>`_.

Supported Models
================

Ocean supports various models to express your problem as an objective function
and submit to samplers for solution:

* :ref:`bqm_sdk` are unconstrained and have binary variables.

  BQMs are typically used for applications that optimize over decisions that could
  either be true (or yes) or false (no); for example, should an antenna transmit,
  or did a network node experience failure?

  Constraints for this model are typically represented by adding
  :ref:`penalty models <penalty_sdk>` to the objective.

* :ref:`cqm_sdk` can be constrained and have real, integer and binary variables.

  CQMs are typically used for applications that optimize problems that might
  include integer and/or binary variables and one or more constraints.

  Constraints for this model are represented natively.

* :ref:`dqm_sdk` are unconstrained and have discrete variables.

  DQMs are typically used for applications that optimize over several distinct
  options; for example, which shift should employee X work, or should the state
  on a map be colored red, blue, green or yellow?

  Constraints for this model are typically represented by adding
  :ref:`penalty models <penalty_sdk>` to the objective.

* :ref:`nl_model_sdk` can be constrained and have different types of variables.

  Nonlinear (NL) models are typically used for applications that optimize over 
  decision variables that represent a common logic, such as subsets of choices 
  or permutations of ordering; for example, which of :math:`X` available shifts 
  should be assigned to each of :math:`Y`` employees, or in which order should 
  a traveling salesperson visit a list of cities?

  Constraints for this model are represented natively, both explicitly and 
  implicitly through the variable types.

.. _formulating_cqm:

Example: CQM for Greatest Rectangle Area
========================================

Consider the simple problem of finding the rectangle with the greatest area when the
perimeter  is limited.

In this example, the perimeter  of the rectangle is set to 8 (meaning the
largest area is for the :math:`2X2` square). A CQM is created with two integer
variables, :math:`i, j`, representing the lengths of the rectangle's sides, an
objective function :math:`-i*j`, representing the rectangle's area (the
multiplication of side :math:`i` by side :math:`j`, with a minus sign because
Ocean samplers minimize rather than maximize), and a constraint
:math:`2i + 2j <= 8`, requiring that the sum of both sides must not exceed the
perimeter .

>>> from dimod import ConstrainedQuadraticModel, Integer
>>> i = Integer('i', upper_bound=4)
>>> j = Integer('j', upper_bound=4)
>>> cqm = ConstrainedQuadraticModel()
>>> cqm.set_objective(-i*j)
>>> cqm.add_constraint(2*i+2*j <= 8, "Max perimeter")
'Max perimeter'

.. _formulating_bqm:

Example: BQM for a Boolean Circuit
==================================

Consider the problem of determining outputs of a Boolean logic circuit.
In its original context (in "problem space"), the circuit might be described with
input and output voltages, equations of its component resistors, transistors,
etc, an equation of logic symbols, multiple or an aggregated truth table, and so
on. You can choose to use Ocean software to formulate BQMs for binary gates
directly in your code or mathematically formulate a BQM, and both can be done in
various ways; for example, a BQM for each gate or one BQM for all the circuit's
gates.

The following are two example formulations.

1. The :ref:`penalty_sdk` section shows that a NOT gate, represented symbolically
   as :math:`x_2 \Leftrightarrow \neg x_1`, is formulated mathematically as BQM,

   .. math::

       -x_1 -x_2  + 2x_1x_2

2. Ocean's :doc:`dimod </docs_dimod/sdk_index>` tool enables the
   following formulation of an AND gate as a BQM:

>>> from dimod.generators import and_gate
>>> bqm = and_gate('in1', 'in2', 'out')

The BQM for this AND gate may look like this:

>>> bqm     # doctest: +SKIP
BinaryQuadraticModel({'in1': 0.0, 'in2': 0.0, 'out': 3.0},
...                  {('in2', 'in1'): 1.0, ('out', 'in1'): -2.0, ('out', 'in2'): -2.0},
...                  0.0,
...                  'BINARY')

The members of the two dicts are linear and quadratic coefficients, respectively,
the third term is a constant offset associated with the model, and the fourth
shows the variable types in this model are binary.

For more detailed information on the parts of Ocean programming model and how
they work together, see :ref:`oceanstack`.

Once you have a model that represents your problem, you sample
it for solutions. :ref:`samplers_and_solvers` explains how to submit your
problem for solution.
