.. _opt_index_intro:

=============================
Get Started with Optimization 
=============================

.. toctree::
    :maxdepth: 1

    opt_intro_hybrid
    opt_leap_hybrid
    opt_dwave_hybrid
    opt_app_dev_workflow
    opt_model_construction_qm
    opt_model_construction_nl
    opt_index_intro_examples
    
Example
=======

The following code creates a constrained quadratic model (CQM) representing
a `knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ and
solves it using a quantum-classical hybrid solver in the |cloud_tm|_ quantum 
cloud service. 

>>> from dimod.generators import random_knapsack 
>>> from dwave.system import LeapHybridCQMSampler
...
>>> cqm = random_knapsack(10)
>>> sampler = LeapHybridCQMSampler()
>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=180,
...                                label="SDK Examples - Bin Packing")  # doctest: +SKIP
