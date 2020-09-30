.. _map_dqm:

================================
Map Coloring: Hybrid DQM Sampler
================================

This example solves the same map coloring problem of :ref:`map_kerberos` to 
demonstrate the `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid discrete 
quadratic model (:term:`DQM`) solver, which enables you to solve problems 
of arbitrary structure and size for variables with discrete values.

See :ref:`map_kerberos` for an description of the map coloring 
:doc:`constraint satisfaction problem </concepts/csp>` (CSP). 

The :ref:`map_coloring` advanced example demonstrates lower-level coding of a similar
problem, which gives the user more control over the solution procedure but requires
the knowledge of some system parameters (e.g., knowing the maximum number of supported
variables for the problem). Example :ref:`hybrid1` demonstrates the hybrid approach to
problem solving in more detail by explicitly configuring the classical and quantum workflows.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in
  :ref:`sapi_access`
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>`, :doc:`dimod </docs_dimod/sdk_index>`.

.. include:: hybrid_solver_service.rst
  :start-after: example-requirements-start-marker
  :end-before: example-requirements-end-marker

Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems on the quantum
computer in two steps: (1) Formulate the problem as a :term:`binary quadratic model` (BQM)
and (2) Solve the BQM with a D-wave system or classical :term:`sampler`. In this example, a
DQM is created to formulate the problem and submitted to 
the `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid DQM solver, 
`hybrid_binary_quadratic_model_version<x>`.

Formulate the Problem
=====================

This example uses the `NetworkX <https://networkx.github.io/>`_ *read_adjlist* function
to read a text file, `usa.adj`, containing the states of the USA and their adjacencies (states
with a shared border) into a graph. The original map information
was found here on `write-only blog of Gregg Lind <https://writeonly.wordpress.com/2009/03/20/adjacency-list-of-states-of-the-united-states-us/>`_ and looks like this::

    # Author Gregg Lind
    # License:  Public Domain.    I would love to hear about any projects you use if it for though!
    #
    AK,HI
    AL,MS,TN,GA,FL
    AR,MO,TN,MS,LA,TX,OK
    AZ,CA,NV,UT,CO,NM
    CA,OR,NV,AZ
    CO,WY,NE,KS,OK,NM,AZ,UT

    # Snipped here for brevity

You can see in the first non-comment line that the state of Alaska ("AK") has Hawaii
("HI") as an adjacency and that Alabama ("AL") shares borders with four states.

>>> import networkx as nx
>>> G = nx.read_adjlist('usa.adj', delimiter = ',')   # doctest: +SKIP

Graph G now represents states as vertices and each state's neighbors as shared edges.

>>> states = G.nodes        # doctest: +SKIP
>>> borders = G.edges       # doctest: +SKIP

You can now create a :class:`dimod.DiscreteQuadraticModel` class to represent
the problem. The problem's variables are the states; any map can be colored with 
four colors, and these four colors are set as the *cases* of these variables.
By setting quadratic bias values of 1 between identical cases of variables that
share a border, and zeros otherwise, you increase the energy of the DQM for 
every two adjacent states with the same color (this is known as a 
:term:`penalty model`).   

>>> import dimod
...
>>> colors = [0, 1, 2, 3]
...
>>> dqm = dimod.DiscreteQuadraticModel()
>>> for state in states:            # doctest: +SKIP
...    _ = dqm.add_variable(4, label=state)      
>>> for s0, s1 in borders:          # doctest: +SKIP
...    dqm.set_quadratic(s0, s1, {(c, c): 1 for c in colors})

Solve the Problem by Sampling
=============================

D-Wave's quantum cloud service provides cloud-based hybrid solvers you can submit
arbitrary BQMs and DQMs to. These solvers, which implement state-of-the-art 
classical algorithms together with intelligent allocation of the quantum
processing unit (QPU) to parts of the problem where it benefits most, are designed 
to accommodate even very large problems. Leap's solvers can relieve you of the
burden of any current and future development and optimization of hybrid 
algorithms that best solve your problem.

Ocean software's :doc:`dwave-system </docs_system/sdk_index>`
:class:`~dwave.system.samplers.LeapHybridDQMSampler` class enables you to easily 
incorporate Leap's hybrid DQM solvers into your application.
The solution printed below has been snipped for brevity.

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()              # doctest: +SKIP
>>> sampleset = dqm_sampler.sample_dqm(dqm)       # doctest: +SKIP
...
>>> print(sampleset.first.energy, sampleset.first.sample)  # doctest: +SKIP
0.0 {'AK': 0, 'AL': 1, 'MS': 0, 'TN': 2, 'GA': 3, 'FL': 0, ...

.. note:: The next code requires `Matplotlib <https://matplotlib.org>`_\ .

Plot the best solution.

>>> import matplotlib.pyplot as plt       # doctest: +SKIP
>>> node_list = [list(G.nodes)[x:x+10] for x in range(0, 50, 10)]   # doctest: +SKIP
>>> node_list[4].append('ND')     # doctest: +SKIP                      
# Adjust the next line if using a different map
>>> nx.draw(G, pos=nx.shell_layout(G, nlist = node_list), with_labels=True, 
...         node_color=list(sampleset.first.sample.values()), node_size=400, 
...         cmap=plt.cm.rainbow)                 # doctest: +SKIP
>>> plt.show()    # doctest: +SKIP

The graphic below shows the result of one such run.

.. figure:: ../_images/usa_map_dqm.png
   :name: USA_MapColoring
   :alt: image
   :align: center
   :scale: 70 %

   One solution ``hybrid_binary_quadratic_model_version1`` found for the USA map-coloring problem.
