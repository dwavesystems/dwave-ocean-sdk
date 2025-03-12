.. start_requirements

The code in this example requires that your development environment have
:ref:`Ocean software <index_ocean_sdk>` and be configured to access SAPI, as
described in the :ref:`ocean_sapi_access_basic` section.

.. end_requirements


.. |workflow_section| replace:: The :ref:`qpu_workflow` section

.. start_standard_steps

|workflow_section| describes the problem-solving workflow as consisting of two
main steps: (1) Formulate the problem as an :term:`objective function` in a
:ref:`supported model <concept_models>` and (2) Solve your model with a
|dwave_short| :term:`solver`.

.. end_standard_steps


.. start_default_solver_config

.. note:: The following code sets a sampler without specifying :term:`SAPI`
    parameters. Configure a default :term:`solver`, as described in the
    :ref:`ocean_sapi_access_basic` section, to run the code as is, or see the
    :ref:`dwave-cloud-client <index_cloud>` tool on how to access a particular
    solver by setting explicit parameters in your code or environment variables.

.. end_default_solver_config


.. start_hybrid_advantage

The `Leap <https://cloud.dwavesys.com/leap/>`_ quantum cloud service provides
:ref:`hybrid solvers <opt_index_properties_parameters>` you can submit your
:ref:`models <concept_models>` to. These solvers, which implement
state-of-the-art classical algorithms together with intelligent allocation of
the quantum processing unit (:term:`QPU`) to parts of the problem where it
benefits most, are designed to accommodate even very large problems. The Leap
services'solvers can relieve you of the burden of any current and future
development and optimization of hybrid algorithms that best solve your problem.

.. end_hybrid_advantage


.. start_qpu1

The following code solves a random problem on a quantum computer.

>>> import dimod
>>> import dwave.system
...
>>> bqm = dimod.generators.ran_r(1, 20)
>>> sampler = dwave.system.EmbeddingComposite(dwave.system.DWaveSampler())
>>> sampleset = sampler.sample(bqm, num_reads=100)      # doctest: +SKIP

.. end_qpu1


.. start_qpu2

The following code solves the known "minimum vertex cover"
graph problem using an annealing quantum computer.

>>> import networkx as nx
>>> import dwave_networkx as dnx
>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> s5 = nx.star_graph(4)
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> min_cover = dnx.min_vertex_cover(s5, sampler)

.. end_qpu2


.. start_nl1

The following code solves an illustrative
`traveling-salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
using a quantum-classical hybrid solver in the Leap service.

>>> from dwave.optimization.generators import traveling_salesperson
>>> from dwave.system import LeapHybridNLSampler
...
>>> DISTANCE_MATRIX = [
...     [0, 656, 227, 578, 489],
...     [656, 0, 889, 141, 170],
...     [227, 889, 0, 773, 705],
...     [578, 141, 773, 0, 161],
...     [489, 170, 705, 161, 0]]
...
>>> model = traveling_salesperson(distance_matrix=DISTANCE_MATRIX)
>>> sampler = LeapHybridNLSampler()     # doctest: +SKIP
>>> results = sampler.sample(
...     model,
...     label='SDK Examples - TSP')  	# doctest: +SKIP

.. end_nl1


.. start_cqm1

The following code creates a constrained quadratic model (CQM) representing
a `knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ and
solves it using a quantum-classical hybrid solver in the Leap service.

>>> from dimod.generators import random_knapsack
>>> from dwave.system import LeapHybridCQMSampler
...
>>> cqm = random_knapsack(10)
>>> sampler = LeapHybridCQMSampler()        # doctest: +SKIP
>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=180,
...                                label="SDK Examples - Bin Packing")  # doctest: +SKIP

.. end_cqm1
