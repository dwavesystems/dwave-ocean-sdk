.. _qpu_intro_classical:

=================
Classical Solvers
=================

.. todo:: add the README info from dwave-samplers
    (https://docs.ocean.dwavesys.com/en/stable/docs_samplers/index.html)

:ref:`Ocean software <index_ocean_sdk>` provides a variety of classical solvers.
You might use a classical solver while developing your code or on a small
version of your problem to verify your code. Some are designed to help with code
development and debugging by deterministically solving small problems, others
can performantly provide good solutions to a wide range of problems.

Such solvers often require fewer or simpler steps to use than directly using
quantum computers and can make a good starting points in developing your
application code. For example, such solvers are unstructured, meaning you do not
have to map the connectivity of your problem's variables to a
:term:`working graph` of the solver (as you would :term:`minor-embed` problems
for a quantum computer).

Although classical solvers are useful for testing code during development, they
might not be sufficiently performant on the hard problems of a production
application. At that point in your code development you might incorporate either
a QPU solver or a hybrid solver.

Classical solvers may be :ref:`determinstic <qpu_intro_classical_deterministic>`
or :ref:`heuristic <qpu_intro_classical_heuristic>`.

.. _qpu_intro_classical_deterministic:

Deterministic Classical Solvers
===============================

During code development and debugging, it can be helpful to have the capability
to exactly solve small test problems, to ensure the best solution is in fact the
global optimum and display the energy gaps between states.

Solvers such as :ref:`dimod <index_dimod>`\ 's
:class:`~dimod.reference.samplers.ExactSolver` and
:class:`~dimod.reference.samplers.ExactPolySolver` brute-force solve problems,
making them slow on any but small problems. For testing, however, they can be
invaluable.

Example
-------

Among several samplers provided in the :doc:`dimod <index_dimod>` tool for
testing your code locally, is the :class:`~dimod.reference.samplers.ExactSolver`
that calculates the energy of all possible samples for a given problem. Such a
sampler can solve a small three-variable problem such as a BQM representing a
Boolean AND gate (see also the :ref:`ocean_workflow_formulating_bqm` section)
as follows:

>>> from dimod.generators import and_gate
>>> from dimod import ExactSolver
>>> bqm = and_gate('in1', 'in2', 'out')
>>> sampler = ExactSolver()
>>> sampleset = sampler.sample(bqm)
>>> print(sampleset)       # doctest: +SKIP
  in1 in2 out energy num_oc.
0   0   0   0    0.0       1
1   1   0   0    0.0       1
3   0   1   0    0.0       1
5   1   1   1    0.0       1
2   1   1   0    2.0       1
4   0   1   1    2.0       1
6   1   0   1    2.0       1
7   0   0   1    6.0       1
['BINARY', 8 rows, 8 samples, 3 variables]

Note that the first four samples are the valid states of the AND gate and have
lower values than the second four, which represent invalid states.

If you use a classical solver running locally on your CPU, a single sample might
provide the optimal solution.

.. _qpu_intro_classical_heuristic:

Heuristic Classical Solvers
===========================

While solutions produced by deterministic solvers are guaranteed to include the
problem's ground states (globally optimal solution), such solvers are limited
to small-sized problems. Classical heuristic solvers can solvers much larger
problems and can often do so performantly.

:ref:`Ocean software <index_ocean_sdk>` provides heuristic classical solvers
that implement various algorithms, such as simulated annealing, tabu search,
and steepest descent (see the :ref:`index_samplers` section).

.. todo:: verify the link above and below to
    https://docs.ocean.dwavesys.com/en/stable/docs_samplers/index.html

Examples
--------

This example solves a two-variable problem using the
:ref:`dwave-samplers <index_samplers>` simulated annealing sampler. For such a
small problem, :code:`num_reads=10` most likely finds the optimal solution.

>>> from dwave.samplers import SimulatedAnnealingSampler
>>> solver = SimulatedAnnealingSampler()
>>> sampleset = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1}, num_reads=10)
>>> sampleset.first.sample["a"] == sampleset.first.sample["b"] == -1
True

This example finds a maximum
`independent set <https://en.wikipedia.org/wiki/Independent_set_(graph_theory)>`_
on a 77-node graph with two different hueristic classical samplers and validates
the best solution found by comparison.

>>> import networkx as nx
>>> import dimod
>>> from dwave.samplers import SimulatedAnnealingSampler, TabuSampler
...
>>> G = nx.generators.les_miserables_graph()
>>> bqm = dimod.generators.maximum_independent_set(G.edges, G.nodes)
>>> len(bqm)
77
>>> sampleset_sa = SimulatedAnnealingSampler().sample(bqm, num_reads=10)
>>> sampleset_tabu = TabuSampler().sample(bqm, num_reads=100)
>>> sum(sampleset_sa.first.sample.values())                    # doctest: +SKIP
35
>>> sum(sampleset_tabu.first.sample.values())                  # doctest: +SKIP
35
>>> [key for key, val in sampleset_sa.first.sample.items() if val][0:5] # doctest: +SKIP
['Anzelma', 'BaronessT', 'Boulatruelle', 'Brujon', 'Champtercier']

Reformulation
=============

The :ref:`qpu_reformulating` section provides guidance on formulating your
problem as a model; some of that content applies to classical solvers too,
especially those that accept binary quadratic models.
Although, for example, limitations on problem size are vastly expanded compared
to QPU solvers, formulations that proliferate ancillary variables might still
perform less well than alternative formulations.

