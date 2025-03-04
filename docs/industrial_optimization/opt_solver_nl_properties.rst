.. _opt_solver_nl_properties:

===========================
Nonlinear Solver Properties
===========================

This section describes the properties of quantum-classical hybrid
:ref:`nonlinear-model <concept_models_nonlinear>` solvers such as the Leap
service's ``hybrid_nonlinear_program_version1``. For the parameters you can
configure, see the :ref:`opt_solver_nl_parameters` section.

.. _property_nl_category:

category
========

.. include:: ../shared/properties.rst
    :start-after: start_category1
    :end-before: end_category1

.. include:: ../shared/properties.rst
    :start-after: start_property_category
    :end-before: end_property_category

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["category"]
'hybrid'


.. _property_nl_maximum_decision_state_size:

maximum_decision_state_size
===========================

Maximum size, in bytes, of all decision-variable states,
:meth:`~dwave.optimization.model.Model.decision_state_size`, accepted by the
solver.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["maximum_decision_state_size"]    # doctest: +SKIP
52428800


.. _property_nl_maximum_number_of_nodes:

maximum_number_of_nodes
=======================

Maximum number of nodes, :meth:`~dwave.optimization.model.Model.num_nodes`,
accepted by the solver.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["maximum_number_of_nodes"]    # doctest: +SKIP
2000000


.. _property_nl_maximum_number_of_states:

maximum_number_of_states
========================

Maximum number of initialized states\ [#]_,
:meth:`~dwave.optimization.model.States.size`, accepted by the solver.

.. [#]
    Submitted models can include states, typically to provide initial
    decision-variable assignments that might accelerate solutions. Such
    included states, with values initialized or not, are counted by
    :ref:`property_nl_maximum_number_of_states`.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["maximum_number_of_states"]    # doctest: +SKIP
1


.. _property_nl_max_state_size:

maximum_state_size
==================

Maximum size, in bytes, of all states,
:meth:`~dwave.optimization.model.Model.state_size`, accepted by the solver.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["maximum_state_size"]    # doctest: +SKIP
786432000


.. _property_nl_maximum_time_limit_hrs:

maximum_time_limit_hrs
======================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_time_limit_hrs
    :end-before: end_property_maximum_time_limit_hrs

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["maximum_time_limit_hrs"]  # doctest: +SKIP
24.0


.. _property_nl_num_nodes_multiplier:

num_nodes_multiplier
====================

Multiplier applied to a problem's total number of
:ref:`nodes <opt_model_construction_nl>`, the product of which is used
in the internal estimate of the problem's minimum runtime.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["num_nodes_multiplier"]    # doctest: +SKIP
0.00008306792043756981


.. _property_nl_num_nodes_state_size_multiplier:

num_nodes_state_size_multiplier
===============================

Multiplier applied to the totals of a problem's state sizes and number of
:ref:`nodes <opt_model_construction_nl>`, the product of which is used in the
internal estimate of the problem's minimum runtime.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["num_nodes_state_size_multiplier"]    # doctest: +SKIP
2.1097317822863965e-12


.. _property_nl_parameters:

parameters
==========

.. include:: ../shared/properties.rst
    :start-after: start_property_parameters
    :end-before: end_property_parameters

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["parameters"]["time_limit"]  # doctest: +SKIP
'Requested runtime in seconds.'


.. _property_nl_quota_conversion_rate:

quota_conversion_rate
=====================

.. include:: ../shared/properties.rst
    :start-after: start_property_quota_conversion_rate
    :end-before: end_property_quota_conversion_rate

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["quota_conversion_rate"]  # doctest: +SKIP
20


.. _property_nl_state_size_multiplier:

state_size_multiplier
=====================

Multiplier applied to a problem's
:ref:`state <opt_model_construction_nl>`-size total, the product of which is
used in the internal estimate of the problem's minimum runtime.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["state_size_multiplier"]    # doctest: +SKIP
2.8379674360396316e-10


.. _property_nl_supported_problem_types:

supported_problem_types
=======================

.. include:: ../shared/properties.rst
    :start-after: start_property_supported_problem_types
    :end-before: end_property_supported_problem_types

Nonlinear solvers support the following energy-minimization problem types:

*   ``nl``

    .. include:: ../shared/models.rst
        :start-after: start_models_nonlinear
        :end-before: end_models_nonlinear

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["supported_problem_types"]  # doctest: +SKIP
['nl']


.. _property_nl_time_constant:

time_constant
=============

Used to estimate the minimum runtime required for a problem.

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["time_constant"]    # doctest: +SKIP
0.012671678446550176


.. _property_nl_version:

version
=======

.. include:: ../shared/properties.rst
    :start-after: start_property_version
    :end-before: end_property_version

Example
-------

>>> from dwave.system import LeapHybridNLSampler
...
>>> sampler = LeapHybridNLSampler()
>>> sampler.properties["version"]  # doctest: +SKIP
1.5
