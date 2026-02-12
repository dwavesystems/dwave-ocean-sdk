
.. start_time_granularity

Time is specified in microseconds. For
:ref:`standard anneals <qpu_annealprotocol_standard>`, input times are rounded
to two decimal places (a granularity of 0.01 :math:`\mu s`); for the
:ref:`fast-anneal protocol <qpu_annealprotocol_fast>`, you can specify times to
a maximum resolution of 0.05%.\ [#]_

.. start_time_granularity_footnote

..  [#]
    The :ref:`fast-anneal protocol <qpu_annealprotocol_fast>` supports a time
    granularity of about 0.05% of the anneal time. For annealing times of about
    10 ns, the granularity is about 5 ps; for anneals of about 20 :math:`\mu s`,
    it is reduced to around 10 ns.

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

    Note that the :ref:`I/O system <qpu_ice_io>` that delivers the anneal
    waveform---the :math:`\Phi_{\rm CCJJ}(s)` term of equation
    :math:numref:`qpu_equation_rfsquid_hamiltonian` in the :ref:`qpu_annealing`
    section---to a QPU limits bandwidth; if
    you configure a too-rapidly changing curve, even with supported slopes,
    expect distorted values of :ref:`parameter_qpu_h` and :ref:`parameter_qpu_j`
    for your problem.
*   Only two points can be specified when :ref:`parameter_qpu_fast_anneal` is
    ``True``.

.. end_schedule_rules

.. start_gt_hamiltonion

.. math::
    :nowrap:

    \begin{equation}
        {\cal H}_{ising} = - \frac{A({s})}{2}
        \left(\sum_i {\hat\sigma_{x}^{(i)}}\right)
        + \frac{B({s})}{2} \left(g(t) \sum_{i} h_i {\hat\sigma_{z}^{(i)}}
        + \sum_{i>j} J_{i,j} {\hat\sigma_{z}^{(i)}} {\hat\sigma_{z}^{(j)}}\right)
    \end{equation}

.. end_gt_hamiltonion