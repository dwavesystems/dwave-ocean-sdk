.. _solving_problems:

==============================
Overview of the Ocean Workflow
==============================

This section explains some of the basics of how you can use D-Wave quantum computers
to solve problems and how Ocean tools can help.

How a D-Wave System Solves Problems
===================================

For quantum computing, as for classical, solving a problem requires that it
be formulated in a way the computer and its software understand.

For example, if you want your laptop to calculate the area of a $1 coin, you might
express the problem as an equation, :math:`A=\pi r^2`, that you program as
:code:`math.pi*13.245**2` in your Python CLI. For a laptop with Python software,
this formulation---a particular string of alphanumeric symbols---causes the manipulation
of bits in a CPU and memory chips that produces the correct result.

The D-Wave system uses a quantum processing unit (QPU) to solve a :term:`binary quadratic model` (BQM)\ [#]_\ :
given :math:`N` variables :math:`x_1,...,x_N`, where each variable
:math:`x_i` can have binary values :math:`0` or :math:`1`, the system finds assignments of
values that minimize

.. math::

    \sum_i^N q_ix_i + \sum_{i<j}^N q_{i,j}x_i  x_j

where :math:`q_i` and :math:`q_{i,j}` are configurable (linear and quadratic) coefficients.
To formulate a problem for the D-Wave system is to program :math:`q_i` and :math:`q_{i,j}` so
that assignments of :math:`x_1,...,x_N` also represent solutions to the problem.

.. [#] The "native" forms of BQM programmed into a D-Wave system are the :term:`Ising` model
       traditionally used in statistical mechanics and its computer-science equivalent,
       shown here, the :term:`QUBO`.

Ocean software can abstract away much of the mathematics and programming for some types of problems.
At its heart is a binary quadratic model (BQM) class that together with other Ocean tools helps
formulate various optimization problems.
It also provides an API to binary quadratic :term:`sampler`\ s (the component used to minimize a BQM
and therefore solve the original problem), such as the D-Wave system and classical algorithms
you can run on your computer.

The following sections describe this problem-solving procedure in
two steps (plus a third that may benefit some problems); see the :ref:`gs`
examples and system documentation for further description.

1. :ref:`formulating`.
2. :ref:`submitting`.
3. :ref:`improving`, if needed, using advanced features.

.. figure:: ../_images/SolutionOverview.png
   :name: SolutionOverview
   :alt: image
   :align: center
   :scale: 80 %

   Solution steps: (1) a problem known in "problem space" (a circuit
   of Boolean gates, a graph, a network, etc) is formulated as a BQM, mathematically or using
   Ocean functionality and (2) the BQM is sampled for solutions.

.. _formulating:

Formulate the Problem as a BQM
==============================

There are different ways of mapping between a problem---chains of amino acids
forming 3D structures of folded proteins, traffic in the streets of Beijing, circuits
of binary gates---and a BQM to be solved (by sampling) with a D-Wave system or locally on
your CPU/GPU.

For example, consider the problem of determining outputs of a Boolean logic circuit. In its original
context (in "problem space"), the circuit might be described with input and output voltages,
equations of its component resistors, transistors, etc, an equation of logic symbols,
multiple or an aggregated truth table, and so on. You can choose to use Ocean software to formulate
BQMs for binary gates directly in your code or mathematically formulate a BQM, and both
can be done in different ways too; for example, a BQM for each gate or one BQM for
all the circuit's gates.

The following are two example formulations.

1. The :ref:`not` example, takes a NOT gate represented symbolically as
   :math:`x_2 \Leftrightarrow \neg x_1` and formulates it mathematically as the following BQM:

   .. math::

       -x_1 -x_2  + 2x_1x_2

   The table below shows that this BQM has lower values for valid states of the NOT
   gate (e.g., :math:`x_1=0, x_2=1`) and higher for invalid states (e.g., :math:`x_1=0, x_2=0`).

   .. table:: Boolean NOT Operation Formulated as a BQM.
      :name: BooleanNOTasQUBO

      ===========  ============  ===============  ============
      :math:`x_1`  :math:`x_2`   **Valid?**       **BQM Value**
      ===========  ============  ===============  ============
      :math:`0`    :math:`1`     Yes              :math:`0`
      :math:`1`    :math:`0`     Yes              :math:`0`
      :math:`0`    :math:`0`     No               :math:`1`
      :math:`1`    :math:`1`     No               :math:`1`
      ===========  ============  ===============  ============

2. Ocean's :doc:`dwavebinarycsp </docs_binarycsp/sdk_index>` tool enables the
   following formulation of an AND gate as a BQM:

   .. code-block:: python

       >>> import dwavebinarycsp
       >>> import dwavebinarycsp.factories.constraint.gates as gates
       >>> csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
       >>> csp.add_constraint(gates.and_gate(['x1', 'x2', 'y1']))  # add an AND gate
       >>> bqm = dwavebinarycsp.stitch(csp)

Once you have a BQM that represents your problem, you sample it for solutions.

.. _submitting:

Solve the BQM with a Sampler
============================

To solve your problem, now represented as a binary quadratic model, you submit it to
a classical, quantum, or quantum-classical hybrid :term:`sampler`.

* :ref:`using_hybrid` describes submitting your problem to a quantum-classical hybrid solver.
* :ref:`using_cpu` describes submitting your problem to a classical solver.
* :ref:`using_qpu` describes submitting your problem to a D-Wave QPU.

For example, the BQM of the AND gate created above may look like this:

>>> bqm     # doctest: +SKIP
BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0},
...                  {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0},
...                  -1.5,
...                  Vartype.BINARY)

The members of the two dicts are linear and quadratic coefficients, respectively,
the third term is a constant offset associated with the model, and the fourth
shows the variable types in this model are binary.

>>> from dwave.system import LeapHybridSampler
>>> sampler = LeapHybridSampler(solver={'category': 'hybrid'})    # doctest: +SKIP
>>> answer = sampler.sample(bqm)   # doctest: +SKIP
>>> print(answer)    # doctest: +SKIP
x1 x2 y1 energy num_oc.
0  0  1  0   -1.5       1
['BINARY', 1 rows, 1 samples, 3 variables]

.. _improving:

Improve the Solutions
=====================

More complex problems than the ones shown above can benefit from some of the D-Wave system's
advanced features and Ocean software's advanced tools.

The mapping from problem variables to qubits, :term:`minor-embedding`, can significantly
affect performance. Ocean tools perform this mapping heuristically so simply rerunning
a problem might improve results. Advanced users may customize the mapping by directly
using the :doc:`minorminer </docs_minorminer/source/sdk_index>` tool, setting
a minor-embedding themselves (or some combination), or using
D-Wave's :doc:`problem-inspector </docs_inspector/sdk_index>` tool.

For example, consider the solution to the AND problem on a D-Wave QPU demonstrated
in :ref:`using_qpu`.

.. note:: The next code requires the use of Ocean's problem inspector.

>>> import dwave.inspector
>>> dwave.inspector.show(response)   # doctest: +SKIP

.. figure:: ../_static/inspector_AND2.png
  :name: inspector_AND2
  :scale: 50 %
  :alt: View rendered by Ocean's problem inspector.

  View of the logical and embedded problem rendered by Ocean's problem inspector. The AND gate's original BQM is represented on the left; its embedded representation, on the right, shows a two-qubit chain (qubits 176 and 180) for variable :math:`x2`. The tool is helpful in visualizing the quality of your embedding.

D-Wave systems offer features such as spin-reversal (gauge) transforms and anneal offsets,
which reduce the impact of possible analog and systematic errors.

You can see the parameters and properties a sampler supports. For example, Ocean's
:doc:`dwave-system </docs_system/sdk_index>` lets you use the
D-Wave's *virtual graphs* feature to simplify minor-embedding. The following example
maps a problem's variables x, y to qubits 1, 5 and variable z to two qubits 0 and 4,
and checks some features supported on the D-Wave system used as a sampler.

.. attention::
   D-Wave's *virtual graphs* feature can require many seconds of D-Wave system time to calibrate
   qubits to compensate for the effects of biases. If your account has limited
   D-Wave system access, consider using *FixedEmbeddingComposite()* instead.

.. code-block:: python

    >>> from dwave.system import DWaveSampler
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

Note that the composed sampler (:code:`VirtualGraphComposite()` in the last example)
inherits properties from the child sampler (:code:`DWaveSampler()` in that example).

See the resources under :ref:`additional_tutorials` and the
`System Documentation <https://docs.dwavesys.com/docs/latest/index.html>`_
for more information.
