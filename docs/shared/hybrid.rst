.. start_definition

Quantum-classical hybrid is the use of both classical and quantum resources to
solve problems, exploiting the complementary strengths that each provides. As
quantum processors grow in size, offloading hard optimization problems to
quantum computers promises performance benefits similar to CPUs' outsourcing of
compute-intensive graphics-display processing to GPUs.

For an overview of, and motivation for, hybrid computing, see this
`Medium Article <https://medium.com/d-wave/three-truths-and-the-advent-of-hybrid-quantum-computing-1941ba46ff8c>`_\ .

.. end_definition


.. start_leap_intro

The quantum-classical hybrid solvers in the |cloud|_ service are intended to
solve arbitrary application problems formulated as a :term:`nonlinear model` or
:term:`quadratic model`\ [#]_.

.. [#]
    Problems submitted **directly** to |dwave_short| quantum computers are in
    the :ref:`binary quadratic model <concept_models_bqm>` (BQM) format:
    unconstrained with binary-valued variables and structured for the
    :term:`topology` of the :term:`QPU`. Hybrid solvers may accept arbitrarily
    structured quadratic models and a nonlinear model, constrained or
    unconstrained, with real, integer, and binary variables.

These solvers, which implement state-of-the-art :term:`classical` algorithms
together with intelligent allocation of the quantum computer to parts of the
problem where it benefits most, are designed to accommodate even very large
problems. Hybrid solvers enable you to benefit from |dwave_short|'s deep
investment in researching, developing, optimizing, and maintaining
:term:`hybrid` algorithms.

.. end_leap_intro


.. start_dwave_hybrid_intro

:ref:`Ocean <index_ocean_sdk>` software's :ref:`dwave-hybrid <index_hybrid>`
tool provides you with a Python framework for building a variety of flexible
hybrid workflows. These use quantum and classical resources together to find
good solutions to your problem. For example, a hybrid workflow might use
classical resources to find a problem's hard core and send that to the
:term:`QPU`, or break a large problem into smaller pieces that can be solved on
a QPU and then recombined.

The *dwave-hybrid* framework enables rapid development of experimental
prototypes, which provide insight into expected performance of the productized
versions. It provides reference samplers and workflows you can quickly plug into
your application code. You can easily experiment with customizing workflows that
best solve your problem. You can also develop your own hybrid components to
optimize performance.

.. end_dwave_hybrid_intro
