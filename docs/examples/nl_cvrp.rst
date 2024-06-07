.. _example_nl_cvrp:

===============
Vehicle Routing
===============

This example demonstrates the use of a `Leap <https://cloud.dwavesys.com/leap/>`_
hybrid :ref:`nonlinear-model <nl_model_sdk>` solver on the well-known 
capacitated vehicle routing problem, 
`CVRP <https://en.wikipedia.org/wiki/Vehicle_routing_problem>`_. 

The goal of this problem is to find the shortest possible routes for a 
fleet of vehicles delivering to multiple customer locations from a central 
depot. Vehicles have a specified delivery capacity, and on the routes to 
locations and then back to the depot, no vehicle is allowed to exceed its 
carrying capacity. 

Example Requirements
====================

.. include:: hybrid_solver_service.rst
	  :start-after: example-requirements-start-marker
	  :end-before: example-requirements-end-marker

Solution Steps
==============

.. include:: hybrid_solver_service.rst
  :start-after: example-steps-start-marker
  :end-before: example-steps-end-marker

This example formulates this problem as a :ref:`nonlinear model <nl_model_sdk>`
and uses the :class:`~dwave.system.samplers.LeapHybridNLSampler` to find good
solutions.

Formulate the Problem
=====================

First, define customer demand and locations. A standard format
for signaling the location of the depot, used by libraries such 
as `CVRPLIB http://vrp.atd-lab.inf.puc-rio.br/index.php/en/>`_, 
is to set the demand of the first location as zero.

>>> demand = [0, 34, 12, 65, 10, 43, 27, 55, 61, 22]
>>> sites = [(15, 38), (23, -19), (44, 62), (3, 12), (-56, -21), (-53, 2), 
...          (33, 63), (14, -33), (42, 41), (13, -62)]

Here there are ten locations, with the depot being located at coordinates
:math:`(15, 38)`.

This example uses one of Ocean software's model generators to instantiate a 
:class:`~dwave.optimization.model.Model` class for a traveling-salesperson problem. 
The :class:`~dwave.optimization.model.Model` class encodes all the information 
(:term:`objective function`, constraints, constants, and decision variables) 
relevant to your models. 

>>> from dwave.optimization.generators import capacitated_vehicle_routing
...
>>> sites_x = [x for x,y in sites]
>>> sites_y = [y for x,y in sites]
>>> model = capacitated_vehicle_routing(
...     demand=demand,
...     number_of_vehicles=2,
...     vehicle_capacity=200,
...     locations_x=sites_x,
...     locations_y=sites_y)

For detailed information on how the CVRP is modelled, 
see the documentation for the 
:class:`~dwave.optimization.generators.capacitated_vehicle_routing` 
generator. 

Solve the Problem by Sampling
=============================

D-Wave's quantum cloud service provides cloud-based
:std:doc:`hybrid solvers <sysdocs_gettingstarted:doc_leap_hybrid>` you can
submit quadratic and nonlinear models to. These solvers, which implement 
state-of-the-art classical algorithms together with intelligent allocation 
of the quantum processing unit (QPU) to parts of the problem where it benefits 
most, are designed to accommodate even very large problems. Leap's solvers can
relieve you of the burden of any current and future development and optimization
of hybrid algorithms that best solve your problem.

Ocean software's :doc:`dwave-system </docs_system/sdk_index>`
:class:`~dwave.system.samplers.LeapHybridNLSampler` class enables you to
easily incorporate Leap's hybrid nonlinear-model solvers into your application:

>>> from dwave.system import LeapHybridNLSampler
>>> sampler = LeapHybridNLSampler()                  # doctest: +SKIP

Submit the model to the selected solver. 

>>> results = sampler.sample(
...     model, 
...     time_limit=30)  	# doctest: +SKIP

You can check information such as timing in the returned results:

>>> print(results.result().timing['charge_time'])       # doctest: +SKIP
30000000

You can iterate through the returned samples.

>>> num_samples = model.states.size()
>>> route, = model.iter_decisions()                     # doctest: +SKIP
>>> vehicle1, vehicle2 = route.iter_successors()        # doctest: +SKIP
>>> for i in range(min(3, num_samples)):
...     print(f"Objective value {int(model.objective.state(i))} for \n" \
...     f"\t route 1: {vehicle1.state(i)} \t route 2: {vehicle1.state(i)}") # doctest: +SKIP
Objective value 484 for 
	 route 1: [4. 3. 7. 1. 5.] 	 route 2: [4. 3. 7. 1. 5.]
Objective value 423 for 
	 route 1: [0. 6. 8. 3. 4.] 	 route 2: [0. 6. 8. 3. 4.]
Objective value 423 for 
	 route 1: [2. 7. 1. 5.] 	 route 2: [2. 7. 1. 5.]

Providing an Initial State
--------------------------

For some problems you might have estimates or guesses of solutions, and 
by providing to the solver, as part of your problem submission, such 
assignments of decision variables as an initial state of the model, you may 
accelerate the solution.

Leap's hybrid nonlinear-model solver supports accepting an initial state
as part of the submitted model.


