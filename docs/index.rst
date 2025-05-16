.. _index:

===========================
|dwave_short| Documentation
===========================

.. meta::
    :description: D-Wave documentation
    :keywords: D-Wave, d-wave documentation, d-wave manuals, quantum computing,
        quantum annealing, optimization, machine learning, sampling, ising
        model, qubo, hamiltonian, hybrid, leap, quantum applications, qubits,
        quantum computing manuals, d-wave user guides, quantum computing howto

.. toctree::
    :hidden:
    :maxdepth: 2

    industrial_optimization/index
    quantum_research/index
    ocean/index
    leap_sapi/index
    concepts/index
    licenses
    bibliography

.. tab-set::

    .. tab-item:: Industrial Optimization
        :name: tab_industrial_optimization
        :selected:

        .. include:: industrial_optimization/index.rst
            :start-after: sections-start-marker
            :end-before: sections-end-marker

    .. tab-item:: Quantum Research
        :name: tab_quantum_research

        .. include:: quantum_research/index.rst
            :start-after: sections-start-marker
            :end-before: sections-end-marker

    .. tab-item:: ML/AI
        :name: tab_ml_ai

        D-Wave's
        `PyTorch Plugin <https://github.com/dwavesystems/dwave-pytorch-plugin>`_
        provides an interface between D-Wave's quantum-classical :term:`hybrid`
        :term:`solvers <solver>` and the `PyTorch <https://pytorch.org/>`_
        framework.

        Also see the :ref:`qpu_stating_problems_machine_learning` section.

        Additional content for this topic is currently under development.


Welcome to |dwave_short|
========================

.. dropdown:: First time here? Click to learn how to navigate the documentation
    :icon: info

    Pages have three navigation bars: top, left, and right.

    *   **Left** navigation bar lets you select a subtopic; for example, how to
        get started, properties, best practices.

    *   **Right** navigation bar displays the topics on your current page.

    *   **Top** navigation bar lets you select the following sections:

        .. list-table::

                *   -   :ref:`Industrial Optimization <index_industrial_optimization>`
                    -   Solving hard commercial optimization problems using
                        :term:`hybrid` :term:`solvers <solver>`.
                *   -   :ref:`Quantum Research <index_quantum_research>`
                    -   Using the quantum processing unit (QPU) directly on
                        :term:`Ising` problems and :term:`QUBO` models.
                *   -   :ref:`Ocean SDK <index_ocean_sdk>`
                    -   Reference documentation for  the software development
                        kit (SDK) used with quantum computers.
                *   -   :ref:`index_leap_sapi`
                    -   Quantum cloud service's account management, release
                        notes, IDE support, etc.
                *   -   :ref:`Concepts <index_concepts>`
                    -   Learn the relevant terminology and the fundamental
                        concepts. **Search for terms here.**
                *   -   **More** > :ref:`Licenses <licenses>`
                    -   Licensing information for the documentation and SDK.
                *   -   **More** > :ref:`Bibliography <bibliography>`
                    -   Cited content.

*It's not a Turing machine, but a machine of a different kind.*

--- Richard Feynman, 1981

..  tab-set::

    .. tab-item:: What D-Wave Does
        :name: tab_what_dwave_does
        :selected:

        Despite the incredible power of today's supercomputers, many complex
        computing problems cannot be addressed by conventional systems. The huge
        growth of data and our need to better understand everything from the
        universe to our own DNA leads us to seek new tools that can help provide
        answers. :term:`Quantum computing <quantum computing>` is the next
        frontier in computing, providing an entirely new approach to solving the
        world's most difficult problems.

        While certainly not easy, much progress has been made in the field of
        quantum computing since 1981, when Feynman gave his famous lecture at
        the California Institute of Technology. Still a relatively young field,
        quantum computing is complex and different approaches are being pursued
        around the world. Today, there are two leading candidate architectures
        for quantum computers: gate model (also known as circuit model) and
        quantum annealing.

        :ref:`Gate-model quantum computing <qpu_gate_model_intro>`
        implements compute algorithms with quantum gates, analogously to the use
        of Boolean gates in classical computers.

        With :term:`quantum annealers <quantum annealer>` you initialize the
        system in a low-energy state and gradually introduce the parameters of a
        problem you wish to solve. The slow change makes it likely that the
        system ends in a low-energy state of the problem, which corresponds to
        an optimal solution. This technique is explained in more detail in the
        :ref:`qpu_quantum_annealing_intro` section.

        Quantum annealing is implemented in |dwave_short|'s generally available
        quantum computers, such as the |dwave_5kq_tm| system, as a single
        quantum algorithm, and this scalable approach to quantum computing has
        enabled us to create quantum processing units (:term:`QPUs <QPU>`) with
        more than 5000 quantum bits (:term:`qubits <qubit>`)---far beyond the
        state of the art for gate-model quantum computing.

        |dwave_short| has been developing various generations of our "machine of
        a different kind," to use Feynman's words, since 1999. We are the
        world's first commercial quantum computer company.

    ..  tab-item:: Quantum Computers
        :name: tab_quantum_computers

        A |dwave_short| quantum computer contains a :term:`QPU` that must be
        kept at a temperature near absolute zero and isolated from the
        surrounding environment in order to behave quantum mechanically. The
        system achieves these requirements as follows:

        *   Cryogenic temperatures, achieved using a closed-loop cryogenic
            dilution refrigerator system. The QPU generally operates at
            temperatures below 20 mK.
        *   Shielding from electromagnetic interference, achieved using a radio
            frequency (RF)-shielded enclosure and a magnetic shielding
            subsystem.

        .. figure:: ./_images/advantage2_system.png
            :name: dwave-components
            :scale: 20 %

            |adv2| quantum computer.

        The |dwave_short| QPU (:numref:`Figure %s <qpu1>`) is a lattice of tiny
        metal loops, each of which is a qubit or a coupler. Below temperatures
        of 9.2 kelvin, these loops become superconductors and exhibit
        quantum-mechanical effects.

        The QPU in |dwave_short|'s |adv2| system has more than 4,400 qubits
        and 40,000 couplers. To reach this scale, it uses over 1,000,000
        Josephson junctions.

        For details on the topology of the QPU, see the
        :ref:`qpu_topologies` section.

        .. figure:: ./_images/qpu.png
            :name: qpu1
            :scale: 30 %

            |dwave_short| QPU.

        .. note::
            |dwave_short|'s quantum computer systems are available for
            on-premises installation. For their physical specifications,
            including electrical, cooling, environmental, and networking
            requirements, download
            :download:`System Specifications for D-Wave Quantum Computers
            <downloadables/09-1313A-A_System_Specifications_for_D-Wave_Quantum_Computers.pdf>`.

            For customers who directly access quantum computer hardware, see the 
            |doc_operations| manual, which includes essential safety
            information.
            
    .. tab-item:: Software Environment
        :name: tab_dwave_software_environment

        Users interact with |dwave_short| quantum computers through a web
        user interface (UI), and through open-source tools that communicate with
        the :term:`Solver <solver>` API (SAPI).
        The SAPI components are responsible for user interaction, user
        authentication, and work scheduling. In turn, SAPI connects to back-end
        servers that send problems to and return results from QPUs and
        additional solvers, which are located in different geographical regions
        (for example, North America or Europe).\ [#]_

        See :numref:`Figure %s <network-gs>` for a simplified view of the
        |dwave_short| software environment.

        .. [#]
            Solvers are available by region.
            To view the supported regions and solvers that are available in each
            one, go to your dashboard in the
            `Leap service <https://cloud.dwavesys.com/leap/>`_.

        .. figure:: ./_images/network-gs.png
            :name: network-gs

            |dwave_short| software environment.

    .. tab-item:: Leap Service
        :name: tab_leap_quantum_cloud_service

        The Leap service is the quantum cloud service from |dwave_short|.
        Learn about the types of problems that the |dwave_short| quantum
        computer can solve, run interactive demos and coding examples on the
        system, contribute your coding ideas, and join the growing conversation
        in our community of like-minded users.

        For more information, see the :ref:`index_leap_sapi` section.

        Sign up for the Leap service here:
        `Leap service signup <https://cloud.dwavesys.com/leap>`_.

    .. tab-item:: Ocean SDK
        :name: tab_ocean_sdk

        |dwave_short|'s Python-based open-source software development kit (SDK),
        Ocean SDK, makes application development for quantum computers rapid and
        efficient and facilitates collaborative projects. See the
        :ref:`index_ocean_sdk` section for the SDK and its reference
        documentation.
