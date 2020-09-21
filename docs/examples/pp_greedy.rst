.. _pp_greedy:

===================================
Postprocessing with a Greedy Solver
===================================

This example improves a :class:`~dimod.SampleSet` returned from a QPU
by postprocessing: it runs a steepest-descent solver initialized with 
the samples of the sampleset to find minima in the samples' neighbourhoods.

The purpose of this example is to illustrate the advantages of postprocessing
results of non-deterministic samplers such as quantum computers. Typically,
Ocean tools do some minimal postprocessing on those samples; for example, 
when you use 
`embedding tools <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/embedding.html>`_
a broken :term:`chain` may be resolved by majority vote of the states of all 
the qubits of the chain. You can often improve results, at a low cost of 
classical processing time, by such postprocessing.    

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in :ref:`sapi_access`.
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>`,  :doc:`dimod </docs_dimod/sdk_index>`, and
  :doc:`dwave-greedy </docs_greedy/sdk_index>`.

.. include:: hybrid_solver_service.rst
  :start-after: example-requirements-start-marker
  :end-before: example-requirements-end-marker

Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems 
on the quantum computer in two steps: (1) Formulate the problem as a 
:term:`binary quadratic model` (BQM) and (2) Solve the BQM with a D-wave 
system or classical :term:`sampler`. This example adds an optional step of 
postprocessing the returned solution.


Formulate the Problem
=====================

This example uses a synthetic problem for illustrative purposes: for all 
couplers of a QPU, it sets quadratic biases equal to random integers between 
-5 to +5.

.. testcode::

    # Create a native Ising problem
    from dwave.system import DWaveSampler
    import numpy as np
    
    sampler = DWaveSampler()
    h = {v: 0.0 for v in sampler.nodelist}
    J = {tuple(c): np.random.choice(list(range(-5, 6))) for c in sampler.edgelist}

Solve the Problem With/Without Postprocessing
=============================================

Because the problem sets values of the Ising problem based on the qubits 
and couplers of a selected QPU (a native problem), you can submit it directly 
to that QPU without :term:`embedding`. The sampleset returned from the QPU is 
used to initialize the steepest-descent algorithm of the 
:doc:`dwave-greedy </docs_greedy/sdk_index>` classical solver, which finds the 
closest minima for all returned samples.   

.. testcode::

    from greedy import SteepestDescentSolver

    solver_greedy = SteepestDescentSolver()

    sampleset_qpu = sampler.sample_ising(h, J, num_reads=100, answer_mode='raw')
    # Postprocess
    sampleset_pp = solver_greedy.sample_ising(h, J, initial_states=sampleset_qpu)

You can graphically compare the results with and without the postprocessing.

.. note:: The next code requires `Matplotlib <https://matplotlib.org>`_\ .

>>> import matplotlib.pyplot as plt    # doctest: +SKIP
...
>>> plt.plot(list(range(100)), sampleset_qpu.record.energy, 'b.-', 
...                            sampleset_pp.record.energy, 'r^-') # doctest: +SKIP
>>> plt.show()    # doctest: +SKIP

The image below shows the result of one particular execution on an Advantage QPU.

.. figure:: ../_images/postprocessing_greedy1.png
   :name: PostprocessingGreedy1
   :alt: image
   :align: center
   :scale: 70 %

   QPU samples before and after postprocessing with a steepest-descent solver.

For reference, this execution had the following median energies for the sampleset
before and after postprocessing, and for a running the classical solver directly on
the problem, in which case it uses random samples to initiate its local searches. 

.. testcode::

    sampleset_greedy = solver_greedy.sample_ising(h, J, num_reads=100)

>>> print("Energies: \n\t
...        SteepestDescentSolver: {}\n\t
...        QPU samples: {}\n\t
...        Postprocessed: {}".format(
...        np.median(sampleset_greedy.record.energy), 
...        np.median(sampleset_qpu.record.energy), 
...        np.median(sampleset_pp.record.energy)))       # doctest: +SKIP
Energies:
        SteepestDescentSolver: -39834.0
        QPU samples: -46387.0
        Postprocessed: -46415.0 

