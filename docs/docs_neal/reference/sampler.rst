.. _sampler_neal:

===========================
Simulated Annealing Sampler
===========================

.. attention::

    ``dwave-neal`` is deprecated since ``dwave-ocean-sdk`` 6.1.0 in favor of
    :ref:`index_dwave_samplers` and will be removed in ``dwave-ocean-sdk`` 8.0.0.
    
    To migrate, use

    .. code-block:: python
   
        from dwave.samplers import SimulatedAnnealingSampler
   
    rather than

    .. code-block:: python
   
        from neal import SimulatedAnnealingSampler

.. automodule:: neal.sampler

Class
=====

.. autoclass:: SimulatedAnnealingSampler

Sampler Properties
==================

.. autosummary::
   :toctree: generated/

   ~SimulatedAnnealingSampler.properties
   ~SimulatedAnnealingSampler.parameters

Methods
=======

.. autosummary::
   :toctree: generated/

   ~SimulatedAnnealingSampler.sample
   ~SimulatedAnnealingSampler.sample_ising
   ~SimulatedAnnealingSampler.sample_qubo

Alias
=====

.. autoclass:: Neal
