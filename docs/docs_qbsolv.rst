.. _qbsolv:

======
qbsolv
======

A decomposing solver that finds a minimum value of a large quadratic unconstrained binary optimization (QUBO) problem by splitting it into pieces. The pieces are solved using a classical solver running the tabu algorithm. qbsolv also enables configuring a D-Wave system as the solver.

.. qbsolv_deprecation-start-marker

.. attention::
   The qbsolv package is deprecated as of the end of 2021 and is planned for
   removal in an Ocean SDK release after March 2022.

   Please update your code to use :ref:`sdk_index_hybrid` or
   `Leap <https://cloud.dwavesys.com/leap/>`_ hybrid solvers instead.

.. qbsolv_deprecation-end-marker

For more information, see `qbsolv documentation <https://docs.ocean.dwavesys.com/projects/qbsolv>`_.
