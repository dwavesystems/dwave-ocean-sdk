.. start_anneal_schedule_rules

The following rules apply to the set of anneal-schedule points provided:

*   Time :math:`t` must increase for all points in the schedule.
*   For forward annealing, the first point must be :math:`(0, 0)`.
*   For reverse annealing, the anneal fraction :math:`s` must start and end at
    :math:`s = 1`.
*   In the final point, anneal fraction :math:`s` must equal 1 and time 
    :math:`t` must not exceed the maximum value in the
    :ref:`property_qpu_annealing_time_range` property.
*   The number of points must be :math:`\geq 2`.
*   The upper bound on the number of points is system-dependent; check the
    :ref:`property_qpu_max_anneal_schedule_points` property. For reverse
    annealing, the maximum number of points allowed is one *more* than the
    number given by this property.
*   The steepest slope of any curve segment,
    :math:`\frac{s_i - s_{i-1}}{t_i - t_{i-1}}` must not be greater than the 
    inverse of the minimum anneal time. For example, for a QPU with a
    :ref:`property_qpu_annealing_time_range` value of :code:`[ 0.5, 2000 ]`,
    the minimum anneal time is 0.5 :math:`\mu s`, so the steepest supported
    slope is 2 :math:`\mu s^{-1}`.
    If you want a section of the piecewise-linear curve that starts at time point
    :math:`t_4 = 30 \mu s` to increase from :math:`s_4=0.7` to :math:`s_5=0.8`,
    this example QPU supports a schedule that contains :math:`t_5 = 30.06 \mu s`
    (:code:`[... [30.0, 0.7], [30.06, 0.8], ...]`), which has a maximum slope of
    :math:`1 \frac{2}{3}`, but not one that contains :math:`t_5 = 30.04 \mu s`
    (:code:`[... [30.0, 0.7], [30.04, 0.8], ...]`), which has a maximum slope of
    :math:`2 \frac{1}{2}`.

    Note that the I/O system that delivers the anneal waveform---the
    :math:`\Phi_{\rm CCJJ}(s)` term of equation
    :math:numref:`qpu_equation_rfsquid_hamiltonian` in the |doc_processor|_
    guide---to a QPU limits  bandwidth with a 30 MHz low-pass filter for
    |dwave_5kq| and |adv2| systems; if you configure a too-rapidly changing
    curve, even with supported slopes, expect distorted values of
    :ref:`parameter_qpu_h` and :ref:`parameter_qpu_j` for your problem.
*   Only two points can be specified when :ref:`parameter_qpu_fast_anneal` is
    ``True``.

.. end_anneal_schedule_rules

.. start_parameter_bqm

Ocean software's :class:`dimod.binary.BinaryQuadraticModel` (BQM) contains 
linear and quadratic biases for problems formulated as 
:std:doc:`binary quadratic models <oceandocs:concepts/bqm>` as well as 
additional information such as variable labels and offset.

.. end_parameter_bqm


.. start_parameter_h

For :ref:`Ising <sysdocs:obj_ising>` problems, the :math:`h` values are the
linear coefficients (biases). A problem definition comprises
both :ref:`parameter_qpu_h` and :ref:`parameter_qpu_j` values.

Because the quantum annealing process minimizes the energy function of the
Hamiltonian, and :math:`h_i` is the coefficient of variable :math:`i`, returned
states of the problem's variables tend toward the opposite sign of their biases;
for example, if you bias the qubits representing variable :math:`v_i` with
:math:`h_i` values of :math:`-1`, variable :math:`v_i` is more likely to have a
final state of :math:`+1` in the solution.

For :ref:`QUBO <sysdocs:obj_qubo>` problems, use :ref:`parameter_qpu_q` instead
of :math:`h` and :math:`J`; see the |doc_getting_started|_ guide for information
on converting between the formulations.

If you are submitting directly through SAPI's REST API, see the |doc_rest_api|_
for more information.

Default is zero linear biases.

.. end_parameter_h


.. start_parameter_j

For :ref:`Ising <sysdocs:obj_ising>` problems, the :math:`J` values are the
quadratic coefficients. The larger the absolute value of :math:`J`, the stronger
the coupling between pairs of variables (and qubits on QPU solvers). An Ising
problem definition comprises both :ref:`parameter_qpu_h` and
:ref:`parameter_qpu_j` values.

Because the quantum annealing process minimizes the energy function of the
Hamiltonian, and this parameter sets the strength of the couplers between
qubits, the following obtains:

-   :math:`\textbf {J < 0}`: Ferromagnetic coupling; coupled qubits tend to be
    in the same state, :math:`(1,1)` or :math:`(-1,-1)`.
-   :math:`\textbf {J > 0}`: Antiferromagnetic coupling; coupled qubits tend to
    be in opposite states, :math:`(-1,1)` or :math:`(1,-1)`.
-   :math:`\textbf {J = 0}`: No coupling; qubit states do not affect each other.

For :ref:`QUBO <sysdocs:obj_qubo>` problems, use :ref:`parameter_qpu_q` instead of 
:math:`h` and :math:`J`; see the |doc_getting_started|_ guide for information 
on converting between the formulations.

If you are submitting directly through SAPI's REST API, see the |doc_rest_api|_ 
for more information.

Default is zero quadratic biases.

.. end_parameter_j


.. start_parameter_label

Problem label you can optionally tag submissions with.
You can set as a label a non-empty string of up to 1024 Windows-1252
characters that has meaning to you or is generated by your application, which
can help you identify your problem submission. You can see this label on the
`Leap <https://cloud.dwavesys.com/leap/>`_ service's dashboard and in solutions 
returned from SAPI.

.. end_parameter_label


.. start_parameter_q

A quadratic unconstrained binary optimization (:ref:`QUBO <sysdocs:obj_qubo>`)
problem is defined using an upper-triangular matrix, :math:`\rm \textbf{Q}`,
which is an :math:`N \times N` matrix of real coefficients, and
:math:`\textbf{x}`, a vector of binary variables. The diagonal entries of
:math:`\rm \textbf{Q}` are the linear coefficients (analogous to :math:`h`, in
Ising problems). The nonzero off-diagonal terms are the quadratic coefficients
that define the strength of the coupling between variables (analogous to
:math:`J`, in Ising problems).

Input may be full or sparse. Both upper- and lower-triangular values can be
used; (:math:`i`, :math:`j`) and (:math:`j`, :math:`i`) entries are added
together.

If you are submitting directly through SAPI's REST API, see the |doc_rest_api|_
for more information.

Default is zero linear and quadratic biases.

.. end_parameter_q


.. start_parameter_time_limit

Specifies the maximum runtime, in seconds, the solver is allowed to work on the
given problem. Can be a float or integer.

Default value is problem dependent.

.. end_parameter_time_limit


.. start_time_granularity

Time is specified in microseconds. For
:ref:`standard anneals <qpu_annealprotocol_standard>`, input times are rounded
to two decimal places (a granularity of 0.01 :math:`\mu s`); for the
:ref:`fast-anneal protocol <qpu_annealprotocol_fast>`, you can specify times to
a maximum resolution of 5%.\ [#]_

..  [#]
    For the fast-anneal protocol, if you are interested in annealing times of
    about 2 ns (``[[0.0, 0.0], [0.002, 1.0]]``), for example, specify no more
    than six decimal places for the time (a granularity of 1 ps), while for
    anneals of about 20 ns, specify no more than five decimal places (a
    granularity of 10 ps). Specifying additional decimal places is not
    meaningful.

.. end_time_granularity
