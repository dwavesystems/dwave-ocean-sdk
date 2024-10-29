.. _opt_model_construction_qm:

=====================================
Model Construction (Quadratic Models)
=====================================

dimod provides a variety of model generators. These are especially useful for testing
code and learning.

See examples of using QPU solvers and `Leap <https://cloud.dwavesys.com/leap>`_
hybrid solvers on these models in Ocean documentation's
:std:doc:`Getting Started examples <oceandocs:getting_started>` and the
`dwave-examples GitHub repository <https://github.com/dwave-examples>`_.

Typically you construct a model when reformulating your problem, using such
techniques as those presented in D-Wave's system documentation's
:std:doc:`sysdocs_gettingstarted:doc_handbook`.

CQM Example: Using a dimod Generator
------------------------------------

This example creates a CQM representing a
`knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ of ten
items.

>>> cqm = dimod.generators.random_knapsack(10)

CQM Example: Symbolic Formulation
---------------------------------

This example constructs a CQM from symbolic math, which is especially useful for
learning and testing with small CQMs.

>>> x = dimod.Binary('x')
>>> y = dimod.Integer('y')
>>> cqm = dimod.CQM()
>>> objective = cqm.set_objective(x+y)
>>> cqm.add_constraint(y <= 3) #doctest: +ELLIPSIS
'...'

For very large models, you might read the data from a file or construct from a NumPy
array.

BQM Example: Using a dimod Generator
------------------------------------

This example generates a BQM from a fully-connected graph (a clique) where all
linear biases are zero and quadratic values are uniformly selected -1 or +1 values.

>>> bqm = dimod.generators.random.ran_r(1, 7)

BQM Example: Python Formulation
-------------------------------

For learning and testing with small models, construction in Python is
convenient.

The `maximum cut <https://en.wikipedia.org/wiki/Maximum_cut>`_ problem is to find
a subset of a graph's vertices such that the number of edges between it and the
complementary subset is as large as possible.

.. figure:: ../_images/four_node_star_graph.png
    :align: center
    :scale: 40 %
    :name: four_node_star_graph
    :alt: Four-node star graph

    Star graph with four nodes.

The `dwave-examples Maximum Cut <https://github.com/dwave-examples/maximum-cut>`_
example demonstrates how such problems can be formulated as QUBOs:

.. math::

   Q = \begin{bmatrix} -3 & 2 & 2 & 2\\
                        0 & -1 & 0 & 0\\
                        0 & 0 & -1 & 0\\
                        0 & 0 & 0 & -1
       \end{bmatrix}

>>> qubo = {(0, 0): -3, (1, 1): -1, (0, 1): 2, (2, 2): -1,
...         (0, 2): 2, (3, 3): -1, (0, 3): 2}
>>> bqm = dimod.BQM.from_qubo(qubo)

BQM Example: Construction from NumPy Arrays
-------------------------------------------

For performance, especially with very large BQMs, you might read the data from a
file using methods, such as :func:`~dimod.binary.BinaryQuadraticModel.from_file`
or from NumPy arrays.

This example creates a BQM representing a long ferromagnetic loop with two opposite
non-zero biases.

>>> import numpy as np
>>> linear = np.zeros(1000)
>>> quadratic = (np.arange(0, 1000), np.arange(1, 1001), -np.ones(1000))
>>> bqm = dimod.BinaryQuadraticModel.from_numpy_vectors(linear, quadratic, 0, "SPIN")
>>> bqm.add_quadratic(0, 10, -1)
>>> bqm.set_linear(0, -1)
>>> bqm.set_linear(500, 1)
>>> bqm.num_variables
1001

QM Example: Interaction Between Integer Variables
-------------------------------------------------

This example constructs a QM with an interaction between two integer variables.

>>> qm = dimod.QuadraticModel()
>>> qm.add_variables_from('INTEGER', ['i', 'j'])
>>> qm.add_quadratic('i', 'j', 1.5)
