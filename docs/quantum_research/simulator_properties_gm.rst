.. _qcdl_simulator_properties:

===============================
Gate-Model Simulator Properties
===============================

.. _property_drsim_category:

category
--------

Type of solver, as a string.

*   ``software-gate``: Gate-model simulator.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()     # doctest: +SKIP
>>> simulator.properties["category"]    # doctest: +SKIP
'software-gate'

.. _property_drsim_default_noise_model:

default_noise_model
-------------------

Default setting for the application of a noise model, as a Boolean.

*   ``True``: A noise model is applied.
*   ``False``: Simulates an ideal QPU, as described in the
    :ref:`qcdl_simulator` section.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["default_noise_model"]     # doctest: +SKIP
False

.. _property_drsim_default_qpu:

default_qpu
-----------

Default selection of the QPU to simulate, as a string.

Supported QPUs are listed in the :ref:`property_drsim_supported_qpu_strings`
property.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> simulator.properties["default_qpu"]     # doctest: +SKIP
'DRsim_21qubits'

.. _property_drsim_default_repeat_until_shots_requested:

default_repeat_until_shots_requested
------------------------------------

Default setting, as a Boolean, for rerunning the circuit until the requested
number of measurements is accumulated, where the accumulated measurements do not
include erasures (see the :ref:`qcdl_basic_result_records` section).

*   ``True``: Repeatedly rerun the circuit.
*   ``False``: Run the circuit the number of times set by the
    :ref:`parameter_drsim_shots` parameter.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                                 # doctest: +SKIP
>>> simulator.properties["default_repeat_until_shots_requested"]    # doctest: +SKIP
False

.. _property_drsim_default_shots:

default_shots
-------------

Default setting for the number of measurements to run (times to execute your
QCDL circuit), as an integer. With dual-rail QPUs, a measurement result can be a
"splat" (see the :ref:`qcdl_basic_measurements` section).

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> simulator.properties["default_shots"]   # doctest: +SKIP
1000

.. _property_drsim_default_time_limit_s:

default_time_limit_s
--------------------

Default maximum runtime, in seconds, the solver is allowed to work on the
given program, as a float.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["default_time_limit_s"]      # doctest: +SKIP
2700

.. _property_drsim_default_transpile:

default_transpile
-----------------

Default setting, as a Boolean, for :ref:`transpiling <qcdl_basic_transpilation>`
the submitted QCDL program.

*   ``True``: Transpile the program.
*   ``False``: Run the circuit exactly as specified in the submitted
    QCDL or return an error.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["default_transpile"]       # doctest: +SKIP
True

.. _property_drsim_maximum_num_qubits:

maximum_num_qubits
------------------

Maximum number of qubits for QCDL circuits, as an integer.

.. note:: :ref:`Transpilation <qcdl_basic_transpilation>` can add and remove
    qubits in your QCDL.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                     # doctest: +SKIP
>>> simulator.properties["maximum_num_qubits"]          # doctest: +SKIP
21

.. _property_drsim_maximum_shots:

maximum_shots
-------------

Maximum value of the :ref:`parameter_drsim_shots` you can specify, as an
integer.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()             # doctest: +SKIP
>>> simulator.properties["maximum_shots"]       # doctest: +SKIP
1000000

.. _property_drsim_maximum_time_limit_s:

maximum_time_limit_s
--------------------

Maximum time, in seconds as a float, that your submitted circuit can run.

This value limits the range of values you can set on the
:ref:`parameter_drsim_time_limit` parameter.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["maximum_time_limit_s"]    # doctest: +SKIP
2700

.. _property_drsim_minimum_shots:

minimum_shots
-------------

Minimum number of times the circuit can be executed, as an integer.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()             # doctest: +SKIP
>>> simulator.properties["minimum_shots"]       # doctest: +SKIP
1

.. _property_drsim_minimum_time_limit_s:

minimum_time_limit_s
--------------------

Minimum time, in seconds as a float, you can specify for the runtime limit (the
:ref:`parameter_drsim_time_limit` parameter) on your submitted circuit.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["minimum_time_limit_s"]    # doctest: +SKIP
1

.. _property_drsim_quota_conversion_rate:

quota_conversion_rate
---------------------

Rate at which user or project quota is consumed for the solver as a ratio to
QPU solver usage. Different solver types may consume quota at different rates.

Time is deducted from your quota according to:

.. math::

    \frac{num\_seconds}{quota\_conversion\_rate}

See the :ref:`leap_hybrid_usage_charges` section for more information.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["quota_conversion_rate"]   # doctest: +SKIP
1

.. _property_drsim_supported_qpu_strings:

supported_qpu_strings
---------------------

Names of supported simulators, as a list of strings.

Available QPUs are the following:

*   ``DRsim_17qubits``: Dual-rail QPU with 17 qubits.
*   ``DRsim_21qubits``: Dual-rail QPU with 21 qubits.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()                 # doctest: +SKIP
>>> simulator.properties["supported_qpu_strings"]   # doctest: +SKIP
['DRsim_17qubits', 'DRsim_21qubits']
