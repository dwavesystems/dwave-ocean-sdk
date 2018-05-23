.. _multi_gate:

=============================================================
Multiple-Gate Circuit: Various Embeddings and Chain Strengths
=============================================================

This example solves a logic circuit problem to demonstrate using Ocean tools
to solve a problem on a D-Wave system.

It builds on the :ref:`map_coloring` example, providing some considerations about
the effect of minor-embedding on performance.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in
  :ref:`dwavesysk`\ , in a configuration file for connection to a D-Wave system,
  as described in
  `dwave-cloud-client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_\ .
* Installation of Ocean tools
  `dwavebinarycsp <http://dwavebinarycsp.readthedocs.io/en/latest/>`_ and
  `dwave-system <https://github.com/dwavesystems/dwave-system>`_\ . For graphics,
  you will also need `pyplot FIX THE LINK HERE <https://networkx.github.io/>`_\ .

Circuit with Multiple Logic Gates
=================================

.. ignore:: not working in my OS env, need to generate in my DOCS env for now

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

.. figure:: ../_static/MultiGateCircuit.png
   :name: Problem_MultiGateCircuit
   :alt: image
   :align: center
   :scale: 90 %

Formulating the Problem
=======================

This example follows two approaches to formulating the problem by converting the
logic gates to penalty models by defining constraints:

#. Single comprehensive constraint::

    import dwavebinarycsp

    def logic_circuit(a, b, c, d, z):
        not1 = not b
        or2 = b or c
        and3 = a and not1
        or4 = or2 or d
        and5 = and3 and or4
        not6 = not or4
        or7 = and5 or not6
        return (z == or7)

    csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
    csp.add_constraint(logic_circuit, ['a', 'b', 'c', 'd', 'z'])


#. Multiple small constraints::

    import dwavebinarycsp
    import dwavebinarycsp.factories.constraint.gates as gates
    import operator

    csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
    csp.add_constraint(operator.ne, ['b', 'not1'])  # add NOT 1 gate
    csp.add_constraint(gates.or_gate(['b', 'c', 'or2']))  # add OR 2 gate
    csp.add_constraint(gates.and_gate(['a', 'not1', 'and3']))  # add AND 3 gate
    csp.add_constraint(gates.or_gate(['d', 'or2', 'or4']))  # add OR 4 gate
    csp.add_constraint(gates.and_gate(['and3', 'or4', 'and5']))  # add AND 5 gate
    csp.add_constraint(operator.ne, ['or4', 'not6'])  # add NOT 6 gate
    csp.add_constraint(gates.or_gate(['and5', 'not6', 'z']))  # add OR 7 gate

.. note:: `dwavebinarycsp` works best for constraints of up to 4 variables; it may not
      function as expected for constraints of over 8 variables.

Example Code
============

This example converts the constraint satisfactions problems above to binary quadratic
models and checks the number of valid and invalid samples returned from a D-Wave system
(using a configuration file for connection to a D-Wave system, as described in
`dwave-cloud-client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_\ ).

.. code-block:: python

    from dwave.system.samplers import DWaveSampler
    from dwave.system.composites import EmbeddingComposite

    bqm = dwavebinarycsp.stitch(csp)

    sampler = EmbeddingComposite(DWaveSampler())
    response = sampler.sample(bqm, num_reads=100)

    valid, invalid, data = 0, 0, []
    for datum in response.data():
    sample, energy, num = datum
    if (csp.check(sample)):
        valid = valid+num
        for i in range(num):
            data.append((sample, energy, '1'))
    else:
        invalid = invalid+num
        for i in range(num):
            data.append((sample, energy, '0'))
    print(valid, invalid)

Results
=======

Algorithmic minor-embedding is heuristic---the results vary significantly based on
the minor-embedding found as shown in the following table:

.. list-table:: Single Constraint
   :widths: 10 20
   :header-rows: 1

   * - Embedding
     - (valid, invalid)
   * - 1
     - (39, 961)
   * - 2
     - (1000, 0)
   * - 3
     - (998, 2)
   * - 4
     - (316, 684)

.. figure:: ../_static/SingleCSPembeddings.png
   :name: SingleCSPembeddings
   :alt: image
   :align: center
   :scale: 70 %

For the second approach, which creates a constraint satisfaction problem based on multiple
small constraints, the minor-embedding needs to bring together a larger number of
variables, and consequently results are weaker. However, results can be greatly improved in
this case by increasing the chain strength.

.. list-table:: Multiple Constraint
   :widths: 10 20 20
   :header-rows: 1

   * - Embedding
     - Chain Strength
     - (valid, invalid)
   * - 1
     - 2
     - (7, 993)
   * - 2
     - 2
     - (417, 583)
   * - 3
     - 3
     - (941, 59)
   * - 4
     - 3
     - (923, 77)

.. figure:: ../_static/MultiCSPembeddings.png
   :name: MultiCSPembeddings
   :alt: image
   :align: center
   :scale: 70 %
