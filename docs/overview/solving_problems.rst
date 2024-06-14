.. _solving_problems:

========================================
Workflow Steps: Formulation and Sampling
========================================

The two main steps of solving problems on quantum computers are:

1. **Formulate your problem as an objective function**

   Objective (cost) functions are mathematical expressions of the problem to be
   optimized; for quantum computing, these are models (e.g., quadratic models\ [#]_\ ) 
   that have lowest values (energy) for good solutions to the problems they represent.

2. **Find good solutions by sampling**

   Samplers are processes that sample from low-energy states of objective functions.
   Find good solutions by submitting your model to one of a variety of
   Ocean's quantum, classical, and hybrid quantum-classical samplers.

.. figure:: ../_images/SolutionOverview.svg
   :name: SolutionOverview
   :alt: image
   :align: center
   :width: 100%

   Solution steps: (1) a problem known in "problem space" (a circuit of Boolean gates, a graph, a network, etc) is formulated as a model, mathematically or using Ocean functionality, and (2) the model is sampled for solutions.

.. [#]
  Quadratic models have one or two variables per term. A simple example of a
  quadratic model is,

  .. math::

      Ax + By + Cxy

  where :math:`A`, :math:`B`, and :math:`C` are constants. Single-variable
  terms---:math:`Ax` and :math:`By` here---are linear with the constant biasing
  the term's variable. Two-variable terms---:math:`Cxy` here---are quadratic with
  a relationship between the variables.

