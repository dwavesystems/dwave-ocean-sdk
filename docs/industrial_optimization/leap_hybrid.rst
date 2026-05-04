.. _opt_leap_hybrid:

=======================
Using the Stride Solver
=======================

This section describes the |cloud|_ service's quantum-classical :term:`hybrid`
nonlinear :term:`solver <solver>`, also known as the |nlstride_tm| (e.g.,
``hybrid_nonlinear_program_version1``), and provides usage information.

.. note::
    Not all accounts have access to this type of solver.


When to Use this Solver
=======================

.. include:: ../shared/models.rst
    :start-after: start_models_nonlinear
    :end-before: end_models_nonlinear

The |nlstride_short| accepts arbitrarily structured problems formulated as
nonlinear models, with any constraints represented natively.

Solver Design Philosophy
------------------------

The :ref:`dwave-optimization <index_optimization>` package and
the |nlstride_short| incorporate features and design principles from each of the
following areas:

*   :ref:`Quantum optimization <optimization_philosophy_quantum_optimization>`
*   :ref:`(Mixed-integer) linear programming <optimization_philosophy_linear_programming>`
*   :ref:`Lists, sets, and other combinatorial variables <optimization_philosophy_combinatorial_variables>`
*   :ref:`Tensor programming <optimization_philosophy_tensor_programming>`

For a detailed description, see the :ref:`optimization_philosophy` section.


Modeling Problems
=================

The :ref:`opt_developing_quantum_applications` section describes the process
used by |dwave_short| and other companies to develop successful quantum
applications, which includes such steps as identifying problems that can benefit
from quantum technology, describing such problems in a way that enables
developers to model it, developing mathematical models, and implementing code.

The :ref:`opt_model_construction_nl` section explains the nonlinear model.

The :ref:`dwave-optimization <index_optimization>` package provides a class for
nonlinear models and model generators for common optimization problems. For
example, the capacitated vehicle routing problem,
`CVRP <https://en.wikipedia.org/wiki/Vehicle_routing_problem>`_, is to find the
shortest possible routes for a fleet of vehicles delivering to multiple customer
locations from a central depot. The model below finds delivery routes for two
vehicles delivering from a depot to nine sites with maximum vehicle capacity
200.

>>> from dwave.optimization.generators import capacitated_vehicle_routing
...
>>> demand = [0, 34, 12, 65, 10, 43, 27, 55, 61, 22]
>>> sites = [(15, 38), (23, -19), (44, 62), (3, 12), (-56, -21), (-53, 2),
...          (33, 63), (14, -33), (42, 41), (13, -62)]
>>> model = capacitated_vehicle_routing(
...     demand=demand,
...     number_of_vehicles=2,
...     vehicle_capacity=200,
...     locations_x=[x for x,y in sites],
...     locations_y=[y for x,y in sites])

For more details on this and other model generators, see the
:ref:`optimization_generators` section.


Submitting problems
===================

Ocean software's :ref:`dwave-system <index_system>` provides the
:class:`~dwave.system.samplers.LeapHybridNLSampler` class for submitting
nonlinear models to the |nlstride_short|.

>>> from dwave.system import LeapHybridNLSampler
>>> sampler = LeapHybridNLSampler()                  # doctest: +SKIP
>>> sampler.solver.name                              # doctest: +SKIP
hybrid_nonlinear_program_version1

Submit the CVRP model to the selected solver.

>>> results = sampler.sample(
...     model,
...     label='SDK Examples - CVRP')                # doctest: +SKIP

Timing & Charges
----------------

The :ref:`opt_leap_hybrid_timing` and :ref:`leap_hybrid_usage_charges`
sections provide information on how solver usage is charged to your account.

>>> results.result().info["timing"]["run_time"]     # doctest: +SKIP
5024685

Properties & Parameters
-----------------------

Real-world problems can be complex and models representing such problems can
quickly grow large. The :ref:`opt_solver_nl_properties` section provides
limitations on your model. For example, the state size of the decision variables
(:meth:`~dwave.optimization.model.Model.decision_state_size`) must not exceed
the maximum supported by the solver (:ref:`maximum_decision_state_size`):

>>> model.decision_state_size() < sampler.properties["maximum_decision_state_size"]   # doctest: +SKIP
True

The :ref:`opt_solver_nl_parameters` section describes the parameters you can
configure when submitting problems to the solver. For example, you might
experiment with various processing times:

>>> results = sampler.sample(
...     model,
...     time_limit=10,
...     label='SDK Examples - CVRP')  	# doctest: +SKIP


Getting Solutions
=================

The |nlstride_short| returns a nondeterministic number of solutions. Any
:term:`feasible states <feasible state>` returned are ordered by objective (from
low to high), and precede infeasible states. While the first sample is the best,
other feasible solutions may be useful.

Solutions are the assignment of values to the model's decision variables. You
access these by iterating through the model's decision variables for each state
you are interested in, typically filtered by feasibility.

Use the model's :meth:`~dwave.optimization.model.Model.iter_decisions` and
:meth:`~dwave.optimization.model.Model.iter_constraints` methods to do so. For
this example, there is a single decision variable (a
:class:`~dwave.optimization.symbols.DisjointLists`).

>>> routes = next(model.iter_decisions())

.. testcode::
    :hide:

    model.states.resize(1)
    routes.set_state(0, [[2., 7., 1., 5.], [4., 3., 8., 6., 0.]])

The best state (state zero) might look like this:

>>> print(f"Feasibility is {all(sym.state(0) for sym in model.iter_constraints())}")
Feasibility is True
>>> print((f"Objective value #0 is {model.objective.state(0).round(2)} for routes\n"
...        f"    {[r.state(0).tolist() for r in routes.iter_successors()]}"))
Objective value #0 is 423.8 for routes
    [[2.0, 7.0, 1.0, 5.0], [4.0, 3.0, 8.0, 6.0, 0.0]]

The :ref:`optimization_generators` section explains the returned solutions and
gives more details on accessing them.

You can iterate over all the states returned by the solver (the
:meth:`~dwave.optimization.states.States.size` method gives the number of
returned states). For some models it can be helpful to retrieve non-decision
variables that calculate useful information: use the
:meth:`~dwave.optimization.model.Model.iter_symbols` method to retrieve such
additional symbols.


Improving Solutions and Productizing
====================================

There can be a significant gap between solving an initial model for your
problem, perhaps simplified and reduced in scale, and an application in
production. The following resources can be useful:

*   The :ref:`opt_model_construction_nl_guidance` subsection of the
    :ref:`opt_model_construction_nl` section discusses guidelines improving
    models.
*   You might have a guess or non-optimal solution you can provide the solver as
    an :ref:`initial state <opt_model_construction_nl_states>` that may reduce
    solution time.
*   The :ref:`opt_index_improving_solutions` section discusses scaling and
    productizing applications.