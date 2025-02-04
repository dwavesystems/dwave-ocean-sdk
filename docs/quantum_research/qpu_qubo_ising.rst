.. _qpu_qubo_ising:

======================
QUBOs and Ising Models
======================

.. todo:: fix this up


how you formulate your objective as the problem Hamiltonian
of a |dwave_short| quantum computer by defining the linear and quadratic
coefficients of a binary quadratic model (BQM) that maps those values to the
qubits and couplers of the QPU.

.. _gs_bqm:

Binary Quadratic Models
=======================

For the QPU, two formulations for objective functions are the :ref:`obj_ising`
and :ref:`obj_qubo`. Both these formulations are binary quadratic models and
conversion between them is trivial\ [#]_.

.. [#]
    Chapter :ref:`getting_started_advanced` provides information on the
    differences and conversion between the two formulations.

.. _obj_ising:

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

.. _obj_qubo:

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

In scalar notation, used throughout most of this document, the objective
function expressed as a QUBO is as follows:

.. math::

    \text{E}_{qubo}(a_i, b_{i,j}; q_i) = \sum_{i} a_i q_i +
    \sum_{i<j} b_{i,j} q_i q_j.

.. note::
    Quadratic unconstrained binary optimization problems---QUBOs---are
    *unconstrained* in that there are no constraints on the variables other
    than those expressed in *Q*.

