.. _keywords:

Specified Keyword Arguments
=============================

The following keyword arguments have been specified for use by one or more
projects.

* :ref:`keyword-num_samples`
* :ref:`keyword-embedding`

.. _keyword-num_samples:

num_samples
-------------

Number of samples to draw. A positive integer.

**Type:** Integer

**Used By:** `dwave_sapi_dimod <https://github.com/dwavesystems/dwave_sapi_dimod>`_, `qbsolv <https://github.com/dwavesystems/qbsolv>`_

.. _keyword-embedding:

embedding
------------

A mapping from a source graph to a target graph. Each node in
source graph is mapped to one or more nodes in the target graph.
Also referred to as a "minor embedding".

**Type:** dict[hashable, iterable]

**Used By:**  dwave_virtual_graph
