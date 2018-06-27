.. _solving_problems:

===================================
Solving Problems on a D-Wave System
===================================

This section explains some of the basics of how D-Wave's quantum processing unit (QPU)
solves problems, what you need to do to use it for your problem, and how Ocean tools
can help.

How a D-Wave System Solves Problems
===================================

For quantum computing, as for classical, the first step in solving a problem is to
express it in a mathematical formulation compatible with the underlying physical hardware.
A D-Wave QPU is a chip with interconnected qubits; for example, a D-Wave 2000Q has up
to 2048 qubits connected in a :term:`Chimera` topology. Programming it consists mostly
of setting two types of values:

* Qubit coupling strength: controls the degree to which two qubits tend to the same state.
* Qubit bias weight: controls the degree to which a qubit tends to a particular state.

Given sets of coupling strengths and bias weights for its qubits, the system finds
low-energy states. If you formulate your problem such that desired outcomes have
low energy values and undesired outcomes have high energy values, the low-energy states
the D-Wave system finds are solutions to your problem. This formulation
is called an *objective function* for the system. More specifically, you formulate
an objective function where variables are "spin up"
(:math:`\uparrow`) and "spin down" (:math:`\downarrow`) states and relationships
between the spins, represented by couplings, are correlations or anti-correlations.
This is the :term:`Ising` model traditionally used in statistical mechanics or its
computer-science equivalent, the :term:`QUBO`, where variables are binary 0 and 1.

Ocean software can abstract away much of that. At its heart is a binary quadratic
model (BQM) class for handling the desired objective function. It helps
formulate objective functions for some common types of optimization problems.
It also provides an API to binary quadratic :term:`sampler`\ s, such as the D-Wave
system and classical algorithms you can run on your computer, which find the
low-energy states that constitute solutions to the problem.

The following sections give an intuitive explanation of these two steps (the
third may benefit some problems) of this problem-solving procedure.

1. :ref:`formulating`: express your problem (how does a protein fold? how do we optimize
   traffic flow in Beijing) as a BQM.
2. :ref:`submitting`: find solutions by sampling low-energy states of the BQM.
3. :ref:`improving`: use performance enhancing features to improve solutions.

.. figure:: ../_static/SolutionOverview.png
   :name: SolutionOverview
   :alt: image
   :align: center
   :scale: 100 %

   Solution steps: (1) formulate a problem that you know in "problem space" (a circuit
   of Boolean gates, a graph, a network, etc) as a BQM, mathematically or using
   Ocean functionality and (2) sample the BQM for probable solutions.

.. _formulating:

Formulate a Problem
===================

There are different ways and considerations to expressing your problem mathematically
for solution by a D-Wave system or locally on your CPU/GPU; that is, mapping from
your problem space (chains of amino acids and 3D structures of folded proteins or the
streets and cars in Beijing) to a representative objective function. Here we provide
an intuitive explanation; see the :ref:`gs` examples and system documentation for
further description.

Consider the problem of determining outputs of a Boolean logic circuit. The circuit
might be expressed in terms of input and output Voltages through equations at the level
of electronic components (resistors, transistors, etc), through logic symbolism,
as an aggregated truth table, and many other ways. But when using a :term:`sampler`
such as a D-Wave system, we express it in a binary formulation that has low energy
values for valid circuit configurations.

For example, any NOT gates (symbolically represented as :math:`z \Leftrightarrow \neg x`)
in the circuit might be represented by a binary equation

.. math::

    E(x, z) = 2xz-x-z+1,

which has low energy for valid states and high energy for invalid states:

.. table:: Energy for a Boolean NOT Operation.
   :name: BooleanNOTAsPenalty

   ===========  ============  ===============  ============
   **x**        **z**         **Energy**       **Valid?**
   ===========  ============  ===============  ============
   :math:`0`    :math:`1`     :math:`0`        Yes
   :math:`1`    :math:`0`     :math:`0`        Yes
   :math:`0`    :math:`0`     :math:`1`        No
   :math:`1`    :math:`1`     :math:`1`        No
   ===========  ============  ===============  ============

If we similarly represent all the circuit's gates and aggregate, overall the resulting
equation has lower energy for valid states, meaning that solutions of the equation
the sampler finds (low-energy configurations of the objective function) represent
solutions to the logic circuit.

You can choose to mathematically formulate the problem, as above or by first logically
aggregating all the circuit's gates into a single logical equation. Alternatively,
you can abstract away the mathematical representation altogether: Ocean tools provide
functionality for representing binary gates directly in your code.

The examples under :ref:`gs` show some ways of formulating a problem.



For example, the NOT gate above

If you state your problem mathematically, as a :term:`Ising` or
:term:`QUBO` formulation, you would typically use the class's methods for instantiating
a BQM. For example, the NOT gate formulation above is a QUBO (see :ref:`not`):
, so
:code:`bqm = dimod.BinaryQuadraticModel.from_qubo()`


.. _submitting:

Sample
======

.. _improving:

Improve the Solutions
=====================
