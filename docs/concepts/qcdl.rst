.. _concept_qcdl:

====
QCDL
====

Quantum circuit description language (QCDL) is an embedded
`Domain Specific Language  <https://en.wikipedia.org/wiki/Domain-specific_language>`_
(DSL) that uses Python as the host language, allowing you to interleave
classical Python preprocessing with quantum gate operations. Programs are
defined with the ``@qcdl`` decorator, which converts an ordinary Python function
into a QCDL program generator that accepts qubit arguments and returns a
dictionary suitable for submission to compiler or simulator services.

The following example creates a
`Bell state <https://en.wikipedia.org/wiki/Bell_state>`_ circuit, producing a
dictionary that can be passed to a compiler or simulator:

.. code-block:: python

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import cx, h, measure

    @qcdl(num_qubits=2)
    def main(q0, q1):
        h(q0)        # Hadamard gate on q0
        cx(q0, q1)   # CNOT with q0 as control, q1 as target
        measure(q0)
        measure(q1)

    qcdl_program = main()

For an introduction to QCDL, see :ref:`gate_workflow` section.