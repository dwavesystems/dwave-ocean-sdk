.. _qpu_workflow:

========================================
Basic Workflow: Formulation and Sampling
========================================

TODO: this is from sources:

* Workflow: Formulation and Sampling 
  (https://docs.dwavesys.com/docs/latest/c_gs_workflow.html)
  chapter of https://docs.dwavesys.com/docs/latest/doc_getting_started.html
  

.. include:: ../shared/workflow.rst
    :start-after: start_workflow_intro
    :end-before: end_workflow_intro

.. _qpu_workflow_objective_functions:

Objective Functions
===================

.. |figObjectiveFunction| replace:: qpuObjectiveFunction

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

Models
======

To express your problem as an objective function and submit to a |dwave_short|
sampler for solution, you typically use one of the quadratic models\ [#]_ 
provided by :std:doc:`Ocean software <oceandocs:index>`:

*   :ref:`bqm_sdk` are unconstrained\ [#]_ and have binary variables.

    BQMs are typically used for applications that optimize over decisions that
    could either be true (or yes) or false (no); for example, should an antenna
    transmit, or did a network node experience failure?

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
    :ref:`higher order models <oceandocs:higher_order>`, which are typically
    reduced to quadratic for sampling.

.. [#]
    Constraints for such models are typically represented by adding
    :ref:`penalty models <sysdocs:cb_techniques>` to the objective, as shown
    in the :ref:`getting_started_formulation_constraints` section.

.. _qpu_workflow_samplers:

Samplers
========

.. include:: ../shared/workflow.rst
    :start-after: start_samplers
    :end-before: end_samplers

.. _qpu_simple_sampling_example:

Simple Sampling Example
-----------------------

.. |figSimpleRandomSampler| replace:: qpuSimpleRandomSampler

.. include:: ../shared/workflow.rst
    :start-after: start_simple_sampler_example
    :end-before: end_simple_sampler_example

.. _qpu_workflow_simple_example:

Simple Workflow Example
=======================

TODO: add example
