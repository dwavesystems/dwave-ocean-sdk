.. start_property_category_hybrid

Type of solver.

*   ``hybrid``: Quantum-classical hybrid; typically one or more classical
    algorithms run on the problem while outsourcing to a quantum processing unit
    (:term:`QPU`) parts of the problem where it benefits most.

.. end_property_category_hybrid


.. start_property_maximum_number_of_biases

Maximum number of biases, both linear and quadratic in total, accepted by the
solver.

.. end_property_maximum_number_of_biases


.. start_property_maximum_number_of_variables

Maximum number of problem variables accepted by the solver.

.. end_property_maximum_number_of_variables


.. start_property_maximum_time_limit_hrs

Maximum allowed run time, in hours, that can be specified for the solver.

.. end_property_maximum_time_limit_hrs


.. |minimum_time_limit| replace:: dummy

.. start_property_minimum_time_limit

Minimum required run time, in seconds, the solver must be allowed to work on the
given problem. Specifies the minimum time as a piecewise-linear curve defined by
a set of floating-point pairs.
The second element is the minimum required time; the first element in each pair
is some measure of the problem, dependent on the solver: |minimum_time_limit|

The minimum time for any particular problem is a linear interpolation calculated
on two pairs that represent the relevant range for the given measure of the
problem. For example, if ``minimum_time_limit`` for a hybrid BQM
solver were ``[[1, 0.1], [100, 10.0], [1000, 20.0]]``, then the minimum time
for a 50-variable problem would be 5 seconds, the linear interpolation of the
first two pairs that represent problems with between 1 to 100 variables.

For more details, see `Ocean software's <index_ocean_sdk>`
:ref:`samplers <system_samplers>` section for solver methods that calculate this
parameter, and their descriptions.

.. end_property_minimum_time_limit


.. start_property_parameters

List of the parameters supported for the solver.

.. end_property_parameters


.. start_property_quota_conversion_rate

Rate at which user or project quota is consumed for the solver as a ratio
to QPU solver usage. Different solver types may consume quota at different
rates.

Time is deducted from your quota according to:

.. math::

    \frac{num\_seconds}{quota\_conversion\_rate}

See the :ref:`leap_hybrid_usage_charges` section for more information.

.. end_property_quota_conversion_rate


.. start_property_supported_problem_types

Indicates what problem types are supported for the solver.

.. end_property_supported_problem_types


.. start_property_version

Version number of the solver.

.. end_property_version
