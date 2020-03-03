.. _embedding_sdk:

===============
Minor-Embedding 
===============

To solve an arbitrarily posed binary quadratic problem directly on a D-Wave system requires mapping,
called *minor embedding*, to a Chimera graph that represents the system's quantum processing unit.
This preprocessing can be done by a composed sampler consisting of the
:class:`~dwave.system.samplers.DWaveSampler()` and a composite that performs minor-embedding.
(This step is handled automatically by :class:`~dwave.system.samplers.LeapHybridSampler()`
and :std:doc:`dwave-hybrid <hybrid:index>` reference samplers.)


