.. _gs_formulation:

============================================
Formulation: Objectives and Quadratic Models
============================================

For quantum computing, as for classical, solving a problem requires that it
be formulated in a way the computer and its software understand.

For example, if you want your laptop to calculate the area of a $1 coin, you might
express the problem as an equation, :math:`A=\pi r^2`, that you program as
:code:`math.pi*13.245**2` in your Python CLI. For a laptop with Python software,
this formulation---a particular string of alphanumeric symbols---causes the manipulation
of bits in a CPU and memory chips that produces the correct result.

.. _gs_objectives:

Objective Functions
===================

With quantum computing, you express your problem in a form that enables solution by
minimization: an *objective function*, which is a mathematical expression of the
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

As an illustrative example, consider the equation :math:`x+1=2`. To solve it
by minimization, you can formulate the objective function :math:`\min_x[2-(x+1)]^2`
by taking the square of the subtraction of one side from another. Minimization
seeks the shortest distance between the sides, which occurs at equality (with the
square eliminating negative distance).

The examples of this :ref:`Getting Started documentation <gs>` show some simple
objective function to help you begin. D-Wave's
:std:doc:`System Documentation <sysdocs_gettingstarted:index>` provides a wealth
of resources on formulating problems.

Supported Models
================

Ocean supports various models to express your problem as an objective function
and submit to samplers for solution:

* :ref:`bqm_sdk` are unconstrained and have binary variables

  Used for applications that optimize over decisions that could either be true
  (or yes) or false (no); for example, should an antenna transmit, or
  did a network node experience failure?

  Constraints for this model are typically represented by
  :ref:`penalty models <penalty_sdk>`.

* :ref:`cqm_sdk` can be constrained and have integer and binary variables

  Used for applications that optimize over decisions that could either be true
  (or yes) or false (no); for example, should an antenna transmit, or
  did a network node experience failure?

  Constraints for this model are represented natively.

* :ref:`dqm_sdk` are unconstrained and have discrete variables

  Used for applications that optimize over several distinct options; for example,
  which shift should employee X work, or should the state on a map be colored red,
  blue, green or yellow?

  Constraints for this model are typically represented by
  :ref:`penalty models <penalty_sdk>`.

.. note:: Ocean also provides support for
   :ref:`higher order models <oceandocs:higher_order>`, which are typically
   reduced to quadratic for sampling.

.. _formulating_bqm:

Example Formulation
===================

There are different ways of mapping between a problem---chains of amino acids
forming 3D structures of folded proteins, traffic in the streets of Beijing,
circuits of binary gates---and a BQM (or :term:`DQM`) to be solved (by sampling)
with a D-Wave system, a :term:`hybrid` solver, or locally on your CPU.

For example, consider the problem of determining outputs of a Boolean logic circuit. In its original
context (in "problem space"), the circuit might be described with input and output voltages,
equations of its component resistors, transistors, etc, an equation of logic symbols,
multiple or an aggregated truth table, and so on. You can choose to use Ocean software to formulate
BQMs for binary gates directly in your code or mathematically formulate a BQM, and both
can be done in different ways too; for example, a BQM for each gate or one BQM for
all the circuit's gates.

The following are two example formulations.

1. The :ref:`not` example, takes a NOT gate represented symbolically as
   :math:`x_2 \Leftrightarrow \neg x_1` and formulates it mathematically as the following BQM:

   .. math::

       -x_1 -x_2  + 2x_1x_2

   The table below shows that this BQM has lower values for valid states of the NOT
   gate (e.g., :math:`x_1=0, x_2=1`) and higher for invalid states (e.g., :math:`x_1=0, x_2=0`).

   .. table:: Boolean NOT Operation Formulated as a BQM.
      :name: BooleanNOTasQUBO

      ===========  ============  ===============  ============
      :math:`x_1`  :math:`x_2`   **Valid?**       **BQM Value**
      ===========  ============  ===============  ============
      :math:`0`    :math:`1`     Yes              :math:`0`
      :math:`1`    :math:`0`     Yes              :math:`0`
      :math:`0`    :math:`0`     No               :math:`1`
      :math:`1`    :math:`1`     No               :math:`1`
      ===========  ============  ===============  ============

2. Ocean's :doc:`dwavebinarycsp </docs_binarycsp/sdk_index>` tool enables the
   following formulation of an AND gate as a BQM:

>>> import dwavebinarycsp
>>> import dwavebinarycsp.factories.constraint.gates as gates
>>> csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
>>> csp.add_constraint(gates.and_gate(['x1', 'x2', 'y1']))  # add an AND gate
>>> bqm = dwavebinarycsp.stitch(csp)

The resultant BQM of this AND gate may look like this:

>>> bqm     # doctest: +SKIP
BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0},
...                  {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0},
...                  0,
...                  'BINARY')

The members of the two dicts are linear and quadratic coefficients, respectively,
the third term is a constant offset associated with the model, and the fourth
shows the variable types in this model are binary.

For more detailed information on the parts of Ocean programming model and how
they work together, see :ref:`oceanstack`.

Once you have a BQM (or :term:`DQM`) that represents your problem, you sample
it for solutions. :ref:`samplers_and_solvers` explains how to submit your
problem for solution.
