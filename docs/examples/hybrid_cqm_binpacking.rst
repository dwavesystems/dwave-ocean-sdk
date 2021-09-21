.. _example_cqm_binpacking:

===========
Bin Packing
===========

This example solves the known hard problem of 
`bin packing <https://en.wikipedia.org/wiki/Bin_packing_problem>`_ to demonstrate
using Leap's hybrid :term:`CQM` solver on a constrained problem of arbitrary 
structure and size.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described
  in :ref:`sapi_access`.
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>` and 
  :doc:`dimod </docs_dimod/sdk_index>`.
* NumPy

.. example-requirements-start-marker

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
and ran :code:`dwave setup`, your installation should meet these requirements.
In D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ IDE, the default workspace
meets these requirements.

.. example-requirements-end-marker

Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems on the quantum
computer in two steps: (1) Formulate the problem as a :term:`quadratic model` (QM)
and (2) Solve the QM with a D-Wave solver.
This example formulates the bin-packing problem as a 
:ref:`constrained quadratic model <cqm_sdk>` and uses the 
:class:`~dwave.system.samplers.LeapHybridCQMSampler` to find good solutions.

Formulate the Problem
=====================

The bin-packing problem is to assign each item in a collection of items with 
differing weights to one of a number of bins with limited capacity in such
a way as to minimize the number of bins used. 

The code below sets the number of items, :code:`num_items`, their weights, 
:code:`weights`, randomly within a configurable range, :code:`item_weight_range`, 
and bin capacity, :code:`bin_capacity`. 

>>> import numpy as np
>>> num_items = 50
>>> item_weight_range = [3, 7]
>>> weights = list(np.random.randint(*item_weight_range, num_items))
>>> bin_capacity = int(10 * np.mean(weights))

Next, a CQM is instantiated. 

>>> from dimod import ConstrainedQuadraticModel, Binary
>>> cqm = ConstrainedQuadraticModel()

Objective Function
------------------

The objective function to minimize is the number of used bins. Because a bin 
is either used or not used, you can use binary variables to indicate whether 
or not a bin is used. Create enough of such variables: the worst possible 
case is that each item requires an entire bin to itself. The binary variable 
:code:`bin_used_<j>` indicates that bin :math:`j` is in use.

>>> bin_used = [Binary(f'bin_used_{j}') for j in range(num_items)]

To minimize the number of bins used is to minimize the value of 
:math:`\sum_j \text{bin_used}_j`.

>>> cqm.set_objective(sum(bin_used))

Constraints
-----------

Each item can only go in one bin. This again is a binary outcome: item :math:`i`
is either in bin :math:`j` (:code:`item_in_bin_<i>_<j> == 1`) or not 
(:code:`item_in_bin_<i>_<j> == 0`). You can express this constraint as 

.. math::

	\sum_j \text{item_in_bin}_{i,j} == 1; 

that is, over all bins :math:`j`, there is just one 
:code:`item_in_bin_<i>_<j> == 1` for each :math:`i`. 

>>> item_in_bin = [[Binary(f'item_in_bin_{i}_{j}') for j in range(num_items)]
...      for i in range(num_items)]
>>> for i in range(num_items):
...     one_bin_per_item = cqm.add_constraint(sum(item_in_bin[i]) == 1, label=f'item_placing_{i}')

Each bin has limited capacity. You can express this constraint for each bin 
:math:`j`: 

.. math::

	\sum_i \text{item_in_bin}_{i, j} * \text{weights}_i <= \text{bin_capacity} 

>>> for j in range(num_items):
...     bin_up_to_capacity = cqm.add_constraint(
...         sum(weights[i] * item_in_bin[i][j] for i in range(num_items)) - bin_used[j] * bin_capacity <= 0,
...         label=f'capacity_bin_{j}')

For 50 items and allowing for the worse case of 50 bins, this CQM requires
over 2000 binary variables: 

>>> len(cqm.variables)
2550

Given that bin capacity is defined above as ten times the average weight, 
one could easily reduce the complexity of this model by significantly reducing 
the number of bins. 

Solve the Problem by Sampling
=============================

D-Wave's quantum cloud service provides cloud-based hybrid solvers you can
submit arbitrary QMs to. These solvers, which implement state-of-the-art 
classical algorithms together with intelligent allocation of the quantum 
processing unit (QPU) to parts of the problem where it benefits most, are 
designed to accommodate even very large problems. Leap's solvers can 
relieve you of the burden of any current and future development and optimization
of hybrid algorithms that best solve your problem.

Ocean software's :doc:`dwave-system </docs_system/sdk_index>`
:class:`~dwave.system.samplers.LeapCQMHybridSampler` class enables you to 
easily incorporate Leap's hybrid CQM solvers into your application:

>>> from dwave.system import LeapHybridCQMSampler
>>> sampler = LeapHybridCQMSampler()     # doctest: +SKIP
>>> sampleset = sampler.sample_cqm(cqm, time_limit=300)  # doctest: +SKIP

For one particular execution, the CQM hybrid sampler returned 55 samples, out of 
which 49 were solutions that met all the constraints, including the best solution 
found: 

>>> print("{} feasible solutions of {}.".format(
...       sampleset.record.is_feasible.sum(), len(sampleset)))   # doctest: +SKIP
49 feasible solutions of 55.

The best solution found a packing that required 13 bins:

>>> best = next(itertools.filterfalse(lambda d: not getattr(d,'is_feasible'),
...             list(sampleset.data())))
>>> selected_bins = [key for key, val in best.sample.items() if 'bin_used' in key and val]
>>> print("{} bins are used.".format(len(selected_bins)))     # doctest: +SKIP
13 bins are used.

>>> def get_indices(name):
...     return [int(digs) for digs in name.split('_') if digs.isdigit()]

>>> for bin in selected_bins:                        # doctest: +SKIP
...     in_bin = [key for key, val in best.sample.items() if 
...        "item_in_bin" in key and 
...        get_indices(key)[1] == get_indices(bin)[0] 
...        and val]
...     b = get_indices(in_bin[0])[1]
...     w = [weights[get_indices(item)[0]] for item in in_bin]
...     print("Bin {} has weights {} for total {}".format(b, w, sum(w)))
Bin 15 has weights [5] for total 5
Bin 16 has weights [5, 6, 5, 6, 3] for total 25
Bin 17 has weights [6, 5] for total 11
Bin 25 has weights [4, 5, 4, 6] for total 19
Bin 29 has weights [4, 3, 6] for total 13
Bin 35 has weights [4, 4, 6, 3, 3, 3] for total 23
Bin 43 has weights [4, 5, 6] for total 15
Bin 47 has weights [4, 3, 3, 3] for total 13
Bin 49 has weights [3, 3, 5, 3, 4] for total 18
Bin 5 has weights [5, 4, 6, 6] for total 21
Bin 6 has weights [6, 3, 3, 5, 4, 3, 4, 5] for total 33
Bin 7 has weights [5, 6] for total 11
Bin 9 has weights [4, 4, 5] for total 13
