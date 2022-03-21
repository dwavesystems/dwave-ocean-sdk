.. _variables_sdk:

=========
Variables
=========

D-Wave's samplers mostly\ [#]_ solve quadratic models of various sorts. Quadratic
models are characterized by having one or two variables per term. A simple example
of a quadratic model is,

  .. math::

    D = Ax + By + Cxy

where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable
terms---:math:`Ax` and :math:`By` here---are *linear* with the constant biasing
the term's variable. Two-variable terms---:math:`Cxy` here---are *quadratic*
with a relationship between the variables.

The variables in these models may be of the following types:

* **Binary**: :math:`v_i \in\{-1,+1\} \text{  or } \{0,1\}`, represented by
  the dimod :class:`~dimod.Vartype` classes :class:`~dimod.Vartype.BINARY` and
  :class:`~dimod.Vartype.SPIN`.

  Typically used for applications that optimize over decisions that could either
  be true (or yes) or false (no)? For example,

  - Should the antenna transmit or no?
  - Did a network node experience failure?

* **Discrete**: for example a variable that can be assigned one of the values of the
  set ``{red, green, blue, yellow}``, represented by the dimod :class:`~dimod.Vartype`
  class :class:`~dimod.Vartype.INTEGER`.

  Typically used for applications that optimize over several distinct options?
  For example,

  - Which shift should employee X work?
  - Should the state be colored red, blue, green or yellow?

* **Integer**: represented by the dimod :class:`~dimod.Vartype` class
  :class:`~dimod.Vartype.INTEGER`.

  Typically used for applications that optimize the number of something? For
  example,

  - How many widgets should be loaded onto the truck?

* **Real**: represented by the dimod :class:`~dimod.Vartype` class
  :class:`~dimod.Vartype.REAL`.

  Typically used for applications that optimize over an uncountable set? For
  example,

  - Where should the sensor be built?

TODO: add symbolic and distinction between label and QM. 

D-Wave's quantum computers solve **binary** quadratic models;
`Leap <https://cloud.dwavesys.com/leap/>`_ `hybrid <hybrid_sdk>`_ solvers can
solver models with more varied variable types.

.. list-table:: Variable Types and Supported Models, Hybrid Samplers
   :header-rows: 1

   * - **Variables**
     - **Models**
     - **Hybrid Samplers**
     - **Examples**
   * - Binary
     - :class:`~dimod.BinaryQuadraticModel`
     - :class:`~dwave.system.samplers.LeapHybridSampler`
     - :ref:`hss`
   * - Binary, discrete
     - :class:`~dimod.DiscreteQuadraticModel`
     - :class:`~dwave.system.samplers.LeapHybridDQMSampler`
     - :ref:`map_dqm`
   * - Binary, integer
     - :class:`~dimod.QuadraticModel`, :class:`~dimod.ConstrainedQuadraticModel`
     - :class:`~dwave.system.samplers.LeapHybridCQMSampler`
     - :ref:`example_cqm_binpacking`, :ref:`example_cqm_stock_selling`
   * - Binary, integer, real
     - :class:`~dimod.ConstrainedQuadraticModel`
     - :class:`~dwave.system.samplers.LeapHybridCQMSampler`
     - :ref:`example_cqm_diet_reals`



.. [#] Ocean also provides some higher-order tools for developing and testing
  your code; for example, the :class:`~dimod.reference.samplers.ExactPolySolver`
  class.
