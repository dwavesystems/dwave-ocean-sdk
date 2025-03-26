.. _opt_example_cqm_binpacking:

=======================
Bin Packing: Binary CQM
=======================

This example solves the known hard problem of
`bin packing <https://en.wikipedia.org/wiki/Bin_packing_problem>`_ to
demonstrate using a `Leap <https://cloud.dwavesys.com/leap/>`_ :term:`hybrid`
:term:`CQM` solver on a :term:`constrained <constraint>` problem with binary
variables.

The bin-packing problem is to pack into a number of bins of limited capacity,
:math:`c`, a collection of items. Each item, :math:`i`, with weight,
:math:`w_i`, should be assigned to bin, :math:`b_j`, in such a way as to
minimize the number of bins used.

Example Requirements
====================

.. include:: ../shared/examples.rst
    :start-after: start_requirements
    :end-before: end_requirements

Solution Steps
==============

.. |workflow_section| replace:: :ref:`opt_workflow`

.. include:: ../shared/examples.rst
    :start-after: start_standard_steps
    :end-before: end_standard_steps

This example formulates the bin-packing problem as a
:ref:`constrained quadratic model <concept_models_cqm>` and uses the
:class:`~dwave.system.samplers.LeapHybridCQMSampler` class to find good
solutions.

Formulate the Problem
=====================

First, set up the problem parameters.

*   :code:`num_items` is the number of items.
*   :code:`weights` assigns weights, :math:`w_i`, to each item, `i`, randomly
    within a configurable range, :code:`item_weight_range`.
*   :code:`bin_capacity` is the bin capacity, :math:`c`, set based on the
    average weight.

>>> import numpy as np
>>> num_items = 15
>>> item_weight_range = [3, 7]
>>> weights = list(np.random.randint(*item_weight_range, num_items))
>>> bin_capacity = int(10 * np.mean(weights))
>>> print("Problem: pack a total weight of {} into bins of capacity {}.".format(
...       sum(weights), bin_capacity))              # doctest: +SKIP
Problem: pack a total weight of 77 into bins of capacity 51.

Instantiate a CQM.

>>> from dimod import ConstrainedQuadraticModel
>>> cqm = ConstrainedQuadraticModel()

You can now formulate an :term:`objective function` to optimize and constraints
any feasible solution must meet, and set these in your CQM.

Objective Function
------------------

The objective function to minimize is the number of used bins. Because a bin
is either used or not, you can indicate bin usage with binary variables.

Binary variable\ [#]_ :code:`bin_used_<j>` indicates that bin :math:`b_j` is in
use. The worst possible case is that each item requires an entire bin to itself,
so the maximum number of bins (and the number of binary variables
:code:`bin_used_<j>` to instantiate) is equal to the number of items,
:code:`num_items`.

>>> from dimod import Binary
>>> bin_used = [Binary(f'bin_used_{j}') for j in range(num_items)]

To minimize the number of used bins is to minimize the sum of
:code:`bin_used_<j>` variables with value 1 (True, meaning the bin is being
used):

.. math::

    \min (\sum_j b_j)

>>> cqm.set_objective(sum(bin_used))

.. [#]

    Always keep in mind that such "variables" are actually
    class :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`
    objects,

    >>> bin_used[0]
    BinaryQuadraticModel({'bin_used_0': 1.0}, {}, 0.0, 'BINARY')

    with a single variable with the requested label, :code:`bin_used_<j>`. This
    means, for example, that multiplying by two doubles the linear bias,

    >>> 2*bin_used[0]
    BinaryQuadraticModel({'bin_used_0': 2.0}, {}, 0.0, 'BINARY')

    multiplying two such "variables" creates a quadratic bias,

    >>> bin_used[0]*bin_used[1]          # doctest: +SKIP
    BinaryQuadraticModel({'bin_used_0': 0.0, 'bin_used_1': 0.0},
    ...                  {('bin_used_1', 'bin_used_0'): 1.0}, 0.0, 'BINARY')

    but multiplying three binary quadratic models requires a non-quadratic term
    and so :code:`bin_used[0]*bin_used[1]*bin_used[2]` cannot generate a binary
    quadratic model and results in an error.

Constraints
-----------

The bin-packing problem has two constraints:

1.  Each item can go into only one bin. This again is a binary outcome: item
    :math:`i` is either in bin :math:`b_j` or not. You can express this
    constraint, using binary variables, :math:`x_{i,j}`, as

    .. math::

        \sum_j x_{i,j} == 1.

    That is, over all :math:`j` bins, there is just one :math:`x_{i,j}` with
    value True (or :code:`item_<i>_in_bin_<j> == 1` in the code below) for each
    :math:`i`.

>>> item_in_bin = [[Binary(f'item_{i}_in_bin_{j}') for j in range(num_items)]
...      for i in range(num_items)]
>>> for i in range(num_items):
...     one_bin_per_item = cqm.add_constraint(sum(item_in_bin[i]) == 1, label=f'item_placing_{i}')

2.  Each bin has limited capacity. You can express this constraint for each bin,
    :math:`b_j`, by summing over :math:`i` per value of :math:`j`:

    .. math::

        \sum_i x_{i, j} * w_i <= c

    That is, for each bin :math:`b_j`, the sum of weights for those items placed
    in the bin (:code:`item_<i>_in_bin_<j> == 1`) does not exceed capacity.

>>> for j in range(num_items):
...     bin_up_to_capacity = cqm.add_constraint(
...         sum(weights[i] * item_in_bin[i][j] for i in range(num_items)) - bin_used[j] * bin_capacity <= 0,
...         label=f'capacity_bin_{j}')

For 15 items and allowing for the worst case of 15 bins, this CQM requires over
200 binary variables:

>>> len(cqm.variables)
240

Given that bin capacity is defined above as ten times the average weight, one
could easily reduce the complexity of this model by setting the number of bins
much smaller.

Solve the Problem by Sampling
=============================

.. include:: ../shared/examples.rst
    :start-after: start_hybrid_advantage
    :end-before: end_hybrid_advantage

Ocean software's :ref:`dwave-system <index_system>`
:class:`~dwave.system.samplers.LeapHybridCQMSampler` class enables you to easily
incorporate Leap's hybrid CQM solvers into your application:

>>> from dwave.system import LeapHybridCQMSampler
>>> sampler = LeapHybridCQMSampler()     # doctest: +SKIP

Submit the CQM to the selected solver. For one particular execution, with a
maximum allowed runtime of 3 minutes, the CQM hybrid sampler returned 47
samples, out of which 31 were solutions that met all the constraints:

>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=180,
...                                label="SDK Examples - Bin Packing")  # doctest: +SKIP
>>> feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  # doctest: +SKIP
>>> if len(feasible_sampleset):      # doctest: +SKIP
...    best = feasible_sampleset.first
...    print("{} feasible solutions of {}.".format(
...       len(feasible_sampleset), len(sampleset)))
31 feasible solutions of 47.

The best solution found a packing that required 2 bins:

>>> selected_bins = [key for key, val in best.sample.items() if 'bin_used' in key and val]   # doctest: +SKIP
>>> print("{} bins are used.".format(len(selected_bins)))     # doctest: +SKIP
2 bins are used.

The code below defines a simple function, :code:`get_indices`, that returns the
indices signifying the bin and item from variable names. This is used below in
parsing the solutions returned from the hybrid solver.

>>> def get_indices(name):
...     return [int(digs) for digs in name.split('_') if digs.isdigit()]

For the best feasible solution, print the packing.

>>> for bin in selected_bins:                        # doctest: +SKIP
...     in_bin = [key for key, val in best.sample.items() if
...        "_in_bin" in key and
...        get_indices(key)[1] == get_indices(bin)[0]
...        and val]
...     b = get_indices(in_bin[0])[1]
...     w = [weights[get_indices(item)[0]] for item in in_bin]
...     print("Bin {} has weights {} for a total of {}.".format(b, w, sum(w)))
Bin 1 has weights [4, 4, 6, 4, 6, 4, 6] for a total of 34.
Bin 14 has weights [5, 6, 4, 6, 4, 6, 6, 6] for a total of 43.

The items were distributed in a way that kept each bin below its capacity.
