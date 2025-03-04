.. _qpu_solver_properties_specific:

=======================================
Per-QPU Solver Properties and Schedules
=======================================

The following sections provide information for advanced users who want to better
understand and leverage the physical implementation of |dwave_short|'s various
quantum processing units (QPUs) available in the Leap service\ [#]_.
This information includes:

*   Summary of a QPU's physical properties---The values provided are
    the physical properties of a calibrated QPU; they are not QPU
    specifications.

    .. note::
        In addition to the physical properties listed herein, each QPU has
        a number of other properties defined in software that are accessible via
        the Solver API. For a global list of the solver properties for a QPU,
        and for a list of the permitted user parameters for each type of solver,
        see
        `Solver Properties and Parameters <https://docs.dwavesys.com/docs/latest/doc_solver_ref.html>`_.
        To retrieve the solver properties for a particular QPU, see the
        `Ocean software documentation <https://docs.ocean.dwavesys.com/en/stable/docs_cloud/reference/generated/dwave.cloud.client.Client.get_solver.html#dwave.cloud.client.Client.get_solver>`_
        for the syntax and examples.

*   Spreadsheet for a QPU's annealing-schedule functions and normalized
    annealing-waveform values---These values are required for computing
    the energy of a problem at a specific point in a QPU's annealing process;
    as such, the spreadsheet provides the values to use for the :math:`A(s)`
    and :math:`B(s)` terms in the Hamiltonian of equation
    :eq:`2 <qpu_equation_quantum_hamiltonian>` for each value of the normalized
    anneal fraction :math:`s`, between 0 and 1 in increments of 0.001. Units for
    these terms are GHz, where the conversion from energy in Joules to Hz is
    through a division by
    `Planck's constant <https://en.wikipedia.org/wiki/Planck_constant>`_
    as follows:

    .. math::
        A(s)_{\text{[GHz]}} &= \frac{A(s)_{\text{[Joules]}}}
        {6.62607004 \times 10^{-34} \times 10^9}

        &= 1.5092 \times 10^{24} A(s)_{\text{[Joules]}}

.. [#]
        Depending on your customer contract, customer plan, and
        :ref:`seat type <admin_def_seat_type>` in a project, you may not have
        access to all QPUs in the Leap service.

Advantage2_prototype2.6
=======================

All data presented in this section are specific to the
**Advantage2_prototype2.6** solver, which is an experimental prototype of
|dwave_short|'s next-generation QPU. The |adv2_tm| prototype QPU is based on
a physical lattice of qubits and couplers known as the *Zephyr*\ |tm| topology.
For information, see the :ref:`topology_intro_zephyr` section.

Physical Properties
-------------------

This table lists the physical properties of the calibrated QPU.

.. tabularcolumns:: |l|L|

.. list-table:: QPU Physical Properties\ [#]_
    :header-rows: 1
    :widths: 3 2

    *   - Property
        - Value

    *   - Model
        - :math:`\text{Advantage2 prototype}`

    *   - Graph size
        - :math:`\text{Z6}`

    *   - Number of :ref:`qubits <property_qpu_qubits>`
        - :math:`1215`

    *   - Number of :ref:`couplers <property_qpu_couplers>`
        - :math:`10788`

    *   - Qubit temperature
        - :math:`16.5 \pm 1.0\ \text{mK}`

    *   - :math:`\rm M_{\rm AFM}`: Maximum mutual inductance for qubit pairs
        - :math:`0.443\ \text{pH}`

    *   - Quantum critical point for 1D chains
        - :math:`2.014\ \text{GHz}`

    *   - :math:`L_q`: Qubit inductance
        - :math:`107\ \text{pH}`

    *   - :math:`C_q`: Qubit capacitance
        - :math:`207\ \text{fF}`

    *   - :math:`I_c`: Qubit critical current
        - :math:`4.57\ \text{µA}`

    *   - `Average single-qubit temperature <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/generated/dwave.system.temperatures.fast_effective_temperature.html#dwave.system.temperatures.fast_effective_temperature>`_
        - :math:`0.117`

    *   - :ref:`Ferromagnetic-problem freezeout <qpu_qa_freezeout>`
        - :math:`0.009`

    *   - :ref:`Single-qubit freezeout <qpu_qa_freezeout>`
        - :math:`0.605`

    *   - :math:`\Phi_{\rm CCJJ}^i`: Initial (at :math:`s=0`) external flux on
          compound Josephson junctions
        - :math:`0.726\ \Phi_0`

    *   - :math:`\Phi_{\rm CCJJ}^f`: Final (at :math:`s=1`) external flux on
          compound Josephson junctions
        - :math:`-0.819\ \Phi_0`

    *   - Readout time range
        - :math:`17.0\ \text{to}\ 87.0\ \text{µs}`

    *   - Programming time
        - :math:`\sim 18200\ \text{µs}`

    *   - QPU-delay-time per sample
        - :math:`20.5\ \text{µs}`

    *   - Readout error rate
        - :math:`\leq 0.001`

.. [#]

Some notes for the QPU properties are as follows:

.. include:: ../shared/qpu_specific_specs.rst
    :start-after: start_qpu_adv_and_adv2_prop_notes
    :end-before: end_qpu_adv_and_adv2_prop_notes

Annealing Schedule
------------------

Download the annealing schedule for the QPU here:
:download:`Advantage2_prototype2.6 Excel spreadsheet <../downloadables/09-1302A-G_Advantage2_prototype2_6_annealing_schedule.xlsx>`.

The standard annealing schedule for the QPU is shown in
:numref:`Figure %s <annealing-schedule-adv2-proto2>`.

.. figure:: ../_images/annealing-schedule-adv2-proto2.png
    :name: annealing-schedule-adv2-proto2

    Standard annealing schedule for the QPU, showing energy changes
    as a function of scaled time.

Advantage_system7.1
===================

All data presented in this section are specific to the **Advantage_system7.1**
solver. The |dwave_5kq| QPU is based on a physical lattice of qubits and
couplers known as the *Pegasus*\ |tm| topology. For information,
see the :ref:`topology_intro_pegasus` section.

Physical Properties
-------------------

This table lists the physical properties of the calibrated QPU.

.. tabularcolumns:: |l|L|

.. list-table:: QPU Physical Properties\ [#]_
    :header-rows: 1
    :widths: 3 2

    *   - Property
        - Value

    *   - Model
        - :math:`\text{Advantage, performance update}`

    *   - Graph size
        - :math:`\text{P16}`

    *   - Number of :ref:`qubits <property_qpu_qubits>`
        - :math:`5554`

    *   - Number of :ref:`couplers <property_qpu_couplers>`
        - :math:`39238`

    *   - Qubit temperature
        - :math:`15.9 \pm 0.1\ \text{mK}`

    *   - :math:`\rm M_{\rm AFM}`: Maximum mutual inductance for qubit pairs
        - :math:`1.551\ \text{pH}`

    *   - Quantum critical point for 1D chains
        - :math:`1.277\ \text{GHz}`

    *   - :math:`L_q`: Qubit inductance
        - :math:`382\ \text{pH}`

    *   - :math:`C_q`: Qubit capacitance
        - :math:`123\ \text{fF}`

    *   - :math:`I_c`: Qubit critical current
        - :math:`1.94\ \text{µA}`

    *   - `Average single-qubit temperature <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/generated/dwave.system.temperatures.fast_effective_temperature.html#dwave.system.temperatures.fast_effective_temperature>`_
        - :math:`0.228`

    *   - :ref:`Ferromagnetic-problem freezeout <qpu_qa_freezeout>`
        - :math:`0.078`

    *   - :ref:`Single-qubit freezeout <qpu_qa_freezeout>`
        - :math:`0.620`

    *   - :math:`\Phi_{\rm CCJJ}^i`: Initial (at :math:`s=0`) external flux on
          compound Josephson junctions
        - :math:`-0.625\ \Phi_0`

    *   - :math:`\Phi_{\rm CCJJ}^f`: Final (at :math:`s=1`) external flux on
          compound Josephson junctions
        - :math:`-0.730\ \Phi_0`

    *   - Readout time range
        - :math:`17.0\ \text{to}\ 265.0\ \text{µs}`

    *   - Programming time
        - :math:`\sim 17700\ \text{µs}`

    *   - QPU-delay-time per sample
        - :math:`20.6\ \text{µs}`

    *   - Readout error rate
        - :math:`\leq 0.001`

.. [#]
    Some notes for the QPU properties are as follows:

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_only_prop_notes
        :end-before: end_qpu_adv_only_prop_notes

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_and_adv2_prop_notes
        :end-before: end_qpu_adv_and_adv2_prop_notes

Annealing Schedule
------------------

Download the annealing schedule for the QPU here:
:download:`Advantage_system7.1 Excel spreadsheet <../downloadables/09-1276A-A_Advantage_system7_1_annealing_schedule.xlsx>`.

The annealing schedule for the QPU is shown in
:numref:`Figure %s <annealing-schedule-adv7>`.

.. figure:: ../_images/annealing-schedule-adv7.png
    :name: annealing-schedule-adv7

    Annealing schedule for the QPU, showing energy changes as a function of
    scaled time.

DAC Quantization Effects
------------------------

.. ice 3

The on-QPU digital-analog converters (DACs) that provide the user-specified
:math:`h` and :math:`J` values have a finite quantization step size. That step
size depends on the value of the :math:`h` and :math:`J` applied because the
response to the DAC output is nonlinear.

:numref:`Figure %s <ip-comp-dac-quantization-adv7>` and
:numref:`Figure %s <co-dac-quantization-adv7>` show the effects of the DAC
quantization step for the DACs controlling the :math:`h` and :math:`J` values,
respectively, for this system.

.. figure:: ../_images/ip-comp-quantization-error-adv7.png
    :name: ip-comp-dac-quantization-adv7

    Typical quantization on the :math:`h` DAC control.

.. figure:: ../_images/coupler-quantization-error-adv7.png
    :name: co-dac-quantization-adv7

    Typical quantization on the :math:`J` DAC control.

Advantage_system6.4
===================

All data presented in this section are specific to the **Advantage_system6.4**
solver. The |dwave_5kq| QPU is based on a physical lattice of qubits and
couplers known as the *Pegasus*\ |tm| topology. For information,
see the :ref:`topology_intro_pegasus` section.

Physical Characteristics
------------------------

This table lists the physical properties of the calibrated QPU.

.. tabularcolumns:: |l|L|

.. list-table:: QPU Physical Properties\ [#]_
    :header-rows: 1
    :widths: 3 2

    *   - Property
        - Value

    *   - Model
        - :math:`\text{Advantage, performance update}`

    *   - Graph size
        - :math:`\text{P16}`

    *   - Number of :ref:`qubits <property_qpu_qubits>`
        - :math:`5612`

    *   - Number of :ref:`couplers <property_qpu_couplers>`
        - :math:`40088`

    *   - Qubit temperature
        - :math:`16.0 \pm 0.1\ \text{mK}`

    *   - :math:`\rm M_{\rm AFM}`: Maximum mutual inductance for qubit pairs
        - :math:`1.554\ \text{pH}`

    *   - Quantum critical point for 1D chains
        - :math:`1.281\ \text{GHz}`

    *   - :math:`L_q`: Qubit inductance
        - :math:`382\ \text{pH}`

    *   - :math:`C_q`: Qubit capacitance
        - :math:`119\ \text{fF}`

    *   - :math:`I_c`: Qubit critical current
        - :math:`1.99\ \text{µA}`

    *   - `Average single-qubit temperature <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/generated/dwave.system.temperatures.fast_effective_temperature.html#dwave.system.temperatures.fast_effective_temperature>`_
        - :math:`0.221`

    *   - :ref:`Ferromagnetic-problem freezeout <qpu_qa_freezeout>`
        - :math:`0.073`

    *   - :ref:`Single-qubit freezeout <qpu_qa_freezeout>`
        - :math:`0.616`

    *   - :math:`\Phi_{\rm CCJJ}^i`: Initial (at :math:`s=0`) external flux on
          compound Josephson junctions
        - :math:`-0.624\ \Phi_0`

    *   - :math:`\Phi_{\rm CCJJ}^f`: Final (at :math:`s=1`) external flux on
          compound Josephson junctions
        - :math:`-0.723\ \Phi_0`

    *   - Readout time range
        - :math:`18.0\ \text{to}\ 173.0\ \text{µs}`

    *   - Programming time
        - :math:`\sim 14200\ \text{µs}`

    *   - QPU-delay-time per sample
        - :math:`20.5\ \text{µs}`

    *   - Readout error rate
        - :math:`\leq 0.001`

.. [#]
    Some notes for the QPU properties are as follows:

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_only_prop_notes
        :end-before: end_qpu_adv_only_prop_notes

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_and_adv2_prop_notes
        :end-before: end_qpu_adv_and_adv2_prop_notes

Annealing Schedule
------------------

Download the annealing schedule for the QPU here:
:download:`Advantage_system6.4 Excel spreadsheet <../downloadables/09-1273A-E_Advantage_system6_4_annealing_schedule.xlsx>`.

The standard annealing schedule for this QPU is shown in
:numref:`Figure %s <annealing-schedule-adv6>`.

.. figure:: ../_images/annealing-schedule-adv6.png
    :name: annealing-schedule-adv6

    Standard annealing schedule for the QPU, showing energy changes
    as a function of scaled time.

DAC Quantization Effects
------------------------

.. ice 3

The on-QPU digital-analog converters (DACs) that provide the user-specified
:math:`h` and :math:`J` values have a finite quantization step size. That step
size depends on the value of the :math:`h` and :math:`J` applied because the
response to the DAC output is nonlinear.

:numref:`Figure %s <ip-comp-dac-quantization-adv6>` and
:numref:`Figure %s <co-dac-quantization-adv6>` show the effects of the DAC
quantization step for the DACs controlling the :math:`h` and :math:`J` values,
respectively, for this system.

.. figure:: ../_images/ip-comp-quantization-error-adv6.png
    :name: ip-comp-dac-quantization-adv6

    Typical quantization on the :math:`h` DAC control.

.. figure:: ../_images/coupler-quantization-error-adv6.png
    :name: co-dac-quantization-adv6
  
    Typical quantization on the :math:`J` DAC control.

Advantage_system5.4
===================

All data presented in this section are specific to the **Advantage_system5.4**
solver. The |dwave_5kq| QPU is based on a physical lattice of qubits and
couplers known as the *Pegasus*\ |tm| topology. For information,
see the :ref:`topology_intro_pegasus` section.

Physical Characteristics
------------------------

This table lists the physical properties of the calibrated QPU.

.. tabularcolumns:: |l|L|

.. list-table:: QPU Physical Properties\ [#]_
    :header-rows: 1
    :widths: 3 2

    *   - Property
        - Value

    *   - Model
        - :math:`\text{Advantage, performance update}`

    *   - Graph size
        - :math:`\text{P16}`

    *   - Number of :ref:`qubits <property_qpu_qubits>`
        - :math:`5614`

    *   - Number of :ref:`couplers <property_qpu_couplers>`
        - :math:`40050`

    *   - Qubit temperature
        - :math:`16.4 \pm 0.1\ \text{mK}`

    *   - :math:`\rm M_{\rm AFM}`: Maximum mutual inductance for qubit pairs
        - :math:`1.687\ \text{pH}`

    *   - Quantum critical point for 1D chains
        - :math:`1.389\ \text{GHz}`

    *   - :math:`L_q`: Qubit inductance
        - :math:`375\ \text{pH}`

    *   - :math:`C_q`: Qubit capacitance
        - :math:`117\ \text{fF}`

    *   - :math:`I_c`: Qubit critical current
        - :math:`2.10\ \text{µA}`

    *   - `Average single-qubit temperature <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/generated/dwave.system.temperatures.fast_effective_temperature.html#dwave.system.temperatures.fast_effective_temperature>`_
        - :math:`0.193`

    *   - :ref:`Ferromagnetic-problem freezeout <qpu_qa_freezeout>`
        - :math:`0.067`

    *   - :ref:`Single-qubit freezeout <qpu_qa_freezeout>`
        - :math:`0.622`

    *   - :math:`\Phi_{\rm CCJJ}^i`: Initial (at :math:`s=0`) external flux on
          compound Josephson junctions
        - :math:`-0.620\ \Phi_0`

    *   - :math:`\Phi_{\rm CCJJ}^f`: Final (at :math:`s=1`) external flux on
          compound Josephson junctions
        - :math:`-0.714\ \Phi_0`

    *   - Readout time range
        - :math:`18.0\ \text{to}\ 123.0\ \text{µs}`

    *   - Programming time
        - :math:`\sim 13300\ \text{µs}`

    *   - QPU-delay-time per sample
        - :math:`21.0\ \text{µs}`

    *   - Readout error rate
        - :math:`\leq 0.001` 

.. [#]
    Some notes for the QPU properties are as follows:

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_only_prop_notes
        :end-before: end_qpu_adv_only_prop_notes

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_and_adv2_prop_notes
        :end-before: end_qpu_adv_and_adv2_prop_notes

Annealing Schedule
------------------

Download the annealing schedule for the QPU here:
:download:`Advantage_system5.4 <../downloadables/09-1265A-E_Advantage_system5_4_annealing_schedule.xlsx>`.

The standard annealing schedule for the QPU is shown in
:numref:`Figure %s <annealing-schedule-adv5>`.

.. figure:: ../_images/annealing-schedule-adv5.png
    :name: annealing-schedule-adv5

    Standard annealing schedule for the QPU, showing energy changes
    as a function of scaled time.

DAC Quantization Effects
------------------------

.. ice 3

The on-QPU digital-analog converters (DACs) that provide the user-specified
:math:`h` and :math:`J` values have a finite quantization step size. That step
size depends on the value of the :math:`h` and :math:`J` applied because the
response to the DAC output is nonlinear.

:numref:`Figure %s <ip-comp-dac-quantization-adv5>` and
:numref:`Figure %s <co-dac-quantization-adv5>` show the effects of the DAC
quantization step for the DACs controlling the :math:`h` and :math:`J` values,
respectively, for this system.

.. figure:: ../_images/ip-comp-quantization-error-adv5.png
    :name: ip-comp-dac-quantization-adv5

    Typical quantization on the :math:`h` DAC control.

.. figure:: ../_images/coupler-quantization-error-adv5.png
    :name: co-dac-quantization-adv5

    Typical quantization on the :math:`J` DAC control.

Advantage_system4.1
===================

All data presented in this section are specific to the **Advantage_system4.1**
solver. The |dwave_5kq| QPU is based on a physical lattice of qubits and
couplers known as the *Pegasus*\ |tm| topology. For information,
see the :ref:`topology_intro_pegasus` section.

Physical Properties
-------------------

This table lists the physical properties of the calibrated QPU.

.. tabularcolumns:: |l|L|

.. list-table:: QPU Physical Properties\ [#]_
    :header-rows: 1
    :widths: 3 2

    *   - Property
        - Value

    *   - Model
        - :math:`\text{Advantage, performance update}`

    *   - Graph size
        - :math:`\text{P16}`

    *   - Number of :ref:`qubits <property_qpu_qubits>`
        - :math:`5627`

    *   - Number of :ref:`couplers <property_qpu_couplers>`
        - :math:`40279`

    *   - Qubit temperature
        - :math:`15.4 \pm 0.1\ \text{mK}`

    *   - :math:`\rm M_{\rm AFM}`: Maximum mutual inductance for qubit pairs
        - :math:`1.647\ \text{pH}`

    *   - Quantum critical point for 1D chains
        - :math:`1.391\ \text{GHz}`

    *   - :math:`L_q`: Qubit inductance
        - :math:`372\ \text{pH}`

    *   - :math:`C_q`: Qubit capacitance
        - :math:`119\ \text{fF}`

    *   - :math:`I_c`: Qubit critical current
        - :math:`2.1\ \text{µA}`

    *   - `Average single-qubit temperature <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/generated/dwave.system.temperatures.fast_effective_temperature.html#dwave.system.temperatures.fast_effective_temperature>`_
        - :math:`0.198`

    *   - :ref:`Ferromagnetic-problem freezeout <qpu_qa_freezeout>`
        - :math:`0.064`

    *   - :ref:`Single-qubit freezeout <qpu_qa_freezeout>`
        - :math:`0.612`

    *   - :math:`\Phi_{\rm CCJJ}^i`: Initial (at :math:`s=0`) external flux on
          compound Josephson junctions
        - :math:`-0.621\ \Phi_0`

    *   - :math:`\Phi_{\rm CCJJ}^f`: Final (at :math:`s=1`) external flux on
          compound Josephson junctions
        - :math:`-0.717\ \Phi_0`

    *   - Readout time range
        - :math:`17.0\ \text{to}\ 235.0\ \text{µs}`

    *   - Programming time
        - :math:`\sim 14100\ \text{µs}`

    *   - QPU-delay-time per sample
        - :math:`20.5\ \text{µs}`

    *   - Readout error rate
        - :math:`\leq 0.001`

.. [#]
    Some notes for the QPU properties are as follows:

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_only_prop_notes
        :end-before: end_qpu_adv_only_prop_notes

    .. include:: ../shared/qpu_specific_specs.rst
        :start-after: start_qpu_adv_and_adv2_prop_notes
        :end-before: end_qpu_adv_and_adv2_prop_notes

Annealing Schedule
------------------

Download the annealing schedule for the QPU here:
:download:`Advantage_system4.1 <../downloadables/09-1263A-B_Advantage_system4_1_annealing_schedule.xlsx>`.

The standard annealing schedule for this QPU is shown in
:numref:`Figure %s <annealing-schedule-adv4>`.

.. figure:: ../_images/annealing-schedule-adv4.png
    :name: annealing-schedule-adv4

    Standard annealing schedule for the QPU, showing energy changes
    as a function of scaled time.

DAC Quantization Effects
------------------------

.. ice 3

The on-QPU digital-analog converters (DACs) that provide the user-specified
:math:`h` and :math:`J` values have a finite quantization step size. That step
size depends on the value of the :math:`h` and :math:`J` applied because the
response to the DAC output is nonlinear.

:numref:`Figure %s <ip-comp-dac-quantization-adv4>` and
:numref:`Figure %s <co-dac-quantization-adv4>` show the effects of the DAC
quantization step for the DACs controlling the :math:`h` and :math:`J` values,
respectively, for this system.

.. figure:: ../_images/ip-comp-quantization-error-adv4.png
    :name: ip-comp-dac-quantization-adv4

    Typical quantization on the :math:`h` DAC control.

.. figure:: ../_images/coupler-quantization-error-adv4.png
    :name: co-dac-quantization-adv4

    Typical quantization on the :math:`J` DAC control.

