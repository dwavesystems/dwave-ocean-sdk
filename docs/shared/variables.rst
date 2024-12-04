.. |variables_table| replace:: dummy

.. start_variables_table

.. list-table:: |variables_table|
    :header-rows: 1

    *   -   **Variable**
        -   **Usage**
        -   **Quadratic Model**
        -   **Nonlinear Model**
    *   -   Binary.

            :math:`v_i \in\{-1,+1\} \text{  or } \{0,1\}`.
        -   Typically used for applications that optimize over decisions that
            could either be true (or yes) or false (no); for example,

            - Should the antenna transmit or no?
            - Did a network node experience failure?
        -   :class:`~dimod.Vartype.BINARY` and :class:`~dimod.Vartype.SPIN`
        -   :class:`~dwave.optimization.symbols.BinaryVariable`
    *   -   Discrete.

            For example, a variable that can be assigned one of the values of
            the set ``{red, green, blue, yellow}``.
        -   Typically used for applications that optimize over several distinct
            options; for example,

            - Which shift should employee X work?
            - Should the state be colored red, blue, green or yellow?
        -   :class:`~dimod.Vartype.INTEGER`
        -
    *   -   Integer.
        -   Typically used for applications that optimize the number of something;
            for example,

            - How many widgets should be loaded onto the truck?
        -   :class:`~dimod.Vartype.INTEGER`
        -    :class:`~dwave.optimization.symbols.IntegerVariable`
    *   -   Real.
        -   Typically used for applications that optimize over an uncountable
            set; for example,

            - Where should the sensor be built?
        -   :class:`~dimod.Vartype.REAL`
        -

.. end_variables_table
