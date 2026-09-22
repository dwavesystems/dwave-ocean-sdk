.. _qpu_index_get_started_gm:

===========================
Get Started with Gate Model
===========================

.. toctree::
    :hidden:
    :maxdepth: 1

    gate_workflow

Learn to submit :term:`QCDL` gate-model algorithms to quantum processing units
(:term:`QPU`) in the |cloud| quantum cloud service.

.. grid:: 2 2 3 3
    :gutter: 2

    .. grid-item-card:: :ref:`gate_workflow`
        :link: gate_workflow
        :link-type: ref

        Introduction to quantum circuit description language (QCDL).

    .. grid-item-card:: :ref:`index_gate`
        :link: index_gate
        :link-type: ref

        QCDL reference guide.

Example
=======

The following example creates a Bell state circuit, producing a dictionary that
can be passed to a compiler or simulator:

>>> from dwave.gate.qcdl import qcdl
>>> from dwave.gate.qcdl.operations import cx, h, measure
...
>>> @qcdl(num_qubits=2)
... def main(q0, q1):
...     h(q0)        # Hadamard gate on q0
...     cx(q0, q1)   # CNOT with q0 as control, q1 as target
...     measure(q0)
...     measure(q1)
...
>>> qcdl_program = main()
