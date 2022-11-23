.. _sdk_index_greedy:

============
dwave-greedy
============

.. attention::

    ``dwave-greedy`` is deprecated since ``dwave-ocean-sdk`` 5.4.0 in favor of
    :ref:`index_dwave_samplers` and will be removed in ``dwave-ocean-sdk`` 7.0.0.

An implementation of a steepest descent solver for binary quadratic models.

Steepest descent is the discrete analogue of gradient descent, but the best
move is computed using a local minimization rather rather than computing a
gradient. At each step, we determine the dimension along which to descend based
on the highest energy drop caused by a variable flip.

.. toctree::
   :caption: Code
   :maxdepth: 1

   reference/index
   Source <https://github.com/dwavesystems/dwave-greedy>
