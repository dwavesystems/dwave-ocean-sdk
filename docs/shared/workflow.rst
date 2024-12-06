
.. start_workflow_intro

This section provides a high-level description of how you solve problems using
quantum computers.

The two main steps of solving problems using quantum computers are:

1.  **Formulate your problem as an objective function**

    :ref:`Objective (cost) functions <concepts_objectives>` are mathematical
    expressions of the problem to be optimized; for quantum computing, these are
    :ref:`quadratic and nonlinear models <gs_concepts_qms>` that have lowest
    values (energy) for good solutions to the problems they represent.

2.  **Find good solutions by sampling**

    :ref:`Samplers <gs_concepts_samplers>` are processes that sample from
    low-energy states of objective functions. Find good solutions by submitting
    your quadratic or nonlinear model to one of a variety of |dwave_short|'s
    quantum, classical, and hybrid quantum-classical samplers.

.. note::
    Samplers run---either remotely (for example, in |dwave_short|’s Leap
    service) or locally on your CPU---on compute resources known as *solvers*.
    (Note that some classical samplers actually brute-force solve small problems
    rather than sample, and these are also referred to as solvers.)

.. end_workflow_intro


.. |figObjectiveFunction| replace:: dummy

.. start_objective

To express a problem for a |dwave_short| solver in a form that enables solution
by minimization, you need an *objective function*, a mathematical expression of
the energy of a system. When the solver is a QPU, the energy is a function of
binary variables representing its qubits; for quantum-classical hybrid solvers,
the objective function might be more abstract.

.. figure:: ../../_images/obj.png
    :name: |figObjectiveFunction|
    :scale: 50 %
    :alt: Energy of objective function.

    Energy of the objective function.

For most problems, the lower the energy of the objective function, the better
the solution. Sometimes any low-energy state is an acceptable solution to the
original problem; for other problems, only optimal solutions are acceptable. The
best solutions typically correspond to the *global minimum* energy in the
solution space; see :numref:`Figure %s <obj>`.

.. end_objective


.. start_simple_objective_example

As an illustrative example, consider solving a simple equation, :math:`x+1=2`,
not by the standard algebraic techniques but by formulating an objective that
at its minimum value assigns a value to the variable, :math:`x`, that is also
a good solution to the original equation.

Taking the square of the subtraction of one side from another, you can formulate
the following objective function to minimize:

.. math::

    \text{E}(x) &= [2-(x+1)]^2

    &= (1-x)^2

In this case minimization, :math:`\min_x{(1-x)^2}`, seeks the shortest distance
between the sides of the original equation, which occurs at equality (with the
square eliminating negative distance).

.. end_simple_objective_example


.. start_samplers

:ref:`Samplers <gs_concepts_samplers>` are processes that sample from low-energy
states of objective functions. Having formulated an
:ref:`objective function <concepts_objectives>` that represents your problem
(typically as a :ref:`quadratic or nonlinear model <gs_concepts_qms>`), you
sample it for solutions.

|dwave_short| provides quantum, classical, and quantum-classical hybrid samplers
that run either remotely (for example, in |dwave_short|’s Leap service) or
locally on your CPU.

*   QPU Solvers

    |dwave_short| currently supports |dwave_5kq| quantum computers.

    This guide focuses on QPU solvers and provides examples of using quantum
    computers to solve problems.

*   Quantum-Classical Hybrid Solvers

    Quantum-classical hybrid is the use of both classical and quantum resources
    to solve problems, exploiting the complementary strengths that each
    provides. For an overview of, and motivation for, hybrid computing, see:
    `Medium Article on Hybrid Computing <https://medium.com/d-wave/three-truths-and-the-advent-of-hybrid-quantum-computing-1941ba46ff8c>`_.

    |dwave_short| provides two types of hybrid solvers:
    :ref:`Leap service's hybrid solvers <sysdocs:doc_leap_hybrid>`, which are
    cloud-based hybrid compute resources, and hybrid solvers developed in Ocean
    software's :std:doc:`dwave-hybrid <oceandocs:docs_hybrid/sdk_index>` tool.

*   Classical Solvers

    You might use a classical solver while developing your code or on a small
    version of your problem to verify your code.

    For information on classical solvers, see the
    :std:doc:`Ocean software documentation <oceandocs:index>`.

.. end_samplers


.. |figSimpleRandomSampler| replace:: dummy

.. start_simple_sampler_example

As an illustrative example, consider solving by sampling the objective,
:math:`\text{E}(x) = (1-x)^2` found in the :ref:`gs_simple_obj_example`
example above to represent equation, :math:`x+1=2`.

This example creates a simple sampler that generates 10 random values of the
variable :math:`x` and selects the one that produces the lowest value of the
objective:

>>> import random
...
>>> x = [random.uniform(-10, 10) for i in range(10)]
>>> e = list(map(lambda x: (1-x)**2, x))
>>> best_found = x[e.index(min(e))]

One particular execution found this best solution:

>>> print('x_i = ' + ' , '.join(f'{x_i:.2f}' for x_i in x))     # doctest: +SKIP
x_i = 7.87, 1.79, 9.61, 2.37, 0.68, -2.93, 3.96, 1.30, -3.85, -0.13
>>> print('e_i = ' + ', '.join(f'{e_i:.2f}' for e_i in e))      # doctest: +SKIP
e_i = 47.23, 0.63, 74.19, 1.89, 0.10, 15.44, 8.77, 0.09, 23.50, 1.28
>>> print("Best solution found is {:.2f}".format(best_found))   # doctest: +SKIP
Best solution found is 1.30

:numref:`Figure %s <simpleRandomSampler>` shows the value of the objective
function for the random values of :math:`x` chosen in the execution above. The
minimum distance between the sides of the original equation, which occurs at
equality, has the lowest value (energy) of :math:`\text{E}(x)`.

.. figure:: ../../_images/random_sampler_x_e.png
    :name: |figSimpleRandomSampler|
    :scale: 75 %
    :alt: Simple random sampler: E(x) versus x.

    Values of the objective function, :math:`\text{E}(x) = (1-x)^2`, versus
    random values of :math:`x` selected by a simple random sampler.

.. end_simple_sampler_example
