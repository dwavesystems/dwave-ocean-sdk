.. _opt_solver_bqm_properties:

=====================
BQM Solver Properties
=====================

.. _property_bqm_category:

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

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["category"]
'hybrid'


.. _property_bqm_maximum_number_of_biases:

maximum_number_of_biases
========================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_number_of_biases
    :end-before: end_property_maximum_number_of_biases

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["maximum_number_of_biases"]  # doctest: +SKIP
200000000


.. _property_bqm_maximum_number_of_variables:

maximum_number_of_variables
===========================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_number_of_variables
    :end-before: end_property_maximum_number_of_variables

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["maximum_number_of_variables"]  # doctest: +SKIP
1000000


.. _property_bqm_maximum_time_limit_hrs:

maximum_time_limit_hrs
======================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_time_limit_hrs
    :end-before: end_property_maximum_time_limit_hrs

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["maximum_time_limit_hrs"]  # doctest: +SKIP
24.0


.. _property_bqm_minimum_time_limit:

minimum_time_limit
==================

.. |minimum_time_limit| replace:: for hybrid BQM solvers, this is the number
    of variables.

.. include:: ../shared/properties.rst
    :start-after: start_property_minimum_time_limit
    :end-before: end_property_minimum_time_limit

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["minimum_time_limit"]       # doctest: +SKIP
[[1, 3.0],
 [1024, 3.0],
 [4096, 10.0],
 [10000, 40.0],
 [30000, 200.0],
 [100000, 600.0],
 [1000000, 600.0]]


.. _property_bqm_parameters:

parameters
==========

.. include:: ../shared/properties.rst
    :start-after: start_property_parameters
    :end-before: end_property_parameters

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["parameters"]["time_limit"]  # doctest: +SKIP
'Maximum requested runtime in seconds.'


.. _property_bqm_quota_conversion_rate:

quota_conversion_rate
=====================

.. include:: ../shared/properties.rst
    :start-after: start_property_quota_conversion_rate
    :end-before: end_property_quota_conversion_rate

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["quota_conversion_rate"]  # doctest: +SKIP
20


.. _property_bqm_supported_problem_types:

supported_problem_types
=======================

.. include:: ../shared/properties.rst
    :start-after: start_property_supported_problem_types
    :end-before: end_property_supported_problem_types

BQM solvers support the following energy-minimization problem types:

*   ``bqm``: Binary quadratic model (BQM) problems; use :math:`0/1`-valued
    variables and :math:`-1/1`-valued variables; constraints are typically
    represented as penalty models.

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["supported_problem_types"]  # doctest: +SKIP
['bqm']


.. _property_bqm_version:

version
=======

.. include:: ../shared/properties.rst
    :start-after: start_property_version
    :end-before: end_property_version

Example
-------

>>> from dwave.system import LeapHybridBQMSampler
...
>>> sampler = LeapHybridBQMSampler()
>>> sampler.properties["version"]  # doctest: +SKIP
2.2
