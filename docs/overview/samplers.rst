.. _samplers_and_solvers:

============================
Solving Problems by Sampling
============================

Having followed the steps of the :ref:`formulating_bqm` section, you sample the
:term:`BQM` that now represents your problem for solutions. Ocean software provides
quantum, classical, and quantum-classical hybrid :term:`sampler`\ s that run
either remotely (for example, in D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_
environment) or locally on your CPU. These compute resources are known as
:term:`solver`\ s.

.. note:: Some classical samplers actually brute-force solve small problems rather
    than sample, and these are also referred to as "solvers".

.. _submitting:

Sample the BQM on a Solver
==========================

Ocean's :term:`sampler`\ s enable you to submit your problem to remote or local
compute resources (:term:`solver`\ s) of different types:

* :ref:`using_hybrid` such as `Leap's <https://cloud.dwavesys.com/leap/>`_ 
  ``hybrid_binary_quadratic_model_version<x>`` solver or, for **discrete** 
  quadratic models (:term:`DQM`), ``hybrid_discrete_quadratic_model_version<x>`` 
* :ref:`using_cpu` such as :class:`~dimod.reference.samplers.ExactSolver` for 
  exact solutions to small problems
* :ref:`using_qpu` such the Advantage and D-Wave 2000Q systems.

The example code below submits the BQM of the AND gate of the :ref:`formulating_bqm` section,

>>> import dimod
>>> bqm = dimod.BinaryQuadraticModel({'x1': 0.0, 'x2': 0.0, 'y1': 6.0},
...                  {('x2', 'x1'): 2.0, ('y1', 'x1'): -4.0, ('y1', 'x2'): -4.0},
...                  0, 'BINARY')

to a Leap hybrid solver.
In this case, :doc:`dwave-system </docs_system/sdk_index>`'s
:class:`~dwave.system.samplers.LeapHybridSampler` is the Ocean sampler and the
remote compute resource selected might be Leap hybrid solver 
``hybrid_binary_quadratic_model_version<x>``.

>>> from dwave.system import LeapHybridSampler
>>> sampler = LeapHybridSampler()    # doctest: +SKIP
>>> answer = sampler.sample(bqm)   # doctest: +SKIP
>>> print(answer)    # doctest: +SKIP
x1 x2 y1 energy num_oc.
0  0  1  0    0.0       1
['BINARY', 1 rows, 1 samples, 3 variables]

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
a minor-embedding themselves, or using
D-Wave's :doc:`problem-inspector </docs_inspector/sdk_index>` tool.

For example, the :ref:`and` example submits the BQM representing an AND gate
to a D-Wave system, which requires mapping the problem's logical variables
to qubits on the QPU. The code below invokes D-Wave's
:doc:`problem-inspector </docs_inspector/sdk_index>` tool to visualize the
minor-embedding.

>>> import dwave.inspector
>>> dwave.inspector.show(response)   # doctest: +SKIP

.. figure:: ../_static/inspector_AND2.png
  :name: inspector_AND2
  :scale: 50 %
  :alt: View rendered by Ocean's problem inspector.

  View of the logical and embedded problem rendered by Ocean's problem inspector. The AND gate's original BQM is represented on the left; its embedded representation on a D-Wave 2000Q system, on the right, shows a two-qubit chain (qubits 176 and 180) for variable :math:`x2`. The tool is helpful in visualizing the quality of your embedding.

Example :ref:`pp_greedy` improves samples returned from a QPU by post-processing with a 
classical greedy algorthim. D-Wave systems offer features such as spin-reversal (gauge) 
transforms and anneal offsets, which reduce the impact of possible analog and systematic errors.

You can see the parameters and properties a sampler supports. For example, Ocean's
:doc:`dwave-system </docs_system/sdk_index>` lets you use the
D-Wave's *virtual graphs* feature to simplify minor-embedding. The following example
maps a problem's variables x, y to qubits 1, 5 and variable z to two qubits 0 and 4,
and checks some features supported on a D-Wave 2000Q system used as a sampler.

.. attention::
   D-Wave's *virtual graphs* feature can require many seconds of D-Wave system time to calibrate
   qubits to compensate for the effects of biases. If your account has limited
   D-Wave system access, consider using :class:`~dwave.system.composites.FixedEmbeddingComposite` 
   instead.

>>> from dwave.system import DWaveSampler, VirtualGraphComposite
>>> qpu = DWaveSampler(solver={'qpu': True, 'topology__type': 'chimera'})
>>> qpu.properties['extended_j_range']
[-2.0, 1.0]
>>> embedding = {'x': {1}, 'y': {5}, 'z': {0, 4}}
>>> sampler = VirtualGraphComposite(qpu, embedding)   # doctest: +SKIP
>>> sampler.parameters         # doctest: +SKIP
{u'anneal_offsets': ['parameters'],
 u'anneal_schedule': ['parameters'],
 u'annealing_time': ['parameters'],
 u'answer_mode': ['parameters'],
 'apply_flux_bias_offsets': [],
 u'auto_scale': ['parameters'], ...

Note that the composed sampler (:class:`~dwave.system.composites.VirtualGraphComposite` 
in the last example) inherits properties from the child sampler 
(:class:`~dwave.system.samplers.DWaveSampler` in that example).

See the resources under :ref:`additional_tutorials` and the
`System Documentation <https://docs.dwavesys.com/docs/latest/index.html>`_
for more information.
