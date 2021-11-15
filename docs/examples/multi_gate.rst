.. _multi_gate:

=====================
Multiple-Gate Circuit
=====================

This example solves a logic-circuit problem on a D-Wave quantum computer. It
expands on the discussion in the :ref:`and` example about the effect of
:term:`minor-embedding` on performance.

.. raw::  latex

    \begin{figure}
    \begin{centering}
    \begin{circuitikz}

    \node (in1) at (0, 6.3) {$a$};
    \node (in2) at (0, 5) {$b$};
    \node (in3) at (0, 2.7) {$c$};
    \node (in4) at (0, 1) {$d$};

    \node(out1) at  (10.5, 4.1) {$z$} ;

    \draw

    (1.75,5) node[not port] (mynot1) {1}
    (2.25,3) node[or port] (myor2) {2}

    (5,6) node[and port] (myand3) {3}
    (5,1) node[or port] (myor4) {4}

    (7,5) node[and port] (myand5) {5}
    (7,1) node[not port] (mynot6) {6}

    (9.25,4) node[or port] (myor7) {7}

    (0.1, 6.25) -- (myand3.in 1)
    (0.1, 5) -- (mynot1.in)
    (0.1, 5) -| (myor2.in 1)
    (0.1, 2.7) -- (myor2.in 2)
    (0.1, 0.75) -- (myor4.in 2)

    (mynot1.out) |- (myand3.in 2)
    (myor2.out) |- (myor4.in 1)
    (myand3.out) |- (myand5.in 1)
    (myor4.out) |- (myand5.in 2)
    (myor4.out) |- (mynot6.in)
    (myand5.out) |- (myor7.in 1)
    (mynot6.out) |- (myor7.in 2)

    (myor7.out) -- (10.4, 4.0);

    \end{circuitikz}\\

    \end{centering}

    \caption{Logic circuit that implements $z=a \overline{b} c + $a \overline{b}
     c + b \overline{d} + c \overline{d}.}
    \label{fig:logicCircuit}
    \end{figure}

    A simple circuit is shown in Figure \ref{fig:logicCircuit}.

.. figure:: ../_images/MultiGateCircuit.png
   :name: Problem_MultiGateCircuit
   :alt: image
   :align: center
   :scale: 90 %

   Circuit with 7 logic gates, 4 inputs (:math:`a, b, c, d`), and 1 output (:math:`z`).
   The circuit implements function :math:`z = \overline{b} (ac + ad + \overline{c}\overline{d})`.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in
  :ref:`sapi_access`
* Ocean tools :doc:`dimod </docs_dimod/sdk_index>` and
  :doc:`dwave-system </docs_system/sdk_index>`. For the
  optional graphics, you will also need `Matplotlib <https://matplotlib.org>`_
  and :doc:`problem-inspector </docs_inspector/sdk_index>`.

.. include:: hybrid_solver_service.rst
  :start-after: example-requirements-start-marker
  :end-before: example-requirements-end-marker

Formulating the Problem as a CSP
================================

Other examples (:ref:`not` and :ref:`and`) show how a Boolean gate is
represented as a *constraint satisfaction problem* (:term:`CSP`) on a quantum
computer. This example does the same for multiple gates that constitute a circuit.

Small-Circuit Problem
---------------------

The code below uses common Boolean gates provided by
:doc:`dimod </docs_dimod/sdk_index>` BQM generators, represents the NOT
operation by flipping the relevant variable, and sums the BQMs. The resulting
aggregate BQM has its lowest value for variable assignments that satisfy all the
constraints representing the circuit's Boolean gates.

>>> from dimod.generators import and_gate, or_gate
...
>>> bqm2 = or_gate('b', 'c', 'out2')
>>> bqm3 = and_gate('a', 'b', 'out3')
>>> bqm3.flip_variable('b')
>>> bqm4 = or_gate('out2', 'd', 'out4')
>>> bqm5 = and_gate('out3', 'out4', 'out5')
>>> bqm7 = or_gate('out5', 'out4', 'z')
>>> bqm7.flip_variable('out4')
...
>>> bqm = bqm2 + bqm3 + bqm4 + bqm5 + bqm7
>>> print(bqm.num_variables)
9

This circuit is small enough to solve by brute force. The following code prints
solutions in which the circuit's output, :math:`z` is true.

>>> from dimod import ExactSolver
>>> solutions = ExactSolver().sample(bqm).lowest()
>>> z = []
>>> out_fields = [key for key in list(next(solutions.data(['sample'])))[0].keys() if 'out' in key]
>>> for datum in solutions.data(['sample', 'energy']):
...    if datum.sample['z'] == 1:
...       for key in out_fields:
...          _ = datum.sample.pop(key)
...       z.append(datum.sample)
>>> for solution in z:
...   print(solution)
{'a': 1, 'b': 0, 'c': 0, 'd': 1, 'z': 1}
{'a': 1, 'b': 0, 'c': 1, 'd': 1, 'z': 1}
{'a': 1, 'b': 0, 'c': 1, 'd': 0, 'z': 1}
{'a': 1, 'b': 0, 'c': 0, 'd': 0, 'z': 1}
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'z': 1}

However, such brute-force methods are not effective for much larger problems.

Large-Circuit Problem
---------------------

In the figure below, the 7-gates circuit solved above is replicated with the
outputs connected through a series of XOR gates.

.. figure:: ../_images/MultiGateCircuit_3Instances.png
   :name: Problem_MultiGateCircuit_3Instances
   :alt: image
   :align: center
   :scale: 90 %

   Multiple replications of the 7-gates circuit (:math:`z = \overline{b} (ac + ad + \overline{c}\overline{d})`) connected by XOR gates.

The :code:`circuit_bqm` function replicates the BQM of the 7-gates circuit above
for a specified number of circuits, connecting the outputs through a cascade of
XOR gates.

>>> from dimod import BinaryQuadraticModel, quicksum
>>> from dimod.generators import and_gate, or_gate, xor_gate
...
>>> def circuit_bqm(n: int = 3) -> BinaryQuadraticModel:
...       "Create a BQM for n replications of the 7-gate circuit."
...
...       if n < 2:
...          raise ValueError("n must be at least 2")
...
...       bqm2 = [or_gate(f"b_{c}", f"c_{c}", f"out2_{c}") for c in range(n)]
...       bqm3 = [and_gate(f"a_{c}", f"b_{c}", f"out3_{c}") for c in range(n)]
...       [bqm.flip_variable("b_{}".format(indx)) for indx, bqm in enumerate(bqm3)]
...       bqm4 = [or_gate(f"out2_{c}", f"d_{c}", f"out4_{c}") for c in range(n)]
...       bqm5 = [and_gate(f"out3_{c}", f"out4_{c}", f"out5_{c}") for c in range(n)]
...       bqm7 = [or_gate(f"out5_{c}", f"out4_{c}", f"z_{c}") for c in range(n)]
...       [bqm.flip_variable("out4_{}".format(indx)) for indx, bqm in enumerate(bqm7)]
...       bqm_z = [xor_gate("z_0", "z_1", "zz0", "aux0")] + [
...                xor_gate(f"z_{c}", f"zz{c-2}", f"zz{c-1}", f"aux{c-1}") for c in range(2, n)]
...       return quicksum(bqm2 + bqm3 + bqm4 + bqm5 + bqm7 + bqm_z)

Create a BQM for six replications of the circuit. For this aggregated circuit,
the number of variables has increased to 64.

>>> num_circuits = 6
>>> bqm = circuit_bqm(num_circuits)
>>> print(bqm.num_variables)
64

Minor-Embedding and Sampling
============================

The :ref:`and` example used the :class:`~dwave.system.composites.EmbeddingComposite`
composite to :term:`minor-embed` its unstructured problem. That composite runs
a :ref:`minorminer algorithm <sdk_index_minorminer>` to find a minorembedding
each time you submit a problem.

However, for some applications the submitted problems might be related or limited
in size in such a way that you can find a common minor embedding for the entire
set of problems you wish to submit. For the current problem, for example, you
might wish to submit the same circuit multiple times while each time fixing
inputs to zero or one in various configurations.

The next code sets up a D-Wave system as the sampler using both the
:class:`~dwave.system.composites.EmbeddingComposite` class and the
:class:`~dwave.system.samplers.DWaveCliqueSampler` class.

.. include:: min_vertex.rst
   :start-after: default-config-start-marker
   :end-before: default-config-end-marker

>>> from dwave.system import DWaveSampler, EmbeddingComposite, DWaveCliqueSampler
...
>>> sampler1 = EmbeddingComposite(DWaveSampler(solver=dict(topology__type='pegasus')))
>>> sampler2 = DWaveCliqueSampler(solver=dict(name=sampler1.child.solver.name))

Performance Comparison: Embedding Time
--------------------------------------

The :class:`~dwave.system.samplers.DWaveCliqueSampler` class can save time
if you submit a sequence of problems that are sub-graphs of a clique embedding
found by the composite on a QPU. The table below shows the minor-embedding
times\ [#]_ for a series on random problems of increasing size\ [#]_. Some
differences of interest are highlighted in bold.

You can see below that while the first submission is slow for the
:class:`~dwave.system.samplers.DWaveCliqueSampler` class, subsequent submissions
are fast. For the :class:`~dwave.system.composites.EmbeddingComposite` class, the
time depends on the size and complexity of each problem, can vary between
submissions of the same problem, and each submission incurs the cost of finding
an embedding anew.

.. list-table:: Minor-Embedding Times
   :widths: 20 10 10 30
   :header-rows: 1

   * - Problem Size: Nodes (Edges)
     - :class:`~dwave.system.composites.EmbeddingComposite`
     - :class:`~dwave.system.samplers.DWaveCliqueSampler`
     - Notes
   * - 10 (5)
     - **0.06**
     - **152.7**
     - :class:`~dwave.system.samplers.DWaveCliqueSampler` calculates all clique
       embeddings for the QPU
   * - 20 (10)
     - 0.41
     - 0.11
     -
   * - 30 (15)
     - 1.39
     - 0.11
     -
   * - 40 (20)
     - 3.88
     - 0.13
     -
   * - 50 (25)
     - 9.7
     - 0.14
     -
   * - 60 (30)
     - 17.91
     - 0.16
     -
   * - 70 (35)
     - 22.02
     - 0.19
     -
   * - 80 (40)
     - **73.74**
     - **0.25**
     -
   * - 90 (45)
     - 65.05
     - 0.22
     -
   * - 100 (50)
     - 28.92
     - 0.25
     - For this instance, :class:`~dwave.system.composites.EmbeddingComposite`
       found a good embedding quickly; other executions might not.

.. [#] The times are approximate: the code measured the blocking time when
   submitting problems, in which minor-embedding is the major component.

.. [#]

  The code below can take several minutes to run. Uncommenting the print statements
  lets you view the execution's progress. Note that if you have already
  executed a submission with :class:`~dwave.system.samplers.DWaveCliqueSampler`,
  your cache might need to be cleared with the
  :func:`minorminer.busclique.busgraph_cache.clear_all_caches`
  function.

  >>> import time
  >>> import networkx as nx
  ...
  >>> samplers = {"sampler1": sampler1, "sampler2": sampler2}
  >>> times = {key: [] for key in samplers.keys()}
  >>> for name, sampler in samplers.items():
  ...    for i in range(10):
  ...       nodes = 10 + 10*i
  ...       edges = 5 + 5*i
  ...       G = nx.random_regular_graph(n=nodes, d=edges)
  ...       # print("Submitting problem of {} nodes and {} edges to sampler {}".format(nodes, edges, name))
  ...       times[name].append(time.time())
  ...       sampler.sample_ising({}, {edge: 1 for edge in G.edges})
  ...       times[name][i] = time.time() - times[name][i]


Performance Comparison: Solution Quality
----------------------------------------


>>> import dwave.inspector


Algorithmic minor-embedding is heuristic---solution results vary significantly based on
the minor-embedding found.
