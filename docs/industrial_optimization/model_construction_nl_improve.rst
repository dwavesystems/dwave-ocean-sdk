.. _opt_model_construction_nl_improve:

======================
Building Better Models
======================

The :ref:`opt_model_construction_nl` section explained the basics of using the
:ref:`dwave-optimization <index_optimization>` package to create nonlinear
models for the |nlstride_tm|. This section provides guidance for improving your
models for performance.

Selecting Decision variables
============================

To assist in selecting the implicitly constrained symbol most appropriate for a
given problem, the table below compares the key characteristics and typical
applications of each.

.. list-table:: Comparative Summary of Implicitly Constrained Symbols
    :widths: 15 20 20 22 22
    :header-rows: 1

    *   - **Feature**
        - ``list(N)``
        - ``set(N)``
        - ``disjoint_lists(...)``
        - ``disjoint_bit_sets(...)``
    *   - **Primary Purpose**
        - Ordered permutation of ``range(N)``
        - Unordered subset of ``range(N)``
        - Disjoint ordered partitions of ``range(primary_set_size)``
        - Disjoint unordered partitions of ``range(primary_set_size)``
    *   - **Order Within Group/List**
        - Yes
        - No
        - Yes (within each list)
        - No (within each set)
    *   - **Item Uniqueness**
        - All ``N`` items appear exactly once in the list
        - Unique subset from universe
        - Each item appears in at most one list; lists are permutations
        - Each item appears in at most one set; sets contain unique items
    *   - **Number of Collections**
        - 1 list
        - 1 set
        - ``num_disjoint_lists``
        - ``num_disjoint_sets``
    *   - **Creation Returns**
        - Single decision variable
        - Single decision variable
        - Main variable + collection of lists
        - Main variable + collection of sets
    *   - **Typical Problem Type**
        - TSP, QAP, sequencing
        - Knapsack, feature selection
        - CVRP, task assignment, multi-machine scheduling
        - Bin packing, clustering, set partitioning
    *   - **Input Parameters**
        - ``N``
        - ``N``
        - ``primary_set_size``, ``num_disjoint_lists``
        - ``primary_set_size``, ``num_disjoint_sets``

.. _opt_model_construction_nl_guidance:

Improving Your Models
=====================

As much as possible, design models along these lines:

1.  Use compact matrix operations in your formulations.

    The `dwave-optimization` package enables you to formulate models using
    linear-algebra conventions similar to `NumPy <https://numpy.org/>`_. Compact
    matrix formulation are usually more efficient and should be preferred.

2.  Exploit the implicit constraints of symbols such as
    :class:`~dwave.optimization.symbols.ListVariable`,
    :class:`~dwave.optimization.symbols.SetVariable`,
    :class:`~dwave.optimization.symbols.DisjointLists`,
    and :class:`~dwave.optimization.symbols.DisjointBitSets`.

    Typically, solver performance strongly depends on the size of the solution
    space for your modelled problem: models with smaller spaces of feasible
    solutions tend to perform better than ones with larger spaces. A powerful
    way to reduce the feasible-solutions space is by using variables that act
    as implicit constraints. This is analogous to judicious typing of a variable
    to meet but not exceed its required assignments: a Boolean variable, ``x``,
    has a solution space of size 2 (:math:`\{True, False\}`) while a
    finite-precision integer variable, ``i``, might have a solution space of
    several billion values.

See the formulations used by the package's
:ref:`model generators <optimization_generators>` and relevant
`GitHub examples <https://github.com/dwave-examples>`_ for reference.

Example: Compact Matrix Formulation
-----------------------------------

Like a large class of real-world problems, optimally loading a truck to convey
the most valuable merchandise while not exceeding limitations on carrying weight
or allowable volume, can be considered a variation on the well-known
`knapsack optimization problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_.
The problem is to maximize the total value of items packed in a knapsack without
exceeding its capacity.

Such real-world problems, when formulated mathematically for automated solution,
typically include a data-transformation step that provides the weights and
values of the problem's items in some structure. Here, an illustrative problem
of just four items is modeled, with weights and values :math:`30, 10, 40, 20`
and :math:`10, 20, 30, 40`, respectively, and a maximum capacity of :math:`30`
for the truck.

For a practical formulation of the knapsack problem, see the code in the
:class:`~dwave.optimization.generators.knapsack` generator.

This example compares two formulations of a small truck-loading problem: an
intuitive model that represents multiple binary decisions with multiple binary
symbols etc. versus a more compact model. The figure below compares the directed
acyclic graphs for these two formulations.


.. figure:: ../_images/knapsack_simple_matrix.png
    :name: knapsackSimpleMatrix
    :alt: Illustrative directed acyclic graph of two models. The left graph has
        ten nodes while the right one has thirty nodes.
    :align: center
    :scale: 80%

    Comparison between models using compact matrix operations (left) and
    less-compact operations (right) in formulation. The less-compact formulation
    has triple the number of symbols. Graphs are created using the package's
    :meth:`~dwave.optimization.model.Model.to_networkx` method.

The two tabs below provide the two formulations.

.. tab-set::

    .. tab-item:: Compact Formulation

        The model in this tab is formulated using compact matrix operations.

        Instantiate a nonlinear model and add the constant symbols.

        >>> model = Model()
        >>> weight = model.constant([30, 10, 40, 20])
        >>> value = model.constant([15, 25, 35, 45])
        >>> capacity = model.constant(30)

        Add a binary-array variable for the items: which items should be
        selected for loading into the truck.

        >>> items = model.binary(4)

        Add a constraint that the total weight must not exceed the truck's
        capacity.

        >>> total_weight = items * weight
        >>> model.add_constraint(total_weight.sum() <= capacity) # doctest: +ELLIPSIS
        <dwave.optimization.symbols.binaryop.LessEqual at ...>

        Add the objective (transport as much valuable merchandise as possible):

        >>> total_value = items * value
        >>> model.minimize(-total_value.sum())

        The size of this model is a third of the alternative formulation
        shown in the second tab:

        >>> model.num_nodes()
        10

    .. tab-item:: Non-compact Formulation

        The model in this tab is formulated using one binary decision variable
        per item. Each variable and constant adds a node to the directed
        acyclic graph.

        Instantiate a nonlinear model and add the constant symbols. The weight
        and value of each item is represented by a symbol.

        >>> model = Model()
        >>> weight0 = model.constant(30)
        >>> weight1 = model.constant(10)
        >>> weight2 = model.constant(40)
        >>> weight3 = model.constant(20)
        >>> val0 = model.constant(15)
        >>> val1 = model.constant(25)
        >>> val2 = model.constant(35)
        >>> val3 = model.constant(45)
        >>> capacity = model.constant(30)

        Add a binary variable for each item: should that item be loaded into the
        truck (yes or no?).

        >>> item0 = model.binary()
        >>> item1 = model.binary()
        >>> item2 = model.binary()
        >>> item3 = model.binary()

        Add the constraint on the total weight:

        >>> total_weight = item0*weight0 + item1*weight1 + item2*weight2 + item3*weight3
        >>> model.add_constraint(total_weight <= capacity) # doctest: +ELLIPSIS
        <dwave.optimization.symbols.binaryop.LessEqual at ...>

        Add the objective to maximize the transported value:

        >>> total_value = item0*val0 + item1*val1 + item2*val2 + item3*val3
        >>> model.minimize(-total_value)

        The size of this model is triple the alternative formulation
        shown in the first tab:

        >>> model.num_nodes()
        28

Compare the two formulations. Prefer compact-matrix formulations for your
models. 

Example: Implicitly Constrained Symbols
---------------------------------------

Consider a problem of selecting a route for several destinations with the cost
increasing on each leg of the itinerary; for the example formulated below, one
can travel through four destinations in any order, one destination per day, with
the transportation cost per unit of travel doubling every subsequent day.

The figure below shows four destinations as dots labeled ``0`` to
``3``, and plots the least costly (green) and most costly (red) routes.

.. figure:: ../_images/best_worst_routes.png
    :name: bestWorstRoutes
    :alt: Plot of two routes between four points, the green one, (3, 2, 1, 0) is
          the least costly while the red one, (2, 1, 3, 0), is the most costly.
    :align: center
    :scale: 80%

    Finding the optimal route between destinations.

The code snippet below defines the cost per leg and the distances between the
four destinations, with values chosen for simple illustration.

>>> import numpy as np
...
>>> cost_per_day = [1, 2, 4]
>>> distance_matrix = np.asarray([
...     [0, 1, np.sqrt(10), np.sqrt(34)],
...     [1, 0, 3, np.sqrt(25)],
...     [np.sqrt(10), 3, 0, 4],
...     [np.sqrt(34), np.sqrt(25), 4, 0]])

This section compares two formulations of this small routing problem: an
intuitive model that uses the generic
:class:`~dwave.optimization.symbols.BinaryVariable` symbol to represent decisions
on ordering the destinations versus a model that uses the implicitly constrained
:class:`~dwave.optimization.symbols.ListVariable` symbol, where the order of
destinations is a permutation of values. The figure below compares the directed
acyclic graphs for these two formulations.


.. figure:: ../_images/route_models.png
    :name: RouteModels
    :alt: Illustrative directed acyclic graph of two models. The left graph has
        far fewer nodes than that one the right.
    :align: center
    :scale: 100%

    Comparison between models using implicitly-constrained decision symbol
    (left) and explicit constrains on a simple binary symbol (right) in
    formulation. The first formulation has fewer symbols.

It is expected that the more compact model that uses implicit constraints will
perform better. 

The two tabs below provide the two formulations.

.. tab-set::

    .. tab-item:: Implicit Constraints

        The model in this tab is formulated using the implicitly
        constrained :class:`~dwave.optimization.symbols.List` symbol.

        >>> model = Model()
        >>> # Add the constants
        >>> cost = model.constant(cost_per_day)
        >>> distances = model.constant(distance_matrix)
        >>> # Add the decision symbol
        >>> route = model.list(4)
        >>> # Optimize the objective
        >>> model.minimize((cost * distances[route[:-1],route[1:]]).sum())

        You can see the objective values for the least and most costly routes
        as permutations of the :math:`[0, 1, 2, 3]` list as follows:

        >>> with model.lock():
        ...     model.states.resize(2)
        ...     route.set_state(0, [3, 2, 1, 0])
        ...     route.set_state(1, [2, 1, 3, 0])
        ...     print(int(model.objective.state(0)), int(model.objective.state(1)))
        14 36

    .. tab-item:: Explicit Constraints

        The model in this tab is formulated using explicit constraints on the
        generic :class:`~dwave.optimization.symbols.BinaryVariable` symbol.

        >>> from dwave.optimization.mathematical import add
        ...
        >>> model = Model()
        >>> # Add the problem constants
        >>> cost = model.constant(cost_per_day)
        >>> distances = model.constant(distance_matrix)

        Define constants that are used to formulate the explicit constraints.

        >>> one = model.constant(1)
        >>> indx_int = model.constant([0, 1, 2, 3])

        Add the decision symbol: for each of the itinerary's four legs, each
        of the four destinations is represented by a binary variable. If leg
        1 should be to destination 2, for example, the value of row 1 is
        :math:`False, False, True, False`. This is a representation known as
        `one-hot encoding <https://en.wikipedia.org/wiki/One-hot>`_.

        >>> itinerary_loc = model.binary((4, 4))

        Add the objective. Here, the :code:`indx_int` constant converts the
        binary one-hot variables to an index of the distance matrix.

        >>> model.minimize(add(*(
        ...     (itinerary_loc[u, pos] * itinerary_loc[v, (pos + 1) % 4] * distances[u, v] +
        ...     itinerary_loc[v, pos] * itinerary_loc[u, (pos + 1) % 4] * distances[v, u]) *
        ...     cost[pos]
        ...     for u in range(4)
        ...     for v in range(u+1, 4)
        ...     for pos in range(3)
        ... )))

        Add explicit one-hot constraints: summing the columns of the decision
        variable must give ones because each destination is visited once;
        summing rows must give ones because each leg visits one destination.

        >>> for i in range(distances.shape()[0]):
        ...     model.add_constraint(itinerary_loc[i, :].sum() <= one)
        ...     model.add_constraint(one <= itinerary_loc[i,:].sum())
        ...     model.add_constraint(itinerary_loc[:, i].sum() <= one)
        ...     model.add_constraint(one <= itinerary_loc[:, i].sum()) # doctest: +ELLIPSIS
        <dwave.optimization.symbols.binaryop.LessEqual at ...>
        ...

        You can see the objective cost for the least costly route
        as follows:

        >>> with model.lock():
        ...     model.states.resize(2)
        ...     itinerary_loc.set_state(0, [
        ...         [0, 0, 0, 1],
        ...         [0, 0, 1, 0],
        ...         [0, 1, 0, 0],
        ...         [1, 0, 0, 0]])
        ...     print(int(model.objective.state(0)))
        14

The directed acyclic graph for the implicitly constrained model has few nodes
and the model is more efficient.
