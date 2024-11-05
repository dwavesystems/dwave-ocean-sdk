.. _opt_scaling:

======================
Scaling for Production
======================

This section provides guidance on coding your application for performance
on problems of the industrial scale supported by
`Leap's <https://cloud.dwavesys.com/leap>`_ quantum-classical hybrid solvers.

While the code examples below focus on
:ref:`constrained quadratic models (CQMs) <intro_cqm>`, most the guidance is also
applicable to :ref:`binary quadratic models (BQMs) <intro_qm_bqm>` and
:ref:`quadratic models (QMs) <intro_qm_qm>`.

This section does not discuss
`algorithmic complexity <https://en.wikipedia.org/wiki/Computational_complexity_theory>`_
or problem formulation.
For information about problem formulation, the
:doc:`sysdocs_gettingstarted:doc_getting_started` guide provides an introduction
and the :doc:`sysdocs_gettingstarted:doc_handbook` guide describes more advanced
techniques.

Simple Example Application
==========================

.. tip::

    .. dev note: in the future we should consider using nbsphinx or similar
        for this. But as of now (April 2022) nbsphinx is a bit immature for
        our needs. E.g. has non-pip-installable requirements, doesn't play
        nicely with intersphinx, etc.

    You can run the following code by downloading the `Jupyter <https://jupyter.org/>`_
    :download:`Notebook <scaling_for_production.ipynb>`.

The code below formulates a simple `bin packing <https://w.wiki/3jz4>`_ problem,
as explained in the Ocean SDK's :doc:`oceandocs:examples/hybrid_cqm_binpacking`
example.

For simplicity, assume that each bin has a capacity of `1` and start by
generating weights for the items you wish to pack. A packing problem with `n`
items results in a  CQM with :math:`n \times (n+1)` binary variables.

.. testcode::

    import numpy as np

    num_items = 100  # results in 10100 binary variables

    weights = np.random.default_rng(42).random(num_items)

Initial Code
============

The first implementation is written for readability and pedagogy.
As shown below, this comes at the cost of speed.

.. testcode::

    import typing

    import dimod


    def bin_packing(weights: typing.Sequence[float]) -> dimod.ConstrainedQuadraticModel:
        """Generate a bin packing problem as a constrained quadratic model."""

        n = len(weights)

        # y_j indicates that bin j is used
        y = [dimod.Binary(f'y_{j}') for j in range(n)]

        # x_i,j indicates that item i is put in bin j
        x = [[dimod.Binary(f'x_{i},{j}') for j in range(n)] for i in range(n)]

        cqm = dimod.ConstrainedQuadraticModel()

        # minimize the number of bins used
        cqm.set_objective(sum(y))

        # each item can go in only one bin
        for i in range(n):
            cqm.add_constraint(sum(x[i]) == 1, label=f'item_placing_{i}')

        # each bin has a capacity that must be respected
        for j in range(n):
            cqm.add_constraint(sum(weights[i] * x[i][j] for i in range(n)) - y[j] <= 0,
                               label=f'capacity_bin_{j}')

        return cqm

Time the construction:

.. testcode::
    :hide:

    bin_packing(weights)

.. code-block:: text

    In [1]: %timeit bin_packing(weights)
    385 ms ± 9.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

.. note::

    Because runtimes are highly system dependent, running the code on your system
    will likely result in different values. The results shown here are illustrative.

Use the quicksum Function
=========================

The easiest improvement you can make is to substitute :func:`~dimod.binary.quicksum`
for the Python :func:`sum`, which creates a large number of intermediate objects
not created by :func:`~dimod.binary.quicksum`.

.. testcode::

    import typing

    import dimod


    def bin_packing(weights: typing.Sequence[float]) -> dimod.ConstrainedQuadraticModel:
        """Generate a bin packing problem as a constrained quadratic model."""

        n = len(weights)

        # y_j indicates that bin j is used
        y = [dimod.Binary(f'y_{j}') for j in range(n)]

        # x_i,j indicates that item i is put in bin j
        x = [[dimod.Binary(f'x_{i},{j}') for j in range(n)] for i in range(n)]

        cqm = dimod.ConstrainedQuadraticModel()

        # minimize the number of bins used
        cqm.set_objective(dimod.quicksum(y))

        # each item can only go in one bin
        for i in range(n):
            cqm.add_constraint(dimod.quicksum(x[i]) == 1, label=f'item_placing_{i}')

        # each bin has a capacity that must be respected
        for j in range(n):
            cqm.add_constraint(dimod.quicksum(weights[i] * x[i][j] for i in range(n)) - y[j] <= 0,
                               label=f'capacity_bin_{j}')

        return cqm

This simple change already reduces the runtime.

.. testcode::
    :hide:

    bin_packing(weights)

.. code-block:: text

    In [1]: %timeit bin_packing(weights)
    294 ms ± 9.39 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Construct Models Directly
=========================

You can achieve an even bigger improvement by skipping symbolic construction
altogether, working directly with variable labels and a single BQM object.

The following small example demonstrates the performance difference. See
:ref:`Symbolic Math <intro_symbolic_math>` for a discussion of the difference
between variables and labels.

.. testcode::

    import dimod

    def make_bqm_symbolic(num_variables: int) -> dimod.BinaryQuadraticModel:
        return dimod.quicksum(2*dimod.Binary(v) for v in range(num_variables))

    def make_bqm_labels(num_variables: int) -> dimod.BinaryQuadraticModel:
        bqm = dimod.BinaryQuadraticModel('BINARY')
        bqm.add_linear_from((v, 2) for v in range(num_variables))
        return bqm

.. testcode::
    :hide:

    make_bqm_symbolic(1000)
    make_bqm_labels(1000)

.. code-block:: text

    In [1]: %timeit make_bqm_symbolic(1000)
    12.7 ms ± 213 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    In [2]: %timeit make_bqm_labels(1000)
    194 µs ± 2.32 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

Apply this same model construction to the binpacking example:

.. testcode::

    import typing

    import dimod


    def bin_packing(weights: typing.Sequence[float]) -> dimod.ConstrainedQuadraticModel:
        """Generate a bin packing problem as a constrained quadratic model."""

        n = len(weights)

        # y_j indicates that bin j is used
        y_labels = [f'y_{j}' for j in range(n)]

        # x_i,j indicates that item i is put in bin j
        x_labels = [[f'x_{i},{j}' for j in range(n)] for i in range(n)]

        cqm = dimod.ConstrainedQuadraticModel()

        # minimize the number of bins used
        objective = dimod.QuadraticModel()
        objective.add_linear_from(((v, 1) for v in y_labels), default_vartype='BINARY')
        cqm.set_objective(objective)

        # each item can only go in one bin
        for i in range(n):
            lhs = dimod.QuadraticModel()
            lhs.add_linear_from(((v, 1) for v in x_labels[i]), default_vartype='BINARY')
            cqm.add_constraint_from_model(lhs, rhs=1, sense='==', label=f'item_placing_{i}')

        # each bin has a capacity that must be respected
        for j in range(n):
            lhs = dimod.QuadraticModel()
            lhs.add_linear_from(((x_labels[i][j], weights[i]) for i in range(n)), default_vartype='BINARY')
            lhs.add_linear(y_labels[j], -1, default_vartype='BINARY')
            cqm.add_constraint_from_model(lhs, rhs=0, sense='<=', label=f'capacity_bin_{j}')

        return cqm

This change significantly reduces runtime.

.. testcode::
    :hide:

    bin_packing(weights)

.. code-block:: text

    In [1]: %timeit bin_packing(weights)
    95.5 ms ± 2.87 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

Add Constraints Without Copying
===============================

By default, the :meth:`~dimod.ConstrainedQuadraticModel.add_constraint` method
creates a copy of the objects you give it to avert mutation of objects that might
be used elsewhere in your code. If these objects are used solely for the
construction of constraints, as in this case, you can safely skip the copying.

.. testcode::

    import typing

    import dimod


    def bin_packing(weights: typing.Sequence[float]) -> dimod.ConstrainedQuadraticModel:
        """Generate a bin packing problem as a constrained quadratic model."""

        n = len(weights)

        # y_j indicates that bin j is used
        y_labels = [f'y_{j}' for j in range(n)]

        # x_i,j indicates that item i is put in bin j
        x_labels = [[f'x_{i},{j}' for j in range(n)] for i in range(n)]

        cqm = dimod.ConstrainedQuadraticModel()

        # we wish to minimize the number of bins used
        objective = dimod.QuadraticModel()
        objective.add_linear_from(((v, 1) for v in y_labels), default_vartype='BINARY')
        cqm.set_objective(objective)

        # each item can only go in one bin
        for i in range(n):
            lhs = dimod.QuadraticModel()
            lhs.add_linear_from(((v, 1) for v in x_labels[i]), default_vartype='BINARY')
            cqm.add_constraint_from_model(lhs, rhs=1, sense='==', label=f'item_placing_{i}', copy=False)

        # each bin has a capacity that must be respected
        for j in range(n):
            lhs = dimod.QuadraticModel()
            lhs.add_linear_from(((x_labels[i][j], weights[i]) for i in range(n)), default_vartype='BINARY')
            lhs.add_linear(y_labels[j], -1, default_vartype='BINARY')
            cqm.add_constraint_from_model(lhs, rhs=0, sense='<=', label=f'capacity_bin_{j}', copy=False)

        return cqm

This results in another performance improvement.

.. testcode::
    :hide:

    bin_packing(weights)

.. code-block:: text

    In [1]: %timeit bin_packing(weights)
    68.1 ms ± 299 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


