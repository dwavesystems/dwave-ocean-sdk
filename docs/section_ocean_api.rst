.. _section_ocean_api:

=========
Ocean API
=========

Ocean software is a suite of tools `D-Wave Systems <https://www.dwavesys.com>`_ provides
on the `D-Wave GitHub repository <https://github.com/dwavesystems>`_ for solving hard
problems with quantum computers.

.. toctree::
    :hidden:
    :maxdepth: 2

    getting_started
    concepts/index
    docs_cli
    packages
    contributing
    licenses

.. sections-start-marker

.. tab-set::

    .. tab-item:: Explore

        .. grid:: 3
            :gutter: 3

            .. grid-item-card:: :ref:`Annealing Model of Quantum Computing <getting_started_qa>` 
         
                Quantum annealing processors naturally return low-energy 
                solutions; some applications require the real minimum energy 
                (optimization problems) and others require good low-energy 
                samples (probabilistic sampling problems). 
                :ref:`... <getting_started_qa>` 

            .. grid-item-card::  :ref:`Gate Model of Quantum Computing <index_gate>`  
                        
                Ocean's :code:`dwave-gate` is a software package for constructing, 
                modifying and running quantum circuits on the included simulator.
         
            .. grid-item-card:: :ref:`Installing Ocean <gs_initial_setup>` 

                Installation is **not needed** if you are using an IDE that 
                implements `"devcontainers" <https://containers.dev/supporting>`_.
                :ref:`... <gs_initial_setup>`

                Run D-Wave's many `open-source examples <https://github.com/dwave-examples>`_
                in GitHub Codespaces with just a mouse click (requires a 
                `Leap <https://cloud.dwavesys.com/leap>`_ account).

            .. grid-item-card:: :ref:`Hybrid solvers <using_hybrid>` 
                        
                :ref:`Leap’s quantum-classical  hybrid solvers <doc_leap_hybrid>` 
                solve arbitrary application problems. (Try this open-source 
                `3D bin-packing example <https://github.com/dwave-examples/3d-bin-packing>`_.) 
                
                Ocean also provides a Python framework,
                :ref:`dwave-hybrid <index_hybrid>`, for building hybrid 
                asynchronous decomposition samplers. 

            .. grid-item-card:: `Leap <https://cloud.dwavesys.com/leap>`_ 
            
                Sign up for Leap quantum cloud service, which gives you 
                immediate, secure access to D-Wave quantum and hybrid 
                solvers, as well as a wealth of information to help you get 
                started :ref:`creating quantum applications <cb_workflow>`.

            .. grid-item-card:: `System Documentation <https://docs.dwavesys.com/docs/latest/index.html>`_ 
            
                Here you will find an :ref:`introduction <doc_gsg>` 
                to D-Wave's quantum computers, their hardware and how they work;
                the :ref:`properties and parameters <doc_spp>` for 
                D-Wave's solvers; :ref:`references <doc_handbook>` on formulating 
                problems and best practices in quantum computing; and much more.

    .. tab-item:: Packages

        .. include:: packages.rst
            :start-after: packages-start-marker
            :end-before: packages-end-marker

.. sections-end-marker

:ref:`Site index <genindex>`


