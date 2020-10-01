.. _dqm_sdk:

=========================
Discrete Quadratic Models 
=========================

The discrete quadratic model (DQM) is a polynomial over discrete variables with
terms all of degree two or less, represented by equation,

.. math::

    E(\bf{v})
    = \sum_{i=1} a_i v_i
    + \sum_{i<j} b_{i,j} v_i v_j 
    + c
    \qquad\qquad v_i \in\{A, B, C, ...\}

where :math:`\{A, B, C, ...\}` are some set of discrete values such 
``{red, green, blue, yellow}`` or ``{3.2, 67}``.  

The :class:`dimod.DiscreteQuadraticModel` class can contain this model and its 
methods provide convenient utilities for working with representations
of a problem.

These models and their use in solving problems on the D-Wave system are described
in the following documentation:

* Example :ref:`map_dqm`

   Shows an example of using `Leap <https://cloud.dwavesys.com/leap/>`_\ 's hybrid
   DQM solver, ``hybrid_binary_quadratic_model_version<x>``, to solve a map
   coloring problem.
* :class:`dimod.DiscreteQuadraticModel` class documentation

   Describes the DQM class and its methods.
* :class:`~dwave.system.samplers.LeapHybridDQMSampler` class documentation

   Describes Leap's DQM solver API.


