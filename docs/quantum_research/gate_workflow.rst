.. _gate_workflow:

================
Using dwave-gate
================

The |cloud|_ quantum cloud service provides access to a simulator that enables
you to test gate-model circuits intended to be executed on a dual-rail quantum
processing unit (QPU). You describe your circuits using the ``dwave-gate``
package's quantum circuit description language (QCDL), described here.

.. _QuantumCircuit: https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit

.. _qcdl_programming_basic:

QCDL: Basic
===========

QCDL is an embedded
`Domain Specific Language  <https://en.wikipedia.org/wiki/Domain-specific_language>`_
(DSL) that uses Python as the host language. If you have some experience coding
in Python, you can understand the structure of QCDL programs.


.. _qcdl_basic_entrypoint:

Program Entry Point
-------------------

You use the :class:`~dwave.gate.qcdl.qcdl`
`Python decorator <https://peps.python.org/pep-0318/>`_\ [#]_ to
mark the `entry point <https://en.wikipedia.org/wiki/Entry_point>`_ to your
QCDL circuit. This decorator converts an otherwise standard Python function into
one that generates QCDL programs when executed.

The decorator can optionally indicate the number of qubits in the program.

This example creates a `Bell state <https://en.wikipedia.org/wiki/Bell_state>`_.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import cx, h, measure

    @qcdl(2)
    def main(q0, q1):
        h(q0)
        cx(q0, q1)
        measure(q0)
        measure(q1)

    qcdl_program = main()

In the code above, the ``@qcdl`` decorator specifies that the entry point
accepts two qubits, the arguments ``q0`` and ``q1`` of ``main()``. The decorated
function ``main()`` returns a
`Pydantic model <https://pydantic.dev/docs/validation/dev/concepts/models/>`_
that you can submit to a compiler or simulator in the |cloud|_ service, as
described in the :ref:`qcdl_submitting_programs` section.

The :func:`~dwave.gate.utils.display.print_qcdl` function can visualize this structure
as readable text, and if run in a `Jupyter <https://jupyter.org/>`_ notebook,
as a display object.

.. testcode::

    from dwave.gate.utils.display import print_qcdl

    print_qcdl(qcdl_program)

The code above displays the following QCDL program.

.. testcode::
    :hide:

    print(print_qcdl(qcdl_program))

.. testoutput::
    :options: +NORMALIZE_WHITESPACE

    begin quantum
        h([q0], q0)
        cx([q0, q1], q0, q1)
        measure([q0], q0, log=True)
        measure([q1], q1, log=True)
    end quantum

If :func:`~dwave.gate.utils.display.print_qcdl` displays poorly, you can output a
string by setting the function's ``to_Display=False`` parameter.

.. [#]
    Python decorators are described in the
    `Decorators <https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators>`_
    section of the Wikipedia article on
    `Python syntax <https://en.wikipedia.org/wiki/Python_syntax_and_semantics>`_
    and multiple internet tutorials.

.. seealso::
        :func:`~dwave.gate.qcdl.qcdl` decorator

.. _qcdl_basic_gates:

Gates
-----

The gates ``dwave-gate`` supports match the method names in a Qiskit
QuantumCircuit_ (e.g., :func:`~dwave.gate.qcdl.operations.h`,
:func:`~dwave.gate.qcdl.operations.sx`, :func:`~dwave.gate.qcdl.operations.rz`,
:func:`~dwave.gate.qcdl.operations.cz`, etc).

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import h, cz

    @qcdl(2)
    def simple_gate_example(q0, q1):
        h(q0)
        cz(control_qubit=q0, target_qubit=q1)

In this example, ``cz(control_qubit=q0, target_qubit=q1)`` is similar to the
Qiskit method call ``cz(q0, q1)``.

.. note::
    For gates that take angles as an argument, ``dwave-gate`` lists qubits
    before angles, whereas Qiskit follows the reverse order.

.. not recommended practice (Amos)
    Quantum gates and operations are executed as if they were member methods of
    qubit instances; the gate operation ``h(q0)`` can also be coded as
    ``q0.h()``

.. note::
    For parameterizable gates, angles are in units of radians when passed as
    literals. When a :class:`~dwave.gate.qcdl.registers.FixedPointRegister` is
    passed as the angle for a gate, its value must be in units of π (see the
    :ref:`qcdl_basic_registers_arithmetic` section for more information).

.. _qcdl_basic_gates_barrier:

Barrier
~~~~~~~

When you submit your QCDL to a QPU in the |cloud|_ service, a transpiler
rewrites the circuit to use the QPU's supported basis gates and topology, as
described in the :ref:`qcdl_basic_transpilation` section. For most algorithms,
any implementation is acceptable but if you are studying fidelity or yield
characterization, you can prevent the transpiler from combining certain gates.
The :func:`~dwave.gate.qcdl.operations.barrier` instruction signals to the
transpiler to not combine gates across your barrier.\ [#]_

For example, if you do not set :func:`~dwave.gate.qcdl.operations.barrier`
instructions on a
`randomized benchmarking <https://en.wikipedia.org/wiki/Randomized_benchmarking>`_
circuit, where the net mathematical effect is an identity operation,
transpilation collapses your QCDL.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import barrier, x

    @qcdl(1)
    def barrier_example(q0):
        x(q0)
        barrier(q0)
        x(q0)

.. [#]
    When the transpiler is not used, the :func:`~dwave.gate.qcdl.operations.barrier`
    instruction might affect some circuit modifications.


.. _qcdl_basic_registers_arithmetic:

Classical Registers & Arithmetic
--------------------------------

QCDL supports integer and fixed-point registers with the
:class:`~dwave.gate.qcdl.registers.Register` and
:class:`~dwave.gate.qcdl.registers.FixedPointRegister` classes. You can use
these registers for simple classical expressions: negation, addition,
subtraction, multiplication, AND, OR, XOR, right-shift, and all six comparisons.

You can use the outputs of these calculations for
:ref:`conditional statements <qcdl_advanced_conditionals>` within complex
real-time classical-quantum logic.

When you store a :class:`~dwave.gate.qcdl.operations.measure` result to a register,
numerical values :math:`0` and :math:`1` are used to represent the logical
projective measurements and :math:`-1` for a ``*`` state (a measurement that was
out of the code space and declared "erased"). For more information, see the
:class:`~dwave.gate.qcdl.LogicalOutcomeToInteger` class.

.. tip::
    The simulator is able to detect register overflow or underflow problems. For
    this among many other reasons, you should validate programs with the
    simulator before running your application on the QPU. Configure simulator
    option ``use_registers=True`` to either warn or raise an exception on such
    conditions.

Supported Operations
~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1

    *   -   Operation
        -   Operators
        -   Operands
        -   Notes
    *   -   Register assignment
        -   :math:`<<=`
        -   :class:`~dwave.gate.qcdl.registers.Register`,
            :class:`~dwave.gate.qcdl.registers.FixedPointRegister`
        -   QCDL uses :math:`<<=` for register assignment, a syntax similar to
            the R language, because Python does not allow the assignment
            operator :math:`=` to be overridden.
    *   -   Standard arithmetic
        -   :math:`+, -, *`
        -   :class:`~dwave.gate.qcdl.registers.Register`,
            :class:`~dwave.gate.qcdl.registers.FixedPointRegister`, literal
        -   Operations between :class:`~dwave.gate.qcdl.registers.Register` and
            :class:`~dwave.gate.qcdl.registers.FixedPointRegister` classes are
            not supported
    *   -   Bitwise operations
        -   :math:`\&, |`, ^
        -   :class:`~dwave.gate.qcdl.registers.Register`, literal
        -
    *   -   Right-shift by :math:`1`
        -
        -   :class:`~dwave.gate.qcdl.registers.Register`
        -
    *   -   Comparison
        -   :math:`==, !=, <, >, <=, >=`
        -   :class:`~dwave.gate.qcdl.registers.Register`,
            :class:`~dwave.gate.qcdl.registers.FixedPointRegister`, literal
        -   Operations between :class:`~dwave.gate.qcdl.registers.Register` and
            :class:`~dwave.gate.qcdl.registers.FixedPointRegister` classes are
            not supported
    *   -   Arbitrary functions
        -   Interpolation table
        -   :class:`~dwave.gate.qcdl.registers.Register`,
            :class:`~dwave.gate.qcdl.registers.FixedPointRegister`
        -   Generated by the
            :func:`~dwave.gate.qcdl.registers.arbitrary_function`
            function

.. testcode::

    from dwave.gate.qcdl import qcdl, Scope

    @qcdl(2)
    def register_example(q0, q1):
        sc = Scope(q0, q1)                  # Scope facilitates control flow
        r1 = sc.Register(2, name="r1")      # naming facilitates debugging
        r2 = sc.Register()
        r2 <<= 1                            # set r2 to 1
        r2 <<= 2 * r1                       # set r2 to 2*r1 = 4

.. attention::
    Registers are not implicitly re-assigned with every shot. Instead, they
    carry the value they ended with from one shot to the next. Typically, for
    most registers, you prefer each shot to be independent, and so should
    re-assign your registers before using them.

.. note::
    *   A register is associated with a qubit. For QCDL programs with some
        complexity, your program must ensure the information in any qubit's
        register is visible to other qubits. The
        :ref:`qcdl_advanced_registers_mirroring` section provides more
        information.
    *   If you pass a :class:`~dwave.gate.qcdl.registers.FixedPointRegister`
        object to a gate as an angle, use units of π instead of radians. For
        example, a value of :math:`1` is equivalent to π.

.. _qcdl_basic_measurements:

Measurements
------------

A logical :func:`~dwave.gate.qcdl.operations.measure` operation on a dual-rail
gate-model quantum computer produces one of three outcomes:

*   :math:`0, 1` represent logical projective measurements.
*   ``*`` (which has numerical representation :math:`-1`), sometimes informally
    referred to as a "splat", represents that a measured qubit was determined to
    be out of the code space and is thereby declared to be "erased".

You may place these "end of the line"-measurement instructions anywhere in your
program. You can measure qubits multiple times in a given shot (usually
resetting the qubit(s) in between).

.. tip::
    Using the :attr:`~dwave.gate.results.Result.tags` property is the recommended way
    to organize measurement data.

Measurement outcomes are handled in three different ways:

1.  If the :func:`~dwave.gate.qcdl.operations.measure` function has
    its ``log`` parameter set to true (``log=True``, the default) the outcome is
    appended to the array associated with the qubit on which it was measured.
    The :class:`~dwave.gate.results.Result` class returns this data to you in
    a 3D array (per ``tag`` argument of the
    :func:`~dwave.gate.qcdl.operations.measure` operation) with shape
    ``(number of measurements per shot, number of shots, number of qubits)``,
    along with the arrays from the other qubits. You can retrieve this data
    structure using the :meth:`~dwave.gate.results.Result.get_memory` method.
    For circuits with a deterministic number of measurements per shot consistent
    for all qubits, you can convert this data structure a counts dictionary with
    the :meth:`~dwave.gate.results.Result.get_counts` method.
2.  The outcome may be saved to a register. Even if the register is defined on
    multiple qubits, only the register copy on the measured qubit is assigned.
    You can return this data with
    :meth:`~dwave.gate.qcdl.QCDLModuleContainer.append_table_row` method (see
    the :ref:`qcdl_basic_result_records` section).
3.  Each qubit implicitly stores its most recent measurement outcome and
    this value may be used in conditional statements.

.. testcode::

    from dwave.gate.qcdl.operations import measure

    @qcdl(1)
    def measurement_example1(q0):
        measure(q0)

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import measure

    @qcdl(1)
    def measurement_example2(q0):
        register = q0.Register()
        measure(q0, register=register, log=False)

.. warning::
    The 3D array of logged measurements is unlikely to be useful if measurement
    data is generated non-deterministically. Unless there is a deterministic
    number of measurements per shot, you cannot relate measurement outcomes with
    the generating instruction.

By default, the :meth:`~dwave.gate.results.Result.get_counts` method returns all data,
including erasures. To return only results without the ``*``, thereby
post-selecting on the detected errors, set the method's ``post_select`` argument
to true.

.. _qcdl_basic_mced:

Mid-Circuit Erasure Detection
-----------------------------

You can non-destructively inspect a dual-rail qubit to detect if it is out of
the code space ("leaked") with the :func:`~dwave.gate.qcdl.operations.mced`
operation. If the test is positive, the qubit is declared erased.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import mced

    @qcdl(1)
    def mced_example(q0):
        register = q0.Register()
        mced(q0, register=register)


.. _qcdl_basic_result_records:

Result Records
--------------

Results are a Python dictionary where keys are set by the
:meth:`~dwave.gate.qcdl.QCDLModuleContainer.append_table_row` method and values are
tables formatted as a
`Polars <https://docs.pola.rs/api/python/stable/reference/index.html>`_
`DataFrame <https://docs.pola.rs/api/python/stable/reference/dataframe/index.html>`_
and returned from the |cloud|_ service in a :class:`~dwave.gate.results.Result`
class.

The :meth:`~dwave.gate.qcdl.QCDLModuleContainer.append_table_row` method retrieves
the values of registers in runtime. When you invoke the method, register data
is written to a set of tables that your application can retrieve. In addition to
using this functionality in algorithms, you can use it for troubleshooting, as
though it were a cross between a print statement and a breakpoint.

If your QCDL uses the :meth:`~dwave.gate.qcdl.QCDLModuleContainer.append_table_row`
method, the :class:`~dwave.gate.results.Result` output contains records that you may
retrieve with the :attr:`~dwave.gate.results.Result.records` property.

.. testcode::
    :skipif: True

    from dwave.gate.qcdl import qcdl
    from dwave.gate.leap import LeapQCDLSimulator

    # Create a QCDL program:
    @qcdl(1)
    def results_record_example(q0):
        r = q0.Register(name="some_classical_data")
        r <<= 13
        q0.append_table_row(r, table_name="my_table")

    simulated_example = results_record_example()

    # Submit the QCDL to a simulator:
    simulator = LeapQCDLSimulator()

    future = simulator.run(
        simulated_example,
        qpu='DRsim_21qubits',
        noise_model=True,
        shots=500,
        label="SDK Examples - Results Record Job Submission")

    # View the returned records:
    result = future.result().result

    record_as_a_dataframe = result.records["q0"]["my_table"]

The result is a
`Polars DataFrame <https://docs.pola.rs/api/python/stable/reference/dataframe/index.html>`_
containing 1 column named ``some_classical_data`` with 500 rows, each of which
have a value of :math:`13`.

.. Leniency control might be added in a later update.

    .. _qcdl_leniency:

    Leniency
    ~~~~~~~~

    Quantum algorithms involve preparing qubits, manipulating them with quantum gates,
    measuring them, and then using the outcomes of those measurements. Many APIs expect these
    measurements to have values of `0` or `1`. But Dual-Rail erasure
    qubits can have another outcome: `*`, indicating that an error has been detected
    so that neither `0` not `1` can be assumed.

    The simplest strategy for dealing with this is total post-selection
    (see :ref:`Measurements <qcdl_basic_measurements>`) which discards
    all data with any detected error.
    Total post-selection maximizes fidelity by eliminating all detected errors, but it
    does so at the cost of throughput: the probability of a given shot having
    no errors decreases rapidly as circuits become wider or deeper, so a smaller percentage
    of data can be returned to the user.

    Although it's usually critical to maximize fidelity, there are practical situations
    where trading off fidelity to improve throughput (and thus, reduce runtime)
    is advantageous. To do this, errors must be "accepted" into output data
    using one of several "leniency" protocols. From the user perspective,
    leniency results in more output strings with only `0`'s and `1`'s, and fewer
    strings with declared `*`'s. It's important to recognize that leniency does not remove
    errors themselves--instead it causes explicitly detected errors to become obscured,
    allowing a user to give up fidelity to boost yield.

Yield Handling
~~~~~~~~~~~~~~

A significant feature of the simulator in the |cloud|_ service is that it flags
detected errors by returning ``*`` as a third measurement outcome in addition to
:math:`0` and :math:`1`, as described in the :ref:`qcdl_basic_measurements`
section. Tools such as Qiskit do not handle these values so tools such as the
`dwave-qiskit-plugin <https://github.com/dwavesystems/dwave-qiskit-plugin>`_
remove individual shots containing a ``*`` when passing information.
Consequently, fewer shots are likely to be returned than the number of shots you
requested.\ [#]_

The :class:`~dwave.gate.results.YieldHandling` class provides a general way of
handling result distributions. It supports options for renormalizing
distributions, ignoring erasures, and others.

.. testcode::

    from dwave.gate.results import YieldHandling
    half_splats = {"00": 100, "0*": 100}
    assert YieldHandling.only_post_selected_counts.apply(half_splats) == ({"00": 100}, 0.5)


Alternatively, the :meth:`~dwave.gate.results.Result.get_counts` method supports
a ``post_select`` argument.

.. [#]
    If an application you use, for example, in computing statistical errors,
    is not robust to results containing fewer shots than requested, you can use
    the :class:`~dwave.gate.results.YieldHandling` class as a workaround
    *temporarily and with caution*.

.. _qcdl_basic_initialize_reset:

Initialize and Reset
--------------------

At the beginning of every shot, the QPU initializes all of the qubits used by
your circuit. You can also explicitly use the
:func:`~dwave.gate.qcdl.operations.initialize` operation in your QCDL.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import initialize

    @qcdl(4)
    def initialize_example(q0, q1, q2, q3):
        initialize(q0, q1, q2, q3)

The operation is more effective on the QPU than any you are able to implement otherwise in
QCDL code.

You can also reset qubits individually.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import initialize

    @qcdl(1)
    def reset_example(q0):
        q0.reset()


.. _qcdl_basic_transpilation:

Transpilation
-------------

While QCDL programs support any single- or two-qubit gate that is supported
by a Qiskit QuantumCircuit_, D-Wave QPUs (and simulator noise models) do not
support all gates. The set of quantum gates that are compatible with a QPU is
called its basis gates. A QCDL program must be transpiled to replace any
unsupported gates with these basis gates.

Transpilation handles the change of gates for you. You may use any gates
you wish to in your QCDL, knowing that the operations executed on the solver
might differ in this way from your code. However, if you want your program
executed verbatim (or an error raised), you can configure compilation and
simulation to not transpile (see the :ref:`qcdl_submitting_programs` section).


.. list-table::
    :header-rows: 1

    *   -   Basis Gates
        -   Description
        -   Availability
    *   -   :func:`~dwave.gate.qcdl.operations.sx`,
            :func:`~dwave.gate.qcdl.operations.x`
        -   Single qubit rotation around the X-axis by π/2 and π respectively.
        -   All operational qubits.
    *   -   :func:`~dwave.gate.qcdl.operations.rz`
        -   Single qubit, parameterizable rotation around the Z-axis.
        -   All operational qubits.
    *   -   :func:`~dwave.gate.qcdl.operations.cz`
        -   Two qubit rotation by π/2 around the ZZ-axis.
        -   Connected, operational qubits.

Transpiler Constraints and Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   Transpilation is a non-deterministic optimization algorithm based on Qiskit.
    Optimality is not
    guaranteed.
*   Depending on topology and your circuit, the transpiler may add qubits and gates to
    the executed program that were not in your QCDL. You might be able to
    prevent this through careful placement of input gates.
*   Returned logged measurements are organized according to the name of the
    qubit used in the :func:`~dwave.gate.qcdl.operations.measure` instruction.


.. _qcdl_advanced:

QCDL: Advanced
==============

.. _qcdl_advanced_procedures:

Procedures
----------

QCDL supports procedures on qubits. A procedure is a subroutine that is
called from another procedure (the :ref:`entrypoint <qcdl_basic_entrypoint>`,
marked with the ``@qcdl`` decorator, is the outermost procedure).

Procedures are useful for:

*   Potentially conserving instruction memory on the QPU
*   Organizing code for visualization purposes
*   Constraining transpilation

A procedure is marked with the :class:`~dwave.gate.qcdl.procedure` decorator.

.. testcode::

    from dwave.gate.qcdl import procedure, qcdl
    from dwave.gate.qcdl.operations import rx, ry

    @procedure
    def my_procedure(qa, qb, increment):
        rx(qa, increment)
        ry(qb, increment)

    @qcdl(2)
    def procedure_example(q0, q1):
        for _ in range(10):
            my_procedure(q0, q1, 0.3)
        my_procedure(q1, q0, 0.5)

A QCDL program calls the procedure just as it would any other Python function.
In the preceding example, if you remove the ``@procedure`` decorator, the
program inlines all the gates into the main procedure.


.. _qcdl_advanced_scope:

Scope
-----

The :class:`~dwave.gate.qcdl.Scope` class enables you to define a set of
operations you can *consistently* reuse on multiple qubits, which is especially
beneficial for for classical and control-flow instructions.

This class is a client-side convenience feature used to generate qubit-level
instructions---it is not represented in the generated QCDL. You may declare any
number of scopes with arbitrary overlaps.

The example below defines a scope containing all the qubits used in the
program. At the end of each shot, all qubits have :math:`1` in their register
if ``q0`` is measured to be :math:`1`. This is a good example for how one might
:ref:`mirror <qcdl_advanced_registers_mirroring>` the same register across
qubits.

.. testcode::

    from dwave.gate.qcdl import qcdl, Scope
    from dwave.gate.qcdl.operations import h, measure

    @qcdl(3)
    def main(q0, q1, q2):
        sc = Scope(q0, q1, q2)
        is_1 = sc.Register()
        is_1 <<= 0
        h(q0)
        measure(q0)
        with sc.If(condition=q0):
            is_1 += 1


.. _qcdl_advanced_synchronization:

Synchronization
---------------

In order to run on a QPU, quantum programs must have all of their gate
operations scheduled, with the start time of each instruction precisely
determined relative to the preceding instruction. Typically, you leave that to
the compiler. For some programs, however, you might need to ensure that certain
operations execute sequentially instead of concurrently; for example, to
complete a measurement on one qubit before another qubit uses that measurement
as a condition.

You can explicitly control such scheduling with the
:meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` instruction. You may apply this
instruction to any number of qubits to indicate that all operations before the
:meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` instruction must be completed
before any operations after the instruction are started.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import x

    @qcdl(2)
    def sync_example(q0, q1):
        x(q0)
        q0.sync(q1)
        x(q1)

The example above ensures that the :func:`~dwave.gate.qcdl.operations.x` on ``q1``
is scheduled to start after the :func:`~dwave.gate.qcdl.operations.x` on ``q0`` has
completed.

Synchronization Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   Compilation inserts implicit :meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync`
    instructions before and after all multi-qubit operations such as gates,
    procedures, and control-flow operations (including shots).
*   The :meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` instruction is not
    sensitive to the ordering of the qubits.
*   An explicit :meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` instruction in the
    program is treated as a :func:`~dwave.gate.qcdl.operations.barrier` instruction
    by the transpiler.
*   Scheduling is performed at compile-time and there is no support for
    "runtime" re-synchronization. If qubits are ever desynchronized, the output
    is meaningless. This means that non-deterministic operations must include
    all qubits in your program.
*   Conditional statements themselves are deterministically scheduled by
    ensuring that an idle is inserted into either the true or false branch so
    that both branches are exactly the same duration.

.. attention::
    The simulator does not model runtime concurrency; it simply executes
    instructions sequentially regardless of which qubit the instruction uses.
    Therefore the :meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` instruction does
    not affect execution order of operations.

    Consider carefully the positioning of any
    :meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` and cautiously validate when
    executing on a QPU (for example, by using a
    :meth:`~dwave.gate.qcdl.QCDLModuleContainer.append_table_row` instruction).

.. _qcdl_advanced_conditionals:

Conditionals
------------

Programs may execute operations subject to a condition. You accomplish this in
two discrete steps:

1.  Use classical logic to compute one bit of information and store it in
    a register. This is the *branch condition*.
2.  Create a true branch statement, and optionally a false branch statement. If
    the branch condition evaluates to :math:`1`, your true branch is executed;
    otherwise, the false branch (or the default idle) is executed.

QCDL supports several ways of setting a branch condition and branching from an
instruction.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import measure, x

    @qcdl(2)
    def branch_example1(q0, q1):
        measure(q1)
        with q0.If(condition=q1):
            x(q0)

In the preceding example, the :func:`~dwave.gate.qcdl.operations.x` gate is executed
if the most recent measurement of ``q1`` was a :math:`1`. Here, the unspecified
false branch---executed if the most recent measurement of ``q1`` was a :math:`0`
or a ``*``---is an idle of equal duration to the true branch.

The next example specifies a false branch. A :func:`~dwave.gate.qcdl.operations.y`
gate is executed in the case of a :math:`0` or a ``*`` instead of the default
idle.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import measure, x, y

    @qcdl(2)
    def branch_example2(q0, q1):
        measure(q1)
        with q0.If(condition=q1) as Else:
            x(q0)
        with Else():
            y(q0)

Supported Condition Values
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1

    *   -   Condition
        -   Description
        -   Notes
    *   -   ``q{N}``
        -   The :math:`N`\ th qubit's most recent measurement. Branches if the
            last measurement for the qubit is :math:`1`.
        -   Volatile and may change at the next measurement.
    *   -   Expressions
        -   A classical expression evaluated at runtime (e.g. ``reg2 < 5``).
        -   See the :ref:`qcdl_basic_registers_arithmetic` section for details.
    *   -   Signal
        -   Specify ``q{N}.signal`` to branch off of the bit that ``q{N}`` is
            currently signaling.
        -   See the :ref:`qcdl_advanced_signals` section for details.
    *   -   ``None``
        -   You can separate the steps of evaluating the branch condition and
            branching by assigning the branch condition before the statement
            (e.g., :meth:`~dwave.gate.qcdl.QCDLModuleContainer.If`), with
            that branch condition persisting if ``None`` is specified. The
            branch condition might be set, for example, by a preceding
            :meth:`~dwave.gate.qcdl.QCDLModuleContainer.all_to_all` or
            :meth:`~dwave.gate.qcdl.QCDLModule.one_to_all` call, which
            places a signal from one qubit onto the branch condition of each
            recipient qubit.
        -   See the :ref:`qcdl_advanced_signals` section.
    *   -   ``True`` or ``False``
        -   Python Boolean that deterministically selects a branch taken by all
            qubits.
        -   For troubleshooting.

Guidelines for Using Conditionals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-   You can nest conditional statements arbitrarily deep.
-   Place the :meth:`~dwave.gate.qcdl.QCDLModuleContainer.If` statement and its true
    and false branches in the same procedure.
-   Use the :class:`~dwave.gate.qcdl.Scope` class to include an arbitrary number of
    qubits in a condition. If your condition value is an expression, take care
    that it evaluates to the same outcome for all qubits.
-   Compilation does not guarantee that a qubit has been measured before it is
    used in a conditional. Use with caution.
-   Since a condition can be a Boolean, if you do not intend that, be careful
    that your Python code does not inadvertently cast the condition to a
    Boolean. (You may find the output of :func:`~dwave.gate.utils.display.print_qcdl`
    helpful for this.)
-   Your true and false branches must not contain operations on qubits that are
    not a part of the conditional branch.

Advanced Examples
~~~~~~~~~~~~~~~~~

This example detects and resets a qubit if it has been erased.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import mced

    @qcdl(1)
    def detect_erasure_example(q0):
        erased = q0.Register(name="erased")
        erased <<= 0
        mced(q0, register=erased)
        with q0.If(erased == 1):
            q0.reset()

This example conditions on a classical register.

.. testcode::

    from dwave.gate.qcdl import qcdl, Scope
    from dwave.gate.qcdl.operations import mced, x

    @qcdl(2)
    def classical_condition_example(q0, q1):
        sc = Scope(q0, q1)
        c0 = sc.Register(2, name="c0")
        c1 = sc.Register()
        # operations that update these registers
        with q1.If( c0 | c1 == 1 ):
            x(q1)

This example updates all registers with the outcome of a particular measurement.

.. testcode::

    from dwave.gate.qcdl import qcdl, Scope
    from dwave.gate.qcdl.operations import mced, x

    @qcdl(2)
    def classical_condition_example(q0, q1):
        sc = Scope(q0, q1)
        register = sc.Register(name="register")
        measure(q0)
        with sc.If(q0):
            register += 1

.. _qcdl_advanced_signals:

Signals for Branch Conditions
-----------------------------

A :ref:`register <qcdl_basic_registers_arithmetic>` is associated with a qubit.
Your QCDL must ensure the information in any qubit's register is visible to all
qubits (:ref:`mirror <qcdl_advanced_registers_mirroring>` the information) in
order, for example, to select the same branch to execute for a
:ref:`conditional statement <qcdl_advanced_conditionals>`.

This requires that you pass some information from the memory associated with one
qubit to that of another, in particular results of a measurement on one qubit
that condition operations on other qubits.

Basic Signal
~~~~~~~~~~~~

For any qubit, you can set the :attr:`~dwave.gate.qcdl.QCDLModule.signal` property
(the *signal*) to a Boolean value for use, in realtime, as a
:ref:`branch condition <qcdl_advanced_conditionals>` by other qubits.

The following example results in the bitstring being either :math:`11` or
:math:`00` (assuming no noise). The
:meth:`~dwave.gate.qcdl.QCDLModuleContainer.sync` operation prevents the
``receiver`` qubit conditioning off of the signal value before the ``sender``
qubit sets it after its measurement. The :ref:`qcdl_advanced_conditionals`
section describes the condition value used in the ``If`` statement.

.. todo:: Amos is updating the simulator for use of signal (see simulator ticket 503)

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import h, measure, x

    @qcdl(2)
    def signal_example(q0, q1):
        receiver = q1
        sender = q0
        h(q0)
        send_register = q0.Register()
        measure(q0, register=send_register)
        sender.master(signal=send_register == 1)
        sender.sync(receiver)
        with receiver.If(sender.signal):
            x(receiver)
        measure(receiver)

.. note::
    If more than one qubit is branching off a signal, it is likely more
    efficient to use the :meth:`~dwave.gate.qcdl.QCDLModule.one_to_all` method.

``one_to_all`` Signal
~~~~~~~~~~~~~~~~~~~~~

The :meth:`~dwave.gate.qcdl.QCDLModule.one_to_all` method signals a Boolean value
from one qubit to a set of other qubits that can use it as a
:ref:`branch condition <qcdl_advanced_conditionals>` to conditionally execute a
branch of operations.

You accomplish this by specifying the following: (1) The origin qubit, (2) an
expression for setting the Boolean value, and (3) the set of qubits that use the
signal for a branch condition

This example results in the bitstring being either `000` or `111` (absent
noise). The :ref:`qcdl_advanced_conditionals` section describes the condition
value used in the ``If`` statement.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import h, measure, x

    @qcdl(3)
    def one_to_all_example(q0, q1, q2):
        h(q0)
        send_register = q0.Register()
        measure(q0, register=send_register)
        sc = Scope(q1, q2)
        q0.one_to_all(sc.qcdl_modules, send_register == 1)
        with sc.If(None):
            x(q1)
            x(q2)
        measure(q1)
        measure(q2)

``all_to_all`` Signal
~~~~~~~~~~~~~~~~~~~~~

The more-general :meth:`~dwave.gate.qcdl.QCDLModuleContainer.all_to_all` method
signals a Boolean value from all qubits to a set of participating qubits to use
as a :ref:`branch condition <qcdl_advanced_conditionals>`.

You accomplish this by specifying the following: (1) A set of qubits that all
contribute one bit to the signal, (2) a reduction operator used to compute a
Boolean value from those bits. The resulting Boolean value conditions all
participating qubits.

This example results in the bitstring being either :math:`000` or :math:`111`
(absent noise). The :ref:`qcdl_advanced_conditionals` section describes the
condition value used in the ``If`` statement here and in subsequent examples.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import h, measure, x

    @qcdl(3)
    def all_to_all_example(q0, q1, q2):
        sc = Scope(q0, q1, q2)
        h(q0)
        name = "bit"

        # all qubits have a copy of the same register:
        send_register = sc.Register(name=name)

        # set the register on q0 to 0 or 1
        measure(q0, register=q0.Register(name=name))

        # if any of the copies of the register are equal to 1, then all
        # will receive a condition of True.
        sc.all_to_all(send_register == 1, reduce_op="|")
        with sc.If(None):
            x(q1)
            x(q2)
        measure(q1)
        measure(q2)

In the next example, if any register has value :math:`1`, update all the
registers to be :math:`1`, otherwise, set them to :math:`0`.

.. testcode::

    from dwave.gate.qcdl import qcdl, Scope

    @qcdl(3)
    def all_to_all_example2(q0, q1, q2):
        sc = Scope(q0, q1, q2)
        register = sc.Register(name="register")
        # operations
        sc.all_to_all(register == 1, reduce_op="|")
        with sc.If(None) as Else:
            register <<= 1
        with Else():
            register <<= 0

The next example loops until a qubit has been erased. The
:ref:`qcdl_advanced_control_flow` section describes QCDL control-flow methods.

.. testcode::

    from dwave.gate.qcdl import qcdl, Scope
    from dwave.gate.qcdl.operations import mced

    @qcdl(2)
    def all_to_all_example3(q0, q1):
        sc = Scope(q0, q1)
        erased = sc.Register(name="erased")
        with sc.DoWhile(None):
            for q in [q0, q1]:
                mced(q, register=erased)
            sc.all_to_all(erased == 0, reduce_op="&")

The next example demonstrates an active reset, looping until all qubits are in a
:math:`\ket 0` state.

.. todo:: The next example needs to be fixed

.. testcode::
    :skipif: True

    from dwave.gate.qcdl import qcdl, Register, Scope
    from dwave.gate.qcdl.operations import mced, measure, x

    @qcdl(2)
    def all_to_all_example4(q0, q1):
        name = "in_0"
        sc = Scope(q0, q1)
        in_0 = sc.Register(name=name)
        with sc.DoWhile(None):
            in_0 <<= 1
            for q in sc.qubits:
                measure(q)
                with q.If(q):
                    x(q)
                    Register(q, name=name) <<= 0
            # if any were not in 0, iterate again
            sc.all_to_all(send=in_0==0, reduce_op="|")


.. _qcdl_advanced_control_flow:

Control Flow
------------

QCDL programs support several control-flow mechanisms.\ [#]_

.. list-table::
    :header-rows: 1

    *   -   Method
        -   Purpose
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Repeat`
        -   Repeats the body of the context manager for a specified number of
            iterations.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.While`
        -   Repeats the body of the context manager as long as the condition is
            true.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.DoWhile`
        -   Unconditionally executes a first iteration of the context manager
            and then, similar to the
            :meth:`~dwave.gate.qcdl.QCDLModuleContainer.While` method, repeats the
            body of the context manager as long as the condition is true. Useful
            if the condition is evaluated only within the loop.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.For`
        -   Repeats the body of the context manager as long as the condition is
            true, similar to the :meth:`~dwave.gate.qcdl.QCDLModuleContainer.While`
            method, but, similarly to a C-style loop, also provides some
            convenience mechanisms for initializing and updating a register.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Break`
        -   Breaks out of a loop structure. Useful for preventing infinite
            loops.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Continue`
        -   Skips the remainder of the body of the context manager and jumps to
            the conditional.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Label`/:meth:`~dwave.gate.qcdl.QCDLModuleContainer.Goto`
        -   A :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Goto` instruction
            unconditionally jumps to the location marked by the corresponding
            :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Label` instruction.
    *   -   :meth:`~dwave.gate.qcdl.QCDLModuleContainer.Return`
        -   Exits a procedure early.

.. [#]

    These are all abstractions built on top of an underlying
    `goto <https://en.wikipedia.org/wiki/Goto>`_ and label mechanism.

.. Attention::
        If your QCDL lets only a subset of qubit branches execute a jump, these
        powerful control-flow expressions risk desychronizing operations on
        qubits, as noted in the :ref:`qcdl_advanced_synchronization` section.
        These control-flow operations are recommended only in a
        :meth:`~dwave.gate.qcdl.Scope` that includes all of the qubits.

.. testcode::

    from dwave.gate.qcdl import procedure, qcdl, Scope
    from dwave.gate.qcdl.operations import rx, ry

    @procedure
    def rotate(q0, q1, increment):
        rx(q0, increment)
        ry(q1, increment)

    @qcdl(2)
    def repeat_example(q0, q1):
        sc = Scope(q0, q1)
        num_iterations = 5
        with sc.Repeat(num_iterations):
            rotate(q0, q0, 0.1)

The following is also an example for how a
:meth:`~dwave.gate.qcdl.QCDLModuleContainer.Repeat` instruction could be
implemented.

.. testcode::

    from dwave.gate.qcdl import procedure, qcdl, Scope

    @qcdl(2)
    def dowhile_example(q0, q1):
        sc = Scope(q0, q1)
        counter = sc.Register(name="counter")
        num_iterations = 5
        counter <<= num_iterations

        with sc.DoWhile(counter > 0):
            counter -= 1


.. _qcdl_advanced_registers_mirroring:

Mirroring
---------

A register is associated with a qubit. When you create a
:class:`~dwave.gate.qcdl.registers.Register` object for the qubits of a
:class:`~dwave.gate.qcdl.Scope` class, it is implemented as a collection of
registers for the qubits in the scope. And when you assign that
:class:`~dwave.gate.qcdl.registers.Register` to a
:func:`~dwave.gate.qcdl.operations.measure` or
:func:`~dwave.gate.qcdl.operations.mced` operation, only the register
associated with the measured qubit is updated (the measurement outcome is
immediately written to that register).

Your QCDL must ensure the information in
any qubit's register is visible to all qubits in the :class:`~dwave.gate.qcdl.Scope`
or :class:`~dwave.gate.qcdl.registers.Register` object (*mirror* the
information). This is needed, for example, to select the same branch to execute
for a :ref:`conditional statement <qcdl_advanced_conditionals>`.

Mirroring requires an extra communication step to ensure that registers
associated with all other qubits of the
:class:`~dwave.gate.qcdl.registers.Register` object are also updated.

For simplicity, you can use the following two cooperative techniques to
implement mirroring.

1.  Execute classical calculations redundantly when possible; for example, use a
    :ref:`scope <qcdl_advanced_scope>` to instantiate registers for all qubits
    or, for each qubit, give its register the same name and execute the same
    operations.
2.  Communicate non indentical information (see the :ref:`qcdl_advanced_signals`
    section). With the :class:`~dwave.gate.qcdl.Scope` class, the only information
    you must update across registers at runtime are (non-deterministic)
    measurement/MCED results.

Guidance on Mirroring
~~~~~~~~~~~~~~~~~~~~~

*   Expressions between registers in different scopes are not supported.
*   Use the ``mirror`` parameter in the :func:`~dwave.gate.qcdl.operations.mced`
    or :func:`~dwave.gate.qcdl.operations.measure` operations to propagate
    measurements among registers.
*   Always use the same scope for conditional statements and register
    instantiation. A good practice is to instantiate one
    :class:`~dwave.gate.qcdl.Scope` object at the start of your QCDL that contains
    all qubits and use that scope for registers and loops, making other scopes
    only for small tasks.
*   It is technically possible to compose a conditional expression using
    registers such that some qubits go to a true branch and others to a false
    branch. This is not recommended and the simulator raises an exception.

.. seealso::

    :func:`~dwave.gate.implementations.mirror_bool_register` and
    :func:`~dwave.gate.implementations.mirror_measurement_register`
    functions


.. _qcdl_simulator:

QPU Simulator
=============

the |cloud|_ service provides a Monte Carlo simulator of QCDL programs. This is
built on top of Qiskit's
`AerStatevector <https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.quantum_info.AerStatevector.html>`_.

This simulator closely models the classical and quantum operation of the QPU
with varying approximations. It instantiates a "state" representing both
classical and quantum components of the hardware and then executes your QCDL
instructions one at a time to update that state. As a Monte Carlo simulator, it
is significantly slower than a "sampling" simulator and scales linearly with the
number of shots; however, its operation is
`embarrassingly parallel <https://en.m.wikipedia.org/wiki/Embarrassingly_parallel>`_.

.. tip::
    Accuracy bears a simulation cost and error handling increases circuit
    complexity. It is advisable to start circuit development against the ideal
    simulator and then introduce error modeling.

    .. for future consideration
        in a controlled way. For example, start by simulating full-precision
        registers before simulating reduced-precision registers; start with
        ideal quantum operations before introducing erasures.

        Amos: Update the above paragraph as new features become available

The simulator in the |cloud|_ service supports two modes of simulations. The
following table compares these two simulation modes.

.. list-table::
    :header-rows: 1

    *   -   Characteristic
        -   Statevector Simulation
        -   Dual-Rail Erasure Simulation
    *   -   Noise model.
        -   Solver parameter :ref:`parameter_drsim_noise_model` set to
            ``False``.

            Useful during initial testing of QCDL programs before introducing
            noise.
        -   Solver parameter :ref:`parameter_drsim_noise_model` set to
            ``True``.

            This simulation is useful for exploring the impact of erasures on
            QCDL programs. It operates by randomly applying Pauli errors,
            leakages, and seepages after quantum gates and idles.
    *   -   Runtime.
        -   Scales as :math:`O(s*g*2^n)` where :math:`n` is the number of qubits,
            :math:`s` the number of shots, and :math:`g` the number of gates.

        -   Slower but same scaling.
    *   -   Supported gates.
        -   All gates available in Qiskit (no transpilation required).
        -   Subset of gates (transpilation required).
    *   -   Support for errors.
        -   No support. (Returns :math:`0` for ``mced``, signifying no leak.)
        -   Supports the ``mced`` instruction to detect if the qubit has been
            erased, and the ``leak`` and ``seep`` instructions to simulate
            leakage and seepage errors.



.. _qcdl_submitting_programs:

Submitting Programs
===================

The :ref:`QPU simulator <qcdl_simulator>` in the |cloud|_ service is intended to
simulate :ref:`gate-model quantum computers <qpu_gate_model_intro>` by executing
programs formulated as QCDL.

The following documentation describes how to work with the |cloud|_ service:

*   The :ref:`index_leap_sapi` section describes the |cloud|_ service.
*   The :ref:`ocean_leap_authorization` section walks you through authorizing
    your Ocean client to access the simulator in the |cloud|_ service.
*   The :ref:`ocean_install` section explains how to install Ocean software.

Descriptions of the supported parameters and simulator properties are provided
in the :ref:`qcdl_simulator_parameters` and :ref:`qcdl_simulator_properties`
sections.

.. _qcdl_submitting_programs_example:

Example Submission
------------------

The example below submits the following
`Bell state <https://en.wikipedia.org/wiki/Bell_state>`_ QCDL program.

.. testcode::

    from dwave.gate.qcdl import qcdl
    from dwave.gate.qcdl.operations import cx, h, measure

    @qcdl(2)
    def bell_program(q0, q1):
        h(q0)
        cx(q0, q1)
        measure(q0)
        measure(q1)

    simulator_job_submission = bell_program()

Submit the program above to a simulator for a dual-rail QPU with 21 qubits,
``DRsim_21qubits``, in the |cloud|_ service.

>>> from dwave.gate.leap import LeapQCDLSimulator
...
>>> simulator = LeapQCDLSimulator()         # doctest: +SKIP
>>> future = simulator.run(                 # doctest: +SKIP
...     simulator_job_submission,
...     qpu='DRsim_21qubits',
...     noise_model=True,
...     shots=500,
...     label="SDK Examples - Bell-Program Job Submission")
>>> result = future.result().result         # doctest: +SKIP

.. _qcdl_submitting_programs_results:

Example Results
---------------

Results are returned as a :class:`~dwave.gate.results.Result` class, that also
includes information such as execution time and provides methods for analyzing
the measurements.

The returned result is a 3D array of ``(measurements per shot, shots, qubits)``.
For the previous example, one measurement is taken per shot, for 500 shots, on
two qubits.

>>> print(result.get_memory().shape)        # doctest: +SKIP
(1, 500, 2)

For one particular execution of the program above, the following counts are
returned.

>>> print(result.get_counts())              # doctest: +SKIP
[{'11': 203, '*1': 14, '00': 230, '0*': 22, '*0': 19, '1*': 10, '**': 2}]

The execution time on the simulator (excluding any queuing time, for example)
for that job submission is about a tenth of a second.

>>> print(result.run_time)                  # doctest: +SKIP
0.093493

See the :ref:`gate_results` section for information about the returned results
and supported methods. The :ref:`qcdl_basic_result_records` section describes
how you store and retrieve records of measurements.



.. unsupported currently

    .. _qcdl_submitting_compiling:

    Compilation
    -----------

    Compilation is required to submit a circuit to a QPU. The compiled artifact is a
    ``.jmz`` file.

    .. note::
        Submitting to a QPU is currently not supported.

    You do not need to compile if you are submitting your QCDL to a simulator, but
    is useful if you wish to validate that your circuit could run on a QPU. You may
    choose to compile to perform a more comprehensive validation of your QCDL
    on the simulator, to ensure both that the program returns the correct results
    and that the compiler is able to generate a set of instructions for the QPU to
    correctly execute. Compilation takes some extra time and you probably do not
    need to compile each simulation.

    .. tip::
        Compile immediately prior to every execution on a QPU to ensure the latest
        calibrated parameters are used. Some applications may be able to reuse a
        previously compiled ``.jmz`` to save time but ``.jmz`` files may expire.

.. compilation unsupported currently

    You can simulate either the QCDL itself directly or a compiled version of the
    QCDL (a ``.jmz`` file).

