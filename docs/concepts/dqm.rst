.. _dqm_sdk:

=========================
Discrete Quadratic Models 
=========================

The discrete quadratic model (DQM) is a polynomial over discrete variables with
terms all of degree two or less, represented by equation,

.. math::

    E(\bf{v})
    = \sum_{i=1} a_i v_i
    + \sum_{i<j} b_{i,j} v_i v_j 
    + c
    \qquad\qquad v_i \in\{A, B, C, ...\}

where :math:`\{A, B, C, ...\}` are some set of discrete values such 
``{red, green, blue, yellow}`` or ``{3.2, 67}``.  

The :class:`dimod.DiscreteQuadraticModel` class can contain this model and its 
methods provide convenient utilities for working with representations
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


