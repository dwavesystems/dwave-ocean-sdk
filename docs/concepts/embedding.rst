.. _embedding_sdk:

===============
Minor-Embedding 
===============

To solve an arbitrarily posed binary quadratic problem directly on a D-Wave system requires mapping,
called *minor embedding*, to a Chimera graph that represents the system's quantum processing unit.
This preprocessing can be done by a composed sampler consisting of the
:class:`~dwave.system.samplers.DWaveSampler()` and a composite that performs minor-embedding.
(This step is handled automatically by :class:`~dwave.system.samplers.LeapHybridSampler()`
and :std:doc:`dwave-hybrid <hybrid:index>` reference samplers.)

For example, a simple two-variable :term:`bqm`,

.. math::

    E(\bf{s}) = - s_0 s_1
    \qquad\qquad s_i\in\{-1,+1\}

might be embedded to two connected qubits, such as 1929 and 1801 on a D-Wave 2000Q system:

.. figure:: ../_images/embedding_2var2qubits.png
	:align: left
	:name: Embedding2var2qubits
	:scale: 60 %
	:alt: Two-variable problem embedded into two qubits.

	Two-variable problem, shown on the left as a graph, is embedded in two connected qubits on a D-Wave 2000Q, shown on the right against the Chimera topology. Variable :math:`s_1`, highlighted in dark magenta, is represented by qubit number 1929 and variable :math:`s_0` is represented by qubit 1801. 

In the D-Wave 2000Q :term:`Chimera` topology, most qubits are conencted to six other qubits, so 
other valid minor-embeddings might be :math:`s_1=1929, s_0=1933` or :math:`s_0=1801, s_0=1807` 
or :math:`s_0=0, s_1=4`.

Chains
------

Larger problems often require chains because the :doc:`QPU topology <oceandocs:concepts/topology>` is not fully connected. 

For example, a fully-conected :math:`K_3` three-variable :term:`bqm`,

.. math::

    E(\bf{s}) = - s_0 s_1 + s_0 s_2 + s_1 s_2
    \qquad\qquad s_i\in\{-1,+1\}

cannot be represented by three qubits in the :term:`Chimera` topology---a :math:`K_3` graph is
not native to the Chimera graph. (Look at the Chimera "unit cell" shown in the 
:doc:`QPU topology <oceandocs:concepts/topology>` section and notice there is no way to connect 
three qubits in a closed loop to form a triangle graph.)

Instead, a variable is represented by a *chain* of physical qubits:


.. figure:: ../_images/embedding_3var4qubits.png
	:align: left
	:name: Embedding3var4qubits
	:scale: 60 %
	:alt: Three-variable fully-connected problem embedded into four qubits.

	Three-variable :math:`K_3` fully-connected problem, shown on the left as a graph, is embedded in four qubits on a D-Wave 2000Q, shown on the right against the Chimera topology. Variable :math:`s_0`, highlighted in dark magenta, is represented by two qubits, numbers 251 and 253. 

The embedding above derived from the hueristic used by :class:`~dwave.system.composites.EmbeddingComposite()`
on the working graph of a D-Wave 2000Q selected by :class:`~dwave.system.samplers.DWaveSampler()`: 

.. code-block:: python

   sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True})) 

Other qubits might have been chosen; for example, 

.. code-block:: python

   sampler = FixedEmbeddingComposite(DWaveSampler(solver={'qpu': True}),  
                  embedding={'s0': [0, 4, 7], 's1': [2], 's2': [3, 6]})

intentionally sets the embedding shown below to represent this same :math:`K_3` graph:

 .. figure:: ../_images/embedding_3var6qubits.png
	:align: left
	:name: Embedding3var6qubits
	:scale: 60 %
	:alt: Three-variable fully-connected problem embedded into six qubits.

	Three-variable :math:`K_3` fully-connected problem is embedded in six qubits on a D-Wave 2000Q. Variable :math:`s_0`, highlighted in dark magenta, is represented by three qubits, numbers 0, 4, and 7; Variable :math:`s_2` is represented by two qubits, numbers 3 and 6, shown with their connecting edge
emphasized (and displaying a solution of :math:`+1`).

Chain Strength
--------------

For a chain of qubits to represent a variable, all its constituent qubits must return the 
same value for a sample. This is accomplished by setting a strong coupling to the edges
connecting these qubits. For the solutions shown above to the :math:`K_3` problem, the
default chain strength achieved identical values and the qubit chains properly represented
the variables of the problem.

However, that is not always the case. For the qubits in a chain to be likely to return identical 
values, the coupling strength for their connecting edges must be strong compared to 
the coupling with other qubits that influence non-identical outcomes.

For example, 

.. math::

    E(\bf{s}) = - s_0 s_1 + s_0 s_2 + s_1 s_2
    \qquad\qquad s_i\in\{-1,+1\}


.. code-block:: python

   sampler = FixedEmbeddingComposite(DWaveSampler(solver={'qpu': True}),  
                  embedding={'s0': [0, 4, 7], 's1': [2], 's2': [3, 6]})

