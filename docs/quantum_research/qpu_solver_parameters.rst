.. _qpu_solver_parameters:

=====================
QPU Solver Parameters
=====================

This section describes the configurable parameters you can set on :term:`QPU`
solvers. The :ref:`qpu_index_solver_properties` section gives the properties of
these solvers, such as the ranges within which parameter values must be set.

.. |anneal_time_parameter_granularity| replace:: with a resolution of 0.01
    :math:`\mu s`

.. |meet_run_duration| replace:: :ref:`parameter_qpu_anneal_schedule` or
    :ref:`parameter_qpu_annealing_time`,
    :ref:`parameter_qpu_readout_thermalization`, :ref:`parameter_qpu_num_reads`
    (samples), and :ref:`parameter_qpu_programming_thermalization` values taken
    together must meet the limitations specified in
    :ref:`property_qpu_problem_run_duration_range`.


.. _parameter_qpu_anneal_offsets:

anneal_offsets
==============

Provides offsets to annealing paths, per qubit.

Provide an array of anneal offset values, in normalized offset units, for all
qubits, working or not. Use 0 for no offset. Negative values produce a negative
offset (qubits are annealed *after* the standard annealing trajectory);
positive values produce a positive offset (qubits are annealed *before* the
standard trajectory). Before using this parameter, query the solver properties
to see whether the :ref:`property_qpu_anneal_offset_ranges` property exists and,
if so, to obtain the permitted offset values per qubit. Default is no offsets.

Relevant Properties
-------------------

*   :ref:`property_qpu_anneal_offset_ranges` defines the ranges of valid anneal
    offset values.
*   :ref:`property_qpu_anneal_offset_step` and
    :ref:`property_qpu_anneal_offset_step_phi0` define the quantization steps.

Example
-------

This example offsets the anneal of a qubit in a two-qubit illustrative
Ising problem.

>>> from dwave.system import FixedEmbeddingComposite, DWaveSampler
>>> qpu = DWaveSampler(solver={'topology__type': 'pegasus'})
>>> J = {(1, 2): -1}
>>> embedding = {1: [30], 2: [2940]}
>>> print(qpu.properties['anneal_offset_ranges'][2940])         # doctest: +SKIP
[-0.7012257815714587, 0.6717794151250857]
>>> sampler = FixedEmbeddingComposite(qpu, embedding)
>>> offset = [0]*qpu.properties['num_qubits']
>>> offset[2940]=0.2                                            # doctest: +SKIP
>>> sampleset = FixedEmbeddingComposite(qpu, embedding).sample_ising(
...     {}, J, num_reads=1000, anneal_offsets=offset)   # doctest: +SKIP

The |dwave_short| system used for this example is an |dwave_5kq| QPU that has
couplers between active qubits 30 and 2940. Select a suitable embedding for the
QPU you run examples on.


.. _parameter_qpu_anneal_schedule:

anneal_schedule
===============

Introduces variations to the :ref:`global anneal schedule <qpu_qa_anneal_sched>`.

For a :ref:`reverse anneal <qpu_qa_anneal_sched_reverse>`, use this parameter
with the :ref:`parameter_qpu_initial_state` and
:ref:`parameter_qpu_reinitialize_state` parameters.

For the :ref:`fast-anneal protocol <qpu_annealprotocol_fast>`, set the
:ref:`parameter_qpu_fast_anneal` to ``True``.

An anneal schedule variation is defined by a series of pairs of floating-point
numbers identifying points in the schedule at which to change slope. The first
element in the pair is time :math:`t` and the second is anneal fraction
:math:`s` in the range [0,1]. The resulting schedule is the piecewise-linear
curve that connects the provided points.

.. include:: ../shared/parameters.rst
    :start-after: start_time_granularity
    :end-before: end_time_granularity

.. include:: ../shared/anneal.rst
    :start-after: start_schedule_rules
    :end-before: end_schedule_rules

Default anneal schedules are described in the
:ref:`QPU-specific anneal schedules <qpu_solver_properties_specific>` section.

Relevant Properties
-------------------

*   :ref:`property_qpu_max_anneal_schedule_points` shows the maximum number of
    points permitted in an anneal schedule.
*   :ref:`property_qpu_default_annealing_time` shows the default annealing time
    for the solver.
*   :ref:`property_qpu_annealing_time_range` and
    :ref:`property_qpu_fast_anneal_time_range` define the limits of the allowable
    time range for the anneal schedule.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_annealing_time` and :ref:`parameter_qpu_anneal_schedule`
    parameters are mutually exclusive.
*   |meet_run_duration|
*   :ref:`parameter_qpu_anneal_schedule` can have only two points for the
    :ref:`fast-anneal protocol <qpu_annealprotocol_fast>` (when
    :ref:`parameter_qpu_fast_anneal` is set to ``True``).

Example
-------

This illustrative example configures a reverse-anneal schedule on a random native
problem.

>>> from dwave.system import DWaveSampler
>>> import random
...
>>> qpu = DWaveSampler()
>>> J = {coupler: random.choice([-1, 1]) for coupler in qpu.edgelist}
>>> initial = {qubit: random.randint(0, 1) for qubit in qpu.nodelist}
>>> reverse_schedule = [[0.0, 1.0], [5, 0.45], [99, 0.45], [100, 1.0]]
>>> reverse_anneal_params = dict(anneal_schedule=reverse_schedule,
...                              initial_state=initial,
...                              reinitialize_state=True)
>>> sampleset = qpu.sample_ising(
...     {}, J, num_reads=1000, **reverse_anneal_params)   # doctest: +SKIP


.. _parameter_qpu_annealing_time:

annealing_time
==============

Sets the duration of quantum annealing time, per read.

.. include:: ../shared/parameters.rst
    :start-after: start_time_granularity
    :end-before: end_time_granularity

This value populates the *qpu_anneal_time_per_sample* field returned in the
:ref:`timing <qpu_sapi_qpu_timing>` structure. Supported values are positive
floating-point numbers.

The allowed range of times depends on the annealing protocol: standard or fast
(activated with :ref:`parameter_qpu_fast_anneal`).

Default value is shown by :ref:`property_qpu_default_annealing_time`.

Relevant Properties
-------------------

*   :ref:`property_qpu_annealing_time_range` defines the supported range of valid
    times for the standard-annealing protocol.
*   :ref:`property_qpu_fast_anneal_time_range` defines the supported range of
    valid times for the :ref:`fast-anneal protocol <qpu_annealprotocol_fast>`.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_annealing_time` and :ref:`parameter_qpu_anneal_schedule`
    parameters are mutually exclusive. Configuring a value of ``T`` for
    :ref:`parameter_qpu_annealing_time` is equivalent to configuring
    :code:`anneal_schedule=[[0, 0], [T, 1]]`.
*   |meet_run_duration|
*   :ref:`parameter_qpu_fast_anneal` switches the allowable range between
    :ref:`property_qpu_annealing_time_range` (default) and
    :ref:`property_qpu_fast_anneal_time_range` ranges.

Example
-------

This illustrative example configures the anneal time on a random native
problem.

>>> from dwave.system import DWaveSampler
>>> import random
...
>>> qpu = DWaveSampler()
>>> J = {coupler: random.choice([-1, 1]) for coupler in qpu.edgelist}
>>> long_time = qpu.properties["annealing_time_range"][1]
>>> sampleset = qpu.sample_ising({}, J, num_reads=10, annealing_time=long_time)


.. _parameter_qpu_answer_mode:

answer_mode
===========

Indicates how answers are returned from the solver\ [#]_. Supported values are,

*   ``raw``: Answers returned individually in the order they were read from the
    solver. Use this setting if the returned time sequences are an important
    part of the solution data.

    The answer contains two fields, *solutions* and *energies*. The *solutions*
    field is a list of lists; the inner lists all have length
    :ref:`property_qpu_num_qubits` and entries from :math:`{-1, +1}` for Ising
    problems or :math:`{0, 1}` for QUBO problems. Values of :math:`3` denote
    unused or inactive qubits. The *energies* field contains the energy of each
    corresponding solution.

*   ``histogram``: Answers returned as a histogram sorted in order of
    increasing energies. Answers contain the *solutions* and *energies* fields,
    but solutions are unique and sorted in increasing-energy order. Duplicate
    answers are merged and include a *num_occurrences* field, which indicates
    how many times each solution appeared.

.. [#]
    Ocean tools receive these answers from SAPI and process them. For example,
    if you submit a problem using Ocean software's
    :class:`~dwave.system.composites.EmbeddingComposite` class, the answer is
    mapped from qubits to the logical variables of your problem.

Default value is ``histogram``.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_initial_state` (which sets the anneal schedule to a
    reverse anneal) returns answers in ``raw`` mode unless you explicitly set
    the answer mode to ``histogram``.
*   :ref:`parameter_qpu_max_answers` specifies the maximum number of answers.
*   :ref:`parameter_qpu_num_reads` defines the number of reads.

Example
-------

This illustrative example sets the answer format to ``raw``.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> J = {('s1', 's2'): 0.5, ('s1', 's3'): 0.5, ('s2', 's3'): 0.5}
>>> sampleset = EmbeddingComposite(DWaveSampler()).sample_ising(
...     {}, J, num_reads=100, answer_mode='raw')


.. _parameter_qpu_auto_scale:

auto_scale
==========

Indicates whether :math:`h` and :math:`J` values are rescaled:

*   ``True``: :math:`h` and :math:`J` values in the problem are rescaled
    to use as much of the range of :math:`h` (:ref:`property_qpu_h_range`) and
    the range of extended :math:`J` (:ref:`property_qpu_extended_j_range`) as
    possible; furthermore, the :math:`h` and :math:`J` values need not lie
    within the solver's range of :math:`h` and extended :math:`J`, but must
    still be finite.

*   ``False``: :math:`h` and :math:`J` values in the problem are used as is. If
    the :math:`h` and :math:`J` values are outside the ranges of :math:`h`
    (:ref:`property_qpu_h_range`) and the extended :math:`J`
    (:ref:`property_qpu_extended_j_range`) of the solver, problem submission
    fails.

By default, this parameter is enabled.

Auto-scaling works as follows. Each QPU has an allowed range of values for the
biases and strengths of qubits and couplers. Unless you explicitly disable
auto-scaling, the values defined in your problem are adjusted to fit the entire
available range and the permitted per-qubit and per-group coupling ranges
specified by the :ref:`property_qpu_per_qubit_coupling_range` (for |dwave_5kq|
QPU solvers) or :ref:`property_qpu_per_group_coupling_range` (for |adv2| QPU
solvers) properties, respectively.

The auto-scaled :math:`h` and :math:`J` values are determined by dividing the
:math:`h` and :math:`J` values in the problem by a positive (non-zero) factor
defined as follows:

.. math::

    \max \bigl\{& \max \left( \frac{\max (h)}{\max (h\_range)}, 0 \right),

        & \max \left( \frac{\min (h)}{\min(h\_range)}, 0 \right),

        & \max \left( \frac{\max(J)}{\max(extended\_J\_range)}, 0 \right),

        & \max \left( \frac{\min(J)}{\min(extended\_J\_range)}, 0 \right),

        & coupling\_limit\bigr\}

The `coupling_limit` element takes into consideration the
:ref:`property_qpu_per_qubit_coupling_range` (for |dwave_5kq| QPU solvers) and
:ref:`property_qpu_per_group_coupling_range` (for |adv2| QPU solvers) properties
as follows:

*   |dwave_5kq| QPU solvers

    .. math::

        coupling\_limit = \max \bigl\{& \max \left(
            \frac{\max (total\_J\_per\_qubit)}{\max (per\_qubit\_coupling\_range)},
            0 \right),

            & \max \left(
                \frac{\min (total\_J\_per\_qubit)}{\min (per\_qubit\_coupling\_range)},
                0 \right) \bigr\}

*   |adv2| QPU solvers

    .. math::

        coupling\_limit = \max \bigl\{& \max \left(
            \frac{\max (total\_J\_per\_group)}{\max (per\_group\_coupling\_range)},
            0 \right),

            & \max \left(
                \frac{\min (total\_J\_per\_group)}{\min (per\_group\_coupling\_range)},
                0 \right) \bigr\}

where the `total_J_per_qubit` and `total_J_per_group` elements represent the
total and per-group total, respectively, of the coupling strength applied to
each qubit.

Ocean software's samplers often have a *chain strength* parameter: because the
QPU's qubits are sparsely connected, problem variables might be represented by
more than one physical qubit (a "chain" of qubits), strongly coupled so as to
return the same value. Typically, chains are generated by minor-embedding tools
such as the :ref:`minorminer <index_minorminer>`

.. todo:: verify the link to minorminer above works

package. Setting a value for chain strength determines the values set for the
couplers used in forming these chains. When using auto-scaling, the :math:`J`
values of chain couplers are scaled together with the given or converted
:math:`J` values. Similarly, if you disable auto-scaling, any chain strength you
specify must result in coupling values within the allowed range for the QPU.

Problems specified in QUBO form are always converted to Ising for the submitted
QMIs. When using auto-scaling, the converted problem's :math:`h` and :math:`J`
values are rescaled as described above. Note that bias values in the converted
form, which have a dependency on the number of quadratic interactions in the
QUBO, can be larger than the maximum bias of the original form. For example,
the four-variable QUBO below, which has a maximum bias value of 2,

.. math::

    \begin{bmatrix} 2 & 2 & 1.5 & 2 \\ 0 & 1.5 & 0 & 0
    \\ 0 & 0 & -0.5 & 0 \\ 0 & 0 & 0 & -1.0
    \end{bmatrix}

when converted to an Ising model, has a bias with a value greater than 2.0,
:math:`h_1=2.375`, as shown below:

>>> import dimod
...
>>> Q = {(1, 1): 2, (2, 2): 1.5, (3, 3): -0.5, (4, 4): -1.0,
...      (1, 2): 2, (1, 3): 1.5, (1, 4): 2}
>>> dimod.qubo_to_ising(Q)
({1: 2.375, 2: 1.25, 3: 0.125, 4: 0.0}, {(1, 2): 0.5, (1, 3): 0.375, (1, 4): 0.5}, 2.375)

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_auto_scale` cannot be used with
    :ref:`parameter_qpu_flux_biases`.

Example
-------

The example checks a QPU's range of :math:`h` and :math:`J` before submitting a
two-variable Ising problem to a QPU. The :ref:`parameter_qpu_auto_scale`
parameter is implicitly `True` for the
:class:`~dwave.system.samplers.DWaveSampler` class, so the :math:`h` and
:math:`J` values are automatically rescaled by :math:`\frac{-7.2}{-4} = 1.8`.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())
...
>>> sampler.child.properties['extended_j_range']
[-2.0, 1.0]
>>> sampler.child.properties['h_range']
[-4.0, 4.0]
>>> h = {'a': -7.2, 'b': 2.3}
>>> J = {('a', 'b'): 1.5}
>>> sampleset = sampler.sample_ising(h, J)


.. _parameter_qpu_bqm:

bqm
===

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_bqm
    :end-before: end_parameter_bqm

For QPU solvers, Ocean software converts to Ising format and submits linear
and quadratic biases.

Example
-------

This example creates a BQM from a QUBO and submits it to a QPU.

>>> import dimod
>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> Q = {(0, 0): -3, (1, 1): -1, (0, 1): 2, (2, 2): -1, (0, 2): 2}
>>> bqm = dimod.BQM.from_qubo(Q)
>>> sampleset = EmbeddingComposite(DWaveSampler()).sample(bqm, num_reads=100)


.. _parameter_qpu_fast_anneal:

fast_anneal
============

When set to ``True``, the :ref:`fast-anneal protocol <qpu_annealprotocol_fast>`
is used instead of the standard anneal.

By default, standard anneal is used (``fast_anneal=False``).

Relevant Properties
-------------------

*   :ref:`property_qpu_fast_anneal_time_range` defines the supported range of
    valid times when using the fast-anneal protocol.

Interacts with Parameters
-------------------------

*   |meet_run_duration|
*   :ref:`parameter_qpu_h` values and :ref:`parameter_qpu_q` diagonal values
    must be zero when ``fast_anneal=True`` (likewise, you cannot configure the
    :ref:`parameter_qpu_h_gain_schedule` parameter).
*   :ref:`parameter_qpu_anneal_schedule` cannot specify more than two points when
    ``fast_anneal=True`` (which means you also cannot use annealing features
    such as pause or reverse anneal).

Example
-------

This example samples a ferromagnetic chain for an anneal time of 8 ns.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> qpu_advantage2 = DWaveSampler(
...     solver={"topology__type": "zephyr"})   # doctest: +SKIP
>>> sampler = EmbeddingComposite(qpu_advantage2)    # doctest: +SKIP
>>> h = 0
>>> J = {(i, i + 1): -1.5 for i in range(20)}
>>> sampleset = sampler.sample_ising(
...     h, J, num_reads=1000,
...     fast_anneal=True, annealing_time=0.008)     # doctest: +SKIP


.. _parameter_qpu_flux_biases:

flux_biases
===========

List of flux-bias offset values, in units of :math:`\Phi_0`, with which to
refine calibration.

Ideally, qubits with :math:`h_i=0` should have equal probability of annealing
to classical states :math:`+1` or :math:`-1` until coupled to a biased qubit.
However, non-idealities in QPU calibration and coupling to its environment
result in some asymmetry. This asymmetry typically increases under strong
coupling (such as when the :ref:`property_qpu_extended_j_range` is used) for
chains. While the effect may be minor for many optimization problems, for
others, such as material simulation, it may be significant. Flux biases can be
used to refine the standard calibration as described in :ref:`qpu_error_fix_fbo`
section.

Flux biases are also useful as a way of biasing qubits indirectly when you
cannot set a bias on the qubit, as in the case of
:ref:`fast anneal <qpu_annealprotocol_fast>`.

Provide an array of flux-bias offset values for all qubits, working or not. Use
0 for no offset. Note that by convention the sign for flux biases is opposite
to that for linear biases :ref:`parameter_qpu_h`. Ocean software provides tools
for conversions between equivalent values of :ref:`parameter_qpu_h` and
flux-bias offsets: :func:`~dwave.system.temperatures.fluxbias_to_h` and
:func:`~dwave.system.temperatures.h_to_fluxbias`.

Default is no flux-bias offsets.

The applied flux bias appears in Hamiltonian equation
:math:numref:`qpu_equation_rfsquid_hamiltonian` of the :ref:`qpu_annealing`
section as a term :math:`I_p \phi_{\rm flux bias} \sigma_z` that grows with the
applied problem energy as :math:`\sqrt{B(s)}`.
Although the dynamics of :ref:`parameter_qpu_h` and flux bias (constant in
time) differ, equivalence at a specific point in the anneal is valid under some
assumptions. :ref:`Ocean software <index_ocean_sdk>` provides
:std:doc:`conversion functions <system_utilities>` between
:ref:`parameter_qpu_h` and flux biases.

See :ref:`this example <qpu_config_emulate_with_fbo>` in the
:ref:`qpu_solver_configuration` section for more-detailed usage information.

Relevant Properties
-------------------

*   :ref:`property_qpu_extended_j_range` defines the extended range of values
    possible for the coupling strengths.
*   :ref:`property_qpu_per_qubit_coupling_range` defines the coupling range
    permitted per qubit for |dwave_5kq| QPU solvers.
*   :ref:`property_qpu_per_group_coupling_range` defines the coupling range
    permitted per group of qubits for |adv2| QPU solvers.
*   :ref:`parameter_qpu_flux_drift_compensation` indicates whether the
    |dwave_short| system compensates for flux drift.

Interacts with Parameters
-------------------------

*   Cannot be used with :ref:`parameter_qpu_auto_scale`.

Example
-------

This example sets flux-bias values for a two-qubit chain in an illustrative
Ising problem.

>>> from dwave.system import FixedEmbeddingComposite, DWaveSampler
...
>>> qpu = DWaveSampler(solver={'topology__type': 'pegasus'})
>>> h = {0: 0, 1: 0.9, 2: -1}
>>> J = {(0, 1): -1, (1, 2): -1}
>>> embedding = {0: [30], 1: [45, 46], 2: [31]}
>>> fb = [0]*qpu.properties['num_qubits']
>>> fb[45] = -0.00005
>>> fb[46] = -0.00005
>>> sampleset = FixedEmbeddingComposite(qpu, embedding).sample_ising(
...     h, J, num_reads=8000, flux_biases=fb)   # doctest: +SKIP
>>> print(f"{sampleset.record.energy}\n{sampleset.record.num_occurrences}")   # doctest: +SKIP
[-2.1 -1.9 -1.9  0.1  0.1]
[ 720 3047 4230    2    1]
>>> fb[45] = +0.00005
>>> fb[46] = +0.00005
>>> sampleset = FixedEmbeddingComposite(qpu, embedding).sample_ising(
...     h, J, num_reads=8000, flux_biases=fb)   # doctest: +SKIP
>>> print(f"{sampleset.record.energy}\n{sampleset.record.num_occurrences}")   # doctest: +SKIP
[-2.1 -1.9 -1.9 -0.1  0.1  0.1]
[3461 2546 1987    2    1    3]

The |dwave_short| system used for this example is an |dwave_5kq| QPU that has
particular couplers. Select a suitable embedding for the QPU you run examples
on.


.. _parameter_qpu_flux_drift_compensation:

flux_drift_compensation
=======================

Boolean flag indicating whether the |dwave_short| system compensates for flux
drift. The procedure it follows to do so is described in detail in the
:ref:`qpu_error_fix_drift` subsection of the :ref:`qpu_errors` section.

* ``flux_drift_compensation=True``: Compensate for flux drift.
* ``flux_drift_compensation=False``: Do not compensate for flux drift.

Default is to compensate for flux drift.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_flux_biases` enables you to apply flux-bias offsets
    manually, which you may want to do if you disable this parameter.

Example
-------

This example disables flux-drift compensation.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> J = {('s1', 's2'): 0.5, ('s1', 's3'): 0.5, ('s2', 's3'): 0.5}
>>> sampleset = sampler.sample_ising({}, J, num_reads=100,
...                                  flux_drift_compensation=False)


.. _parameter_qpu_h:

h
=

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_h
    :end-before: end_parameter_h

.. note::
    For QPU solvers, the programming cycle programs the solver to the specified
    :math:`h` and :math:`J` values for a given Ising problem (or derived from
    the specified :math:`Q` values of a given QUBO problem). However, since QPU
    precision is limited, the :math:`h` and :math:`J` values realized on the
    solver may deviate slightly from the requested (or derived) values. For more
    information, see the :ref:`qpu_errors` section.

Relevant Properties
-------------------

*   :ref:`property_qpu_h_range` defines the supported :math:`h` range for QPU
    solvers.
*   :ref:`property_qpu_qubits` and :ref:`property_qpu_couplers` define the working
    graph of QPU solvers.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_auto_scale` enables you to submit problems to QPU
    solvers with values outside :ref:`property_qpu_h_range` and
    :ref:`property_qpu_extended_j_range` and have the system automatically scale
    them to fit.
*   :ref:`parameter_qpu_fast_anneal` cannot be used with :ref:`parameter_qpu_h`
    values that are not zero.

Example
-------

This example sets random linear and quadratic biases on all qubits.

>>> import random
>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> h = {n: random.randint(-1, 1) for n in sampler.nodelist}
>>> J = {e: random.choices([-1, 1])[0] for e in sampler.edgelist}
>>> sampleset = sampler.sample_ising(h, J, num_reads=10)


.. _parameter_qpu_h_gain_schedule:

h_gain_schedule
===============

Sets a time-dependent gain for linear coefficients (qubit biases, see the
:ref:`parameter_qpu_h` parameter) in the Hamiltonian.

This parameter enables you to specify the :math:`g(t)` function in the
Hamiltonian,

.. math::
    :nowrap:

    \begin{equation}
        {\cal H}_{ising} = - \frac{A({s})}{2}
        \left(\sum_i {\hat\sigma_{x}^{(i)}}\right)
        + \frac{B({s})}{2} \left(g(t) \sum_{i} h_i {\hat\sigma_{z}^{(i)}}
        + \sum_{i>j} J_{i,j} {\hat\sigma_{z}^{(i)}} {\hat\sigma_{z}^{(j)}}\right)
    \end{equation}

where :math:`{\hat\sigma_{x,z}^{(i)}}` are Pauli matrices operating on a qubit
:math:`q_i` and :math:`h_i` and :math:`J_{i,j}` are the qubit biases and
coupling strengths.

This time-dependent gain, :math:`g(t)`, is specified, similarly to the
:ref:`parameter_qpu_anneal_schedule` parameter, by a series of pairs of
floating-point numbers identifying points in the schedule at which to change
the gain applied to :ref:`parameter_qpu_h`. The first element in the pair is
time, :math:`t` in microseconds |anneal_time_parameter_granularity|; the second,
the unitless :math:`g` in the range :ref:`property_qpu_h_gain_schedule_range`.
The resulting time-dependent gain is the piecewise-linear curve that connects
the provided points over the same range of times as the
:ref:`parameter_qpu_anneal_schedule`.

The following rules apply to the set of gain points provided:

*   Time :math:`t`, in microseconds, must increase for all points in the
    schedule.
*   The first point of time must be zero, :math:`t=0.0`.
*   The last point of time must match the last time in the
    :ref:`parameter_qpu_anneal_schedule` or the
    :ref:`parameter_qpu_annealing_time`.
*   The number of points must be :math:`\geq 2`.
*   The steepest slope of any curve segment,
    :math:`\frac{g_i - g_{i-1}}{t_i - t_{i-1}}`, must be within the bounds
    supported by the selected QPU.\ [#]_  Note that the I/O system that delivers
    the :ref:`parameter_qpu_h`-controlling waveform---the :math:`\Phi^x_i(s)`
    term of equation :math:numref:`qpu_equation_rfsquid_hamiltonian` in the
    :ref:`qpu_annealing` section---to a QPU limits bandwidth using a low-pass
    filter with a cutoff frequency of 3 MHz for |dwave_5kq| systems and 30 MHz
    for |adv2| systems; if you configure a too-rapidly changing curve, even
    within the supported bounds, expect distorted values of
    :ref:`parameter_qpu_h` for your problem.

.. [#]
    To see the supported slope for a particular QPU, submit a test problem with
    slopes that are expected to violate any limitations; you can then read the
    range of supported slopes in the returned error message. (Your account in
    the Leap service is not charged for rejected problems.)

    Supported slopes are typically under :math:`\frac{G_{max} - G_{min}}{0.02}`,
    where :math:`G_{min}` and :math:`G_{max}` here stand for the range limits
    of the time-dependent gain for the QPU. For example, for a QPU with
    :ref:`property_qpu_h_gain_schedule_range` value of :code:`[-3, 3]`, a slope
    above :math:`\frac{3 - (-3)}{0.02} = 300`, which occurs for a schedule that
    contains :code:`[... [10.0, 0], [10.01, 3], ...]`, is likely to return an
    error message with the maximum allowed slope.

Default :math:`g(t)`, when left unspecified, is 1, which can be explicitly coded
as

.. code-block:: py

    h_gain_schedule=[[0,1],[t_final,1]]

where `t_final` is the requested annealing time.

Relevant Properties
-------------------

*   :ref:`property_qpu_h_gain_schedule_range` defines the range of the
    time-dependent gain values permitted for the solver.

    .. note::
        In conjunction with the :ref:`parameter_qpu_auto_scale` parameter, the
        :ref:`parameter_qpu_h_gain_schedule` parameter enables you to extend
        the range of your submitted problem's linear coefficients
        (:ref:`parameter_qpu_h`) beyond the advertised
        :ref:`property_qpu_h_range`. Such use is not recommended for standard
        problem solving: the QPU is calibrated for linearity only within the
        advertised :ref:`property_qpu_h_range` and :ref:`property_qpu_j_range`.
        Increased integrated control errors (ICE) are expected outside that
        range.

        If you configure :code:`auto_scale=False` when using this parameter,
        ensure that :math:`\max_i(h\_gain*h_i)` and :math:`\min_i(h\_gain*h_i)`
        are within :ref:`property_qpu_h_range`.

*   :ref:`property_qpu_max_anneal_schedule_points` defines the maximum number of
    anneal-schedule points permitted.
*   :ref:`property_qpu_max_h_gain_schedule_points` defines the maximum number of
    gain changes allowed.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_h` defines the linear biases for the problem.
*   :ref:`parameter_qpu_anneal_schedule` defines the anneal schedule.
*   Cannot be used with the :ref:`fast-anneal protocol <qpu_annealprotocol_fast>`
    (activated by the :ref:`parameter_qpu_fast_anneal` parameter).

Example
-------

This illustrative example sets an h-gain schedule.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> h = {'s1': 1, 's2': 1.5, 's3': -0.75}
>>> J = {('s1', 's2'): 0.5, ('s1', 's3'): 0.5, ('s2', 's3'): 0.5}
>>> anneal_schedule = [[0.0, 0.0], [40.0, 0.4], [140.0, 0.4], [150, 1.0]]
>>> h_schedule = [[0.0, 1], [40.0, 1], [140.0, 2], [143.0, 0], [150, 0]]
>>> sampleset = sampler.sample_ising(h, J, num_reads=500,
...                                  anneal_schedule=anneal_schedule,
...                                  h_gain_schedule=h_schedule)


.. _parameter_qpu_initial_state:

initial_state
=============

Initial state to which the system is set for reverse annealing. Specifies the
initial classical state of all qubits.

Provide (*qubit*, *state*) pairs, where *qubit* is the qubit index, *i*, and
*state* is:

*   -1 or 1: Ising problems, active qubits
*   0 or 1: QUBO problems, active qubits
*   3: Unused or inactive qubits

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_anneal_schedule` defines the anneal schedule. When
    :ref:`parameter_qpu_initial_state` is provided, indicates that the requested
    anneal schedule change is a reverse anneal.
*   :ref:`parameter_qpu_answer_mode` is ``raw`` by default for reverse anneals.
*   :ref:`parameter_qpu_reinitialize_state` reinitializes for each anneal. Note
    that this impacts timing.
*   Cannot be used with the
    :ref:`fast-anneal protocol <qpu_annealprotocol_fast>` (activated by the
    :ref:`parameter_qpu_fast_anneal` parameter).

Example
-------

This illustrative example configures a reverse-anneal schedule on a random
native problem.

>>> import random
>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> J = {coupler: random.choice([-1, 1]) for coupler in qpu.edgelist}
>>> initial = {qubit: random.randint(0, 1) for qubit in qpu.nodelist}
>>> reverse_schedule = [[0.0, 1.0], [5, 0.45], [99, 0.45], [100, 1.0]]
>>> reverse_anneal_params = dict(anneal_schedule=reverse_schedule,
...                              initial_state=initial,
...                              reinitialize_state=True)
>>> sampleset = sampler.sample_ising(
...     {}, J, num_reads=1000, **reverse_anneal_params)   # doctest: +SKIP


.. _parameter_qpu_j:

J
=

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_j
    :end-before: end_parameter_j

.. note::
    For QPU solvers the programming cycle programs the solver to the specified
    :math:`h` and :math:`J` values for a given Ising problem (or derived from
    the specified :math:`Q` values of a given QUBO problem). However, since QPU
    precision is limited, the :math:`h` and :math:`J` values realized on the
    solver may deviate slightly from the requested (or derived) values. For more
    information, see the :ref:`qpu_errors` section.

Relevant Properties
-------------------

*   :ref:`property_qpu_j_range` defines the supported :math:`J` range for QPU
    solvers.
*   :ref:`property_qpu_extended_j_range` defines an extended range of values
    possible for the coupling strengths for QPU solvers.
*   :ref:`property_qpu_per_qubit_coupling_range` defines the limits on coupling
    range permitted per qubit if you use :ref:`property_qpu_extended_j_range`.
*   :ref:`property_qpu_qubits` and :ref:`property_qpu_couplers` define the
    working graph of QPU solvers.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_auto_scale` enables you to submit problems to QPU
    solvers with values outside :ref:`property_qpu_h_range` and
    :ref:`property_qpu_extended_j_range` and have the system automatically scale
    them to fit.
*   :ref:`parameter_qpu_flux_biases` compensates for biases introduced by
    strong negative couplings if you use :ref:`property_qpu_extended_j_range`.

Example
-------

This example sets random linear and quadratic biases on all qubits.

>>> import random
>>> from dwave.system import DWaveSampler
...
>>> sampler = DWaveSampler()
>>> h = {n: random.randint(-1, 1) for n in sampler.nodelist}
>>> J = {e: random.choices([-1, 1])[0] for e in sampler.edgelist}
>>> sampleset = sampler.sample_ising(h, J, num_reads=10)


.. _parameter_qpu_label:

label
=====

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_label
    :end-before: end_parameter_label

Example
-------

This example submits a simple Ising problem with a label and shows how such
labels are displayed on the dashboard.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> sampleset = sampler.sample_ising({}, {('a', 'b'): -.05},
...                                  label="Test Ising Problem 1")
>>> print(sampleset.info["problem_label"])
Test Ising Problem 1

.. figure:: ../_images/leap_problem_label.png
    :align: center
    :name: LeapProblemLabelQpu
    :alt: Problem labels on dashboard.
    :height: 200 pt
    :width: 400 pt

    Problem labels on the dashboard.


.. _parameter_qpu_max_answers:

max_answers
===========

Specifies the maximum number of answers returned from the solver. Must be an
integer greater than 0.

*   If :ref:`parameter_qpu_answer_mode` is ``histogram``: Total number of
    distinct answers. Because answers in this mode are sorted by energy, these
    are the best ``max_answers`` answers.
*   If :ref:`parameter_qpu_answer_mode` is ``raw``: Limits the returned values
    to the first :ref:`parameter_qpu_max_answers` of
    :ref:`parameter_qpu_num_reads` samples. In this mode,
    :ref:`parameter_qpu_max_answers` should never be more than
    :ref:`parameter_qpu_num_reads`.

Default value is :ref:`parameter_qpu_num_reads`.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_num_reads` defines the maximum number of requested
    answers.
*   :ref:`parameter_qpu_answer_mode` defines the answer mode.

Example
-------

This illustrative example resulted in fewer samples than the configured
:ref:`parameter_qpu_num_reads`.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> J = {('s1', 's2'): 0.5, ('s1', 's3'): 0.5, ('s2', 's3'): 0.5}
>>> sampleset = sampler.sample_ising({}, J, num_reads=1000,
...                                  max_answers=5)
>>> print(sampleset)                                     # doctest: +SKIP
  s1 s2 s3 energy num_oc. chain_.
0 +1 -1 -1   -0.5     202     0.0
1 -1 -1 +1   -0.5     132     0.0
2 +1 -1 +1   -0.5     112     0.0
3 -1 +1 -1   -0.5     248     0.0
4 -1 +1 +1   -0.5      95     0.0
['SPIN', 5 rows, 789 samples, 3 variables]


.. _parameter_qpu_num_reads:

num_reads
=========

Indicates the number of states (output solutions) to read\ [#]_ from the solver.
Must be a positive integer in the range given by the
:ref:`property_qpu_num_reads_range` solver property.

.. [#]
    Terms synonymous to *reads* are *anneals* and *samples*.

Default value is ``1``.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_max_answers` sets the maximum number of answers to be
    returned from the solver.
*   |meet_run_duration|

Example
-------

This illustrative example requests 1250 samples.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> sampleset = sampler.sample_qubo(Q, answer_mode='raw', num_reads=1250)
>>> len(sampleset)
1250


.. _parameter_qpu_num_spin_reversal_transforms:

num_spin_reversal_transforms
============================

This parameter is obsolete.

For :ref:`qpu_config_srt`, use the
:ref:`Ocean software's <index_ocean_sdk>`
:class:`~dwave.preprocessing.composites.SpinReversalTransformComposite`
composite instead.


.. _parameter_qpu_programming_thermalization:

programming_thermalization
==========================

Sets the time, in microseconds |anneal_time_parameter_granularity|, to wait
after programming the QPU for it to cool back to base temperature (i.e.,
post-programming thermalization time). Lower values accelerate solving at the
expense of solution quality. Supported values are positive floating-point
numbers. This value contributes to the total *qpu_programming_time*, which is
returned by SAPI in the :ref:`timing <qpu_sapi_qpu_timing>` structure.

Default value for a solver is given in the
:ref:`property_qpu_default_programming_thermalization` property.

Relevant Properties
-------------------

*   :ref:`property_qpu_programming_thermalization_range` defines the range of
    allowed values.

Interacts with Parameters
-------------------------

*   |meet_run_duration|

Example
-------

This illustrative example sets a value of half the supported maximum.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> pt = int(sampler.child.properties["programming_thermalization_range"][1]/2) # doctest: +SKIP
>>> sampleset = sampler.sample_qubo(Q, num_reads=10,
...                                 programming_thermalization=pt) # doctest: +SKIP


.. _parameter_qpu_q:

Q
=

.. include:: ../shared/parameters.rst
    :start-after: start_parameter_q
    :end-before: end_parameter_q

.. note:: For QPU solvers the following obtains:

    *   If a :math:`Q` value is assigned to a coupler not present, an exception
        is raised. Only entries indexed by working couplers may be nonzero.

    *   QUBO problems are converted to Ising format before they run on the
        solver. Ising format uses :math:`h` (qubit bias) and :math:`J` (coupling
        strength) to represent the problem; see also :ref:`parameter_qpu_h` and
        :ref:`parameter_qpu_j`.

    *   The programming cycle programs the solver to the specified :math:`h`
        and :math:`J` values for a given Ising problem (or derived from the
        specified :math:`Q` values of a given QUBO problem). However, since QPU
        precision is limited, the :math:`h` and :math:`J` values realized on the
        solver may deviate slightly from the requested (or derived) values. For
        more information, see the :ref:`qpu_errors` section.

Relevant Properties
-------------------

*   :ref:`property_qpu_h_range` and :ref:`property_qpu_extended_j_range` define
    the supported ranges for QPU solvers. Be aware that problems with values
    outside the supported range are, by default, scaled to fit within the
    supported range; see the :ref:`parameter_qpu_auto_scale` parameter for more
    information.
*   :ref:`property_qpu_qubits` and :ref:`property_qpu_couplers` define the
    :term:`working graph` of QPU solvers.

Interacts with Parameters
-------------------------

*   :ref:`property_qpu_extended_j_range` defines an extended range of values
    possible for the coupling strengths for QPU solvers.
*   :ref:`property_qpu_per_qubit_coupling_range` defines the limits on coupling
    range permitted per qubit if you use :ref:`property_qpu_extended_j_range`.
*   :ref:`parameter_qpu_auto_scale` enables you to submit problems to QPU
    solvers with values outside :ref:`property_qpu_h_range` and
    :ref:`property_qpu_extended_j_range` and have the system automatically
    scale them to fit.
*   :ref:`parameter_qpu_fast_anneal` cannot be used with diagonal values (linear
    coefficients, equivalent to :ref:`parameter_qpu_h` values in Ising problems)
    that are not zero.

Example
-------

This example submits a QUBO to a QPU solver.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
...
>>> Q = {(0, 0): -3, (1, 1): -1, (0, 1): 2, (2, 2): -1, (0, 2): 2}
>>> sampleset = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=100)


.. _parameter_qpu_readout_thermalization:

readout_thermalization
======================

Sets the time, in microseconds |anneal_time_parameter_granularity|, to wait
after each state is read from the QPU for it to cool back to base temperature
(i.e., post-readout thermalization time). This value contributes to the
*qpu_delay_time_per_sample* time returned by SAPI in the
:ref:`timing <qpu_sapi_qpu_timing>` structure. Supported values are positive
floating-point numbers.

Default value for a solver is given in the
:ref:`property_qpu_default_readout_thermalization` property.

Relevant Properties
-------------------

*   :ref:`property_qpu_readout_thermalization_range` defines the range of
    allowed values.

Interacts with Parameters
-------------------------

*   |meet_run_duration|

Example
-------

This illustrative example sets a value of half the supported maximum.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> rt = int(sampler.child.properties["readout_thermalization_range"][1]/2) # doctest: +SKIP
>>> sampleset = sampler.sample_qubo(Q, num_reads=10,
...                                 readout_thermalization=rt) # doctest: +SKIP


.. _parameter_qpu_reduce_intersample_correlation:

reduce_intersample_correlation
==============================

Reduces sample-to-sample correlations caused by the spin-bath polarization
effect\ [#]_ by adding a delay between reads.

.. [#]

    See the :ref:`qpu_errors_spinbath_polarization` section for more information
    on this effect.

Boolean flag indicating whether the system adds a delay.

*   ``reduce_intersample_correlation=True``: Adds delay.
*   ``reduce_intersample_correlation=False`` (default): Does not add delay.

.. important::
    Enabling this parameter drastically increases problem run times. To avoid
    exceeding the maximum problem run time configured for your system, limit the
    number of reads when using this feature. For more information on timing,
    see the :ref:`qpu_operation_timing` section.

Default is to not add delay between reads.

Example
-------

This illustrative example configures a delay between reads.

>>> from dwave.system import EmbeddingComposite, DWaveSampler
...
>>> sampler = EmbeddingComposite(DWaveSampler())
>>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
>>> sampleset = sampler.sample_qubo(Q, num_reads=10,
...                                 reduce_intersample_correlation=True)


.. _parameter_qpu_reinitialize_state:

reinitialize_state
==================

When using the reverse annealing feature, you must supply the initial state to
which the system is set; see the :ref:`parameter_qpu_initial_state` parameter.
If multiple reads are requested in a single call to the Solver API, you have
two options for the starting state of the system. These are controlled by the
:ref:`parameter_qpu_reinitialize_state` Boolean parameter:

*   ``reinitialize_state=True``: Reinitialize to the specified initial state
    for every anneal-readout cycle. Each anneal begins from the state given in
    the :ref:`parameter_qpu_initial_state` parameter. The amount of time
    required to reinitialize varies by system; see the
    :ref:`property_qpu_problem_timing_data` property for this information.
*   ``reinitialize_state=False``: Initialize only at the beginning, before the
    first anneal cycle. Each anneal (after the first) is initialized from the
    final state of the qubits after the previous cycle. Be aware that even if
    this parameter is disabled, reverse annealing adds a small amount of time
    (:math:`\approx 10 \ \mu s`) for each read.

See also :ref:`parameter_qpu_anneal_schedule`.

Default is to reinitialize to the specified initial state for every anneal in
reverse-anneal submissions.

Interacts with Parameters
-------------------------

*   :ref:`parameter_qpu_anneal_schedule` defines the anneal schedule.
*   |meet_run_duration|
*   Cannot be used with the fast-anneal protocol (activated by the
    :ref:`parameter_qpu_fast_anneal` parameter).

Example
-------

This illustrative example configures a reverse-anneal schedule on a random native
problem with each anneal initialized from the final state of the previous cycle.

>>> import random
>>> from dwave.system import DWaveSampler
...
>>> qpu = DWaveSampler()
>>> J = {coupler: random.choice([-1, 1]) for coupler in qpu.edgelist}
>>> initial = {qubit: random.randint(0, 1) for qubit in qpu.nodelist}
>>> reverse_schedule = [[0.0, 1.0], [5, 0.45], [99, 0.45], [100, 1.0]]
>>> reverse_anneal_params = dict(anneal_schedule=reverse_schedule,
...                              initial_state=initial,
...                              reinitialize_state=False)
>>> sampleset = qpu.sample_ising({}, J, num_reads=1000,
...                              **reverse_anneal_params)   # doctest: +SKIP
