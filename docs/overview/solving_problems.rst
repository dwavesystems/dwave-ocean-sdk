.. _solving_problems:

========================================
Workflow Steps: Formulation and Sampling
========================================

The two main steps of solving problems on quantum computers are:

1. **Formulate your problem as an objective function**

   Objective (cost) functions are mathematical expressions of the problem to be
   optimized; for quantum computing, these are quadratic models that have lowest
   values (energy) for good solutions to the problems they represent.

2. **Find good solutions by sampling the quadratic model**

   Samplers are processes that sample from low-energy states of objective functions.
   Find good solutions by submitting your quadratic model to one of a variety of
   quantum, classical, and hybrid quantum-classical samplers.

.. figure:: ../_images/SolutionOverview.png
   :name: SolutionOverview
   :alt: image
   :align: center
   :height: 350 pt
   :width: 850 pt

   Solution steps: (1) a problem known in "problem space" (a circuit of Boolean gates, a graph, a network, etc) is formulated as a quadratic model, mathematically or using Ocean functionality, and (2) the model is sampled for solutions.

.. _formulating_bqm:

Formulate Your Problem for a Quantum Computer
=============================================

There are different ways of mapping between a problem---chains of amino acids
forming 3D structures of folded proteins, traffic in the streets of Beijing,
circuits of binary gates---and a BQM (or :term:`DQM`) to be solved (by sampling)
with a D-Wave system, a :term:`hybrid` solver, or locally on your CPU.

For example, consider the problem of determining outputs of a Boolean logic circuit. In its original
context (in "problem space"), the circuit might be described with input and output voltages,
equations of its component resistors, transistors, etc, an equation of logic symbols,
multiple or an aggregated truth table, and so on. You can choose to use Ocean software to formulate
BQMs for binary gates directly in your code or mathematically formulate a BQM, and both
can be done in different ways too; for example, a BQM for each gate or one BQM for
all the circuit's gates.

The following are two example formulations.

1. The :ref:`not` example, takes a NOT gate represented symbolically as
   :math:`x_2 \Leftrightarrow \neg x_1` and formulates it mathematically as the following BQM:

   .. math::

       -x_1 -x_2  + 2x_1x_2

   The table below shows that this BQM has lower values for valid states of the NOT
   gate (e.g., :math:`x_1=0, x_2=1`) and higher for invalid states (e.g., :math:`x_1=0, x_2=0`).

   .. table:: Boolean NOT Operation Formulated as a BQM.
      :name: BooleanNOTasQUBO

      ===========  ============  ===============  ============
      :math:`x_1`  :math:`x_2`   **Valid?**       **BQM Value**
      ===========  ============  ===============  ============
      :math:`0`    :math:`1`     Yes              :math:`0`
      :math:`1`    :math:`0`     Yes              :math:`0`
      :math:`0`    :math:`0`     No               :math:`1`
      :math:`1`    :math:`1`     No               :math:`1`
      ===========  ============  ===============  ============

2. Ocean's :doc:`dimod </docs_dimod/sdk_index>` tool enables the
   following formulation of an AND gate as a BQM:

>>> from dimod.generators import and_gate
>>> bqm = and_gate('in1', 'in2', 'out')

The BQM for this AND gate may look like this:

>>> bqm     # doctest: +SKIP
BinaryQuadraticModel({'in1': 0.0, 'in2': 0.0, 'out': 3.0},
...                  {('in2', 'in1'): 1.0, ('out', 'in1'): -2.0, ('out', 'in2'): -2.0},
...                  0.0,
...                  'BINARY')

The members of the two dicts are linear and quadratic coefficients, respectively,
the third term is a constant offset associated with the model, and the fourth
shows the variable types in this model are binary.

For more detailed information on the parts of Ocean programming model and how
they work together, see :ref:`oceanstack`.
