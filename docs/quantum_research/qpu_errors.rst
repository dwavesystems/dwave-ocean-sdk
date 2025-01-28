.. _qpu_errors:

===========================
Errors and Error Correction 
===========================

* Error Sources for Problem Representation 
  (https://docs.dwavesys.com/docs/latest/c_qpu_ice.html)
  chapter of https://docs.dwavesys.com/docs/latest/doc_qpu.html
* Other Error Sources 
  (https://docs.dwavesys.com/docs/latest/c_qpu_errors.html)
  chapter of https://docs.dwavesys.com/docs/latest/doc_qpu.html
* Error-Correction Features 
  (https://docs.dwavesys.com/docs/latest/c_qpu_error_correction.html)
  chapter of https://docs.dwavesys.com/docs/latest/doc_qpu.html

Error Sources for Problem Representation
========================================

The dynamic range of :math:`h` and :math:`J` values may be limited by
*integrated control errors* (ICE). The term *ICE* refers collectively to these
sources of infidelity in problem representation. This chapter provides an
overview of ICE, describes the main sources that contribute to it, and provides
guidance on measuring its effects.

.. note:: Data given in this chapter are representative of |dwave_short|
    systems.

.. _qpu_ice_overview:

Overview of ICE
===============

Although :math:`h` and :math:`J` may be specified as double-precision floats,
some loss of fidelity occurs in implementing these values in the |dwave_short|
QPU. This fidelity loss may affect performance for some types of problems.

Specifically, instead of finding low-energy states to an optimization problem
defined by :math:`h` and :math:`J` as in equation
:math:numref:`qpu_equation_ising_objective`, the QPU solves a slightly altered
problem that can be modeled as

.. math::
    :nowrap:

    \begin{equation}
        E^{\delta}_{ising} ({\bf s})  =  \sum_{i=1}^N (h_i  + \delta  h_i  ) s_i
        +  \sum_{i=1}^N \sum_{j=i+1}^{N} (J_{i,j}  + \delta J_{i,j} )  s_i s_j,
    \end{equation}

where :math:`\delta h_i` and :math:`\delta J_{i,j}` characterize the errors in
parameters :math:`h_i` and :math:`J_{i,j}`, respectively.\ [#]_

.. [#]
    Because :math:`\delta h` and :math:`\delta J` are summed over :math:`N`,
    fidelity limitations tend to have a greater effect on performance for
    full-QPU sized problems, for a given dynamic range and distribution of
    :math:`h` and :math:`J`.

The error :math:`\delta h_i` depends on :math:`h_i` and on the values of all
incident couplers :math:`J_{i,j}` and neighbors :math:`h_j`, as well as *their*
incident couplers :math:`J_{j,k}` and next neighbors :math:`h_k`. That is, if
spin :math:`i` is connected to spin :math:`j`, and spin :math:`j` is connected
to spin :math:`k` in the topological graph, then :math:`\delta h_i` may depend,
to varying extents, on :math:`h_i, h_j, h_k`, :math:`J_{i,j}`, and
:math:`J_{j,k}`. This dependency holds when the relevant qubits and couplings
are present in the graph, irrespective of whether they are set to nonzero
values. Similarly, :math:`\delta J_{i,j}` depends on spins and couplings in the
local neighborhood of :math:`J_{i,j}`. For example, if a given problem is
specified by :math:`(h_1  = 1 ,  h_2 = 1,  J_{1,2} = -1)`, the QPU might
actually solve the problem :math:`(h_1 = 1.01, h_2 = 0.99, J_{1,2} = -1.01)`.
Changing just a single parameter in the problem could change all three error
terms, altering the problem in different ways.

The *probability distribution* of :math:`\delta h` and :math:`\delta J` is an
ensemble across a set of problem settings :math:`h` and :math:`J` and across all
:math:`i` and :math:`i,j` pairs. The :math:`\delta h` and :math:`\delta J`
values are Gaussian-distributed with mean :math:`\mu` and standard deviation
:math:`\sigma` that vary with anneal fraction :math:`s` during the anneal.\ [#]_
The QPU control system is calibrated so that there is typically a value of
:math:`s` for which :math:`\mu` is zero. This point is chosen to be somewhere
between the single qubit freezeout point described in the
:ref:`qpu_qa_freezeout` section (later in the anneal), and at the quantum
critical point of a one-dimensional Ising chain (earlier in the anneal).
Distributions with nonzero :math:`\mu` for some values of :math:`s` are
considered to be due to *systematic errors* discussed later in this chapter.
Thus, the expected deviations of :math:`h` and :math:`J` during operation are
the sum of a systematic contribution :math:`\mu` and a random component with
standard deviation :math:`\sigma.`

.. [#]
    Assumed for simplicity; distributions seen in actual results are close to
    this.

:numref:`Figure %s <gaussian_systematic_h>` and
:numref:`Figure %s <gaussian_systematic_j>` show example measurements of
:math:`\delta h` and :math:`\delta J` distributions at different fractional
times :math:`s`. See the :ref:`qpu_ice_measure_2spin` section for a description
of the measurement method.

.. figure:: ../../_images/gaussian_systematic_h.png
    :name: gaussian_systematic_h
    :alt: Two graphs showing delta h distributions estimated from best fit
        parameters to a thermal model. The left graph shows the standard
        deviation of delta h distributions at different points in the anneal
        schedule for two different values of J. Along its horizontal axis is s
        (normalized annealing time) from 0.2 to 0.9, marked in increments of
        0.1. Along its vertical axis is delta h from 0.008 to 0.026 marked in
        increments of 0.002. Two lines are plotted in the graph representing
        J=-0.7 and J=0.7. Both start at approximately s=.275 and end at
        approximately s=0.75. The line representing J=-0.7 begins approximately
        at delta h = 0.025 and takes a shallow backwards S curve downward to end
        at approximately delta h = 0.01. The line representing J=0.7 follows a
        similar trajectory, but below the other line by approximately 0.002
        delta h units. The right graph shows the mean values. Along its
        horizontal axis is s (normalized annealing time) from 0.2 to 0.9 in
        increments of 0.1. Along its vertical axis is delta h from -0.06 to 0.01
        in increments of 0.01. Two lines are plotted in the graph representing
        J=-0.7 and J=0.7. Both start at approximately s=.275 and end at
        approximately s=0.75. The line representing J=-0.7 begins approximately
        at delta h = -0.05 and takes a shallow backwards S curve upward to end
        at approximately delta h = -0.013. The line representing J=0.7 follows a
        similar trajectory, but above the other line by approximately 0.001
        delta h units.

    :math:`\delta h` distributions estimated from best-fit parameters to a
    thermal model. The left plot shows the standard deviation of the
    distribution and the right plot shows the mean. Data were taken for logical
    qubits between size 1 (larger :math:`s`) and size 5 (smaller :math:`s`) to
    get an estimate of :math:`\delta h` over a range of :math:`s`. Data shown
    are representative of |dwave_short| 2X systems.

.. figure:: ../../_images/gaussian_systematic_j.png
    :name: gaussian_systematic_j
    :alt: Two graphs showing delta J distributions estimated from best fit
        parameters to a thermal model. The left graph shows the standard
        deviation of delta J distributions at different points in the anneal
        schedule for two different values of J. Along its horizontal axis is s
        (normalized annealing time) from 0.2 to 0.9 in increments of 0.1. Along
        its vertical axis is delta J from 0.009 to 0.016 in increments of 0.001
        Two lines are plotted in the graph representing J=-0.7 and J=0.7. Both
        start at approximately s=.275 and end at approximately s=0.75. The line
        representing J=-0.7 begins approximately at delta J = 0.0135 and after
        arching up to about delta J = 0.0145 at s=0.35, slopes sharply down to
        the right to about delta J = 0.0095. The line representing J=0.7 begins
        approximately at delta J = 0.0155 and ends up close to the other line
        by the end. The right graph shows the mean values. Along its horizontal
        axis is s (normalized annealing time) from 0.2 to 0.9 in increments of
        0.1. Along its vertical axis is delta J from -0.02 to 0.03 in
        increments of 0.005. Two lines are plotted in the graph representing
        J=-0.7 and J=0.7. Both start at approximately s=.275 and end at
        approximately s=0.75. The line representing J=-0.7 begins approximately
        at delta J = 0.025 near the upper right of the chart and slopes down to
        end at approximately delta J = -0.01. In contrast, the line
        representing J=0.7 starts at approximately delta J = -0.175 in the
        lower left of the chart and ends at approximately delta J = -0.005.

    :math:`\delta J` distributions estimated from best-fit parameters to a
    thermal model. The left plot shows the standard deviation of the
    distribution and the right plot shows the mean. Data were taken for logical
    qubits between size 1 (larger :math:`s`) and size 5 (smaller :math:`s`) to
    get an estimate of :math:`\delta J` over a range of :math:`s`. Data shown
    are representative of |dwave_short| 2X systems.

.. _qpu_ice_sources:

Sources of ICE
==============

The Ising spins on the |dwave_short| QPU are intrinsically analog, controlled
through spatially local magnetic fields. The controls are a combination of the
output of DACs and other analog signals shared among groups of spins.
A calibration procedure, conducted when the QPU first comes online, determines
the mapping between Ising problem specifications :math:`h` and :math:`J`, and
the control values used during annealing.

QPU calibration is a significant part of the time required to install a
|dwave_short| system at a site. It involves a series of measurements of the QPU
and the refrigerator to obtain data used to build models that achieve the
desired Ising spin Hamiltonian.

These models identify several factors that contribute to distortions of
:math:`h` and :math:`J` due to ICE. Understanding these factors, and how to
compensate for them, can guide your choices in :math:`h` and :math:`J` when you
specify a problem. Listed below are the dominant sources of ICE. The subsections
that follow give additional details.

*   :ref:`qpu_ice_background_susceptibility` (ICE1)

    The qubits behave weakly as couplers, which leads to effective
    next-nearest-neighbor (NNN) :math:`J` interactions and a leakage of applied
    :math:`h` biases from a qubit to its neighbors.
*   :ref:`qpu_ice_flux_noise_qubits` (ICE2)

    The qubits experience low-frequency :math:`1/f`-like flux noise. This noise
    contributes an error that varies in time (that is, between runs on the QPU),
    and also varies with :math:`s`.
*   :ref:`qpu_ice_dac_quantization` (ICE3)

    The DACs that provide the specified :math:`h` and :math:`J` values have a
    finite quantization step size.
*   :ref:`qpu_ice_io` (ICE4)

    The ratio of :math:`h/J` may differ slightly for different annealing
    parameters such as :math:`t_f`.
*   :ref:`qpu_ice_error_h_scale_interqubits` (ICE5)

    Qubits cannot be made perfectly identical. As a result, individual spins may
    have slightly different magnitudes (persistent currents) and tunneling
    energies. These differences also vary with anneal fraction :math:`s`.

.. _qpu_ice_background_susceptibility:

Background Susceptibility
-------------------------

During the annealing process, every Ising spin has a coupler-like effect on its
neighbors (that is, the spins to which it is connected by couplings) that is not
captured by the problem Hamiltonian. This effect takes two main forms:

*   Spin :math:`i` induces *next-nearest neighbor* (NNN) couplings between pairs
    of its neighboring spins.
*   The applied :math:`h` bias *leaks* from spin :math:`i` to its neighboring
    spins.\ [#]_

.. [#]
    A more detailed description of how this arises from flux qubits is in
    [Har2010]_.

The strength of this *background susceptibility* effect is characterized by a
parameter :math:`\chi`.\ [#]_

.. [#]
    Use of the :math:`\chi` symbol is consistent with the usage in physics of
    :math:`\chi` to characterize the susceptibility of a magnetic system. This
    document uses a normalized :math:`\chi = M_{\rm AFM} \chi_q`, where
    :math:`M_{\rm AFM}` is the maximum available antiferromagnetic mutual
    inductance, and :math:`\chi_q = \frac{dI_p}{d\Phi_q}` is the physical qubit
    susceptibility.


.. figure:: ../../_images/three-spin-updated.png
    :name: three_spin_chain
    :alt: Three-spin chain to look at the effects of Kai. Diagram showing two
        3-qubit chains, labeled A (top chain) and B (bottom chain). A comprises
        3 qubits, labeled h1, h2, and h3. A coupler labeled J 1 2 connects h1
        and h2. A coupler labeled J 2 3 connects h2 and h3. B shows the same
        system, but with now with labels showing induced couplings and h biases
        due to qubit susceptibility, Kai.

    **a)** Three-spin system to look at the effect of :math:`\chi`. Three spins,
    red circles, labeled :math:`1, 2, 3` with local :math:`h`-biases of
    :math:`h_1, h_2, h_3`, respectively, and couplings between neighboring spins
    denoted by lines of :math:`J_{1,2}` between spin :math:`1` and spin
    :math:`2`, and :math:`J_{2,3}` between spin :math:`2` and spin :math:`3`.
    **b)** The model for the system showing induced couplings and
    :math:`h`-biases due to qubit susceptibility, :math:`\chi`.

.. figure:: ../../_images/chi_vs_s.png
    :name: chi_vs_s
    :alt: Graph showing Kai as a function of s (normalized annealing time). It
        shows how Kai typically varies with s, from around -0.04 early in the
        anneal to near -0.015 late in the anneal, at which point single-spin
        dynamics freeze out. Along its horizontal axis is s (normalized
        annealing time) from 0.2 to 0.9, in increments of 0.1. Along its
        vertical axis is Kai from -0.04 to -0.015, in increments of 0.005. One
        line is plotted in the graph; 19 points are plotted and connected by
        linear segments. The first point is in the lower left corner at
        approximately s = 0.26, Kai = -0.04; the last is in the upper right
        corner at approximately Kai = 0.78, s = -0.015.

    :math:`\chi` variation during the anneal. Data shown are representative of
    |dwave_short| 2X systems.

For example, consider the three-spin problem shown in
:numref:`Figure %s <three_spin_chain>`. This system is described by the Ising
energy function

.. math::
    :nowrap:

    \begin{equation}
        E_{3} (\vc s) = + h_1 s_1 + h_2 s_2 + h_3 s_3 +
        J_{1,2} s_1 s_2 + J_{2,3} s_2 s_3.
    \end{equation}

The energy function solved by the QPU, however, has some extra terms:

.. math::
    :nowrap:

    \begin{equation}
        E^\delta_{\chi} (\vc s) =
        \underbrace{
            + h_2 \chi J_{1,2} s_1 + h_1 \chi J_{1,2} s_2 +
            h_3 \chi J_{2,3} s_2 + h_2 \chi J_{2,3} s_3
        }_\text{$h$ leakage}
        +
        \underbrace{
            J_{1,2} \chi J_{2,3}  s_1  s_3
        }_\text{NNN coupling}.
    \end{equation}

The NNN coupling occurs because spin 1 induces an interaction between spins 1
and 3 with magnitude :math:`J_{1,2} \chi J_{2,3}`. Similarly, :math:`h_2` leaks
onto spin 1, with magnitude :math:`h_2 \chi J_{1,2}`, and so on for the other
terms.

:numref:`Figure %s <chi_vs_s>` shows how :math:`\chi` typically varies with
:math:`s`, from around -0.04 early in the anneal to near -0.015 late in the
anneal, at which point single-spin dynamics freeze out.

.. _qpu_ice_flux_noise_qubits:

Flux Noise of the Qubits
------------------------

As another component of ICE, each :math:`h_i` is subject to an independent (but
time-dependent) error term that comes from the :math:`1/f` flux noise of the
qubits.\ [#]_ There are fluctuations in the flux noise that have lower frequency
than the typical inverse annealing time, so problems solved in quick succession
have correlated contributions from flux noise. By default, flux drift is
automatically corrected every hour by the |dwave_short| system so that it is
bounded and approximately Gaussian when averaged across all times; see the
:ref:`qpu_error_fix_drift` section for the procedure. You can disable this
automatic correction by setting the :ref:`sysdocs:param_fdc` solver parameter to
``False``. If you do so, apply flux-bias offsets manually; see the
:ref:`qpu_error_fix_fbo` section.

.. [#]
    Couplers also have :math:`1/f` flux noise, but this effect is insignificant
    compared to :math:`\delta h` and :math:`\delta J`.

Because the physical source of noise is flux fluctuations on the qubits, the
*effective* level of noise is larger earlier in the anneal when the persistent
current in qubits is smaller, so that :math:`h` is relatively smaller in
physical flux units; see the :ref:`qpu_rfsquid_qubit` section and the
:ref:`qpu_characterize_flux_noise` section for details.

The Fourier spectrum of the fluctuations of :math:`\delta h^2` varies
approximately as :math:`A^2/f^\alpha`, where :math:`f` is frequency from 1 mHz
to the highest-resolvable frequency, :math:`A` is the amplitude of the
fluctuations at :math:`f = 1` Hz, and :math:`\alpha` is the spectral tilt---or
frequency dependence---of the fluctuations. Due to the flux drift compensation,
the spectrum becomes flat and close to zero below 1 mHz. Integrating the noise
from 1 mHz to 1 MHz (the relevant band of interest observable directly), the
Gaussian contribution to :math:`\delta h` is approximately 0.009 early in the
anneal and less later in the anneal.
:numref:`Figure %s <example_64q_noise_spectrum>` shows typical data for a
64-qubit system.

.. figure:: ../../_images/example_64q_noise_spectrum.png
    :name: example_64q_noise_spectrum
    :alt: Graph showing the fluctuation spectrum for a 64-qubit cluster. It
        shows the power spectral density of the signal, in effective h units,
        plotted as a function of frequency. Along its horizontal axis is
        frequency in hertz from 0.001 to 0, marked in multiples of 10. Along its
        vertical axis is spectral density in h units from 0.0001 to .01, marked
        in multiples of 10. The graph shows a scatter plot of points overlaid by
        a best-fit line. The line is a concave curve, starting in the upper left
        and descending steeply to the lower right. The majority of the plotted
        points are on the lower right.
    :scale: 60

    Power spectral density of :math:`h` fluctuations for a 64-qubit cluster.
    Data are taken by strongly coupling 64 qubits together and measuring the
    magnetization fluctuation of the system over time. The power spectral
    density of this signal, in effective :math:`h` units, is plotted as a
    function of frequency. The solid line shows a best fit to the model
    :math:`A^2/f^{\alpha} + wn`, where :math:`wn` is the statistical noise floor
    of the measurement technique and is not a measurement of any intrinsic
    broadband fluctuation of the qubit environment. See the
    :ref:`qpu_characterize_flux_noise` section for more details. Data shown are
    representative of |dwave_short| 2X systems.

.. _qpu_ice_dac_quantization:

DAC Quantization
----------------

The DACs that provide the user-specified :math:`h` and :math:`J` values have a
finite quantization step size. That step size depends on the value of the
:math:`h` or :math:`J` applied because the response to the DAC output is
nonlinear.

This random error contribution is described by a uniform distribution centered
at 0 and having errors :math:`\pm b`. Typical errors for :math:`h` and :math:`J`
are shown in :numref:`Figure %s <quantization_error>`. Note that these errors
are smaller than other contributors to ICE.

.. figure:: ../../_images/quantization_error.png
    :name: quantization_error
    :alt: Two graphs showing the boundaries of the distributions of errors in h
        and J. The left graph shows the typical quantization step for the DAC
        controlling the h parameter. Along its horizontal axis are h values
        from -2 to 2, marked in increments of 1. Along its vertical axis are the
        quantization boundaries in h units from 0 to 0.009, marked in increments
        of 0.001. A single smooth line runs in a shallow concave curve from the
        top left corner, where h = -2 and h units = 0.0082, to the bottom right
        corner, where h = 2 and h units = 0.0005. The right graph shows the
        typical quantization step for the DAC controlling the J parameter. Along
        its horizontal axis are J values from -1 to 1, marked in increments of
        0.5. Along its vertical axis are the quantization boundaries in J units
        from 0 to 0.005, marked in increments of 0.0005. A single smooth line
        runs in a shallow concave curve from the top left corner, where J = -1
        and J units = 0.0045, to the bottom right corner, where J = 1 and J
        units = 0.00025.

    Typical quantization step for the DAC controlling the :math:`h` parameter
    (left) and :math:`J` parameter (right). For example, :math:`h = 0.000` may
    be off by as much as :math:`\pm 0.008` when realized on the QPU. Over all
    qubits, you might find a worst-case qubit biased with :math:`h = 0.008`, and
    another worst-case qubit biased with :math:`h = -0.008`. Data shown are
    representative of |dwave_short| 2X systems.

.. _qpu_ice_io:

I/O System Effects
------------------

Several time-dependent analog signals are applied to the QPU during the
annealing process. Because the I/O system that delivers these signals has finite
bandwidth,\ [#]_ the waveforms must be tuned for each anneal to minimize any
potential distortion of the signals throughout the annealing process. As a
result, the ratio of :math:`h/J` may vary slightly with :math:`t_f` and with
scaled anneal fraction :math:`s`.

.. [#]
    The anneal and :ref:`param_h`-controlling
    waveforms---:math:`\Phi_{\rm CCJJ}(s)` and :math:`\Phi^x_i(s)` terms,
    respectively, of equation :math:numref:`qpu_equation_rfsquid_hamiltonian` in
    the |doc_processor|_ guide---pass through low-pass filters with the
    following cutoff frequencies:

    *   For :math:`\Phi_{\rm CCJJ}(s)`: 30 MHz on both |dwave_5kq| and |adv2_tm|
        systems
    *   For :math:`\Phi^x_i(s)`: 3 MHz for |dwave_5kq| systems and 30 MHz for
        |adv2| systems

.. _qpu_ice_error_h_scale_interqubits:

Distribution of :math:`h` Scale Across Qubits
---------------------------------------------

Assuming a fixed temperature of the system, and :math:`J=0`, the expected graph
of the relationship between user-specified :math:`h` and QPU-realized :math:`h`
has slope = 1, reflecting a constant mean offset :math:`\mu` in the distribution
of :math:`\delta h`. The measured slopes, however, are different for each spin,
and are Gaussian-distributed.

This divergence results from small variations in the physical size of each qubit
and from imperfections that arise when attempting to homogenize the macroscopic
parameters---physical inductance :math:`L`,  capacitance :math:`C`, and
Josephson junction critical current :math:`I_c`---across all physical qubits in
the QPU.

Assuming a fixed temperature for the system, the ideal relationship, or slope,
between qubit population and applied :math:`h` is identical across an ensemble
of devices. The distribution of measured slopes, however, is
Gaussian-distributed with a standard deviation of approximately 1\%, which
contributes to :math:`\delta h` and :math:`\delta J`. This distribution results
from differences in the magnitude of each spin :math:`s_i`; see the
:ref:`qpu_ice_measure_2spin` section.

.. _qpu_ice_measuring:

Measuring ICE
=============

This section describes how to measure the effects of :math:`1/f` noise as well
as how to harness effective two-spin systems to measure the effects of ICE.

.. _qpu_ice_measure_f_noise:

Measuring :math:`1/f` Noise
---------------------------

A straightforward way to look at the :math:`1/f` noise in the :math:`h`
parameter is to set all :math:`h` and :math:`J` values equal to 0 on the full
QPU and observe how resulting qubit distributions drift over time in repeated
tests. This approach identifies the effective :math:`1/f` noise error on
:math:`h` when referenced to the single qubit freezeout point :math:`s^*_q`. To
probe the :math:`1/f` noise at earlier anneal times (and to amplify the error
signal), create clusters of strongly coupled qubits and measure the
time-dependent behavior of the net magnetization of system as described in the
next section.

.. _qpu_ice_measure_2spin:

Using Two-Spin Systems to Measure ICE
-------------------------------------

You can use the results of problems defined on pairs of Ising spins scattered
over the topological graph to help to characterize ICE effects.

.. _qpu_ice_measure_2spin_simple:

Simple Two-Spin Systems
........................

The simplest version of such problems has two Ising spins with biases
:math:`h_1` and :math:`h_2` and a coupling between them of weight :math:`J`.
The energy of this system is

.. math::
    :label: qpu_2spin_equation

        E_{2spin}(\vc s) = +h_1 s_1 + h_2 s_2 + J s_1 s_2.

To measure ICE using simple two-spin systems, first find all independent edge
sets of the available graph; that is, the sets of two-spin systems that can be
manipulated independently. Simultaneously, for each set, ask the QPU to solve
the independent two-spin problems at a variety of :math:`h_1` and :math:`h_2`
settings near the phase boundaries indicated in
:numref:`Figure %s <2q_chi_diagram>`. Then fit the resulting data to a thermal
model to estimate the deviations, :math:`\delta h` and :math:`\delta J`, from
equation :math:numref:`qpu_2spin_equation` above using the correction terms of
equation :math:numref:`qpu_2spin_delta_equation` below.

The two-spin phase diagram in :numref:`Figure %s <2q_chi_diagram>` characterizes
the lowest energy state of the system as a function of :math:`h_1` and
:math:`h_2` for given :math:`J`, here set to :math:`J=-0.5`. The dashed line
delineates regions of the :math:`h_1` and :math:`h_2` space where resulting
Ising spins are indicated by the up (:math:`s = 1`) and down (:math:`s = -1`)
arrows. Applying a larger magnitude (more negative) :math:`J` value increases
ferromagnetic interactions, growing the regions of :math:`\downarrow \downarrow`
and :math:`\uparrow \uparrow` while shrinking the regions of
:math:`\downarrow \uparrow` and :math:`\uparrow \downarrow`.

The ideal diagram may be compared to one obtained assuming the existence of
background susceptibility errors. For this problem, the :math:`\chi` correction
terms are

.. math::
    :label: qpu_2spin_delta_equation

        E^\delta_{2spin} (\vc s) = +h_2 \chi J s_1  + h_1 \chi J s_2.

The :math:`h`-leakage effects are shown in :numref:`Figure %s <2q_chi_diagram>`:
the blue lines denote the boundaries of the different spin ordering regions for
the case where :math:`\chi = -0.05`, versus the ideal case shown by the dashed
lines. (The two-spin system does not have NNN effects.)

.. figure:: ../../_images/2q_chi_diagram.png
    :name: 2q_chi_diagram
    :alt: Graph showing the effect of h ICE on a 2-qubit phase diagram for
        J = -0.5. Along its horizontal axis are values for h 1 from -1 to 1,
        marked in increments of 0.5. Along its vertical axis are values for h 2
        from -1 to 1, marked in increments of 0.2. Dashed lines show the
        expected locations of the phase boundaries between the four possible
        states of the system under ideal ising spin behavior. Solid lines show
        the locations of the phase boundaries for Kai = -0.05. The expected and
        ICE effect lines are very slightly offset in places.

    Two-qubit (two Ising spin) phase diagram for :math:`J = -0.5`. The dashed
    lines show the locations of the expected phase boundaries between the four
    possible states of the system under the assumption of ideal Ising spin
    behavior. The solid lines show the locations of the phase boundaries for
    :math:`\chi = -0.05.` To estimate the Ising spin parameters without
    systematic bias, :math:`\chi` must be included in any model of the physical
    system. Data shown are representative of |dwave_short| 2X systems.

Given the form of the :math:`h`-leakage terms, applying small adjustments to the
:math:`h` biases on the original problem can compensate somewhat for this error.
However, :math:`\chi` varies during the anneal (see
:numref:`Figure %s <chi_vs_s>`), and this correction corresponds to one specific
point during the anneal. The single qubit freezeout point for typical anneal
times occurs when :math:`s \approx 0.8` and :math:`A(s)` is around 100 MHz (see
:numref:`Figure %s <annealing-functions>`). This is the last point in the anneal
where any meaningful spin-flip dynamics occur; at that point :math:`\chi` is
approximately -0.015, so that value can, in principle, compensate for
:math:`h`-leakage. A better approach, however, is to choose :math:`\chi` to
correspond to a point earlier in the anneal---at or before the crossing point of
:math:`A(s)` and :math:`B(s)`. This is the localization point of a
one-dimensional chain of spins.

.. _qpu_ice_measure_2spin_large:

Effective Two-Spin Systems For Larger Problems
..............................................

Similar measurements may be repeated for larger problems made up of *logical
spins* formed by strongly coupled groups of spins with strong intracluster
coupling weights :math:`J_{cluster}`. Pairs of clusters are connected by the
intercluster coupling weight :math:`J`, and the :math:`h_1` and :math:`h_2`
weights are assigned to all spins in each cluster. These clusters freeze out at
different anneal times depending on the number of spins and on coupling
strengths :math:`J` and :math:`J_{cluster}`, as shown in
:numref:`Figure %s <annealing_functions_5us>` and
:numref:`Figure %s <annealing_functions_100us>`. These *effective two-spin
instances* make it possible to probe ICE effects on :math:`h` and :math:`J` at
different times during the anneal.

For each logical qubit size up to 6 (corresponding to 6+6 spins) held together
with :math:`J_{\text{cluster}}=1`, ask the QPU to solve independent problems on
the full-sized graph for varying :math:`J`, :math:`h_1` and :math:`h_2`. Then
fit the measured results to a fixed-temperature model of the phase diagram for
the ideal problem---appropriately adjusted to the larger qubit counts, including
the proper :math:`\chi` contributions from the logical qubit components.

The dominant effects taken into account during the fitting to the phase diagram
model are:

*   The :math:`J` realized may vary from the :math:`J` requested. ICE effects on
    couplings characterized by :math:`\delta J` are shown in
    :numref:`Figure %s <gaussian_systematic_J>`.
*   With large-enough samples of logical two-spin problems, random
    :math:`\delta h` errors cancel out; what remains is an offset field for each
    spin.  This offset, :math:`h_{offset}`, characterizes the intrinsic flux
    offset of the logical qubit that is independent of :math:`h`.
*   The difference between specified :math:`h` and realized :math:`h` may vary
    as described in the :ref:`qpu_ice_error_h_scale_interqubits` section.
    :numref:`Figure %s <2q_misbalancing_diagram>` shows the effect of this type
    of error on the phase diagram.
*   Additional warping of the phase diagram occurs as :math:`\chi` changes from
    :math:`-0.04` to :math:`-0.015` through anneal time :math:`s`.

.. figure:: ../../_images/2q_misbalancing_diagram.png
    :name: 2q_misbalancing_diagram
    :alt: Graph showing the effect of h ICE on a 2-qubit system with spins of
        different magnitude when there is a difference between specified h and
        realized h. Along its horizontal axis are values for h 1 from -1 to 1,
        marked in increments of 0.5. Along its vertical axis are values for h 2
        from -1 to 1, marked in increments of 0.2. Dashed lines show the
        expected locations of the phase boundaries before the four possible
        states of the system under ideal ising spin behavior. Solid lines show
        the locations of the phase boundaries with a misbalancing of spin
        magnitude of 0.05. The expected and ICE effect lines are very slightly
        offset in places.

    Two-qubit (two Ising-spin) phase diagram for two spins of different
    magnitude (two qubits with different :math:`I_p`) for a sample :math:`\chi`
    value of :math:`J = -0.5`. The dashed lines show the locations of the
    expected phase boundaries between the four possible states of the system
    under the assumption of identical spin magnitudes. The solid lines show the
    locations of the phase boundaries for spin magnitudes that differ by
    :math:`0.05`. Data shown are representative of |dwave_short| 2X systems.

.. _qpu_characterize_flux_noise:

Characterizing the Effect of Flux Noise
=======================================

This section characterizes the effects of flux noise on the quantum annealing
process. The :ref:`qpu_error_correction` chapter describes the procedure that
|dwave_short| uses to correct for drift.

Let there be a flux qubit biased at degeneracy :math:`h=0` with tunneling energy
:math:`\Delta_q`. Let the qubit be subject to flux noise with noise spectral
density :math:`S_{\Phi}(f)`. If this qubit is subjected to experiments over a
time interval :math:`t_{\rm exp}`, then it is subject to a random flux bias
whose flux-flux correlator can be expressed as

.. math::
    :nowrap:

    \begin{equation}
        \left<\Phi_n(t)\Phi_n(0)\right> =
        \int_{f_{\rm min}}^{f_{\rm max}}
            df S_\Phi(f) \frac{\sin^2 2\pi f t}{(\pi f)^2}
    \end{equation}

where :math:`f_{\rm min} = 1/t_{\rm exp}` and
:math:`f_{\rm max} = \Delta_q/h`.\ [#]_

.. [#]
    The derivation of this expression follows the same logic as that for the
    phase-phase correlator given in Eq. 10c of Phys. Rev. B *67*, 094510 (2003),
    albeit with an appropriate low-frequency cutoff.

The ambiguity with quantum annealing is in defining the appropriate choice of
:math:`\Delta_q`, since this quantity is swept during an experiment. The value
of :math:`\Delta_q` should be the point in the anneal at which a given qubit
localizes. For a single isolated qubit, the appropriate value of
:math:`\Delta_q` is on the order of the inverse decoherence time
:math:`1/T_2^*`, where :math:`T_2^*` is a function of :math:`\Delta_q`. Thus,
:math:`\Delta_q` becomes that of the coherent-incoherent crossover. For a system
of coupled qubits, localization can occur at much larger values of
:math:`\Delta_q`. In this case, the coupled qubit system can undergo a phase
transition earlier in the anneal where the qubits are coherent. |dwave_short|
QPUs realize these phase transitions at :math:`\Delta_q/h \sim 2` GHz.

For example, the calculation of the fractional error in the dimensionless
1-local bias :math:`h_i` proceeds as follows. Typical qubits experience
low-frequency flux noise characterized by a noise spectral density of the form

.. math::
    :nowrap:

    \begin{equation}
        S_\Phi(f) = \frac{A}{f^\alpha}
    \end{equation}

with amplitude such that
:math:`{\sqrt S_\Phi ({\rm 1 Hz}) \sim 2 \mu\Phi_0/\sqrt{\rm Hz}}` and exponent
:math:`0.75 \leq \alpha < 1`. Given that the uncertainty in :math:`\alpha` is
large and a lack of experimental evidence that the form given above is valid up
to frequencies of order :math:`\Delta_q/h \sim 2` GHz, :math:`\alpha = 1` is
used in these calculations. Integrating this equation from
:math:`f_{\rm min} = 1` mHz to :math:`f_{\rm max} = 2` GHz yields an integrated
flux noise

.. math::
    :nowrap:

    \begin{equation}
        \delta \Phi_n = \sqrt{\int_{f_{\rm min}}^{f_{\rm max}} df S_\Phi(f)}
        \approx 10\ \mu\Phi_0.
    \end{equation}

A qubit with :math:`\Delta_q/h = 2` GHz also possesses a persistent current
:math:`|I_p| \approx 0.8` :math:`\mu`\ A. The maximum achievable
antiferromagnetic coupling between a pair of qubits is
:math:`M_{\rm AFM} \approx 2  \ {\rm pH}`. Thus, the scale of :math:`h` is set
by

.. math::
    :nowrap:

    \begin{equation}
        \Phi_h \equiv M_{\rm AFM} |I_p| \approx 0.8 \ {\rm m} \Phi_0.
    \end{equation}

The relative error in the dimensionless parameter :math:`h_i` is then

.. math::
    :nowrap:

    \begin{equation}
        \delta h_i \equiv \frac{\delta \Phi_n}{\Phi_h} \approx 0.01.
    \end{equation}

.. _qpu_ice_example_effects_quality:

Example of ICE Effects on Solution Quality
============================================

As discussed in the :ref:`qpu_ice_sources` section, the distributions
:math:`\delta h` and :math:`\delta J` depend on annealing time :math:`t_f` and
vary with anneal fraction :math:`s` during the anneal. Because :math:`\delta h`
and :math:`\delta J` may vary with :math:`s` (as well as with any errors in the
ratio :math:`h/J`), ICE can drive a system across a phase boundary---whether a
quantum phase transition or a later classical phase transition.

Consider a simple two-spin problem with biases :math:`h_1 = h_2 = 0.01` and
:math:`J = -0.5`. You can expect to see spins :math:`\downarrow \downarrow`
(that is, :math:`s_1, s_2 = -1`) in the problem solution. If :math:`\delta h` is
such that the QPU sees :math:`h_1, h_2 = -0.01` early in the anneal, the system
localizes in the :math:`\uparrow \uparrow` state. Perhaps later, the effective
ICE signal becomes smaller and the system crosses a phase boundary to prefer
:math:`\downarrow \downarrow`.  Depending on when this happens in relation to
freezeout time, the system may or may not be able to respond:

*   If :math:`\delta h` changes early enough in the anneal, the system can
    respond and provide the correct answer.
*   If :math:`\delta h` occurs too late, the early ICE is effectively locked in
    and both spins remain up.

This example shows that there are two components to ICE: the final error on the
classical Ising spin system defined by equation
:math:numref:`qpu_equation_ising_objective`, and the rest of the error
contributing to a variation in the anneal path on the way to the final classical
Hamiltonian. Depending on problem details, either of these effects may
dominate---exchanging roles earlier, later, or at multiple times in the anneal.

Other Error Sources
===================

As well as the ICE effects discussed at length in the :ref:`qpu_ice_ranges`
chapter, a number of other factors may affect system performance, including
temperature, high-energy photon flux, readout fidelity, programming errors, and
spin-bath polarization. This chapter looks at each of these in turn. For
guidance on how to work around some of these factors to get improved
performance, see the |doc_cookbook|_ guide.

.. _qpu_errors_temperature:

Temperature
===========

In a formal sense, temperature is defined for a system in thermodynamic
equilibrium. In a practical sense, however, if the equilibrium time of a given
subsystem is very short compared to the relaxation time between subsystems, then
that subsystem may not be in thermal equilibrium with other subsystems capable
of exchanging energy.

For example, the superconducting QPU and the block of metal attached to both it
and a separate low-temperature thermometer have distinct temperatures. The
thermometer measures the temperature of the dilution refrigerator's mixing
chamber; however, this may be a couple of millikelvin colder than the QPU.
Furthermore, there is a distinction between the temperature of the
quasiparticles in a superconducting wiring layer of the QPU and its phonons, and
between the phonons of the wiring layer and those of the silicon substrate.

For timescales over which the annealing algorithm operates, the qubits are
considered to be in equilibrium with a thermal bath at an effective temperature
that can be measured, for example, by looking at the equilibrium distribution of
single, uncoupled qubits when held in a fixed longitudinal and transverse field.
(See :numref:`Figure %s <annealing-functions>` and [Joh2011]_, Supplemental
Information, section II.D page 8.)

Ensuring that a QPU operates at millikelvin-scale temperatures requires
minimizing the amount of energy deposited on the QPU, as well as ensuring that
energy is efficiently removed from it. Nevertheless, some heat is dissipated on
the QPU during normal operation, particularly during the programming cycle. This
can, depending on the frequency of programming, increase the effective
temperature of the qubits and therefore affect solution quality.

Temperature effects vary from QPU to QPU, and depend on a number of
manufacturing-related details. In practice, the effects can be quantified by
performing the aforementioned equilibrium distribution tests when no programming
is being performed and again when programming is done at maximum frequency, and
then comparing the values.\ [#]_

.. [#]
    This corresponds to a case where many problems, each requesting only a small
    number of reads, are queued to run on the QPU.

.. include:: ../shared/qpu_specific_specs.rst
    :start-after: start_call_support
    :end-before: end_call_support

As a simple illustration of the effect of thermal equilibration, consider a
single-qubit problem. As shown in :numref:`Figure %s <annealing_functions_5us>`,
you find that single qubits freeze out at an :math:`s` value of roughly
:math:`0.7`. At that point, :math:`B(s)`---for the particular QPU shown---is
approximately 7 GHz. Before this freezeout point, you can assume that the single
qubits are in thermal equilibrium at some temperature :math:`T` after which no
further dynamics are present. At :math:`s = 0.7`, an applied :math:`h` of
:math:`1.0` to the single qubit results in an energy difference between the up
and down states of 7 GHz. The expected distribution for the spin up population
is: :math:`P_{\uparrow} / 1-P_{\uparrow} = e^{-\delta E / k_b T}`.

Because :math:`\delta E = B(s) h`, you can sweep :math:`h` over a small range
and fit the result to a hyperbolic tangent and extract the resulting :math:`T`
of the QPU. :numref:`Figure %s <single-qubit-temp>` shows the results of a
measurement where you sweep the :math:`h` values on all the qubits on a QPU,
shift the curves to have the same centers, and then fit the averaged data to a
hyperbolic tangent to extract the effective temperature of the qubits.

As a consequence, even when the temperature of the mixing chamber is constant,
the effective temperature of the qubits may vary by a few millikelvin, depending
on usage.

.. figure:: ../../_images/single-qubit-temperature-extraction.png
    :name: single-qubit-temp
    :width: 80 %
    :alt: Graph showing single qubit temperature extraction.

    Single qubit temperature extraction: Sampling the trivial 1-qubit problem,
    :math:`H = -h_i s_i` on the QPU for qubit :math:`i` (averaged over all
    qubits after centering each data set) for several values of :math:`h_i` on
    the x-axis, results in the blue points shown in this plot. Fitting the data
    to a Boltzmann distribution gives the red curve and allows us to extract an
    effective temperature of :math:`14.2` mK for this sample data. Conversion
    from :math:`h_i` to energy bias is done by looking at the anneal schedule
    :math:`B(s)` at the single qubit freezeout point in
    :numref:`Figure %s <annealing_functions_5us>`.

.. _qpu_errors_high_energy_photon:

High-Energy Photon Flux
=======================

The presence of relatively high-energy photons also plays a role. *High-energy*,
in this context, means that photon energy and population exceed what would be
expected at equilibrium at the measured effective qubit temperature.

These photons enter the QPU from higher-temperature stages through cryogenic
filtering. When the annealing algorithm runs, they can cause transitions to much
higher-energy problem states than would be expected given the equilibrium
picture discussed in the previous section. Given a constant flux of high-energy
photons, the probability of such a transition should increase the longer the
annealing algorithm takes. This phenomenon may manifest as an appearance of
solutions with energies much higher than the expected thermal distribution. This
effect grows with longer anneal times.

.. note::
    The anneal schedule feature discussed the :ref:`qpu_qa_anneal_sched` section
    allows you to insert pauses at intermediate values of :math:`s`. Be aware
    that pausing at intermediate points in the quantum annealing process may
    increase the probability of transitions to higher energy states. As with the
    standard annealing schedule, the phenomenon may manifest as an appearance of
    solutions with energies much higher than the expected thermal distribution
    of energies and the effect grows with pause time.

.. _qpu_errors_readout_fidelity:

Readout Fidelity
================

Readout fidelity is not typically a significant factor in the |dwave_short|
quantum computer. Averaged over an ensemble of randomized bit strings, the
typical readout fidelity of the system is greater than 99%. That is, one out of
every 100 reads of a given problem may report a solution that is different from
that found by the QPU by one or more bit flips.

For guidelines on how to use multiple reads to identify readout errors and make
the best use of QPU time, see the |doc_cookbook|_ guide.

.. _qpu_errors_programming:

Programming Errors
==================

A problem that uses all available qubits and couplers has a greater than 90%
chance of being programmed without error. Occasionally, however, programming (or
reset) issues occur during the programming cycle of the QPU, moving the problem
implementation on the QPU far enough away from the intended problem that the
solutions computed by the QPU do not overlap the low-energy subspace of the
intended problem. If low-energy answers for a single problem are critical,
submit the problem at least twice.

.. note::
    Spin-reversal transforms reprogram the system and thereby offer another way
    to reduce the impact of these errors; for more information on this
    technique, see the |doc_cookbook|_ guide.

.. _qpu_errors_spinbath_polarization:

Spin-Bath Polarization Effect
=============================

One of the main sources of environmental noise affecting the qubit is magnetic
fluctuations from an ensemble of spins local to the qubit wiring. This produces
low-frequency flux noise that can cause the misspecification errors referred to
in this document as "ICE 1." In addition, the persistent current flowing in the
qubit body during the quantum annealing algorithm produces a magnetic field that
can partially align or *polarize* this ensemble of spins.

This partially polarized environment may bias the body of the qubit. This
phenomenon may manifest, for example, in measurements of single qubit transition
widths (the width of qubit population versus *h* bias). For very long anneal
times, the polarized environment may add to the external *h* bias, producing a
transition width that is narrower than the width expected from a thermal
distribution. The partially polarized environment can also produce
sample-to-sample correlations, biasing the QPU towards previously achieved spin
configurations.

To reduce these sample-to-sample correlations, enable the
:ref:`sysdocs:param_reduce_intersample` solver parameter. This setting adds
optimal delay times before each anneal, giving the spin bath time to depolarize
and thereby lose the effects from the previous read. It adds a delay that varies
(approximately) between :math:`200` microseconds and :math:`10` milliseconds,
increasing linearly with increasing length of the schedule:

.. math::
    :nowrap:

    \begin{equation}
        delay = 500 + \frac{\rm{T} (10000 - 500)}{2000}
    \end{equation}

where T is the total time of the anneal schedule.

.. important::
    Enabling this parameter drastically increases problem run times. To avoid
    exceeding the maximum problem run time configured for your system, limit the
    number of reads  when using this feature. For more information, see the
    :ref:`qpu_operation_timing` section.

The anneal schedule feature discussed in the :ref:`qpu_annealing` chapter allows
you to insert pauses at intermediate values of :math:`s`. Be aware that pausing
at intermediate points in the quantum annealing process may increase the degree
of polarization of the spin environment and thus the size of the bias back on
the body of the qubit.


Error-Correction Features
=========================

|dwave_short| quantum computers provide some features to alleviate the effects
of the errors described in previous chapters. Additionally, you can mitigate
some effects through the techniques described in the |doc_cookbook|_ guide.

.. _qpu_error_fix_drift:

Drift Correction
================

Flux noise is described and its effects characterized in the
:ref:`qpu_ice_flux_noise_qubits` and :ref:`qpu_characterize_flux_noise` sections
of the :ref:`qpu_ice_ranges` chapter.

By default, the |dwave_short| system uses the following procedure to measure and
correct for the longest drifts once an hour. You can disable the application of
any correction by setting the :ref:`sysdocs:param_fdc` solver parameter to
``False``. If you do so, you should apply flux-bias offsets manually; see the
:ref:`qpu_error_fix_fbo` section.

1.  The number of reads for a given measurement, :math:`N_\mathrm{reads}`, is
    set to 2000.
#.  A measurement of the zero-problem, with all :math:`h_i = J_{i,j} = 0` is
    performed, and the average spin computed for the :math:`i`-th qubit
    according to :math:`\left<s_i\right> = \sum_j{s_i^{(j)}}/N_\mathrm{reads}`,
    where :math:`s_i^{(j)} \in \{+1,-1\}` and the sum is performed over the
    :math:`N_\mathrm{reads}` independent anneal-read cycles.
#.  The flux offset drift of the :math:`i`-th qubit is estimated as
    :math:`\delta\Phi_i = w_i\left<s_i\right>`, where :math:`w_i` is the thermal
    transition width of qubit :math:`i`; defined below.
#.  The measured :math:`\delta\Phi_i` are corrected with an opposing on-QPU
    qubit flux--bias shift. The magnitude of the shift applied on any given
    iteration is capped to minimize problems due to (infrequent) large
    :math:`\delta\Phi_i` measurement errors.
#.  :math:`N_\mathrm{reads}` is doubled, up to a maximum of 20,000.
#.  The procedure repeats from step 2 at least 6 times. It repeats beyond 6 if
    the magnitude of any of the :math:`\delta\Phi_i` after the last iteration is
    significantly larger than the expected variation due to :math:`1/f` flux
    noise.

The thermal width, :math:`w_i`, of qubit :math:`i` is determined during QPU
calibration by measuring the isolated qubit (:math:`J_{i,j} = 0` everywhere)
average spin :math:`\left<s_i(\Phi_i^{(x)})\right>` as a function of applied
flux bias :math:`\Phi_i^{(x)}` for each qubit, and fitting to the expression
:math:`\tanh{\left[(\Phi_i^{(x)}-\Phi_i^{(0)})/w_i\right]}`, where
:math:`\Phi_i^{(0)}` and :math:`w_i` are fit parameters.

For a typical :math:`w_i` of order 100 :math:`\mu\Phi_0`, statistical error is
measured at :math:`100~\mu\Phi_0/\sqrt{20000} \simeq 1~\mu\Phi_0`. This is much
smaller than the root mean square (RMS) flux noise, which is on the order of 10
:math:`\mu\Phi_0` for the relevant time scales.

.. _qpu_extended_j_range:

Extended :math:`J` Range
========================

Ising minimization problems that the |dwave_short| system solves may require
that the model representing a problem be minor-embedded on the working graph, a
process that involves creating qubit chains to represent logical variables, as
introduced in the :ref:`minor-embedding <sysdocs:getting_started_embedding>`
chapter of the |doc_getting_started|_ guide. In an embedding, intra-chain qubit
couplings must be strong compared to the input couplings between the chains.

Most discussions of chain strength involve the ratio of two absolute values:

*   *Chain coupling strength*---Magnitude of couplings between qubits in a chain
*   *Problem scale*---Maximum magnitude of couplings among qubits (physical or
    logical) in a problem

that is,

.. math::
    :nowrap:

    \begin{equation}
        \frac{chain\_coupling\_strength}{problem\_scale}.
    \end{equation}

For example, if all of the chains have :math:`J` values of :math:`-1`, and the
rescaled\ [#]_ logical problem has :math:`J` values of :math:`- \frac{1}{4}` to
:math:`+ \frac{1}{4}`, you say that the chain strength is :math:`4`. Likewise,
if the chains have :math:`J` values of :math:`-2`, and the rescaled logical
problem has :math:`J` values of :math:`- \frac{1}{2}` to :math:`+ \frac{1}{2}`,
again you say that the chain strength is :math:`4`.

.. [#]
    See the description of the :ref:`sysdocs:param_autoscale` solver parameter
    in the |doc_solver_properties|_ guide.

Because the range of coupling strengths available is finite, chaining is
typically accomplished by setting the coupling strength to the largest allowed
negative value and scaling down the input couplings relative to that. Yet a
reduced energy scale for the input couplings may make it harder for the QPU to
find global optima for a problem.

To address this issue, some solvers support stronger chain couplings through an
:ref:`sysdocs:property_extended_j` solver property. Because embedded problems
typically have chain couplings that are at least twice as strong as the other
couplings, and standard chain couplings are all negative, this feature
effectively doubles the energy scale available for embedded problems; see
:numref:`Figure %s <extendedJ>`.

.. figure:: ../../_images/extendedJ.png
    :name: extendedJ
    :scale: 50 %
    :alt: Schematic diagram of a Chimera graph showing how qubits connect as
        described in the figure caption.

    Embedding an input that does not fit directly on a |dwave_short| QPU. The
    original problem (A) has a green vertex that is replaced by a chain of two
    vertices connected with a ferromagnetic coupling (B). With the standard
    coupling range, the embedded problem must be scaled down for the QPU, which
    can lead to decreased performance (C). However, with an extended coupling
    range, no rescaling is necessary (D).

Using the available larger negative values of :math:`J` increases the dynamic
:math:`J` range. On embedded problems, which use strong chains of qubits to
build the underlying graph, this increased range means that the problem
couplings are less affected by ICE and other effects. However, strong negative
couplings can bias a chain and therefore flux-bias offsets might be needed to
recalibrate it to compensate for this effect; see the :ref:`qpu_error_fix_fbo`
section for more information.

.. _qpu_error_fix_fbo:

Calibration Refinement
======================

In an optimal QPU calibration, annealing unbiased qubits produces spin-state
statistics that are equally split between spin-up and spin-down. When plotted
against the :math:`h` values, this even distribution results in a sigmoid curve
that passes through the point of origin (0,0). However, non-idealities in QPU
calibration and coupling to its environment result in some asymmetry. This
asymmetry typically increases under strong coupling (such as when the
:ref:`property_extended_j` is used for chains): a :math:`J`-induced bias (an
offset magnetic field that is potentially :math:`s`-dependent).\ [#]_. These
effects shift the sigmoid curve of plotted :math:`h` values from its ideal path,
as shown in :numref:`Figure %s <fb-sigmoid>`.

.. figure:: ../../_images/flux_bias_offset.png
    :name: fb-sigmoid
    :width: 80 %
    :alt: Graph showing ideal and offset h sigmoid

    Magnetization (mean spin value) of a six-qubit chain on an |adv2_tm|
    QPU as a function of applied per-qubit flux-bias offset. A sigmoid function
    (:math:`\tanh()`, the dashed line) fit to the measurements intersects the
    horizontal grid line slightly above the zero.

.. [#]

    This offset occurs because of the higher susceptibility of the tunable
    coupler [Har2009]_.

While the effect may be minor for many optimization problems, for others, such
as material simulation, it may be significant. You can compensate by refining
the calibration, applying per-qubit :ref:`param_flux_biases` to nudge the
plotted :math:`h` sigmoid to its ideal position.

Flux biases can be used to refine the standard calibration. [Che2023]_ describes
(and links to code) techniques that tune the Hamiltonian to reduce the
differences between the symmetric ideal and the asymmetric measurements on the
QPU.

.. note::
    The applied flux bias is constant in time (and :math:`s`), but it appears in
    the Hamiltonian shown in equation
    :math:numref:`qpu_equation_rfsquid_hamiltonian` as a term
    :math:`I_p \phi_{\rm flux bias} \sigma_z`---the applied energy grows as
    :math:`\sqrt{B(s)}`. An applied flux bias is different from an applied
    :math:`h`; do not use one to correct an error in the other.

.. _qpu_error_fix_virtualgraph:

Virtual Graphs
==============

.. include:: ../shared/notes.rst
    :start-after: start_virtual_graph_deprecation
    :end-before: end_virtual_graph_deprecatio

The |dwave_short| *virtual graph* feature (see the
:class:`~oceandocs:dwave.system.composites.virtual_graph.VirtualGraphComposite`
class) simplifies the process of minor-embedding by enabling you to more easily
create, optimize, use, and reuse an embedding for a given working graph. When
you submit an embedding and specify a chain strength using these tools, they
automatically calibrate the qubits in a chain to compensate for the effects of
biases that may be introduced as a result of strong couplings. For more
information on virtual graphs, see
*Virtual Graphs for High-Performance Embedded Topologies*, |dwave_short| White
Paper Series, no. 14-1020A, 2017. This and other white papers are available from
https://www.dwavesys.com/resources/publications.

Virtual graphs make use of :ref:`qpu_extended_j_range` and
:ref:`qpu_error_fix_fbo` features. These controls allow chains to behave more
like physical qubits on the working graph, thereby improving the performance of
embedded sampling and optimization problems.

.. note::
    Despite the similarity in name, the virtual graphs feature is unrelated to
    |dwave_short|'s virtual full-yield chip (VFYC) solver.

Whether virtual graph features are available may vary by solver; check for the
:ref:`sysdocs:property_extended_j` property to see if it is present and what the
range is. (The :ref:`sysdocs:property_j_range` property is unchanged.) When
using an extended :math:`J` range, be aware that there are additional limits on
the total coupling per qubit: the sum of the :math:`J` values for each qubit
must be in the range specified by the :ref:`sysdocs:property_pqcr` solver
property.

Flux-biases are set through the :ref:`sysdocs:param_flux_biases` parameter,
which takes a list of doubles (floating-point numbers) of length equal to the
number of working qubits. Flux-bias units are :math:`\Phi_0`; typical values
needed are :math:`< 10^{-4} \ \Phi_0`. Maximum allowed values are typically
:math:`> 10^{-2} \ \Phi_0`. The minimum step size is smaller than the typical
levels of intrinsic :math:`1/f` noise; see the
:ref:`qpu_characterize_flux_noise` section.

.. note::
    By default, the |dwave_short| system automatically compensates for flux
    drift as described in the :ref:`qpu_characterize_flux_noise` section. If you
    choose to disable this behavior, you should apply flux-bias offsets manually
    through the :ref:`sysdocs:param_flux_biases` parameter.

Be aware of the following points when using virtual graph features:

*   Autoscaling is not supported with flux-bias offsets. When you use this
    feature, autoscaling is automatically disabled by default, unlike in the
    usual system behavior.
*   The :math:`J` value of every coupler must fall within the range advertised
    by the :ref:`sysdocs:property_extended_j` property.
*   The sum of all the :math:`J` values of the couplers connected to a qubit
    must fall within the :ref:`sysdocs:property_pqcr` property. For example, if
    this property is ``[-9.0 6.0]``, the following :math:`J` values for a
    six-coupler qubit are permissible:

    .. math::

        1, 1, 1, 1, 1, 1,

    where the sum is :math:`6`, and also

    .. math::

        1, 1, 1, -2, -2, -2,

    where the sum is :math:`-3`. However, the following values, when summed,
    exceed the range and therefore are impermissible:

    .. math::

        -2, -2, -2, -2, -2, -2.

*   While the extended :math:`J` range in principle allows you to create almost
    arbitrarily long chains without breakage, the maximum chain length where
    embedded problems work well is expected to be in the range of 5 to 7 qubits.
*   When embedding logical qubits using the extended :math:`J` range, limit the
    degree, :math:`D`, of each node in the logical qubit tree to

    .. math::
        :nowrap:

        \begin{equation}
        \begin{array}{rcl}
            D &=& {\rm floor} \bigg[ 
            \frac{\min(per\_qubit\_coupling\_range)}{\min(extended\_j\_range)
            - \min(j\_range)} \\
            & & -\frac{num\_couplers\_per\_qubit  \times \min(j\_range)}
                {\min(extended\_j\_range) - \min(j\_range)} \bigg]
        \end{array}
        \end{equation}

    where :math:`num\_couplers\_per\_qubit = 5` for the |dwave_5kq_tm| QPU; see
    the :ref:`QPU Architecture <sysdocs:getting_started_topologies>` section of
    the |doc_getting_started|_ guide.



