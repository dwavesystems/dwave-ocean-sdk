.. _concept_hybrid:

======
Hybrid 
======

Quantum-classical hybrid is the use of both classical and quantum resources to solve problems, 
exploiting the complementary strengths that each provides. As quantum processors grow in size, 
offloading hard optimization problems to quantum computers promises performance benefits similar 
to CPUs' outsourcing of compute-intensive graphics-display processing to GPUs. 

For an overview of, and motivation for, hybrid computing, see this 
`Medium Article <https://medium.com/d-wave/three-truths-and-the-advent-of-hybrid-quantum-computing-1941ba46ff8c>`_\ . 

D-Wave's `Leap quantum cloud service <https://cloud.dwavesys.com/leap>`_ provides cloud-based 
hybrid solvers you can submit arbitrary BQMs to. These solvers, which implement state-of-the-art 
classical algorithms together with intelligent allocation of the quantum processing unit (QPU) 
to parts of the problem where it benefits most, are designed to accommodate even very large problems. 
Leap's solvers can relieve you of the burden of any current and future development and optimization 
of hybrid algorithms that best solve your problem. 

:ref:`dwave-hybrid <sdk_index_hybrid>` provides you with a Python framework for building a 
variety of flexible hybrid workflows. These use quantum and classical resources together to find 
good solutions to your problem. For example, a hybrid workflow might use classical resources to 
find a problem’s hard core and send that to the QPU, or break a large problem into smaller pieces 
that can be solved on a QPU and then recombined.

The *dwave-hybrid* framework enables rapid development of experimental prototypes, which provide 
insight into expected performance of the productized versions. It provides reference samplers and 
workflows you can quickly plug into your application code. You can easily experiment with customizing
workflows that best solve your problem. You can also develop your own hybrid components to optimize
performance.  

Related Information
===================

*   :ref:`opt_index_hybrid` gets you started with hybrid samplers.
*   :ref:`opt_index_hybrid_solvers` describes the supported hybrid solvers in the Leap service.
*   :ref:`opt_index_using` describes best practices.
