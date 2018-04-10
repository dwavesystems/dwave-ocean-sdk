.. _and:

================
Boolean AND Gate
================

This example solves a simple problem of a Boolean AND gate to demonstrate using Ocean tools
to solve a problem on a D-Wave system.

It adds to the minimal example of :ref:`not` the following more advanced features:

* :term:`Minor-embedding` that includes a chain.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in
  :ref:`dwavesysk`\ , in a configuration file for connection to a D-Wave system,
  as described in
  `dwave-cloud-client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_\ .
* Installation of Ocean tools `dwave-system <https://github.com/dwavesystems/dwave-system>`_\ .

From NOT to AND: an Important Difference
========================================

As explained in :ref:`not`, the penalty function for a NOT gate, represented
as a fully connected :math:`K_2` graph, can be can be :term:`minor-embed`\ ded onto two
qubits of a :term:`Chimera` unit cell. In contrast, the penalty function this example uses
for an AND gate requires a fully connected :math:`K_3` graph, which is not natively supported
in the Chimera graph. It requires the chaining of qubits as part of the minor-embedding.

Representing a NOT Gate as a BQM
================================

Similar to :ref:`not` this example uses a penalty function it converts into a :term:`QUBO`.

AND as a Penalty Function
-------------------------

Ocean has tools to produce a :term:`penalty function` but this example uses a known
formulation of AND as penalty function:

.. math::

    z \Leftrightarrow x_1 \wedge x_2: \qquad x_1 x_2 - 2(x_1+x_2)z +3z.

You can verify this in the same way as was done in the :ref:`not` example.

AND as a QUBO
-------------

Sometimes penalty functions are of cubic or higher degree and must be
reformulated as quadratic to be mapped onto the native (:term:`Ising`) binary
quadratic model used by the D-Wave system.

In this case, the penalty function is quadratic, and easily ordered in the familiar
QUBO formulation:

.. math::

    E(a_i, b_{i,j}; x_i) = 3x_3 + x_1x_2 - 2x_1x_3 - 2x_2x_3

where :math:`z=x_3` is the AND gate's output, :math:`x_1, x_2` the inputs, linear
coefficients are :math:`a_1=3`, and quadratic coefficients are :math:`b_{1,2}=1
b_{1,3}=-2, b_{2,3}=-2`.
The coefficients matrix is,

.. math::

     Q = \begin{bmatrix} 0 & 1 & -2\\
                           & 0 & -2\\
                           &   & 3 \end{bmatrix}

Minor-Embedding the BQM
=======================

You can see that the QUBO above representing an AND penalty function can be
represented as a fully connected :math:`K_3` graph; qubits of a Chimera unit cell
do not natively support :math:`K_3` graphs so the minor-embedding in this case
relies on chaining at least two qubits for a connecting edge.

To understand how a :math:`K_3` graph fits on the Chimera graph, look at the
Chimera unit cell structure shown here. You cannot connect 3 qubits in a
closed loop. However, you can make a closed loop of 4 qubits using,
say, qubits 0, 1, 4, and 5.

.. figure:: ../_static/unit-cell.png
  :name: unit-cell
  :scale: 20 %
  :alt: Unit cell

  Chimera unit cell.

To fit the 3-qubit loop into a 4-sided structure, create a chain of 2 physical qubits
that represent a single variable. For example, chain qubit 0 and qubit 5 to represent variable :math:`z`.

.. figure:: ../_static/Embedding_Chimera_AND.png
  :name: Embedding_Chimera_AND
  :scale: 60 %
  :alt: Embedding a triangular graph into Chimera by using a chain.

  Embedding a :math:`K_3` graph into Chimera by using a chain.

The strength of the coupler between :math:`q_0` and :math:`q_5`, which represents
variable :math:`z`, must be set to correlate the qubits strongly, so that in most
solutions, :math:`q_0 = q_5 = z`.

Example Code
============

The example configures a D-Wave :term:`solver` you have access to as a
:term:`sampler` and submits a :term:`QUBO` formulation of an AND gate to it for
20 samples. The results should mostly show values representing :math:`z=x_1x_2`\ .

.. note:: As stated in the requirements section above, you should have set up
     a configuration file for connection to a D-Wave system, as described in
     `dwave-cloud-client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_\ .

     Such a file might look similar to this example configuration file located in
     /home/susan/.config/dwave/dwave.conf:

     [defaults]

     endpoint = https://url.of.some.dwavesystem.com/sapi

     client = qpu

     [dw2000]

     solver = EXAMPLE_2000Q_SYSTEM

     token = ABC-123456789123456789123456789

This example uses manual :term:`minor-embedding` for clearer understanding
(typically you automate the process). Rather than hoping the target qubits are
active on the selected solver, this example verifies that. If not all the target
qubits are active, select alternative qubits from the same or another
:term:`Chimera` unit cell.

.. code-block:: python

    >>> from dwave.system.samplers import DWaveSampler
    >>> DWaveSampler().nodelist # doctest: +SKIP
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    >>> # Snipped above response for brevity

For the solver selected by default in this example's D-Wave Cloud Client
configuration file, all the qubits in the first Chimera unit cell (qubits 0 to
7) are active.

This example uses the Virtual Graph feature to minor-embed the AND gate.

.. code-block:: python

    >>> from dwave.system.samplers import DWaveSampler
    >>> from dwave.system.composites import VirtualGraphComposite
    >>> embedding = {'x1': {1}, 'x2': {5}, 'z': {0, 4}}
    >>> sampler = VirtualGraphComposite(DWaveSampler(), embedding)
    >>> Q = {('x1', 'x2'): 1, ('x1', 'z'): -2, ('x2', 'z'): -2, ('z', 'z'): 3}
    >>> response = sampler.sample_qubo(Q, num_reads=20)
    >>> for sample in response.samples():
    ...     print(sample)
    ...
    {'x2': 0, 'x1': 1, 'z': 0}
    {'x2': 0, 'x1': 0, 'z': 0}
    {'x2': 0, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 1, 'z': 1}
    {'x2': 1, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 0, 'z': 0}
    {'x2': 0, 'x1': 1, 'z': 0}
    {'x2': 0, 'x1': 0, 'z': 0}
    {'x2': 0, 'x1': 1, 'z': 0}
    {'x2': 0, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 1, 'z': 1}
    {'x2': 1, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 0, 'z': 0}
    {'x2': 0, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 0, 'z': 0}
    {'x2': 1, 'x1': 1, 'z': 1}
    {'x2': 0, 'x1': 0, 'z': 0}
    {'x2': 0, 'x1': 1, 'z': 0}
    {'x2': 0, 'x1': 0, 'z': 0}
