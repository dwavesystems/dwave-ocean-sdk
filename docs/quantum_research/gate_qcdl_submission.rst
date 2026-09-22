.. _qcdl_using_solver:

===========================
Using the Gate-Model Solver
===========================

The |cloud|_ quantum cloud service provides access to a simulator that enables
you to test gate-model circuits intended to be executed on a dual-rail quantum
processing unit (QPU). You describe your circuits using the ``dwave-gate``
package's quantum circuit description language (QCDL), described here.

.. _QuantumCircuit: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit

.. _qcdl_onboarding:

Onboarding for Beta Testers
===========================

.. important::
    Features for real-time control, which are being phased into dual-rail
    quantum computing systems, are already available on the simulator in the
    |cloud|_ service for prototyping and learning.

To construct :term:`QCDL` programs and submit to the dual-rail simulator in the
|cloud|_ service you need the following:

1.  A |cloud|_ account that has been invited to beta test the dual-rail
    simulator.
2.  A development environment with the :ref:`index_ocean_sdk`.

.. _qcdl_onboarding_new_users:

New Users
---------

If you are already using Ocean software for an existing |cloud|_ service
account, see the :ref:`qcdl_onboarding_previous_users` section for working with
another project.

If you have accepted an invitation to the |cloud|_ service for the first time to
use the dual-rail simulator, the following documentation gets you started with
submitting your programs:

*   The :ref:`index_leap_sapi` section.

    This section describes the |cloud|_ service: the dashboard where you can see
    your access to :term:`solver`\ s such as the dual-rail simulator, the API
    token you need to submit programs to the simulator, whitelisting information
    if required by your organization, and more.

*   The :ref:`ocean_index_get_started` section.

    This section explains how to start using the :ref:`index_ocean_sdk`, which
    lets you write :term:`QCDL` programs and submit them to the simulator.

.. note::
    Installing the SDK is recommended. If you chose to install only the
    :ref:`index_gate` package, see the installation instructions
    `here <https://github.com/dwavesystems/dwave-gate/blob/main/README.rst>`_.

.. _qcdl_onboarding_previous_users:

Previous Users
--------------

To submit programs to the dual-rail simulator in the |cloud|_ service, you must
accept the emailed invitation to a new project. You use the API token from this
project to access and send jobs to the simulator.

The :ref:`ocean_leap_authorization` section describes how to work with multiple
projects (see the "Multiple Leap Projects" tab).

The following are two simple ways to use the beta-tester project's API token
from your existing development environment.

*   Add a section to your ``dwave.conf`` file.

    You can see your ``dwave.conf`` file using the methods described in the
    :ref:`cloud_configuration` or using the :ref:`D-Wave CLI <ocean_dwave_cli>`
    section.

    For example, add a ``beta`` section, which is used for your beta testing::

        [defaults]
        token = ABC-123456789123456789123456789

        [beta]
        token = BETA-123456789123456789123456789

    You can then set ``profile="beta"`` to use the beta-tester project's API
    token when accessing the simulator.

    >>> from dwave.gate.leap import LeapQCDLSimulator
    ...
    >>> simulator = LeapQCDLSimulator(profile="beta")         # doctest: +SKIP

    You can use the following :ref:`D-Wave CLI <ocean_dwave_cli>` commands to
    authorize Ocean software to access the |cloud|_ service and Configure a
    ``beta`` profile,::

        $ dwave auth login
        $ dwave config create --profile beta --auto-token --project "Beta Testing"

    where ``Beta Testing`` should be replaced with the project name as displayed
    in the |cloud|_ service. The commands locate your existing configuration
    file, or create one if needed, then create a new profile called ``beta``,
    and ask you for your SAPI token to create the new profile.

*   Set the ``DWAVE_API_TOKEN`` environment variable.

    You can set this environment variable for a Unix operating system with a
    Bash command such as,
    ``export DWAVE_API_TOKEN="BETA-123456789123456789123456789"``, for example,
    or for a Windows system with a command such as
    ``set DWAVE_API_TOKEN=BETA-123456789123456789123456789``.

    Remember to delete that environment variable when you return to your
    work on your previous project.


.. _qcdl_simulator:

QPU Simulator
=============

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

The following documentation describes how to work with the |cloud|_ service:

*   The :ref:`index_leap_sapi` section describes the |cloud|_ service.
*   The :ref:`ocean_leap_authorization` section walks you through authorizing
    your Ocean client to access the simulator in the |cloud|_ service.
*   The :ref:`ocean_install` section explains how to install Ocean software.

Descriptions of the supported parameters and simulator properties are provided
in the :ref:`qcdl_simulator_parameters` and :ref:`qcdl_simulator_properties`
sections.

.. _qcdl_submitting_programs_example:

Example Submission
------------------

The example below submits the following
`Bell state <https://en.wikipedia.org/wiki/Bell_state>`_ QCDL program.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import cx, h, measure

    @qcdl(2)
    def bell_program(q0, q1):
        h(q0)
        cx(q0, q1)
        measure(q0)
        measure(q1)

    simulator_job_submission = bell_program()

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
---------------

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
