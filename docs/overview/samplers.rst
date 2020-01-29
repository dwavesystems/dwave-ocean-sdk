.. _samplers_and_solvers:

============================
Solving Problems by Sampling
============================

Having formulated your original problem, as described in the :ref:`solving_problems`
section, into a :term:`BQM`, you sample it for solutions. Ocean
software provides quantum, classical, and quantum-classical :term:`sampler`\ s that run
either remotely (for example, in D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_
environment) or locally on your CPU. These compute resources are known as
:term:`solver`\ s.

.. note:: Some classical samplers actually brute-force solve small problems rather
    than sample, and these are also referred to as "solvers".

.. _submitting:

Sample the BQM on a Solver
==========================

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

The example code below submits the BQM to a Leap hybrid solver. In this case,
:doc:`dimod </docs_dimod/sdk_index>`'s :class:`dimod.LeapHybridSampler` is the Ocean
sampler and the remote compute resource selected might be Leap hybrid solver
`hybrid_v1`.

>>> from dwave.system import LeapHybridSampler
>>> sampler = LeapHybridSampler(solver={'category': 'hybrid'})    # doctest: +SKIP
>>> answer = sampler.sample(bqm)   # doctest: +SKIP
>>> print(answer)    # doctest: +SKIP
x1 x2 y1 energy num_oc.
0  0  1  0   -1.5       1
['BINARY', 1 rows, 1 samples, 3 variables]

Several of the :ref:`gs` Examples section demonstrate solving problems on the
D-Wave system, starting from very simple and gradually increasing the complexity.


.. _improving:

Improve the Solutions
=====================

More complex problems than the ones shown above can benefit from some of the D-Wave system's
advanced features and Ocean software's advanced tools.

When sampling directly on the D-Wave QPU, the mapping from problem variables to qubits,
:term:`minor-embedding`, can significantly
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
