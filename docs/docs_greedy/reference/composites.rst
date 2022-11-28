.. _included_composites:

.. attention::

    ``dwave-greedy`` is deprecated since ``dwave-ocean-sdk`` 6.1.0 in favor of
    :ref:`index_dwave_samplers` and will be removed in ``dwave-ocean-sdk`` 8.0.0.

==========
Composites
==========

The `dwave-greedy` package currently includes just one composite,
:class:`~greedy.composite.SteepestDescentComposite`.

.. currentmodule:: greedy.composite


SteepestDescentComposite
========================

Class
-----

.. autoclass:: SteepestDescentComposite

Attributes
----------

.. autosummary::
   :toctree: generated/

   SteepestDescentComposite.properties
   SteepestDescentComposite.parameters

Methods
-------

.. autosummary::
   :toctree: generated/

   SteepestDescentComposite.sample
   SteepestDescentComposite.sample_ising
   SteepestDescentComposite.sample_qubo
