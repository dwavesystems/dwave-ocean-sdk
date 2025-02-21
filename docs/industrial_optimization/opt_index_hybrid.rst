.. _opt_index_hybrid:

========================
Sampling: Hybrid Solvers
========================

.. toctree::
    :hidden:
    :maxdepth: 1

    opt_leap_hybrid
    opt_dwave_hybrid

.. include:: ../shared/hybrid.rst
    :start-after: start_definition
    :end-before: end_definition

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`opt_leap_hybrid`
        :link: opt_leap_hybrid
        :link-type: ref

        Hybrid solvers hosted in the Leap service.

    .. grid-item-card:: :ref:`opt_dwave_hybrid`
        :link: opt_dwave_hybrid
        :link-type: ref

        Ocean\ |tm| software's general framework for building hybrid
        samplers.


.. todo:: move the following content lower

.. _leap_hybrid_solvers:

Leap's Hybrid Solvers
=====================

.. include:: ../shared/hybrid.rst
    :start-after: start_leap_intro
    :end-before: end_leap_intro

:ref:`hss` is an example of submitting a problem for solution on a Leap hybrid solver.


.. _dwave_hybrid_solvers:

dwave-hybrid Hybrid Solvers
===========================

.. include:: ../shared/hybrid.rst
    :start-after: start_dwave_hybrid_intro
    :end-before: end_dwave_hybrid_intro

:ref:`map_kerberos` and :ref:`hybrid1` are examples of solving problems using
*dwave-hybrid* samplers.
