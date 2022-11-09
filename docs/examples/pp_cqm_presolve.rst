.. _pp_cqm_presolve:

===============================
Preprocessing with CQM Presolve
===============================

This example uses explicit preprocessing to maximize performance when using
a Leap classical-quantum hybrid Constrained Quadratic Model (CQM) solver.

By default, Leap's CQM solver executes presolve algorithms in a preprocessing
stage of its problem solving. You can locally run the presolve algorithms provided
in Ocean prior to submitting your CQM to a solver, possibly reducing the size of
the submitted problem and improving its structure.

The purpose of this example is to show how to use Ocean's
:class:`~dwave.preprocessing.presolve.Presolver` class.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in :ref:`sapi_access`.
* Ocean tools :doc:`dimod </docs_dimod/sdk_index>` and :doc:`dwave-preprocessing </docs_preprocessing/sdk_index>`.

.. include:: hybrid_solver_service.rst
  :start-after: example-requirements-start-marker
  :end-before: example-requirements-end-marker

Solution Steps
==============

.. include:: hybrid_solver_service.rst
  :start-after: example-steps-start-marker
  :end-before: example-steps-end-marker

This example adds an optional step of preprocessing the submitted model.

Formulate the Problem
=====================

This example uses a simplified problem for illustrative purposes: a CQM with no
objective and just a single, one-variable constraint. This is sufficient to
show how to run :class:`~dwave.preprocessing.presolve.Presolver` methods.

The CQM created below has a constraint requiring that integer variable ``j``
not exceed 5.

.. testcode::

    import dimod

    j = dimod.Integer("j")
    cqm = dimod.ConstrainedQuadraticModel()
    cqm.set_objective(-j)
    cqm.add_constraint(j <= 5, "Maximum j")

Clearly, the global optimum for this CQM occurs for the default value of the lower
bound of ``j``.

>>> cqm.lower_bound("j")
0.0

Run Presolve
============

To run Ocean's presolve algorithms locally, instantiate a :class:`~dwave.preprocessing.presolve.Presolver`
on your CQM and apply a supported presolve (default is used here).

.. testcode::

    from dwave.preprocessing.presolve import Presolver

    presolve = Presolver(cqm)
    presolve.load_default_presolvers()
    presolve.apply()

You now have a preprocessed CQM you can submit to a CQM solver such as a Leap CQM solver.

>>> reduced_cqm = presolve.detach_model()
>>> print(reduced_cqm.constraints)
{}

The dimod :class:`~dimod.reference.samplers.ExactCQMSolver` test solver is
capable of solving this very simple CQM.

>>> sampleset = dimod.ExactCQMSolver().sample_cqm(reduced_cqm)
>>> print(sampleset.first)
Sample(sample={0: 0}, energy=0.0, num_occurrences=1, is_satisfied=array([], dtype=bool), is_feasible=True)

View the solution as assignments of the original CQM's variables: 

>>> presolve.restore_samples(sampleset.first.sample)
(array([[0.]]), Variables(['j']))
