.. start_about

Intended Audience
=================

This document is for users of the |dwave_short| quantum computer system who want
to better understand and leverage the physical implementation of the quantum
processing unit (QPU) architecture. It assumes that readers have a background in
quantum annealing and are familiar with Ising problem formulations.

Scope
=====

This document describes the physical properties of a particular calibrated QPU.
It includes a summary of its physical properties and graphed data showing the
anneal schedule and other details.

.. note:: The values provided in this document are the physical properties of a
    calibrated QPU. They are not product specifications.

Related Documentation
=====================

Use this document in conjunction with the following other documents:

*   |doc_getting_started|_\ ---Introduces the |dwave_short| system.
*   |doc_processor|_\ ---Defines terms, provides in-depth background information
    on  the |dwave_short| QPU, the quantum annealing process, ICE effects, and
    timing.
*   |doc_solver_properties|_\ ---Describes the solver properties and parameters
    that are passed to and from QPUs and other solvers via the Solver API.

.. raw:: latex

    \newpage

.. end_about


.. start_pegasus

.. TODO merge this content with the topology content and just reference it from
    QPU-specific page

The |dwave_5kq| QPU is based on a physical lattice of qubits and couplers known
as the *Pegasus*\ |tm| topology. This topology comprises a repeated structure
wherein each qubit is coupled to twelve oppositely aligned, and three similarly
aligned, qubits. A basic unit cell contains twenty-four such qubits, with each
qubit coupled to one similarly aligned qubit in the cell and two similarly
aligned qubits in adjacent cells. As a whole, the |dwave_5kq| QPU is a lattice
of :math:`16 \rm{x} 16` such tiles, denoted as a *P16* graph. The global
structure can be seen as a system of diagonally arranged K4,4 bicliques, with
couplers between oppositely aligned qubits both within and between the
diagonals. For more information on the Pegasus topology, see 
`Getting Started with D-Wave Solvers <https://docs.dwavesys.com/docs/latest/c_gs_4.html#pegasus-graph>`_.

.. figure:: ../../_images/Pegasus_qubits.*
    :name: PegasusQubits
    :height: 300 pt
    :width: 300 pt
    :align: center
    :alt: Pegasus qubits.

    A cropped view of the ideal Pegasus topology with qubits represented as
    horizontal and vertical loops. Shown here are approximately three rows of 12
    vertical qubits and three columns of 12 horizontal qubits for a total of 72
    qubits, 36 vertical and 36 horizontal. This figure shows a portion of the
    ideal topology and does not represent a particular QPU.

Each |dwave_5kq| QPU is fabricated with more than 5000 qubits and more than
35,000 couplers. Of this total, the number of devices, and the specific set of
devices, that can be made
available in the graph might change during a system cooldown and calibration
cycle. The subset of the graph available to users is the *working graph.* The
*yield* of the working graph is the percentage of working qubits that are
present.

You can retrieve the sets of active qubits (``nodelist``) and couplers
(``edgelist``) for this QPU using the Ocean tools. For more information, see
`Ocean software documentation <https://docs.ocean.dwavesys.com/en/stable/docs_system/reference/samplers.html>`_.

.. end_pegasus


.. start_hamiltonian

The following equation shows the quantum Hamiltonian that governs the annealing
process, where :math:`{\hat\sigma_{\rm {x,z}}^{(i)}}` are Pauli matrices
operating on a qubit :math:`q_i` and nonzero values of :math:`h_i` and
:math:`J_{i,j}` are limited to those available in the graph.

.. math::
    :nowrap:

    \begin{equation}
        {\cal H}_{\rm {ising}} = - \frac{A({s})}{2}
        \left(\sum_i {\hat\sigma_{\rm {x}}^{(i)}}\right) +
        \frac{B({s})}{2}
        \left(\sum_{i} h_i {\hat\sigma_{\rm {z}}^{(i)}} + \sum_{i>j} J_{i,j}
        {\hat\sigma_{\rm {z}}^{(i)}} {\hat\sigma_{\rm {z}}^{(j)}}\right)
    \end{equation}

.. end_hamiltonian


.. start_ice

ICE on :math:`h` and :math:`J` affects the user-specified problem such that the
QPU solves a slightly modified version of that problem, modeled as follows:

.. math::
    :nowrap:

    \begin{equation}
        E^{\delta}_{\rm {ising}} ({\bf s}) =
        \sum_i \left(h_i + \delta h_i(s)\right) s_i +
        \sum_{i>j} \left(J_{i,j} + \delta J_{i,j}(s)\right) s_i s_j,
    \end{equation}

where :math:`s` is the scaled time :math:`t/t_f`, and :math:`s_i` is the spin
state of qubit :math:`i`. The :math:`\delta h` and :math:`\delta J` values are
Gaussian distributed with mean :math:`\mu` and standard deviation
:math:`\sigma` that vary with :math:`s` during the anneal.

.. end_ice


.. start_ocean_properties

.. TODO make this more more generic and move to shared/notes.rst

.. note::
    In addition to the above list of physical properties, each QPU has a number
    of other properties defined in software that are accessible via the Solver
    API. For a global list of the solver properties for a QPU, and for a list of
    the permitted user parameters for each type of solver, see
    `Solver Properties and Parameters <https://docs.dwavesys.com/docs/latest/doc_solver_ref.html>`_.
    To retrieve the solver properties for a particular QPU, see the
    `Ocean software documentation <https://docs.ocean.dwavesys.com/en/stable/docs_cloud/reference/generated/dwave.cloud.client.Client.get_solver.html#dwave.cloud.client.Client.get_solver>`_ for the syntax and examples. 

.. end_ocean_properties


.. start_call_support

.. TODO make this more more generic and move to shared/notes.rst

.. note::
    Contact |support_email|_ to obtain the detailed properties of your system.

.. end_call_support