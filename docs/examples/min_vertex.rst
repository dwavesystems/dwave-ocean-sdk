.. _min_vertex:

============
Vertex Cover
============

This example solves a few small examples of a known graph problem, *minimum vertex cover*.
A `vertex cover <https://en.wikipedia.org/wiki/Vertex_cover>`_ is a set of vertices 
such that each edge of the graph is incident with at least one vertex in the set. 
A minimum vertex cover is the vertex cover of smallest size.

The purpose of this example is to help a new user to submit a problem to a
D-Wave system using Ocean tools with little configuration or coding.
Other examples demonstrate more advanced steps that might be needed for
complex problems.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in :ref:`dwavesys`.
* Ocean tools :std:doc:`dwave-system <system:index>`,  :std:doc:`dimod <dimod:index>`, and
  :std:doc:`dwave_networkx <networkx:index>`.

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
and ran :code:`dwave config create`, your installation should meet these requirements.


Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems on the quantum
computer in two steps: (1) Formulate the problem as a :term:`binary quadratic model` (BQM)
and (2) Solve the BQM with a D-wave system or classical :term:`sampler`. In this example, a
function in Ocean software handles both steps. Our task is mainly to select the sampler used
to solve the problem.

Formulate the Problem
=====================

The real-world application for this example might be a network provider's routers interconnected
by fiberoptic cables or traffic lights in a city's intersections. It is posed as a graph
problem; here, the five-node star graph shown below. Intuitively, the solution to this small
example is obvious --- the minimum set of vertices that touch all edges is node 0, but the general
problem of finding such a set is NP hard.

.. figure:: ../_static/minVertexS5.png
   :name: min_Vertex_S5
   :alt: image
   :align: center
   :scale: 70 %

   A five-node star graph.

First, we run the code snippet below to create a star graph where node 0 is hub to four other nodes.
The code uses `NetworkX <https://networkx.github.io/documentation/stable/index.html>`_\ , which is
part of your *dwave_networkx* or *dwave-ocean-sdk* installation.

>>> import networkx as nx
>>> s5 = nx.star_graph(4)

Solve the Problem by Sampling
=============================

For small numbers of variables, even your computer's CPU can solve minimum vertex covers
quickly. In this example, we demonstrate how to solve the problem both classically 
on your CPU and on the quantum computer.

Solving Classically on a CPU
----------------------------

Before using the D-Wave system, it can sometimes be helpful to test code locally.
Here we select one of Ocean software's test samplers to solve classically on a CPU.
Ocean's :std:doc:`dimod <dimod:index>` provides a sampler that
simply returns the BQM's value for every possible assignment of variable values.

>>> from dimod.reference.samplers import ExactSolver
>>> sampler = ExactSolver()

The next code lines use Ocean's :std:doc:`dwave_networkx <networkx:index>`
to produce a BQM for our :code:`s5` graph and solve it on our selected sampler. In other
examples the BQM is explicitly created but the Ocean tool used here abstracts the
BQM: given the problem graph it returns a solution to a BQM it creates internally.

>>> import dwave_networkx as dnx
>>> print(dnx.min_vertex_cover(s5, sampler))
[0]

Solving on a D-Wave System
--------------------------

We now use a sampler from Ocean software's
:std:doc:`dwave-system <system:index>` to solve on a
D-Wave system. In addition to *DWaveSampler()*, we use *EmbeddingComposite()*, which maps
unstructured problems to the graph structure of the selected sampler, a process known as
:term:`minor-embedding`: our problem star graph must be mapped to the QPU's numerically
indexed qubits.

.. note:: In the code below, replace sampler parameters in the third line. If
      you configured a default solver, as described in :ref:`dwavesys`, you
      should be able to set the sampler without parameters as
      :code:`sampler = EmbeddingComposite(DWaveSampler())`.
      You can see this information by running :code:`dwave config inspect` in your terminal.

>>> from dwave.system.samplers import DWaveSampler
>>> from dwave.system.composites import EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler(endpoint='https://URL_to_my_D-Wave_system/', token='ABC-123456789012345678901234567890', solver='My_D-Wave_Solver'))
>>> print(dnx.min_vertex_cover(s5, sampler))
[0]


Additional Problem Graphs
=========================

The figure below shows another five-node (wheel) graph.

.. figure:: ../_static/minVertexW5.png
   :name: min_Vertex_W5
   :alt: image
   :align: center
   :scale: 70 %

   A five-node wheel graph.

The code snippet below creates a new graph and solves on a
D-Wave system. 

>>> w5 = nx.wheel_graph(5)
>>> print(dnx.min_vertex_cover(w5, sampler))
[0, 1, 3]

Note that the solution found for this problem is not unique; for example,
[0, 2, 4] is also a valid solution.

>>> print(dnx.min_vertex_cover(w5, sampler))
[0, 2, 4]

The figure below shows a ten-node (circular-ladder) graph.

.. figure:: ../_static/minVertexC5.png
   :name: min_Vertex_C5
   :alt: image
   :align: center
   :scale: 70 %

   A ten-node circular-ladder graph.

The code snippet below replaces the problem graph and submits twice to the
D-Wave system for solution, producing two of the possible valid solutions.

>>> c5 = nx.circular_ladder_graph(5)
>>> print(dnx.min_vertex_cover(c5, sampler))
[0, 2, 3, 6, 8, 9]
>>> print(dnx.min_vertex_cover(c5, sampler))
[1, 3, 4, 5, 7, 9]


Summary
=======

In the terminology of :ref:`oceanstack`\ , Ocean tools moved the original problem through the
following layers:

* Application: an example application might be placing limited numbers of traffic-monitoring
  equipment on routers in a telecommunication network. Such problems can be posed as graphs.
* Method: graph mapping. Many different real-world problems can be formulated as instances
  of classified graph problems. Some of these are hard and the best currently known algorithms
  for solution may not scale well. Quantum computing might provide better solutions. In this example,
  vertex cover is a hard problem that can be solved on D-Wave systems.
* Sampler API: the Ocean tool internally builds a BQM with lowest values ("ground states") that
  correspond to a minimum vertex cover and uses our selected sampler to solve it.
* Sampler: classical *ExactSolver()* and then *DWaveSampler()*.
* Compute resource: first a local CPU then a D-Wave system.
