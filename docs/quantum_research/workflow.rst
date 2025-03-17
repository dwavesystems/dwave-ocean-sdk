.. _qpu_workflow:

========================================
Basic Workflow: Formulation and Sampling
========================================

This section provides a high-level description of how you solve problems using
quantum computers directly. For solving problems with :term:`hybrid`
:term:`solver`\ s, see the :ref:`opt_workflow` section.

.. include:: ../shared/workflow.rst
    :start-after: start_workflow_intro
    :end-before: end_workflow_intro

.. _qpu_workflow_objective_functions:

Objective Functions
===================

.. include:: ../shared/workflow.rst
    :start-after: start_objective
    :end-before: end_objective

.. _qpu_workflow_simple_obj_example:

Simple Objective Example
------------------------

.. include:: ../shared/workflow.rst
    :start-after: start_simple_objective_example
    :end-before: end_simple_objective_example

The :ref:`qpu_simple_sampling_example` example below shows an equally simple
solution by sampling.

.. _qpu_workflow_models:

Supported Models
----------------

To express your problem as an objective function and submit to a |dwave_short|
sampler for solution, you typically use one of the
:ref:`Ocean software <index_ocean_sdk>` quadratic\ [#]_
:ref:`models <concept_models>` supported by |dwave_short| quantum computers:

*   .. include:: ../shared/models.rst
        :start-after: start_models_bqm
        :end-before: end_models_bqm
*   .. include:: ../shared/models.rst
        :start-after: start_models_ising
        :end-before: end_models_ising
*   .. include:: ../shared/models.rst
        :start-after: start_models_qubo
        :end-before: end_models_qubo

.. [#]
    Quadratic functions have one or two variables per term. A simple example of
    a quadratic function is,

    .. math::

        D = Ax + By + Cxy

    where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable
    terms---:math:`Ax` and :math:`By` here---are linear with the constant
    biasing the term's variable. Two-variable terms---:math:`Cxy` here---are
    quadratic with a relationship between the variables.

    Ocean software also provides support for
    :ref:`higher order models <dimod_higher_order_models>`, which are typically
    reduced to quadratic for sampling.

.. _qpu_workflow_samplers:

Samplers
========

.. include:: ../shared/workflow.rst
    :start-after: start_samplers
    :end-before: end_samplers

.. _qpu_simple_sampling_example:

Simple Sampling Example
-----------------------

.. include:: ../shared/workflow.rst
    :start-after: start_simple_sampler_example
    :end-before: end_simple_sampler_example

.. _qpu_workflow_simple_example:

.. todo:: add example: Simple Workflow Example

    Simple Workflow Example (title)
