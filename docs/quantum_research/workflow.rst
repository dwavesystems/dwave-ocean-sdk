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

Simple Workflow Example
=======================

This example uses the :ref:`Ocean software <index_ocean_sdk>` package,
:ref:`index_dimod`, to formulate a small objective function: the
:func:`~dimod.generators.combinations` function generates a :term:`BQM` that
represents the problem of selecting exactly :math:`k` of :math:`n` binary
variables.

The following code creates a BQM that is minimized when exactly two
(:math:`k=2`) of the three (:math:`n=3`) variables :code:`a, b, c` are
:math:`1`:

>>> import dimod
>>> bqm = dimod.generators.combinations(['a', 'b', 'c'], 2)

Now solve on a |dwave_short| quantum computer using the
:class:`~dwave.system.samplers.DWaveSampler` sampler from Ocean software's
:ref:`index_system` package. Also use its
:class:`~dwave.system.composites.EmbeddingComposite` composite to map the
unstructured problem (variables such as :math:`a` etc.) to the sampler's
:ref:`graph structure <qpu_topologies>` (the QPU's numerically indexed qubits)
in a process known as :term:`minor-embedding`.

The next code sets up a D-Wave quantum computer as the sampler.

.. include:: ../shared/examples.rst
    :start-after: start_default_solver_config
    :end-before: end_default_solver_config

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())

Because the sampled solution is probabilistic, returned solutions may differ
between runs. Typically, when submitting a problem to the system, you ask for
many samples, not just one. This way, you see multiple “best” answers and reduce
the probability of settling on a suboptimal answer. Below, ask for 1000 samples.

>>> sampleset = sampler.sample(bqm, num_reads=1000, label='SDK Examples - QPU Workflow')
>>> print(sampleset)        # doctest: +SKIP
   a  b  c energy num_oc. chain_.
0  1  1  0    0.0     323     0.0
1  1  0  1    0.0     339     0.0
2  0  1  1    0.0     336     0.0
3  1  1  1    1.0       1     0.0
4  1  0  0    1.0       1     0.0
['BINARY', 5 rows, 1000 samples, 3 variables]

Almost all the returned samples represent valid value assignments for the
:math:`\binom{N}{k}` problem, and minima (low-energy states) of the BQM, and
with high likelihood the best (lowest-energy: here :math:`0.0` in the
:code:`energy` column) samples satisfy the formulation (two :math:`1`\ s among
the three variables columns, :code:`a, b, c`).