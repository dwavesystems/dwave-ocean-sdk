.. _and:

================
Boolean NOT Gate
================

This example solves a simple problem of a Boolean NOT gate to demonstrate using Ocean tools
to solve a problem on a D-Wave system.

The purpose of this minimal example is to help a new user establish a connection
to a D-Wave system with little configuration. Other examples demonstrate the more
advanced steps that are typically needed for solving actual problems.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in :ref:`dwavesysk`
* Installation of Ocean tools `dwave-system <https://github.com/dwavesystems/dwave-system>`_ and `dimod <https://github.com/dwavesystems/dimod>`_\ .

Representing a NOT Gate as a BQM
================================

In the terminology of :ref:'stack', Ocean tools move the original problem through the
following layers:

* Application is a logic operation; the problem space is Boolean variables.
* The method used here is a :term:`penalty function`. This simple example uses a known penalty
  function. Other examples use Ocean tools to produce penalty functions.
* The sampler API is a :term:`QUBO` representation of the binary quadratic model (BQM).
* The sampler is a D-Wave :term:`solver`.
* The compute resource is a D-Wave system.

NOT as a Penalty Function
-------------------------

Ocean has tools to produce :term:`penalty functions` but this example uses a known
formulation of NOT as penalty function:

.. math::

    z \Leftrightarrow \neg x: \qquad 2xz-x-z+1.

The table below shows that this function penalizes states
that represent a malfunctioning gate while no penalty is applied to a functioning
gate. In this table, column **x** is all possible states of the gate's input;
column :math:`\mathbf{z_{valid}}` is the corresponding output values of a
functioning gate while :math:`\mathbf{z_{fault}}` is the corresponding
output values of a malfunctioning gate, which are simply
:math:`z_{fault} = \neg z_{valid}`; column  :math:`\mathbf{P_{valid}}` is
the value the penalty function adds to the energy of the :term:`objective function`
when the gate is functioning (zero, a functioning gate must not be penalized)
while column :math:`\mathbf{P_{fault}}` is the value the penalty function
adds when the gate is malfunctioning (nonzero, the objective function must
be penalized with a higher energy).

.. table:: Boolean NOT Operation as a Penalty.
   :name: BooleanNOTAsPenalty

   ===========  ============================  =============================  ===========================  ===
   **x**        :math:`\mathbf{z_{valid}}`    :math:`\mathbf{z_{fault}}`     :math:`\mathbf{P_{valid}}`   :math:`\mathbf{P_{fault}}`
   ===========  ============================  =============================  ===========================  ===
   :math:`0`    :math:`1`                     :math:`0`                      :math:`0`                    :math:`1`
   :math:`1`    :math:`0`                     :math:`1`                      :math:`0`                    :math:`1`
   ===========  ============================  =============================  ===========================  ===

For example, the state :math:`x, z_{valid}=0,1` of the first row is
represented by the penalty function with :math:`x=0` and :math:`z = 1 = \neg x`.
For this functioning gate, the value of :math:`P_{valid}` is

.. math::

    2xz-x-z+1 = 2 \times 0 \times 1 - 0 - 1 + 1 = -1+1=0,

not penalizing the valid configuration. In contrast, the state :math:`x,
x_{fault}=0,0` of the first row is represented by the penalty function with
:math:`x=0` and :math:`z = 0 \ne \neg x`. For this malfunctioning gate, the
value of :math:`P_{fault}` is

.. math::

    2xz-x-z+1 = 2 \times 0 \times 0 -0 -0 +1 =1,

adding an energy cost of :math:`1` to the incorrect configuration.

This example drops the freestanding constant, which as no effect on the relative energies.
The penalty function used is,

.. math::

    2xz-x-z.

NOT as a QUBO
-------------

Sometimes penalty functions are of cubic or higher degree and must be
reformulated as quadratic to be mapped onto the native (:term:`Ising`) binary
quadratic model used by the D-Wave system.

In this case, the penalty function is quadratic, and easily ordered in the familiar
QUBO formulation:

.. math::

    E(a_i, b_{i,j}; x_i) = -x_1 -x_2  + 2x_1x_2

where :math:`z=x_2` is the AND gate's output, :math:`x=x_1` the input, linear
coefficients are :math:`a_1=a_2=-1`. and quadratic coefficient is :math:`b_{1,2}=2`.
The coefficients matrix is,

.. math::

     Q = \begin{bmatrix} -1 & 2 \\ 0 & -1 \end{bmatrix}

Minor-Embedding the BQM
=======================

The D-Wave system minimizes the energy of an :term:`Ising` spin configuration whose pairwise
interactions lie on the edges of a :math:`M,N,L` :term:`Chimera` graph. To solve a given
Ising spin problem with arbitrary pairwise interaction structure, you
:term:`minor-embed` its graph into a Chimera graph by using qubits to represent missing edges.

The penalty function for the NOT gate can be represented
as a fully connected :math:`K_2` graph that can be can be minor embedded onto two
qubits of a Chimera unit cell.


The figure below shows a minor embedding of the NOT gate into a unit cell of
a D-Wave 2000Q QPU, in this case, the topmost left cell of the Chimera graph.

.. figure:: ../_static/Problem_CFD_Embedding_ChimeraNOT.png
   :name: Problem_CFD_Embedding_ChimeraNOT
   :alt: image
   :align: center
   :scale: 90 %

   A NOT gate minor embedded into the topmost left unit cell of a
   D-Wave 2000Q QPU. Variables :math:`x_1,x_2` are minor
   embedded as physical qubits :math:`q_0,q_4`, represented as a 0 and 4
   inside a blue circle. Biases :math:`a_1,a_2=-1,-1` and coupling
   strength :math:`b_{1,2}=2` are also shown.

Example Code
============

The example configures a D-Wave :term:`solver` you have access to as a :term:`sampler`
and submits a :term:`QUBO` formulation of an OR gate to it for 20 samples. The results
should mostly show opposite values for the two variables (:math:`z=\neg x`); that
is, when qubit 0 has value 0, qubit 4 should have value 1, and vice versa.

.. note:: The embedding here presumes that qubits 0 and 4 are active on the target QPU.
      It's possible one might be inactive, in which case any other pair of connected qubits may
      be used. Active qubits can be seen through the sampler's properties but for the purpose of
      this simple example, you can choose pairs (1, 5) or (7, 11) for example.

.. note:: The arguments of the DWaveSampler() function below must be replaced with
      the requirements section above.

.. code-block:: python

   >>> from dwave.system.samplers import DWaveSampler
   >>> import dimod
   >>> sampler = DWaveSampler(endpoint='https://URL_to_my_D-Wave_system/', token='ABC-123456789012345678901234567890', solver='My_D-Wave_Solver')
   >>> Q = {(0, 0): -1, (0, 4): 0, (4, 0): 2, (4, 4): -1}
   >>> response = sampler.sample_qubo(Q, num_reads=20)
   >>> for sample in response.samples():   # doctest: +SKIP
   ...    print(sample)
   ...
   {0: 1, 4: 0}
   {0: 0, 4: 1}
   {0: 0, 4: 1}
   {0: 0, 4: 1}
   {0: 0, 4: 1}
   {0: 1, 4: 0}
   {0: 1, 4: 0}
   {0: 1, 4: 0}
   {0: 1, 4: 0}
   {0: 1, 4: 0}
   {0: 1, 4: 0}
   {0: 0, 4: 1}
   {0: 0, 4: 1}
   {0: 0, 4: 1}
   {0: 1, 4: 0}
   {0: 1, 4: 0}
   {0: 0, 4: 1}
   {0: 1, 4: 0}
   {0: 0, 4: 1}
   {0: 0, 4: 1}
