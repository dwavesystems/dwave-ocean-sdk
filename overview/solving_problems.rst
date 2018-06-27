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
third may benefit some problems) of this problem-solving procedure; see the :ref:`gs`
examples and system documentation for further description.

1. :ref:`formulating` your problem as a BQM.
2. :ref:`submitting` low-energy states of the BQM to find solutions.
3. :ref:`improving` solutions with advanced features.

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

There are different ways of mapping between any problem space (chains of amino acids
forming 3D structures of folded proteins, traffic in the streets of Beijing, circuits
of binary gates) and a BQM to be solved by sampling with a D-Wave system or locally on
your CPU/GPU. Here we provide an intuitive example.

Consider the problem of determining outputs of a Boolean logic circuit. In problem space
the circuit might be described with input and output Voltages, equations of
its electronic components (resistors, transistors, etc), logic symbols,
multiple or an aggregated truth table, and so on. You can mathematically
formulate a BQM---in different ways too, for example a BQM for each gate or one BQM for
all the circuit's gates---or use Ocean's formulations of binary gates directly in your
code.

For example, as shown in :ref:`not`, a NOT gate represented symbolically as
:math:`x_2 \Leftrightarrow \neg x_1` in problem space might be formulated
mathematically as the following QUBO:

.. math::

    E(a_i, b_{i,j}; x_i) = -x_1 -x_2  + 2x_1x_2

The following table shows that this QUBO has low energy for valid states of the NOT
gate and high energy for invalid states.

.. table:: Energy for a Boolean NOT Operation Formulated as a QUBO.
   :name: BooleanNOTAsPenalty

   ===========  ============  ===============  ============
   :math:`x_1`  :math:`x_2`   **Energy**       **Valid?**
   ===========  ============  ===============  ============
   :math:`0`    :math:`1`     :math:`0`        Yes
   :math:`1`    :math:`0`     :math:`0`        Yes
   :math:`0`    :math:`0`     :math:`1`        No
   :math:`1`    :math:`1`     :math:`1`        No
   ===========  ============  ===============  ============

If you formulate your problem as an Ising or QUBO model, Ocean lets you instantiate
a BQM from that; for example, :code:`bqm = dimod.BinaryQuadraticModel.from_qubo()`.

For some problems you might be able to skip the mathematical formulation and directly
use formulations that Ocean provides. For example, the
`dwavebinarycsp <http://dwavebinarycsp.readthedocs.io/en/latest/>`_ tool enables the
following formulation of an AND gate as a BQM:

.. code-block:: python

    >>> import dwavebinarycsp
    >>> import dwavebinarycsp.factories.constraint.gates as gates
    >>> csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
    >>> csp.add_constraint(gates.and_gate(['x1', 'x2', 'y1']))  # add an AND gate
    >>> bqm = dwavebinarycsp.stitch(csp)

Once you have a BQM that represents your problem, you sample it.

.. _submitting:

Sample
======

.. _improving:

Improve the Solutions
=====================
