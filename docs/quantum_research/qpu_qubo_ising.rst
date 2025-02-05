.. _qpu_qubo_ising:

======================
QUBOs and Ising Models
======================

The :ref:`qpu_quantum_annealing_intro` section explains how the |dwave_short|
QPU uses quantum annealing to find the minimum of an energy landscape defined by
the biases and couplings applied to its qubits in the form of a problem
Hamiltonian. As described in the :ref:`qpu_workflow` section, to solve a problem
by sampling, you formulate an :term:`objective function` such that when
the :term:`solver` finds its minimum, it is finding solutions to your problem.

This section describes the objective functions (the problem Hamiltonians) for
the |dwave_short| quantum computer. The linear and quadratic coefficients of
these models map to values of the qubits and couplers of the QPU.

Finally, the :ref:`qpu_qubo_ising_example` section gives a simple example.

.. todo:: consider consolidating and importing the ising & qubo definitions from
    concepts/models

.. _qpu_qubo_ising_bqm:

Binary Quadratic Models
=======================

For the QPU, two formulations for objective functions are the
:ref:`qpu_qubo_ising_ising` and :ref:`qpu_qubo_ising_qubo`. Both these
formulations are binary quadratic models and conversion between them is
trivial, as shown in the :ref:`qpu_qubo_ising_transformations` section.

.. _qpu_qubo_ising_ising:

Ising Model
-----------

The Ising model is traditionally used in statistical mechanics. Variables are
"spin up" (:math:`\uparrow`) and "spin down" (:math:`\downarrow`), states that
correspond to :math:`+1` and :math:`-1` values. Relationships between the spins,
represented by couplings, are correlations or anti-correlations. The objective
function expressed as an Ising model is as follows:

.. math::

    \text{E}_{ising}(\vc s) = \sum_{i=1}^N h_i s_i +
    \sum_{i=1}^N \sum_{j=i+1}^N J_{i,j} s_i s_j

where the linear coefficients corresponding to qubit biases are :math:`h_i`,
and the quadratic coefficients corresponding to coupling strengths are
:math:`J_{i,j}`.

.. _qpu_qubo_ising_qubo:

QUBO
----

QUBO problems are traditionally used in computer science, with variables taking
values 1 (TRUE) and 0 (FALSE).

A QUBO problem is defined using an upper-diagonal matrix :math:`Q`, which is an
:math:`N` x :math:`N` upper-triangular matrix of real weights, and :math:`x`, a
vector of binary variables, as minimizing the function

.. math::

    f(x) = \sum_{i} {Q_{i,i}}{x_i} + \sum_{i<j} {Q_{i,j}}{x_i}{x_j}

where the diagonal terms :math:`Q_{i,i}` are the linear coefficients and the
nonzero off-diagonal terms  :math:`Q_{i,j}` are the quadratic coefficients.

This can be expressed more concisely as

.. math::

    \min_{{x} \in {\{0,1\}^n}} {x}^{T} {Q}{x}.

In scalar notation, the objective function expressed as a QUBO is as follows:

.. math::

    \text{E}_{qubo}(a_i, b_{i,j}; q_i) = \sum_{i} a_i q_i +
    \sum_{i<j} b_{i,j} q_i q_j.

.. note::
    Quadratic unconstrained binary optimization problems---QUBOs---are
    *unconstrained* in that there are no constraints on the variables other
    than those expressed in *Q*.

.. _qpu_qubo_ising_example:

Example: Formulate an Ising Model
=================================

The problem is to formulate a BQM that represents "the value of :math:`v_1`
should be identical to the value of :math:`v_2`", where :math:`v_1` and
:math:`v_2` are binary-valued variables.\ [#]_

.. [#]
    This could be one small part of a larger problem, for example, an
    `integer_factorization <https://en.wikipedia.org/wiki/Integer_factorization>`_
    problem formulated with Boolean gates, as demonstrated in the
    `Leap service <https://cloud.dwavesys.com/leap/>`_ demo and
    `Factoring Jupyter Notebook <https://github.com/dwave-examples/factoring-notebook>`_.
    The larger problem is to satisfy a constraint that two variables
    representing factors be assigned values such that their multiplication
    equals the factored number. The constraint of this section's example might
    represent a connection between two gates of such a formulation of the
    factoring problem.

Step 1 is to state just a constraint, :math:`v_1` equals :math:`v_2`.

Step 2 is just to write the constraint as either an equation or a truth table
(the problem's variables are already binary valued).

This example shows both: the constraint as an equation is simply,
:math:`v_1 = v_2`, and below it is represented as a truth table (notice that
for an Ising formulation the values are :math:`\{-1, 1\}` rather than
:math:`\{0, 1\}`).

======== ============= =================== =======================
State    :math:`v_1`   :math:`v_2`         :math:`v_1 = v_2`
======== ============= =================== =======================
1        -1            -1                  True
2        -1            1                   False
3        1             -1                  False
4        1             1                   True
======== ============= =================== =======================

Step 3 here also demonstrates reformulating for both expressions. First, note
that for two variables, the :ref:`qpu_qubo_ising_ising` formulation reduces to,

.. math::

    \text{E}(h_i, J_{i,j}; S_i) = h_1 s_1 + h_2 s_2 + J_{1,2} s_1 s_2.

Reformulating the equality expression as a minimization can be done as follows:

.. math::

    v_1 = v_2 \qquad \rightarrow \qquad \min_v[v_1 - v_2]^2

Expanding the square gives,

.. math::

    \min_v[v_1 - v_2]^2 &= \min_v[v_1^2 + v_2^2 - 2v_1v_2] \\
    &= \min_v[1 + 1 -2v_1v_2] \\
    &= \min_v[2 -2v_1v_2]

You can now map the minimization directly to :math:`-2 s_1 s_2`, dropping the
constant.

Notice that for this Ising model the energy gap between the ground states
(e.g., :math:`E(s_1=s_2=-1)=-2`) and the excited states (e.g.,
:math:`E(s_1=-1, s_2=+1)=+2`) is 4. If you want a gap of 1, your Ising model is
:math:`E(s_1, s_2) = -0.5 s_1 s_2`.

Alternatively, if you prefer a truth table, you can reformulate as a penalty
function. Here, an energy gap of 1 is chosen.

======== ============= =================== =======================
State    :math:`v_1`   :math:`v_2`         Penalty
======== ============= =================== =======================
1        -1            -1                  p
2        -1            1                   p+1
3        1             -1                  p+1
4        1             1                   p
======== ============= =================== =======================

Substituting the values of the table's variables for variables :math:`s_1, s_2`
in the two-variable Ising model above, and the desired penalty for the
resulting energy, produces for the four rows of the table these four
equalities:

.. math::

    \text{State 1} \qquad h_1 (-1) + h_2 (-1) + J_{1,2} (-1) (-1) &= p \\
    \text{State 2} \qquad h_1 (-1) + h_2 (+1) + J_{1,2} (-1) (+1) &= p+1 \\
    \text{State 3} \qquad h_1 (+1) + h_2 (-1) + J_{1,2} (+1) (-1) &= p+1 \\
    \text{State 4} \qquad h_1 (+1) + h_2 (+1) + J_{1,2} (+1) (+1) &= p

Giving the following four equations with four variables:

.. math::

    -h_1 - h_2 + J_{1,2} &= p \\
    -h_1 + h_2 - J_{1,2} &= p+1 \\
    h_1 - h_2 - J_{1,2}  &= p+1 \\
    h_1 + h_2 + J_{1,2}  &= p

Solving these equations\ [#]_ gives :math:`E(s_1, s_2) = -0.5 s_1 s_2`.

.. [#]

    Adding the first and fourth equation immediately gives :math:`J_{1,2} = p`.
    Adding the second and third, and replacing :math:`J_{1,2}` for :math:`p`,
    gives :math:`J_{1,2} = p = -0.5`. Adding the first two equations, with
    these now-known values, produces :math:`h_1 = h_2 = 0`.

Submitting for solution on a |dwave_short| quantum computer is similar
to the submission shown in the :ref:`qpu_example_constrained_xnor` section,
where it is done for QUBOs:

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())
...
>>> h = {}
>>> J = {('s1', 's2'): -0.5}
>>> sampleset = sampler.sample_ising(h, J, num_reads=1000)
>>> print(sampleset)                    # doctest: +SKIP
  s1 s2 energy num_oc. chain_.
0 -1 -1   -0.5     372     0.0
1 +1 +1   -0.5     628     0.0
['SPIN', 2 rows, 1000 samples, 2 variables]

See also an alternative way of looking at this example as a simple :term:`CSP`
in the :ref:`qpu_example_unconstrained_sat` section.

.. _qpu_qubo_ising_transformations:

Ising-QUBO Transformations
==========================

The transformation between these formats is trivial:

.. math::

    s = 2x - 1.

Example of Transforming a QUBO to Ising Format
----------------------------------------------

Use :math:`x_i \mapsto \frac{s_i +1}{2}` to translate a QUBO model to an Ising
model, as here:

.. math::

    \begin{array}{rcl}
    f(x) &=& -22x_1 - 6x_2 - 14x_3 + 20x_1x_2 + 28x_1x_3 + 9 \\
    \tilde{f}(s) &=& -22 \left( \frac{s_1+1}{2} \right) -
    6 \left( \frac{s_2+1}{2} \right) - 14 \left(\frac{s_3+1}{2} \right) \\
    & & + 20 \left(\frac{s_1+1}{2} \right) \left( \frac{s_2+1}{2} \right)
    + 28 \left( \frac{s_1+1}{2} \right) \left( \frac{s_3+1}{2} \right) + 9 \\
    &=& -11s_1-11 - 3s_2-3 - 7s_3-7 + 5s_1s_2 + 5s_1 + 5s_2 +5 + 7s_1s_3 \\
    & & + 7s_1 + 7s_3 + 7 + 9 \\
    &=& s_1 + 2s_2 + 5s_1s_2 + 7s_1s_3
    \end{array}

Ocean software can automate such conversion for you:

>>> import dimod
>>> dimod.qubo_to_ising({('x1', 'x1'): -22, ('x2', 'x2'): -6, ('x3', 'x3'): -14,
...                      ('x1', 'x2'): 20, ('x1', 'x3'): 28},
...                      offset=9)
({'x1': 1.0, 'x2': 2.0, 'x3': 0.0}, {('x1', 'x2'): 5.0, ('x1', 'x3'): 7.0}, 0.0)

Example of Transforming a Ising to QUBO Format
----------------------------------------------

Use :math:`s_i \mapsto 2x_i -1` to translate an Ising model to a QUBO model, as
here:

.. math::

    \begin{array}{rcl}
    g(s) &=& s_1 + 2s_2 + 5s_1s_2 + 7s_1s_3 \\
    \tilde{g}(x) &=& (2x_1 - 1) + 2(2x_2 - 1) + 5(2x_1 - 1)(2x_2 - 1) \\
    & & + 7(2x_1 - 1)(2x_3 - 1)\\
    &=& 2x_1 - 1 + 4x_2 - 2 + 20x_1x_2 - 10x_1 - 10x_2 + 5 + 28x_1x_3 - 14x_1 \\
    & & - 14x_3 + 7 \\
    &=& - 22x_1 - 6x_2 - 14x_3 + 20x_1x_2 + 28x_1x_3 + 9
    \end{array}

Using Ocean software:

>>> import dimod
>>> dimod.ising_to_qubo({'s1': 1, 's2': 2},
...                     {('s1', 's2'): 5, ('s1', 's3'): 7}) # doctest: +SKIP
({('s1', 's1'): -22.0, ('s2', 's2'): -6.0, ('s1', 's2'): 20.0,
  ('s1', 's3'): 28.0, ('s3', 's3'): -14.0},
  9.0)