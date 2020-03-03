.. _topology_sdk:

============
QPU Topology 
============

To solve a :term:`bqm` on the D-Wave system, you
must map it to a graph that represents the topology of the system's
qubits. For D-Wave 2000Q systems, this is the *chimera* topology; for 
next-generation Advantage systems, this is the *Pegasus* topology.

Chimera
-------

The Chimera architecture comprises sets of connected unit cells, each with four
horizontal qubits connected to four vertical qubits via couplers (bipartite
connectivity). Unit cells are tiled vertically and horizontally with adjacent
qubits connected, creating a lattice of sparsely connected qubits. A unit cell
is typically rendered as either a cross or a column.

.. figure:: ../_images/ChimeraUnitCell.png
	:align: center
	:name: ChimeraUnitCell
	:scale: 40 %
	:alt: Chimera unit cell.

	Chimera unit cell.


.. figure:: ../_images/chimera.png
  :name: chimera
  :scale: 70 %
  :alt: Chimera graph.  qubits are arranged in unit cells that form bipartite connections.

  A :math:`3 {\rm x} 3`  Chimera graph, denoted C3. Qubits are arranged in 9 unit cells.

Chimera qubits are considered to have a nominal length of 4 (each qubit
is connected to 4 orthogonal qubits through internal couplers) and degree of 6 (each qubit
is coupled to 6 different qubits).

The notation CN refers to a Chimera graph consisting of an :math:`N{\rm x}N` grid of unit cells.
The D-Wave 2000Q QPU supports a C16 Chimera graph: its 2048 qubits are logically mapped into a
:math:`16 {\rm x} 16` matrix of unit cells of 8 qubits.

Pegasus
-------

In Pegasus as in Chimera, qubits are “oriented” vertically or horizontally but similarly aligned
qubits can also be also shifted by distances and in groupings that differ between Pegasus families.
Pegasus qubits are also more densely connected and have three types of coupler:

- *Internal couplers*.
  Internal couplers connect pairs of orthogonal (with opposite orientation) qubits. In Pegasus,
  each qubit is connected via internal coupling to 12 other qubits (versus four in the Chimera topology).
- *External couplers*.
  External couplers connect vertical qubits to adjacent vertical qubits and horizontal
  qubits to adjacent horizontal qubits. Each qubit has one or two external couplers.
- *Odd couplers*.
  Odd couplers connect similarly aligned pairs of qubits. Each qubit has one odd coupler.

.. figure:: ../_images/pegasus_qubits.png
	:align: center
	:name: pegasus_qubits
	:scale: 100 %
	:alt: Pegasus qubits

	Pegasus qubits. Qubits are drawn as horizontal and vertical loops. The horizontal qubit in the center, shown with its odd coupler in red and numbered 1, is internally coupled to vertical qubits, in pairs 3 through 8, each pair and its odd coupler shown in a different color, and externally coupled to horizontal qubits 2 and 9, each shown in a different color.

.. figure:: ../_images/pegasus_roadway.png
	:align: center
	:name: pegasus_roadway
	:scale: 100 %
	:alt: Pegasus roadway graphic

	Pegasus qubits. Qubits in this "roadway" graphic are represented as dots and couplers as lines. The top qubit in the center, shown in red and numbered 1, is oddly coupled to the (red) qubit shown directly below it, internally coupled to vertical qubits, in pairs 3 through 8, each pair and its odd coupler shown in a different color, and externally coupled to horizontal qubits 2 and 9, each shown in a different color.

Pegasus qubits are considered to have a nominal length of 12 (each qubit is connected to
12 orthogonal qubits through internal couplers) and degree of 15 (each qubit is coupled to
15 different qubits).

As we use the notation CN to refer to a Chimera graph with size parameter N, we refer to instances
of Pegasus topologies by PN; for example, P3 is a graph with 144 nodes.

