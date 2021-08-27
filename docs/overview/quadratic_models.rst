.. _quadratic_models:

================
Quadratic Models
================

For quantum computing, as for classical, solving a problem requires that it
be formulated in a way the computer and its software understand.

For example, if you want your laptop to calculate the area of a $1 coin, you might
express the problem as an equation, :math:`A=\pi r^2`, that you program as
:code:`math.pi*13.245**2` in your Python CLI. For a laptop with Python software,
this formulation---a particular string of alphanumeric symbols---causes the manipulation
of bits in a CPU and memory chips that produces the correct result.

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
by minimization, you can formulate the objective function
:math:`\min_x[2-(x+1)]^2`
by taking the square of the subtraction of one side from another. Minimization
seeks the shortest distance between the sides, which occurs at equality (with the
square eliminating negative distance).

Supported Models
================

Ocean supports a few models you can use to express your problem as an objective
function:

* :ref:`bqm_sdk`
* :ref:`dqm_sdk`
