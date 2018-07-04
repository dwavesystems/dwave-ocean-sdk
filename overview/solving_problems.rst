.. _solving_problems:

===================================
Solving Problems on a D-Wave System
===================================

This section explains some of the basics of how D-Wave's quantum processing unit (QPU)
solves problems, what you need to do to use it for your problem, and how Ocean tools
can help.

How a D-Wave System Solves Problems
===================================

For quantum computing, as for classical, solving a problem requires that it
be expressed it in a formulation compatible with the underlying physical hardware.

When you want to calculate the area of a $1 coin on your laptop, for example, you may
enter the equation :math:`A=\pi r^2` into software that converts it to binary operations
suited for the underlying adders, registers, and memory chips that manipulate bits.
A D-Wave QPU is a chip with interconnected qubits; for example, a D-Wave 2000Q has up to
2048 qubits connected in a :term:`Chimera` topology. Programming it consists mostly of
setting two inputs:

* Qubit bias weights: control the degree to which a qubit tends to a particular state.
* Qubit coupling strengths: control the degree to which two qubits tend to the same state.

Once you express your problem in a formulation\ [#]_ such that desired outcomes have
low energy values and undesired outcomes high energy values, the D-Wave system solves
your problem by finding the low-energy states.

This formulation, called an *objective function* for the system, is the :term:`Ising`
model traditionally used in statistical mechanics or its computer-science equivalent,
the :term:`QUBO`, where variables are binary 0 and 1.

.. [#]
    Given :math:`N` variables :math:`\pmb{s}=[s_1,...,s_N]` corresponding
    to physical Ising spins :math:`s_i \in \{-1,+1\}`, configurations of an Ising model
    have energy,

    .. math::

        E(\pmb{s}|\pmb{h},\pmb{J})  = \left\{ \sum_{i=1}^N h_i s_i + \sum_{i<j}^N J_{i,j} s_i s_j  \right\}

    where :math:`h_i` are biases and :math:`J_{i,j}` couplings between spins.

Ocean software can abstract away much of the mathematics and programming. At its heart
is a binary quadratic model (BQM) class for handling the desired objective function. It helps
formulate objective functions for some common types of optimization problems.
It also provides an API to binary quadratic :term:`sampler`\ s, such as the D-Wave
system and classical algorithms you can run on your computer, which find the
low-energy states that constitute solutions to the problem.

The following sections give an intuitive explanation of these two steps (the
third may benefit some problems) of this problem-solving procedure; see the :ref:`gs`
examples and system documentation for further description.

1. :ref:`formulating` as a BQM.
2. :ref:`submitting` low-energy states of the BQM to find solutions.
3. :ref:`improving`, if needed, using advanced features.

.. figure:: ../_static/SolutionOverview.png
   :name: SolutionOverview
   :alt: image
   :align: center
   :scale: 90 %

   Solution steps: (1) formulate a problem that you know in "problem space" (a circuit
   of Boolean gates, a graph, a network, etc) as a BQM, mathematically or using
   Ocean functionality and (2) sample the BQM for solutions.

.. _formulating:

Formulate a Problem
===================

There are different ways of mapping between any problem space (chains of amino acids
forming 3D structures of folded proteins, traffic in the streets of Beijing, circuits
of binary gates) and a BQM to be solved by sampling with a D-Wave system or locally on
your CPU/GPU. Here we provide an intuitive example.

Consider the problem of determining outputs of a Boolean logic circuit. In problem space
the circuit might be described with input and output voltages, equations of
its electronic components (resistors, transistors, etc), logic symbols,
multiple or an aggregated truth table, and so on. You can mathematically
formulate a BQM---in different ways too, for example a BQM for each gate or one BQM for
all the circuit's gates---or use Ocean's formulations of binary gates directly in your
code.

For example, as shown in the :ref:`not` example, a NOT gate represented symbolically as
:math:`x_2 \Leftrightarrow \neg x_1` in problem space might be formulated
mathematically as the following QUBO:

.. math::

    E(x) = -x_1 -x_2  + 2x_1x_2

The following table shows that this QUBO has low energy for valid states of the NOT
gate and high energy for invalid states.

.. table:: Energy for a Boolean NOT Operation Formulated as a QUBO.
   :name: BooleanNOTAsPenalty

   ===========  ============  ===============  ============
   :math:`x_1`  :math:`x_2`   **Energy**       **Valid?**
   ===========  ============  ===============  ============
   :math:`0`    :math:`1`     :math:`0`        Yes
   :math:`1`    :math:`0`     :math:`0`        Yes
   :math:`0`    :math:`0`     :math:`1`        No
   :math:`1`    :math:`1`     :math:`1`        No
   ===========  ============  ===============  ============

If you formulate your problem as an Ising or QUBO model, Ocean lets you instantiate
a BQM from that; for example, :code:`bqm = dimod.BinaryQuadraticModel.from_qubo()`.

For some problems you can skip the mathematical formulation; for example, Ocean's
`dwavebinarycsp <http://dwavebinarycsp.readthedocs.io/en/latest/>`_ tool enables the
following formulation of an AND gate as a BQM:

.. code-block:: python

    >>> import dwavebinarycsp
    >>> import dwavebinarycsp.factories.constraint.gates as gates
    >>> csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
    >>> csp.add_constraint(gates.and_gate(['x1', 'x2', 'y1']))  # add an AND gate
    >>> bqm = dwavebinarycsp.stitch(csp)

Once you have a BQM that represents your problem, you sample it.

.. _submitting:

Sample
======

To solve your problem, now represented as a binary quadratic model, you submit it
to a sampler. If you use a classical solver running locally on your CPU, a single sample
might provide the lowest energy state of the system and thus the optimal solution.
When you use a probabilistic sampler like the D-Wave system, you typically program
for multiple reads.

If you plan to use the D-Wave system to sample, follow the configuration described
under :ref:`dwavesys`.

For example, the BQM of the AND gate created above may look like this:

.. code-block:: python

    >>> bqm     # doctest: +SKIP
    BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0}, {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0}, -1.5, Vartype.BINARY)

where the members of the two dicts are linear and quadratic biases, respectively,
the third term is a constant energy offset associated with the model, and the fourth
shows the variable types in this model are binary.

Ocean's `dimod <http://dimod.readthedocs.io/en/latest/>`_ tool provides a reference solver
that calculates the energy of all possible samples. Such a sampler can solve a small
three-variable problem like the AND gate.

.. code-block:: python

    >>> from dimod.reference.samplers import ExactSolver
    >>> sampler = ExactSolver()
    >>> response = sampler.sample(bqm)    # doctest: +SKIP
    >>> for sample, energy in response.data():     # doctest: +SKIP
    ...    print(sample, energy)
    ...
    {'x1': 0, 'x2': 0, 'y1': 0} -1.5
    {'x1': 1, 'x2': 0, 'y1': 0} -1.5
    {'x1': 0, 'x2': 1, 'y1': 0} -1.5
    {'x1': 1, 'x2': 1, 'y1': 1} -1.5
    {'x1': 1, 'x2': 1, 'y1': 0} 0.5
    {'x1': 0, 'x2': 1, 'y1': 1} 0.5
    {'x1': 1, 'x2': 0, 'y1': 1} 0.5
    {'x1': 0, 'x2': 0, 'y1': 1} 4.5

Note that the first four samples are the valid configurations of the AND gate and have
lower energy than the second four, which represent invalid configurations.

Ocean's `dwave-system <http://dwave-system.readthedocs.io/en/latest/>`_ tool enables
you to use a D-Wave system as a sampler. In addition to *DWaveSampler()*, the tool
provides a *EmbeddingComposite()* composite that maps unstructured problems to the graph
structure of the selected sampler, a process known as :term:`minor-embedding`; in our case,
the problem's variables (x1, x2, y1) to particular qubits on a QPU.

Because of the sampler's probabilistic nature, you typically request multiple samples
for a problem; this example sets `num_reads` to 1000.

.. code-block:: python

    >>> from dwave.system.samplers import DWaveSampler
    >>> from dwave.system.composites import EmbeddingComposite
    >>> sampler = EmbeddingComposite(DWaveSampler())
    >>> response = sampler.sample(bqm, num_reads=1000)   # doctest: +SKIP
    >>> for sample, energy, num_occurrences in response.data():     # doctest: +SKIP
    ...    print(sample, "Energy: ", energy, "Occurrences: ", num_occurrences)
    ...
    {'x1': 0, 'x2': 1, 'y1': 0} Energy:  -1.5 Occurrences:  92
    {'x1': 1, 'x2': 1, 'y1': 1} Energy:  -1.5 Occurrences:  256
    {'x1': 0, 'x2': 0, 'y1': 0} Energy:  -1.5 Occurrences:  264
    {'x1': 1, 'x2': 0, 'y1': 0} Energy:  -1.5 Occurrences:  173
    {'x1': 1, 'x2': 0, 'y1': 1} Energy:  0.5 Occurrences:  215

Note that the first four samples are the valid configurations of the AND gate and have
lower energy than invalid configuration :math:`x1=1, x2=0, y1=1`.

.. _improving:

Improve the Solutions
=====================

More complex problems than the ones shown above can benefit from some of the D-Wave system's
advanced features and Ocean software's advanced tools.

The mapping from problem variables to qubits, :term:`minor-embedding`, can significantly
affect performance. Ocean tools perform this mapping heuristically so simply rerunning
a problem might improve results. Advanced users may customize the mapping by directly
using the `minorminer <http://minorminer.readthedocs.io/en/latest/>`_ tool or setting
a minor-embedding themselves (or some combination).

D-Wave systems offer features such as spin-reversal (gauge) transforms and anneal offsets,
which reduce the impact of possible analog and systematic errors due to inherent qubit
biases, and others.

You can see the parameters and properties a sampler supports. For example, Ocean's
`dwave-system <http://dwave-system.readthedocs.io/en/latest/>`_ lets you use the
D-Wave's *virtual graphs* feature to simplify minor-embedding. The following example
maps a problem's variables x, y to qubits 1, 5 and variable z to two qubits 0 and 4,
and checks some features supported on the D-Wave system used as a sampler.

.. code-block:: python

    >>> from dwave.system.samplers import DWaveSampler
    >>> from dwave.system.composites import VirtualGraphComposite
    >>> DWaveSampler().properties['extended_j_range']
    [-2.0, 1.0]
    >>> embedding = {'x': {1}, 'y': {5}, 'z': {0, 4}}
    >>> sampler = VirtualGraphComposite(DWaveSampler(), embedding)
    >>> sampler.parameters
    {u'anneal_offsets': ['parameters'],
     u'anneal_schedule': ['parameters'],
     u'annealing_time': ['parameters'],
     u'answer_mode': ['parameters'],
     'apply_flux_bias_offsets': [],
     u'auto_scale': ['parameters'],
    >>>  # Snipped above response for brevity

Note that the composed sampler (VirtualGraphComposite in the example) inherits properties
from the child sampler (DWaveSampler).

See the system documentation for more information.
