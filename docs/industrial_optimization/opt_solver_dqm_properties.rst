.. _opt_solver_dqm_properties:

=====================
DQM Solver Properties
=====================

This section describes the properties of quantum-classical hybrid
:ref:`discrete quadratic model <concept_models_dqm>` solvers such as the Leap
service's ``hybrid_discrete_quadratic_model_version1``. For the parameters
you can configure, see the :ref:`opt_solver_dqm_parameters` section.

.. _property_dqm_category:

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

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["category"]
'hybrid'


.. _property_dqm_maximum_number_of_biases:

maximum_number_of_biases
========================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_number_of_biases
    :end-before: end_property_maximum_number_of_biases

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["maximum_number_of_biases"]  # doctest: +SKIP
5000000000


.. _property_dqm_maximum_number_of_cases:

maximum_number_of_cases
=======================

Maximum number of cases accepted by the solver.

For more details about cases and their role in DQMs, see the
:ref:`concept_models_dqm` section.

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["maximum_number_of_cases"]    # doctest: +SKIP
500000


.. _property_dqm_maximum_number_of_variables:

maximum_number_of_variables
===========================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_number_of_variables
    :end-before: end_property_maximum_number_of_variables

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["maximum_number_of_variables"]  # doctest: +SKIP
5000


.. _property_dqm_maximum_time_limit_hrs:

maximum_time_limit_hrs
======================

.. include:: ../shared/properties.rst
    :start-after: start_property_maximum_time_limit_hrs
    :end-before: end_property_maximum_time_limit_hrs

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["maximum_time_limit_hrs"]  # doctest: +SKIP
24.0


.. _property_dqm_minimum_time_limit:

minimum_time_limit
==================

.. |minimum_time_limit| replace:: for hybrid DQM solvers, this is a combination
    of the numbers of interactions, variables, and cases that reflects the
    "density" of connectivity between the problem's variables.

.. include:: ../shared/properties.rst
    :start-after: start_property_minimum_time_limit
    :end-before: end_property_minimum_time_limit

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["minimum_time_limit"]       # doctest: +SKIP
[[20000,5],
 [100000,6],
 [200000,13],
 [500000,34],
 [1000000,71],
 [2000000,152],
 [5000000,250],
 [20000000,400],
 [250000000,1200]]


.. _property_dqm_parameters:

parameters
==========

.. include:: ../shared/properties.rst
    :start-after: start_property_parameters
    :end-before: end_property_parameters

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["parameters"]["time_limit"]  # doctest: +SKIP
'Maximum requested runtime in seconds.'


.. _property_dqm_quota_conversion_rate:

quota_conversion_rate
=====================

.. include:: ../shared/properties.rst
    :start-after: start_property_quota_conversion_rate
    :end-before: end_property_quota_conversion_rate

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["quota_conversion_rate"]  # doctest: +SKIP
20


.. _property_dqm_supported_problem_types:

supported_problem_types
=======================

.. include:: ../shared/properties.rst
    :start-after: start_property_supported_problem_types
    :end-before: end_property_supported_problem_types

DQM solvers support the following energy-minimization problem types:

*   ``dqm``

    .. include:: ../shared/models.rst
        :start-after: start_models_dqm
        :end-before: end_models_dqm

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["supported_problem_types"]  # doctest: +SKIP
['dqm']


.. _property_dqm_version:

version
=======

.. include:: ../shared/properties.rst
    :start-after: start_property_version
    :end-before: end_property_version

Example
-------

>>> from dwave.system import LeapHybridDQMSampler
...
>>> sampler = LeapHybridDQMSampler()
>>> sampler.properties["version"]  # doctest: +SKIP
1.12
