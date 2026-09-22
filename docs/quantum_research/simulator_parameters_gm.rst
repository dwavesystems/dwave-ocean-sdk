.. _qcdl_simulator_parameters:

===============================
Gate-Model Simulator Parameters
===============================

The examples in this section submit the QCDL program defined in the
:ref:`qcdl_submitting_programs_example` section.


.. _parameter_drsim_noise_model:

noise_model
-----------

Boolean flag that applies a noise model.

*   ``noise_model=True``: Apply a noise model.
*   ``noise_model=False``: Do not apply a noise model (simulate an ideal QPU,
    as described in the :ref:`qcdl_simulator` section).

The default value is specified by the :ref:`property_drsim_default_noise_model`
property.

This example applies a noise model for the program submitted to the simulator.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     noise_model=True)
>>> result = future.result().result         # doctest: +SKIP

.. _parameter_drsim_qpu:

qpu
---

The QPU to simulate, formatted as a string.

The :ref:`property_drsim_supported_qpu_strings` property lists the supported
values. The default QPU to simulate is specified by the
:ref:`property_drsim_default_qpu` property.

This example submits a QCDL program to a dual-rail QPU simulator with 21 qubits,
``DRsim_21qubits`` .

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     qpu='DRsim_21qubits')
>>> result = future.result().result         # doctest: +SKIP


.. _parameter_drsim_repeat_until_shots_requested:

repeat_until_shots_requested
----------------------------

Boolean flag to run the circuit repeatedly until a target number of
non-erased measurements are accumulated.

Running a circuit might return, under noisy conditions, measurements that are
declared to be “erased”, as described in the :ref:`qcdl_basic_measurements`
section. To try to achieve the required number of non-erasure measurements
indicted by the :ref:`parameter_drsim_shots` parameter, as counted after
post-selection to remove "splats" (see the :ref:`qcdl_basic_result_records`
section), you can select to repeatedly run the circuit. With yield defined as
the percentage of shots without erasures, the required number of executions (and
runtime) is proportional to the value of the :ref:`parameter_drsim_shots`
parameter and the reciprocal of the yield, and grows exponentially with
increased noise.

*   ``repeat_until_shots_requested=True``: Repeatedly run the circuit until
    the requested number of non-erasure measurements, indicated by the
    :ref:`parameter_drsim_shots` parameter, is accumulated with
    ``post_select=True``. Under noisy conditions the circuit might be executed a
    greater number of times than set by the :ref:`parameter_drsim_shots`
    parameter.
*   ``repeat_until_shots_requested=False``: Run the circuit the number of times
    set by the :ref:`parameter_drsim_shots` parameter. Under noisy conditions,
    fewer non-erasure measurements than indicated by the
    :ref:`parameter_drsim_shots` parameter might be accumulated with
    ``post_select=True``.

The default value is set by the
:ref:`property_drsim_default_repeat_until_shots_requested` property.

If runtime exceeds the value you specified in the
:ref:`parameter_drsim_time_limit` parameter (or the default value of the
:ref:`property_drsim_default_time_limit_s` property), execution
terminates.

This example repeatedly executes the circuit, under noisy conditions, to
accumulate 10 non-erasure measurements.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     shots=10,
...     noise_model=True,
...     repeat_until_shots_requested=True)
>>> result = future.result().result         # doctest: +SKIP

The sum of non-splat states in the returned results is the requested number of
shots:

>>> print(sum(result.get_counts(post_select=True)[0].values())) # doctest: +SKIP
10

.. _parameter_drsim_shots:

shots
-----

The number of measurements to run, formatted as an integer.

Your QCDL program is executed once for each requested measurement.

The specified value must not exceed the value of the
:ref:`property_drsim_maximum_shots` property. Execution time is limited by the
value you specified in the :ref:`parameter_drsim_time_limit` parameter (or
the default value of the :ref:`property_drsim_default_time_limit_s` property).

The default value is to measure the number of times specified by the
:ref:`property_drsim_default_shots` property.

This example executes the circuit 1000 times.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     shots=1000)
>>> result = future.result().result         # doctest: +SKIP

.. _parameter_drsim_time_limit:

time_limit
----------

Specifies the maximum runtime, in seconds, the solver is allowed to work on the
given program. Can be a float or integer.

The specified time must be between the values of the
:ref:`property_drsim_maximum_time_limit_s` and
:ref:`property_drsim_minimum_time_limit_s` properties.

The default runtime limit is specified by the
:ref:`property_drsim_default_time_limit_s` property.

This example sets a maximum runtime of 10 minutes.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     time_limit=10*60)
>>> result = future.result().result         # doctest: +SKIP

.. _parameter_drsim_transpile:

transpile
---------

Boolean flag to rewrite the submitted QCDL circuit to use the QPU's supported
basis gates and topology, as described in the :ref:`qcdl_basic_transpilation`
section.

*   ``transpile=True``: Transpile the circuit.
*   ``transpile=False``: Run the circuit exactly as specified in the submitted
    QCDL or return an error.

The default value is specified by the :ref:`property_drsim_default_transpile`
property.

This example requires that the QCDL circuit be submitted as written to the
simulator.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     noise_model=True,
...     transpile=False)
>>> result = future.result().result         # doctest: +SKIP
