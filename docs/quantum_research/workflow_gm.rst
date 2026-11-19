.. _qpu_workflow_gm:

=========================================
Basic Workflow: Writing & Submitting QCDL
=========================================

The two main steps of running quantum algorithms on **dual-rail** quantum
computers are:

1.  **Formulate your algorithm as a QCDL program**

    :term:`QCDL` is introduced in the :ref:`gate_workflow` section and described
    in detail in the :ref:`gate_api_ref` section.

2.  **Submit your QCDL program to a gate-model solver**

    You can then submit your QCDL program to a gate-model solver, for example a
    dual-rail simulator, as described in the :ref:`qcdl_using_simulator`
    section.

Example
=======

.. include:: ../shared/examples.rst
    :start-after: start_gm_sim1
    :end-before: end_gm_sim1