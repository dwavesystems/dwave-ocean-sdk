.. _dqm_sdk:

=========================
Discrete Quadratic Models 
=========================

The discrete quadratic model (DQM) is a polynomial over *discrete* variables, 
with all terms of degree two or less, where a discrete variable represents some 
collection of distinct values, such as ``{red, green, blue, yellow}`` or 
``{3.2, 67}``, which are called the variable's *cases*.  

A discrete quadratic model may be defined as

.. math::

    H(\bf{d}) = \sum_{i} a_i(\bf{d}_i) + \sum_{i,j} b_{i,j}(\bf{d}_i,\bf{d}_j) + c

where :math:`\bf{d}_i` are the discrete variables, :math:`a_i()` and :math:`b_{i,j}()` 
are real-valued functions, and :math:`c` is a constant (offset).

You can represent any DQM with an equivalent model over **binary** variables 
by replacing each discrete variable, :math:`\bf{d}_i`, with a vector of binary 
variables using `one-hot encoding <https://en.wikipedia.org/wiki/One-hot>`_, 
where exactly one binary variable is True and all others are False: 
:math:`\sum_a x_{i,a} = 1 \quad \forall i`. 

In particular, a discrete quadratic model for :math:`N` discrete variables, 
:math:`\bf{d}_i`, each with :math:`n_i` cases, is then defined by using a 
binary variable, :math:`x_{i,u}`, to indicate whether discrete variable 
:math:`\bf{d}_i` is set to case :math:`u`. The objective function can be 
expressed by the equation:

.. math::

    E(\bf{x})
    = \sum_{i=1}^N \sum_{u=1}^{n_i} a_{i,u} x_{i,u}
    + \sum_{i=1}^N \sum_{j=i+1}^N \sum_{u=1}^{n_i} \sum_{v=1}^{n_j} b_{i,j,u,v} x_{i,u} x_{j,v}
    + c

Both representations are equivalent over the *feasible space*; that is, the 
solutions that meet the one-hot-encoding constraints. The second representation
ascribes energies both to the feasible space (satisfying constraints), and an 
infeasible space (violating constraints). The second representation is used 
by Ocean tools.

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

