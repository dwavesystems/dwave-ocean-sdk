.. _using_qpu:

===============
Quantum Solvers
===============

Ocean's :doc:`dwave-system </docs_system/sdk_index>` tool enables
you to use a D-Wave system as a sampler. In addition to *DWaveSampler()*, the tool
provides a *EmbeddingComposite()* composite that maps unstructured problems to the graph
structure of the selected sampler, a process known as :term:`minor-embedding`.
For the AND gate of the :ref:`formulating_bqm` section, the problem is defined on
alphanumeric variables :math:`x1, x2, y1`, that must be mapped to the QPU's numerically
indexed qubits.

Because of the sampler's probabilistic nature, you typically request multiple samples
for a problem; this example sets `num_reads` to 1000.

.. code-block:: python

    >>> from dwave.system import DWaveSampler, EmbeddingComposite
    >>> sampler = EmbeddingComposite(DWaveSampler())
    >>> response = sampler.sample(bqm, num_reads=1000)   # doctest: +SKIP
    >>> for datum in response.data(['sample', 'energy', 'num_occurrences']):     # doctest: +SKIP
    ...    print(datum.sample, datum.energy, "Occurrences: ", datum.num_occurrences)
    ...
    {'x1': 0, 'x2': 1, 'y1': 0} -1.5 Occurrences:  92
    {'x1': 1, 'x2': 1, 'y1': 1} -1.5 Occurrences:  256
    {'x1': 0, 'x2': 0, 'y1': 0} -1.5 Occurrences:  264
    {'x1': 1, 'x2': 0, 'y1': 0} -1.5 Occurrences:  173
    {'x1': 1, 'x2': 0, 'y1': 1} 0.5 Occurrences:  215

Note that the first four samples are the valid states of the AND gate and have
lower values than invalid state :math:`x1=1, x2=0, y1=1`.

Once you have configured a
:doc:`D-Wave Cloud Client configuration file </docs_cloud/sdk_index>` as described in
the :ref:`sapi_access` section, your default solver configuration is used when you
submit a problem without explicitly overriding it.

Several of the examples in the :ref:`gs` Example's section show how to submit problems
to D-Wave systems.
