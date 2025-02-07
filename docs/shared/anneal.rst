
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


.. start_schedule_rules

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
    If you want a section of the piecewise-linear curve that starts at time
    point :math:`t_4 = 30 \mu s` to increase from :math:`s_4=0.7` to
    :math:`s_5=0.8`, this example QPU supports a schedule that contains
    :math:`t_5 = 30.06 \mu s` (:code:`[... [30.0, 0.7], [30.06, 0.8], ...]`),
    which has a maximum slope of :math:`1 \frac{2}{3}`, but not one that
    contains :math:`t_5 = 30.04 \mu s`
    (:code:`[... [30.0, 0.7], [30.04, 0.8], ...]`), which has a maximum slope of
    :math:`2 \frac{1}{2}`.

    Note that the I/O system that delivers the anneal waveform---the
    :math:`\Phi_{\rm CCJJ}(s)` term of equation
    :math:numref:`qpu_equation_rfsquid_hamiltonian` in the :ref:`qpu_annealing`
    section---to a QPU limits  bandwidth with a 30 MHz low-pass filter for
    |dwave_5kq| and |adv2| systems; if you configure a too-rapidly changing
    curve, even with supported slopes, expect distorted values of
    :ref:`parameter_qpu_h` and :ref:`parameter_qpu_j` for your problem.
*   Only two points can be specified when :ref:`parameter_qpu_fast_anneal` is
    ``True``.

.. end_schedule_rules