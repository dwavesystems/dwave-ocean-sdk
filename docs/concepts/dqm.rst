.. _dqm_sdk:

=========================
Discrete Quadratic Models 
=========================

The discrete quadratic model (DQM) is a polynomial over discrete variables with
terms all of degree two or less.  Suppose that there are :math:`N` discrete
variables :math:`\bf{d}_i`, each with :math:`n_i` cases.  Conceptually, the
cases may represent any collection of discrete values, such as ``{red, green,
blue, yellow}`` or ``{3.2, 67}``.  Using a binary variable :math:`x_{i,u}` to
indicate whether discrete variable :math:`\bf{d}_i` is set to case :math:`u`,
the objective function can be expressed by the equation:

.. math::

    E(\bf{x})
    = \sum_{i=1}^N \sum_{u=1}^{n_i} a_{i,u} x_{i,u}
    + \sum_{i=1}^N \sum_{j=i+1}^N \sum_{u=1}^{n_i} \sum_{v=1}^{n_j} b_{i,j,u,v} x_{i,u} x_{j,v}
    + c

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


