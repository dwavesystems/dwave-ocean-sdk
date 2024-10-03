.. _opt_intro_hybrid:

==============
Hybrid Solvers
==============

Quantum-classical hybrid is the use of both classical and quantum resources to solve
problems, exploiting the complementary strengths that each provides. For an overview of,
and motivation for, hybrid computing, see:
`Medium Article on Hybrid Computing <https://medium.com/d-wave/three-truths-and-the-advent-of-hybrid-quantum-computing-1941ba46ff8c>`_.

Ocean software currently supports two types of hybrid solvers:

* :ref:`leap_hybrid_solvers` are cloud-based hybrid compute resources.
* :ref:`dwave_hybrid_solvers` are hybrid solvers developed in Ocean's :doc:`dwave-hybrid </docs_hybrid/sdk_index>` tool.

.. _leap_hybrid_solvers:

Leap's Hybrid Solvers
=====================

D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ quantum cloud service provides
cloud-based hybrid solvers to which you can submit arbitrary models. 
These solvers, which implement state-of-the-art classical algorithms together 
with intelligent allocation of the quantum processing unit (QPU) to parts of
the problem where it benefits most, are designed to accommodate even very large
problems. Leap's solvers can relieve you of the burden of any current and 
future development and optimization of hybrid algorithms that best solve 
your problem.

:ref:`hss` is an example of submitting a problem for solution on a Leap hybrid solver.


.. _dwave_hybrid_solvers:

dwave-hybrid Hybrid Solvers
===========================

:doc:`dwave-hybrid </docs_hybrid/sdk_index>` provides you with a Python framework
for building a variety of flexible
hybrid workflows. These use quantum and classical resources together to find good
solutions to your problem. For example, a hybrid workflow might use classical resources
to find a problem’s hard core and send that to the QPU, or break a large problem
into smaller pieces that can be solved on a QPU and then recombined.

The *dwave-hybrid* framework enables rapid development of experimental prototypes, which
provide insight into expected performance of the productized versions. It provides
reference samplers and workflows you can quickly plug into your application code. You
can easily experiment with customizing workflows that best solve your problem. You can
also develop your own hybrid components to optimize performance.

:ref:`map_kerberos` and :ref:`hybrid1` are examples of solving problems using
*dwave-hybrid* samplers.
