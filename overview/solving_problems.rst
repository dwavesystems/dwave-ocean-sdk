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
to 2048 qubits connected in a manner that forms a :term:`Chimera` graph. Whatever
equation represents the problem you wish to solve, you submit it to the D-Wave system by
programming two fundamental controls:

* Qubit coupling strength: controls the degree to which two variables tend to agree.
* Qubit bias weight: controls the degree to which a variable tends to a particular outcome.

In fact, the equation (called an *objective function*) expresses the
energy of the system as a function of binary variables representing the qubits. The D-Wave
system solves the problem by finding its low energy configurations.

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

.. _submitting:

Submitting a Problem
====================

.. _improving:

Improving the Solutions
=======================
