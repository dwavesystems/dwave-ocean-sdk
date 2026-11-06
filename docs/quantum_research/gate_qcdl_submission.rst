.. _qcdl_using_simulator:

==============================
Using the Gate-Model Simulator
==============================

The |cloud|_ quantum cloud service provides access to a simulator that enables
you to test gate-model circuits intended to be executed on a dual-rail quantum
processing unit (QPU). You describe your circuits using the :ref:`index_gate`
package's quantum circuit description language (QCDL), introduced in the
:ref:`gate_workflow` section and described in detail in the :ref:`gate_api_ref`
section.

.. _QuantumCircuit: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit


.. _qcdl_simulator:

About the Simulator
===================

the |cloud|_ service provides a Monte Carlo simulator of QCDL programs. This is
built on top of Qiskit's
`AerStatevector <https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.quantum_info.AerStatevector.html>`_.

This simulator closely models the classical and quantum operation of the QPU
with varying approximations. It instantiates a "state" representing both
classical and quantum components of the hardware and then executes your QCDL
instructions one at a time to update that state. As a Monte Carlo simulator, it
is significantly slower than a "sampling" simulator and scales linearly with the
number of shots; however, its operation is
`embarrassingly parallel <https://en.m.wikipedia.org/wiki/Embarrassingly_parallel>`_.

.. tip::
    Accuracy bears a simulation cost and error handling increases circuit
    complexity. It is advisable to start circuit development against the ideal
    simulator and then introduce error modeling.

    .. for future consideration
        in a controlled way. For example, start by simulating full-precision
        registers before simulating reduced-precision registers; start with
        ideal quantum operations before introducing erasures.

        Amos: Update the above paragraph as new features become available

The simulator in the |cloud|_ service supports two modes of simulations. The
following table compares these two simulation modes.

.. list-table::
    :header-rows: 1

    *   -   Characteristic
        -   Statevector Simulation
        -   Dual-Rail Erasure Simulation
    *   -   Noise model.
        -   Solver parameter :ref:`parameter_drsim_noise_model` set to
            ``False``.

            Useful during initial testing of QCDL programs before introducing
            noise.
        -   Solver parameter :ref:`parameter_drsim_noise_model` set to
            ``True``.

            This simulation is useful for exploring the impact of erasures on
            QCDL programs. It operates by randomly applying Pauli errors,
            leakages, and seepages after quantum gates and idles.
    *   -   Runtime.
        -   Scales as :math:`O(s*g*2^n)` where :math:`n` is the number of qubits,
            :math:`s` the number of shots, and :math:`g` the number of gates.

        -   Slower but same scaling.
    *   -   Supported gates.
        -   All gates available in Qiskit (no transpilation required).
        -   Subset of gates (transpilation required).
    *   -   Support for errors.
        -   No support. (Returns :math:`0` for ``mced``, signifying no leak.)
        -   Supports the ``mced`` instruction to detect if the qubit has been
            erased, and the ``leak`` and ``seep`` instructions to simulate
            leakage and seepage errors.


.. _qcdl_submitting_programs:

Submitting Programs
===================

The :ref:`QPU simulator <qcdl_simulator>` in the |cloud|_ service is intended to
simulate :ref:`gate-model quantum computers <qpu_gate_model_intro>` by executing
programs formulated as QCDL.

Descriptions of the supported parameters and simulator properties are provided
in the :ref:`qcdl_simulator_parameters` and :ref:`qcdl_simulator_properties`
sections.

.. _qcdl_submitting_programs_example:

Example Submission
==================

The example below submits the following
`Bell state <https://en.wikipedia.org/wiki/Bell_state>`_ QCDL program.

.. include:: ../shared/examples.rst
    :start-after: start_gm_sim_bell
    :end-before: end_gm_sim_bell

Submit the program above to a simulator for a dual-rail QPU with 21 qubits,
``DRsim_21qubits``, in the |cloud|_ service.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     qpu='DRsim_21qubits',
...     noise_model=True,
...     shots=500,
...     label="SDK Examples - Bell-Program Job Submission")
>>> result = future.result().result         # doctest: +SKIP

.. _qcdl_submitting_programs_results:

Example Results
===============

Results are returned as a :class:`~dwave.gate.results.Result` class, that also
includes information such as execution time and provides methods for analyzing
the measurements.

The returned result is a 3D array of ``(measurements per shot, shots, qubits)``.
For the previous example, one measurement is taken per shot, for 500 shots, on
two qubits.

>>> print(result.get_memory().shape)        # doctest: +SKIP
(1, 500, 2)

For one particular execution of the program above, the following counts are
returned.

>>> print(result.get_counts())              # doctest: +SKIP
[{'11': 203, '*1': 14, '00': 230, '0*': 22, '*0': 19, '1*': 10, '**': 2}]

The execution time on the simulator (excluding any queuing time, for example)
for that job submission is about a tenth of a second.

>>> print(result.run_time)                  # doctest: +SKIP
0.093493

See the :ref:`gate_results` section for information about the returned results
and supported methods. The :ref:`qcdl_basic_result_records` section describes
how you store and retrieve records of measurements.
