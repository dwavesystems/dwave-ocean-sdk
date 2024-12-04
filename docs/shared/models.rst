.. |models_variables_table| replace:: dummy

.. start_model_variables_table

.. list-table:: |models_variables_table|
    :header-rows: 1

    *   -   **Model**
        -   **Variables**
        -   **Ocean Class & Sampler**
    *   -   **Constrained:**
        -
        -
    *   -   :ref:`concept_models_cqm`
        -   Binary, integer, real
        -   :class:`~dimod.ConstrainedQuadraticModel`,
            :class:`~dwave.system.samplers.LeapHybridCQMSampler`
    *   -   :ref:`concept_models_nonlinear` 
        -   Binary, integer
        -   :class:`~dwave.optimization.model.Model`,
            :class:`~dwave.system.samplers.LeapHybridNLSampler`
    *   -   **Unconstrained:**
        -
        -
    *   -   :ref:`concept_models_ising`
        -   Spin
        -   :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`,
            :class:`~dwave.system.samplers.DWaveSampler`
    *   -   :ref:`concept_models_qubo`
        -   Binary
        -   :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`,
            :class:`~dwave.system.samplers.DWaveSampler`
    *   -   :ref:`concept_models_bqm`
        -   Binary, spin
        -   :class:`~dimod.binary.binary_quadratic_model.BinaryQuadraticModel`,
            :class:`~dwave.system.samplers.LeapHybridSampler`, :class:`~dwave.system.samplers.DWaveSampler`
    *   -   :ref:`concept_models_dqm`
        -   Binary, discrete
        -   :class:`~dimod.DiscreteQuadraticModel`,
            :class:`~dwave.system.samplers.LeapHybridDQMSampler`

.. end_model_variables_table

