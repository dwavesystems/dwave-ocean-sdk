.. _qpu_solver_properties_all:

=============================
General QPU Solver Properties
=============================

.. |anneal_time_display_granularity| replace:: with a resolution of 0.01
    :math:`\mu s`

This section describes the properties in common to all :term:`QPU` solvers and
shows how you can query their values through :term:`SAPI`; for properties
specific to the hardware of a particular QPU, see the
:ref:`qpu_solver_properties_specific` section.

For the parameters you can configure, see the :ref:`qpu_solver_parameters`
section.

.. _property_qpu_anneal_offset_ranges:

anneal_offset_ranges
====================

Array of ranges of valid anneal offset values, in normalized offset units, for
each qubit. The negative values represent the largest number of normalized
offset units by which a qubit's anneal path may be delayed. The positive values
represent the largest number of normalized offset units by which a qubit's
anneal path may be advanced.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["anneal_offset_ranges"][50:55]       # doctest: +SKIP
[[-0.6437569799443247, 0.5093937328282595],
 [-0.6409899716199288, 0.5697835920492209],
 [-0.6468663649068287, 0.5211452841036136],
 [-0.6435316809914349, 0.5011584701861175],
 [-0.6500326191157569, 0.5392206819650301]]


.. _property_qpu_anneal_offset_step:

anneal_offset_step
==================

Quantization step size of anneal offset values in normalized units.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["anneal_offset_step"]      # doctest: +SKIP
-0.00017565852000668507


.. _property_qpu_anneal_offset_step_phi0:

anneal_offset_step_phi0
=======================

Quantization step size in physical units (annealing flux-bias units):
:math:`\Phi_0`.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["anneal_offset_step_phi0"]           # doctest: +SKIP
1.486239425109832e-05


.. _property_qpu_annealing_time_range:

annealing_time_range
====================

Range of time, in microseconds |anneal_time_display_granularity|,
possible for one anneal (read).
The lower limit in this range is the fastest quench possible for this solver
using the standard-anneal protocol. See also the
:ref:`property_qpu_fast_anneal_time_range`.

Default annealing time is specified by the
:ref:`property_qpu_default_annealing_time` property.

Example
-------

.. todo:: verify we can enable this test

.. skip test until SDK>6.7.0 (https://github.com/dwavesystems/dwave-system/pull/503)

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["annealing_time_range"]        # doctest: +SKIP
[0.5, 2000.0]


.. _property_qpu_category:

category
========

.. |category| replace:: ``qpu``: Quantum computers such as the |dwave_5kq|
    system.

.. include:: ../shared/properties.rst
    :start-after: start_property_category
    :end-before: end_property_category

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["category"]
'qpu'


.. _property_qpu_chip_id:

chip_id
=======

Name of the solver.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["chip_id"]             # doctest: +SKIP
'Advantage_system1.1'


.. _property_qpu_couplers:

couplers
========

Couplers in the working graph. A coupler contains two elements [*q1*, *q2*],
where both *q1* and *q2* appear in the list of working qubits, in the range
[0, *num_qubits* - 1] and in ascending order (i.e., *q1* < *q2*). These are the
couplers that can be programmed with nonzero :math:`J` values.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["couplers"][:5]           # doctest: +SKIP
[[30, 31], [31, 32], [32, 33], [33, 34], [34, 35]]


.. _property_qpu_default_annealing_time:

default_annealing_time
======================

Default time, in microseconds |anneal_time_display_granularity|, for one anneal
(read). You can change the annealing time for a given problem by using the
:ref:`parameter_qpu_annealing_time` or :ref:`parameter_qpu_anneal_schedule`
parameters, but do not exceed the upper limit given by the
:ref:`property_qpu_annealing_time_range` or
:ref:`property_qpu_fast_anneal_time_range` property.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["default_annealing_time"]        # doctest: +SKIP
20.0


.. _property_qpu_default_programming_thermalization:

default_programming_thermalization
==================================

Default time, in microseconds |anneal_time_display_granularity|, that the
system waits after programming the QPU for it to return to base temperature.
This value contributes to the total *qpu_programming_time*,
which is returned by SAPI with the problem solutions.

You can change this value using the
:ref:`parameter_qpu_programming_thermalization` parameter.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["default_programming_thermalization"]   # doctest: +SKIP
1000.0


.. _property_qpu_default_readout_thermalization:

default_readout_thermalization
==============================

Default time, in microseconds |anneal_time_display_granularity|, that the
system waits after each state is read from the QPU for it to cool back to base
temperature. This value contributes to the *qpu_delay_time_per_sample* field,
which is returned by SAPI with the problem solutions.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["default_readout_thermalization"]   # doctest: +SKIP
0.0


.. _property_qpu_extended_j_range:

extended_j_range
================

Extended range of values possible for the coupling strengths (quadratic
coefficients), :math:`J`, for this solver. Strong negative couplings may be
necessary for some embeddings; however, such chains may require additional
calibration through the :ref:`parameter_qpu_flux_biases` parameter to
compensate for biases introduced by strong negative couplings. See also
:ref:`property_qpu_per_qubit_coupling_range` and
:ref:`property_qpu_per_group_coupling_range`.

The :ref:`parameter_qpu_auto_scale` parameter, which rescales :math:`h` and
:math:`J` values in the problem to use as much of the range of :math:`h`
(:ref:`property_qpu_h_range`) and the range of :math:`J`
(:ref:`property_qpu_extended_j_range`) as possible, enables you to submit
problems with values outside these ranges and have the system automatically
scale them to fit.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["extended_j_range"]
[-2.0, 1.0]


.. _property_qpu_fast_anneal_time_range:

fast_anneal_time_range
======================

Range of time, in microseconds with a resolution of up to picoseconds,\ [#]_
possible for one anneal (read). The lower limit in this range is the fastest
quench possible for this solver.

Default annealing time is specified by the
:ref:`property_qpu_default_annealing_time` property.

..  [#]
    The :ref:`fast-anneal protocol <qpu_annealprotocol_fast>` supports a time
    granularity of about 0.05% of the anneal time. For annealing times of about
    10 ns, the granularity is about 5 ps; for anneals of about 20 :math:`\mu s`,
    it is reduced to around 10 ns.

Example
-------

.. todo:: verify we can enable this test

.. skip test until SDK>6.7.0 (https://github.com/dwavesystems/dwave-system/pull/503)

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["fast_anneal_time_range"]        # doctest: +SKIP
[0.005, 2000.0]


.. _property_qpu_h_gain_schedule_range:

h_gain_schedule_range
=====================

Range of the time-dependent gain applied to qubit biases for this solver.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["h_gain_schedule_range"]        # doctest: +SKIP
[-4.0, 4.0]


.. _property_qpu_h_range:

h_range
=======

Range of values possible for the qubit biases (linear coefficients), :math:`h`,
for this solver.

The :ref:`parameter_qpu_auto_scale` parameter, which rescales :math:`h` and
:math:`J` values in the problem to use as much of the range of :math:`h`
(:ref:`property_qpu_h_range`) and the range of :math:`J`
(:ref:`property_qpu_extended_j_range`) as possible, enables you to submit
problems with values outside these ranges and have the system automatically
scale them to fit.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["h_range"]
[-4.0, 4.0]


.. _property_qpu_j_range:

j_range
=======

Range of values possible for the coupling strengths (quadratic coefficients),
:math:`J`, for this solver.

See also the :ref:`property_qpu_extended_j_range` solver property.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["j_range"]               # doctest: +SKIP
[-1.0, 1.0]


.. _property_qpu_max_anneal_schedule_points:

max_anneal_schedule_points
==========================

Maximum number of points permitted in a PWL waveform submitted to change the
default anneal schedule.

For reverse annealing, the maximum number of points allowed is one more than the
number given in the :ref:`property_qpu_max_anneal_schedule_points` property.

Example
-------

.. todo:: verify we can enable this test

.. skip test until SDK>6.7.0 (https://github.com/dwavesystems/dwave-system/pull/503)

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["max_anneal_schedule_points"]   # doctest: +SKIP
12


.. _property_qpu_max_h_gain_schedule_points:

max_h_gain_schedule_points
==========================

Maximum number of points permitted in a PWL waveform submitted to set a
time-dependent gain on linear coefficients (qubit biases, see the
:ref:`parameter_qpu_h` parameter) in the Hamiltonian.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["max_h_gain_schedule_points"]     # doctest: +SKIP
20


.. _property_qpu_num_qubits:

num_qubits
==========

Total number of qubits, both working and nonworking,\ [#]_ in the QPU.

.. [#]
  The :ref:`property_qpu_qubits` property provides the indices of qubits in the
  QPU's :ref:`working graph <topologies_working_graph>`, which are the qubits
  you can use for problem solving.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["num_qubits"]               # doctest: +SKIP
5760


.. _property_qpu_num_reads_range:

num_reads_range
===============

Range of values possible for the number of reads that you can request for a
problem.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["num_reads_range"]
[1, 10000]


.. _property_qpu_parameters:

parameters
==========

.. include:: ../shared/properties.rst
    :start-after: start_property_parameters
    :end-before: end_property_parameters

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["parameters"]["num_reads"]  # doctest: +SKIP
'Number of states to read (answers to return), as a positive integer.'


.. _property_qpu_per_group_coupling_range:

per_group_coupling_range
========================

Supported on |adv2| QPUs only.

Coupling range permitted per group of qubits for this solver. The couplers of
every qubit are divided into two similar sized groups to which apply
limitations on the total of all coupling strengths.

Strong negative couplings may be necessary for some embeddings, and can be
enabled by using the :ref:`property_qpu_extended_j_range` range of :math:`J`
values. However, total :math:`J` values of the couplers for a group of qubits
must not exceed the range specified by this property. Also, chains may require
additional calibration through the :ref:`parameter_qpu_flux_biases` parameter
to compensate for biases introduced by strong negative couplings.

The :ref:`parameter_qpu_auto_scale` parameter scales a problem's :math:`J`
values such that the total :math:`J` values of the couplers for a group of
qubits is within the range specified by this property.

.. todo:: update the link below:

For more information, Ocean software's
:std:doc:`coupling_groups <docs_system/reference/generated/dwave.system.coupling_groups.coupling_groups>`
function.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler(solver={"topology__type": "zephyr"}) # doctest: +SKIP
>>> sampler.properties["per_group_coupling_range"]        # doctest: +SKIP
[-13.000 10.000]


.. _property_qpu_per_qubit_coupling_range:

per_qubit_coupling_range
========================

Supported on |dwave_5kq| QPUs only.

Coupling range permitted per qubit for this solver.

Strong negative couplings may be necessary for some embeddings, and can be
enabled by using the :ref:`property_qpu_extended_j_range` range of :math:`J`
values. However, the total :math:`J` values of the couplers for a qubit must
not exceed the range specified by this property. Also, chains may require
additional calibration through the :ref:`parameter_qpu_flux_biases` parameter
to compensate for biases introduced by strong negative couplings.

The :ref:`parameter_qpu_auto_scale` parameter scales a problem's :math:`J`
values such that the total :math:`J` values of the couplers for a qubit is
within the range specified by this property.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler(solver={"topology__type": "pegasus"}) # doctest: +SKIP
>>> sampler.properties["per_qubit_coupling_range"]        # doctest: +SKIP
[-18.0, 15.0]


.. _property_qpu_problem_run_duration_range:

problem_run_duration_range
==========================

Range of time, in microseconds |anneal_time_display_granularity|, that a
submitted problem is allowed to run.

For details about how the run-duration limit is calculated, see
:ref:`qpu_timing_runtime_limits`.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["problem_run_duration_range"]       # doctest: +SKIP
[0.0, 1000000.0]


.. _property_qpu_problem_timing_data:

problem_timing_data
===================

Key-value pairs that contain sample timing data and specify the version 1.0.x
problem-timing model used to estimate problem runtimes for a QPU solver. For
details about using the timing data to estimate the QPU access times for
problem submissions, see the :ref:`qpu_runtime_estimating` section.

The key-value pairs are the following:

*   ``decorrelation_max_nominal_anneal_time``: Parameter, in microseconds,
    used in the calculation of inter-sample correlation time.
    For more information, see the
    :ref:`parameter_qpu_reduce_intersample_correlation` solver property.

*   ``decorrelation_time_range``: Range of inter-sample correlation time,
    in microseconds, to add to the per-sample delay time as specified in the
    ``qpu_delay_time_per_sample`` field. Scales linearly with the anneal time
    from 0 to the amount returned in the
    ``decorrelation_max_nominal_anneal_time`` field. For more details, see the
    :ref:`parameter_qpu_reduce_intersample_correlation` solver parameter.

*   ``default_annealing_time``: See the
    :ref:`property_qpu_default_annealing_time` solver property.

*   ``default_programming_thermalization``: See the
    :ref:`property_qpu_default_programming_thermalization` solver property.

*   ``default_readout_thermalization``: See the
    :ref:`property_qpu_default_readout_thermalization` solver property.

*   ``qpu_delay_time_per_sample``: Default for the per-sample delay time
    in microseconds.

*   ``readout_time_model``: The readout-time model used to generate
    the set of data points; these data points define a piecewise-linear curve
    of typical readout times as a function of the number of qubits in a
    representative set of problems embedded on a QPU. The data points are
    provided in the ``readout_time_model_parameters`` field. Supported values
    that specify the scale of the curve are:

    *   ``pwl_log_log``: The log scale is used for both the horizontal
        and vertical axes.

    *   ``pwl_linear``: The linear scale is used for both the horizontal
        and vertical axes.

*   ``readout_time_model_parameters``: A set of :math:`2N` data points
    generated by the readout-time model specified in the ``readout_time_model``
    field.

*   ``reverse_annealing_with_reinit_delay_time_delta``: Extra per-sample
    delay time, in microseconds, when reverse annealing is used and the
    :ref:`parameter_qpu_reinitialize_state` parameter is true.

*   ``reverse_annealing_with_reinit_prog_time_delta``: Extra programming time,
    in microseconds, when reverse annealing is used and the 
    :ref:`parameter_qpu_reinitialize_state` solver parameter is true.

*   ``reverse_annealing_without_reinit_delay_time_delta``: Extra per-sample
    delay time, in microseconds, when reverse annealing is used and the
    :ref:`parameter_qpu_reinitialize_state` solver parameter is false.

*   ``reverse_annealing_without_reinit_prog_time_delta``: Extra programming
    time, in microseconds, when reverse annealing is used and the
    :ref:`parameter_qpu_reinitialize_state` solver parameter is false.

*   ``typical_programming_time``: Typical programming time in microseconds.

*   ``version``: Version of the problem-timing model.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["problem_timing_data"]   # doctest: +SKIP
{'version': '1.0.0', 'typical_programming_time': 14072.88,
'reverse_annealing_with_reinit_prog_time_delta': 0.0,
'reverse_annealing_without_reinit_prog_time_delta': 5.55,
'default_programming_thermalization': 1000.0, 'default_annealing_time': 20.0,
'readout_time_model': 'pwl_log_log',
'readout_time_model_parameters': [0.0, 0.7699665876947938, 1.7242758696010096,
2.711975459489206, 3.1639057672764026, 3.750276915153992, 1.539131714800995,
1.8726623164229292, 2.125631787097315, 2.332672340068556, 2.371606651233025,
2.3716219271760215], 'qpu_delay_time_per_sample': 20.54,
'reverse_annealing_with_reinit_delay_time_delta': -4.5,
'reverse_annealing_without_reinit_delay_time_delta': -1.5,
'default_readout_thermalization': 0.0, 'decorrelation_max_nominal_anneal_time': 2000.0,
'decorrelation_time_range': [500.0, 10000.0]}


.. _property_qpu_programming_thermalization_range:

programming_thermalization_range
================================

Range of time, in microseconds |anneal_time_display_granularity|, possible for
the system to wait after programming the QPU for it to cool back to base
temperature. This value contributes to the total *qpu_programming_time*, which
is returned by SAPI with the problem solutions.

You can change this value using the
:ref:`parameter_qpu_programming_thermalization` parameter, but be aware that
values lower than the default accelerate solving at the expense of solution
quality.

Default value for a solver is given in the
:ref:`property_qpu_default_programming_thermalization` property.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["programming_thermalization_range"]   # doctest: +SKIP
[0.0, 10000.0]


.. _property_qpu_qubits:

qubits
======

Indices of the working graph.

In a |dwave_short| QPU, the set of qubits and couplers that are available for
computation is known as the :ref:`working graph <topologies_working_graph>`.
The working graph typically does not contain all the qubits and couplers that
are fabricated and physically present in the QPU. For example, an |dwave_5kq|
QPU with its 5760 qubits (the :ref:`property_qpu_num_qubits` property), of
which a maximum of 5640 are calibrated for problem solving (the programmable
fabric, or largest component of the full Pegasus\ |tm| graph), might have a
working graph of 5627 qubits (a *yield* of 99.7%) due to 13 qubits that were
not brought into a consistent parametric regime in the calibration process. For
such a system, the value of the ``qubits`` property is the sequence of integers
between 30, the first of the 5640 fabric qubits, and 5729, the last of those
5640 qubits, minus indices of the 13 non-working qubits.\ [#]_

.. [#]
    You can see the qubit indexing scheme of such an |dwave_5kq| QPU
    with Ocean software's :func:`dwave_networkx.pegasus_graph` function,
    which enables you to generate Pegasus graphs.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["qubits"][:5]         # doctest: +SKIP
[30, 31, 32, 33, 34]


.. _property_qpu_quota_conversion_rate:

quota_conversion_rate
=====================

.. include:: ../shared/properties.rst
    :start-after: start_property_quota_conversion_rate
    :end-before: end_property_quota_conversion_rate

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["quota_conversion_rate"]  # doctest: +SKIP
1


.. _property_qpu_readout_thermalization_range:

readout_thermalization_range
============================

Range of time, in microseconds |anneal_time_display_granularity|, possible for
the system to wait after each state is read from the QPU for it to cool back to
base temperature. This value contributes to the *qpu_delay_time_per_sample*
field, which is returned by SAPI with the problem solutions.

Default readout thermalization time is specified in the
:ref:`property_qpu_default_readout_thermalization` property.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["readout_thermalization_range"]       # doctest: +SKIP
[0.0, 10000.0]


.. _property_qpu_supported_problem_types:

supported_problem_types
=======================

.. include:: ../shared/properties.rst
    :start-after: start_property_supported_problem_types
    :end-before: end_property_supported_problem_types

QPU solvers support the following energy-minimization problem types:

*   ``qubo``: Quadratic unconstrained binary optimization (QUBO) problems; use
    :math:`0/1`-valued variables.
*   ``ising``: Ising model problems; use :math:`-1/1`-valued variables.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["supported_problem_types"]  # doctest: +SKIP
['ising', 'qubo']


.. _property_qpu_tags:

tags
====

May hold attributes about a solver that you can use to have a client program
choose one solver over another.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["tags"]  # doctest: +SKIP
[]


.. _property_qpu_topology:

topology
========

Indicates the topology ``type`` (``pegasus`` or ``zephyr``) and ``shape`` of
the QPU graph.

Example
-------

The topology seen in this example is a P16 Pegasus graph. See the
:ref:`qpu_topologies` section for a description of QPU topologies.

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["topology"]                    # doctest: +SKIP
{'type': 'pegasus', 'shape': [16]}


.. _property_qpu_vfyc:

vfyc
====

Obsolete property that is always :code:`False`.

Example
-------

>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> sampler.properties["vfyc"]              # doctest: +SKIP
False
