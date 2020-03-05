.. _bqm_sdk:

=======================
Binary Quadratic Models 
=======================

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

The :class:`.BinaryQuadraticModel` class can contain both these models and its methods provide
convenient utilities for working with, and interworking between, the two representations
of a problem.

These models and their use in solving problems on the D-Wave system is described
in the following documentation:

* :std:doc:`Getting Started with the D-Wave System <sysdocs_gettingstarted:doc_getting_started>`

   Introduces key concepts such as objective functions, Ising models, QUBOs, and graphs, explains
   how these models are used to represent problems, and provides some simple examples.
* :std:doc:`D-Wave Problem-Solving Handbook <sysdocs_gettingstarted:doc_handbook>`

   Provides a variety of techniques for, and examples of, reformulating problems as BQMs.
* :std:doc:`Solving Problems on a D-Wave System <oceandocs:overview/solving_problems>`

   Describes and demonstrates the use of BQM in the context of Ocean software.


