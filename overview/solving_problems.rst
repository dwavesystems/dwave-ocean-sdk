.. _solving_problems:

===================================
Solving Problems on a D-Wave System
===================================

This section explains the basics of how D-Wave's quantum processing unit (QPU)
solves problems, what you need to do to use it for your problem, and how Ocean tools
can help.

How a D-Wave System Solves Problems
===================================

For quantum computing, as for classical, the first step in solving a problem is to
express it in a mathematical formulation compatible with the underlying physical hardware.
A D-Wave QPU is a chip with interconnected qubits; for example, a D-Wave 2000Q has up
to 2048 qubits connected in a :term:`Chimera` topology. Whatever
equation represents the problem you wish to solve, you submit it to the D-Wave system by
programming two fundamental controls:

* Qubit coupling strength: controls the degree to which two variables tend to agree.
* Qubit bias weight: controls the degree to which a variable tends to a particular outcome.

In fact, the equation (called an *objective function*) expresses the
energy of the system as a function of binary variables representing the qubits.
If you express your problem as an objective function such that desired outcomes have
low energy values and undesired outcomes have high energy values, the D-Wave
system solves your problem by finding low energy configurations of the objective
function.

.. toctree::
   :maxdepth: 1
   :hidden:

   technical_description

You can see a more technical description under :ref:`technical_description` or simply
use Ocean tools to abstract away those details of the solution steps:

1. :ref:`formulating`: express your problem (how does a protein fold? how do we optimize
   traffic flow in Beijing) in suitable mathematical equations.
2. :ref:`submitting`: give programming instructions to a D-Wave system.
3. :ref:`improving`: use performance enhancing features to improve solutions.

.. _formulating:

Formulating a Problem
=====================

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

.. table:: Energy for a Boolean NOT Operation as a Penalty.
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

.. _submitting:

Submitting a Problem
====================

.. _improving:

Improving the Solutions
=======================
