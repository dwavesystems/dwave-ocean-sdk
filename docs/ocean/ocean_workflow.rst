.. _ocean_workflow:

========================================
Workflow Steps: Formulation and Sampling
========================================

The two main steps of solving problems on quantum computers are:

1. **Formulate your problem as an objective function**

   Objective (cost) functions are mathematical expressions of the problem to be
   optimized; for quantum computing, these are models (e.g., quadratic models\ [#]_\ ) 
   that have lowest values (energy) for good solutions to the problems they represent.

2. **Find good solutions by sampling**

   Samplers are processes that sample from low-energy states of objective functions.
   Find good solutions by submitting your model to one of a variety of
   Ocean's quantum, classical, and hybrid quantum-classical samplers.

.. figure:: ../_images/SolutionOverview.svg
   :name: SolutionOverview
   :alt: image
   :align: center
   :width: 100%

   Solution steps: (1) a problem known in "problem space" (a circuit of Boolean gates, a graph, a network, etc) is formulated as a model, mathematically or using Ocean functionality, and (2) the model is sampled for solutions.

.. [#]
  Quadratic models have one or two variables per term. A simple example of a
  quadratic model is,

  .. math::

      Ax + By + Cxy

  where :math:`A`, :math:`B`, and :math:`C` are constants. Single-variable
  terms---:math:`Ax` and :math:`By` here---are linear with the constant biasing
  the term's variable. Two-variable terms---:math:`Cxy` here---are quadratic with
  a relationship between the variables.

Formulation
===========

For quantum computing, as for classical, solving a problem requires that it
be formulated in a way the computer and its software understand.

For example, if you want your laptop to calculate the area of a $1 coin, you might
express the problem as an equation, :math:`A=\pi r^2`, that you program as
:code:`math.pi*13.245**2` in your Python terminal. For a laptop with Python software,
this formulation---a particular string of alphanumeric symbols---causes the manipulation
of bits in a CPU and memory chips that produces the correct result.

.. _gs_objectives:

Objective Functions
-------------------

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
----------------

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
----------------------------------------

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

.. _ocean_workflow_formulating_bqm:

Example: BQM for a Boolean Circuit
----------------------------------

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

Sampling: Minimizing the Objective
==================================

Having formulated an objective function that represents your problem as described
in the :ref:`gs_formulation` section, you sample this :term:`quadratic model` (QM)
or :term:`nonlinear model` for solutions. Ocean software provides quantum, classical, 
and quantum-classical hybrid :term:`sampler`\ s that run either remotely (for example, 
in D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ environment) or locally on 
your CPU. These compute resources are known as :term:`solver`\ s.

.. note:: Some classical samplers actually brute-force solve small problems rather
    than sample, and these are also referred to as "solvers".

Ocean's :term:`sampler`\ s enable you to submit your problem to remote or local
compute resources (:term:`solver`\ s) of different types:

* :ref:`using_hybrid` such as `Leap's <https://cloud.dwavesys.com/leap/>`_
  ``hybrid_binary_quadratic_model_version<x>`` solver or
  ``hybrid_nonlinear_program_version<x>``.
* :ref:`using_cpu` such as :class:`~dimod.reference.samplers.ExactSolver` for
  exact solutions to small problems
* :ref:`using_qpu` such as the Advantage system.

.. _submitting:

Submit the Model to a Solver
----------------------------

The example code below submits a BQM representing a Boolean AND gate (see also the
:ref:`ocean_workflow_formulating_bqm` section) to a Leap hybrid solver.
In this case, :doc:`dwave-system </docs_system/sdk_index>`'s
:class:`~dwave.system.samplers.LeapHybridSampler` is the Ocean sampler and the
remote compute resource selected might be Leap hybrid solver
``hybrid_binary_quadratic_model_version<x>``.

>>> from dimod.generators import and_gate
>>> from dwave.system import LeapHybridSampler
>>> bqm = and_gate('x1', 'x2', 'y1')
>>> sampler = LeapHybridSampler()    # doctest: +SKIP
>>> answer = sampler.sample(bqm)   # doctest: +SKIP
>>> print(answer)    # doctest: +SKIP
  x1 x2 y1 energy num_oc.
0  1  1  1    0.0       1
['BINARY', 1 rows, 1 samples, 3 variables]

.. _improving:

Improve the Solutions
---------------------

For complex problems, you can often improve solutions and performance by applying
some of Ocean software's preprocessing, postprocessing, and diagnostic tools.

Additionally, when submitting problems directly to a D-Wave system (:ref:`using_qpu`),
you can benefit from some advanced features (for example features such as
spin-reversal transforms and anneal offsets, which reduce the impact of possible
analog and systematic errors) and the techniques described in the
:std:doc:`Problem Solving Handbook <sysdocs_gettingstarted:doc_handbook>` guide.

Example: Preprocessing
~~~~~~~~~~~~~~~~~~~~~~

:std:doc:`dwave-preprocessing <oceandocs:docs_preprocessing/sdk_index>` provides
algorithms such as roof duality, which fixes some of a problem's variables before
submitting to a sampler.

As an illustrative example, consider the binary quadratic model, :math:`x + yz`.
Clearly :math:`x=0` for all the best solutions (variable assignments that minimize
the value of the model) because any assignment of variables that sets :math:`x=1`
adds a value of 1 compared to assignments that set :math:`x=0`. (On the other
hand, assignment :math:`y=0, z=0`, assignment :math:`y=0, z=1`, and assignment
:math:`y=1, z=0` are all equally good.) Therefore, you can fix variable :math:`x`
and solve a smaller problem.

>>> from dimod import BinaryQuadraticModel
>>> from dwave.preprocessing import roof_duality
>>> bqm = BinaryQuadraticModel({'x': 1}, {('y', 'z'): 1}, 0,'BINARY')
>>> roof_duality(bqm)
(0.0, {'x': 0})

For problems with hundreds or thousands of variables, such preprocessing can
significantly improve performance.

Example: Diagnostics
~~~~~~~~~~~~~~~~~~~~

When sampling directly on the D-Wave QPU, the mapping from problem variables to qubits,
:term:`minor-embedding`, can significantly
affect performance. Ocean tools perform this mapping heuristically so simply rerunning
a problem might improve results. Advanced users may customize the mapping by directly
using the :std:doc:`minorminer <oceandocs:docs_minorminer/source/sdk_index>` tool,
setting a minor-embedding themselves, or using D-Wave's
:doc:`problem-inspector </docs_inspector/sdk_index>` tool.

For example, the :ref:`and` example submits the BQM representing an AND gate
to a D-Wave system, which requires mapping the problem's logical variables
to qubits on the QPU. The code below invokes D-Wave's
:doc:`problem-inspector </docs_inspector/sdk_index>` tool to visualize the
minor-embedding.

>>> import dwave.inspector
>>> dwave.inspector.show(response)   # doctest: +SKIP

.. figure:: ../_images/inspector_AND2.png
  :name: inspector_AND2
  :scale: 50 %
  :alt: View rendered by Ocean's problem inspector.

  View of the logical and embedded problem rendered by Ocean's problem inspector. The AND gate's original BQM is represented on the left; its embedded representation on a D-Wave system, on the right, shows a two-qubit chain (qubits 176 and 180) for variable :math:`x2`. The tool is helpful in visualizing the quality of your embedding.

Example: Postprocessing
~~~~~~~~~~~~~~~~~~~~~~~

Example :ref:`pp_greedy` improves samples returned from a QPU by post-processing with a
classical greedy algorthim.
