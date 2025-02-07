.. start_filter

To retrieve a subset of solver fields, create a list of the subset of solver
fields by specifying the ``filter`` parameter via the following syntax::

    filter={all|none}[,{+|-}field]... [,{+|-}field]

where:

``all``
    Initializes the list with all solver fields. This is the default.

``none``
    Initializes the list with no solver fields.

``{+|-}field``
    Adds (``+``) or removes (``-``) a solver field to or from the list. The
    fields are evaluated left to right; for example, if a field is both added
    and removed, the last action prevails. To specify the
    :ref:`solver properties <qpu_solver_properties_all>` in a solver's
    ``properties`` dict, use dot notation as follows::

        properties.property[.property]... [.property]

    For example::

        properties.problem_timing_data.typical_programming_time

If a field does not exist or a field does not contain a value, nothing is
returned for that field. The maximum size of the SAPI URL in the request is
8 KB; thus, the specified ``filter`` parameter must not extend the URL beyond
this maximum.

.. end_filter


.. start_bqm_file

The serialized file may look like this:

.. code-block::

    b'DIMODBQM\x02\x00\xb2\x00\x00\x00{"dtype": "float64", "itype": "int32",
    "ntype": "int32", "shape": [2, 1], "type": "BinaryQuadraticModel", "variables": true,
    "vartype": "BINARY"}\n                                \x00\x00\x00\x00\x00\x00
    \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00
    \x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xbf
    \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xbfVARS8\x00\x00
    \x00["x", "y"]

.. end_bqm_file


.. start_problem_resource_fields

.. tabularcolumns:: |p{4cm}|p{8cm}|

.. table:: Problem Resource Fields

    =============== ===========================
    Key             Value
    =============== ===========================
    answer          Content of the answer depends on the solver and
                    parameters used.
    id              Unique identifier of the problem. Can be used to retrieve
                    problem information, solutions, and messages.
    label           Optional user-defined string (label) for a problem.
    status          One of the problem states as defined in :ref:`lifecycle`.
                    For example, ``CANCELLED`` for cancelled problems.
    submitted_on    Time when problem was submitted.
    solved_on       If this problem is in terminal state (``COMPLETED``,
                    ``CANCELLED`` or ``FAILED``), time when problem was solved
                    or cancelled.
    type            One of the supported values for the
                    ``supported_problem_types`` property; see, for example, the
                    :ref:`property_qpu_supported_problem_types` for QPUs.
    =============== ===========================

.. end_problem_resource_fields


.. start_solver_resource_fields

.. tabularcolumns:: |p{4cm}|p{9.5cm}|

.. table:: Solver Resource Fields

    ============== ==============================
    Field          Description
    ============== ==============================
    avg_load       Average current load for the solver.
    description    Description of the solver.
    id             Unique ID (name) of the solver.
    properties     :ref:`Solver properties <qpu_solver_properties_all>`
                   that reside in the ``properties`` dict; for example,
                   supported problem types, active qubits, active couplers,
                   total number of qubits, and so on.
    status         Status of the solver; for example, a status of
                   ``ONLINE`` is returned if it is available and ``OFFLINE``
                   if it is unavailable.
    ============== ==============================

.. end_solver_resource_fields


.. start_answer_encoding

The following table describes the ``answer`` field for a QPU solver.

.. tabularcolumns:: |p{4.5cm}|p{9.5cm}|

.. table:: ``answer`` Field and Encoding for QPU Solvers

    ================= ===========================
    Key               Value
    ================= ===========================
    format            String: ``qp``
    num_variables     Total number of variables (active or otherwise) that the
                      solver has. JSON integer.
    solutions         Base-64--encoded string of bit-packed solutions (with
                      0 = -1 for Ising problems).  Bits are in little-endian
                      order. Each solution is padded to end on a byte boundary
                      and contains values for active qubits only. Ordered by the
                      values of ``energies``.
    energies          Base-64--encoded string of energies, each a little-endian
                      8-byte floating-point number (doubles). Ordered from low
                      to high.
    active_variables  Base-64--encoded string of the indices of the problem's
                      active variables. The indices are 4-byte little-endian
                      integers.
    num_occurrences   Base-64--encoded string of the number of occurrences of
                      each solution when :ref:`parameter_qpu_answer_mode` is
                      ``histogram``. The numbers are 4-byte little-endian
                      integers. Ordered by the values of ``energies``.
    timing            Solver-specific JSON object reporting the time that the
                      solver took to handle the problem.
    ================= ===========================

.. end_answer_encoding


.. start_answer_bq

.. in the future this might become a table but current use of REST API does not
    justify high-maintenance content

For quantum-classical hybrid solvers, the ``answer`` field differs. For
example, ``format`` might be ``bq`` and fields might include the type of
variables (e.g., ``INTEGER``), version, etc.

.. end_answer_bq


.. start_timeout

You can customize polling by adding the optional ``timeout`` parameter to
specify the blocking time, in seconds, for this request. Supported values are
integers between 1 to 30.

.. end_timeout