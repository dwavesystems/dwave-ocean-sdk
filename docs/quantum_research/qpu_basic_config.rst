.. _qpu_basic_config:

=======================
Basic QPU Configuration
=======================

Setting appropriate parameters can be both hard and crucial to finding good
solutions. The :ref:`qpu_solver_parameters` section describes the parameters you
can configure on the QPU and the :ref:`qpu_solver_configuration` section
provides guidance on best practices.

This section shows some minimal configuration parameters to get you started.

.. _qpu_basic_config_num_reads:

num_reads
=========

Consider the outcome of submitting the *exactly-one-true* constraint of the
:ref:`qpu_example_constrained_xnor` section without specifying the number of
anneals.

.. testcode::

    from dwave.system import DWaveSampler, EmbeddingComposite
    sampler = EmbeddingComposite(DWaveSampler())
    Q = {('a', 'a'): -1, ('b', 'b'): -1, ('c', 'c'): -1,
         ('a', 'b'): 2, ('b', 'c'): 2, ('a', 'c'): 2}
    sampleset = sampler.sample_qubo(Q)

The single run above returned a solution that is correct but incomplete in that
it is one of three possible ground states:

>>> print(sampleset)                         # doctest: +SKIP
   a  b  c energy num_oc. chain_.
0  0  1  0   -1.0       1     0.0
['BINARY', 1 rows, 1 samples, 3 variables]

For harder problems, the number of anneals you request might determine whether
or not you see correct or good solutions at all.

.. _qpu_basic_config_auto_scale:

auto_scale
==========

In the :ref:`qpu_example_unconstrained_sat` section, you develop a QUBO for a
simple SAT problem,

.. math::

    E(q_i) = 0.1 q_1 + 0.1 q_2 - 0.2 q_1 q_2,

where :math:`a_1 = a_2 = 0.1` is set to an arbitrary positive number.

Consider now assigning a value of 0.5 to the qubit biases and likewise
multiplying the coupler strength fivefold to -1, uniformly scaling the
objective function by 5. The scaled QUBO is now,

.. math::

    E(q_i) = 0.5 q_1 + 0.5 q_2 - q_1 q_2

This objective function also favors states 0 and 4, but the objective value
for the excited states is now 0.5 rather than 0.1 previously:

======== ============= =================== =======================
State    :math:`q_1`   :math:`q_2`         Objective Value
======== ============= =================== =======================
1        0             0                   0
2        0             1                   0.5
3        1             0                   0.5
4        1             1                   0
======== ============= =================== =======================

Recall that the previous objective function returned results that included a
small fraction of excited states. One might expect that increasing the value
(penalty) of the objective function for the excited states---enlarging the
energy gap between the ground state and excited states---would make the excited
states harder to reach and therefore less probable.

In fact problems submitted to a QPU solver can benefit from an
*autoscaling* feature: each QPU has an allowed range of values for its qubit
biases and coupler strengths (:math:`a` and :math:`b` in the QUBO format); by
default, the system adjusts the :math:`a` and :math:`b` values of submitted
problems to make use of the entire available range before configuring the QPU's
biases and coupler strengths.

You can explicitly disable autoscaling (:code:`auto_scale=False`). Below are
results for submitting both QUBOs with and without autoscaling.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())
...
>>> # Define QUBOs
>>> Q1 = {('q1', 'q1'): 0.1, ('q2', 'q2'): 0.1, ('q1', 'q2'): -0.2}
>>> Q2 = {('q1', 'q1'): 0.5, ('q2', 'q2'): 0.5, ('q1', 'q2'): -1}
...
>>> # Autoscaling on for original QUBO
>>> sampleset = sampler.sample_qubo(Q1, num_reads=5000)
>>> print(sampleset)                         # doctest: +SKIP
  q1 q2 energy num_oc. chain_.
0  0  0    0.0    2764     0.0
1  1  1    0.0    2233     0.0
2  0  1    0.1       1     0.0
3  1  0    0.1       2     0.0
['BINARY', 4 rows, 5000 samples, 2 variables]
...
>>> # Autoscaling on for scaled-up QUBO
>>> sampleset = sampler.sample_qubo(Q2, num_reads=5000)
>>> print(sampleset)                       # doctest: +SKIP
  q1 q2 energy num_oc. chain_.
0  0  0    0.0    3429     0.0
1  1  1    0.0    1570     0.0
2  0  1    0.5       1     0.0
['BINARY', 3 rows, 5000 samples, 2 variables]
...
>>> # Autoscaling off for original QUBO
>>> sampleset = sampler.sample_qubo(Q1, num_reads=5000, auto_scale=False)
>>> print(sampleset)                      # doctest: +SKIP
  q1 q2 energy num_oc. chain_.
0  0  0    0.0    1603     0.0
1  1  1    0.0    1669     0.0
2  0  1    0.1     824     0.0
3  1  0    0.1     904     0.0
['BINARY', 4 rows, 5000 samples, 2 variables]
...
>>> # Autoscaling off for scaled-up QUBO
>>> sampleset = sampler.sample_qubo(Q2, num_reads=5000, auto_scale=False)
>>> print(sampleset)                         # doctest: +SKIP
  q1 q2 energy num_oc. chain_.
0  0  0    0.0    2773     0.0
1  1  1    0.0    2000     0.0
2  1  0    0.5     103     0.0
3  0  1    0.5     124     0.0
['BINARY', 4 rows, 5000 samples, 2 variables]

With autoscaling (the default), the two problems are run on the QPU with the
same qubit biases and coupling strengths and therefore return similar
solutions. (The energies and objective values reported are for the pre-scaling
values.) With autoscaling disabled, the first problem, with its smaller energy
gap, returns more samples of the excited states.

.. _qpu_basic_config_chain_strength:

chain_strength
==============

Although not a parameter of |dwave_short| solvers, :code:`chain_strength`---a
parameter used by some Ocean tools submitting problems to quantum
samplers---may also be crucial to successfully solving some problems.

The :ref:`qpu_example_constrained_xnor` section explains that for a chain of
qubits to represent a variable, all its constituent qubits must return the same
value for a sample, and that this is accomplished by setting a strong coupling
to the edges connecting these qubits. It set a value that was a bit stronger
than the coupler strength representing edges of the problem.

The last statement might have raised the question, Why not simply maximize the
coupling strength for all qubits in all chains? Now, having learnt about the
:ref:`qpu_basic_config_auto_scale` parameter, you can understand the answer.

In the problem of the :ref:`qpu_example_constrained_xnor` section, the values
set for the problem are:

*   qubit biases: -1 and 1,
*   coupler strengths between qubits representing variables: 2
*   coupler strength between qubits of a chain: -3

Consider a simplified QPU that has a range of -1 to 1 for both biases and
coupler strengths. For the maximum value of -3 to fit into the range, it must
be scaled down to -1 (i.e., divided by 3). The scaled problem programmed on
such a QPU has values:

*   qubit biases: :math:`\frac{-1}{3}` and :math:`\frac{1}{3}`
*   coupler strengths between qubits representing variables:
    :math:`\frac{2}{3}`
*   coupler strength between qubits of a chain: -1

If you instead were to use a chain strength of -10, the programmed values are
now:

*   qubit biases: :math:`\frac{-1}{10}` and :math:`\frac{1}{10}`
*   coupler strengths between qubits representing variables:
    :math:`\frac{2}{10}`
*   coupler strength between qubits of a chain: -1

Notice that the difference between positive and negative qubit biases has
shrunk from :math:`\frac{2}{3}` (:math:`\frac{1}{3}` - :math:`\frac{-1}{3}`) to
just 0.2, and likewise the coupling between qubits representing variables. The
QPU is not a high-precision digital computer, it is analog and
:ref:`noisy <qpu_errors>`. For problems with a variety of values for its linear
and quadratic coefficients, overly large chain strength degrades the problem
definition.

Ocean software tries to set smart default values for your chain strengths.
However, complex problems might require "tuning" of chain strengths to reach
acceptable solution quality.

Ocean software provides tools and information to help you find good values for
chain strengths when its default values are inadequate.

For example, you might see information on *broken chains* (chains with qubits
that are not all in a single state at the end of the anneal) in returned
solutions; if a high percentage of results have broken chains, you might need
to increase the coupler strengths; if no or few chains are broken, possibly
chain strengths are too strong.

Ocean software's :ref:`problem inspector <index_inspector>` is a tool for
visualizing problems submitted to, and answers received from, |dwave_short|
systems. It helps you see the chains and potential problems.

.. _qpu_basic_config_spin_reversal_transforms:

num_spin_reversal_transforms
============================

Although not a parameter of |dwave_short| solvers,
:code:`num_spin_reversal_transforms`---a parameter used by
:ref:`Ocean software <index_ocean_sdk>`\ 's
:class:`~dwave.preprocessing.composites.SpinReversalTransformComposite`
composite when submitting problems to quantum samplers---may be very helpful to
performance on some problems.

Notice that the results shown in the :ref:`qpu_basic_config_auto_scale` section
above tend to display some asymmetry between the two valid solutions. Qubits on
a QPU can be biased to some small degree in one direction or another. The
:ref:`qpu_config_srt` section guide, explains how spin-reversal
transforms can improve results by reducing the impact of analog errors that may
exist on the QPU.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> from dwave.preprocessing import SpinReversalTransformComposite
...
>>> sampler = EmbeddingComposite(SpinReversalTransformComposite(DWaveSampler()))
...
>>> Q1 = {('q1', 'q1'): 0.1, ('q2', 'q2'): 0.1, ('q1', 'q2'): -0.2}
>>> sampleset = sampler.sample_qubo(Q1, num_reads=500, num_spin_reversal_transforms=10)
>>> print(sampleset.aggregate())                                  # doctest: +SKIP
q1 q2 energy num_oc. chain_.
0  0  0    0.0    2538     0.0
1  1  1    0.0    2461     0.0
2  1  0    0.1       1     0.0
['BINARY', 3 rows, 5000 samples, 2 variables]

The rerunning of one of the :ref:`gsg_auto_scale` section's submissions above
produced results that are more symmetrical in this case. The use of this
composite has a cost of longer runtime.

Next Steps for Learning about Solver Parameters
===============================================

Once you have submitted a few first problems of your own to |dwave_short|
solvers, and you are ready to ensure your submissions are configured to produce
the best solutions, familiarize yourself with the solver parameters.

You can learn more about solver parameters here:

*   The :ref:`qpu_solver_parameters` section describes the parameters you can
    configure on the QPU.
*   The :ref:`qpu_solver_configuration` section provides guidance on best
    practices for using the QPU.