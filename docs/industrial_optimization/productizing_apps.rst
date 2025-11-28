.. _opt_productizing_quantum_apps:

=========================
Productizing Applications
=========================

This section provides insight into preparing and designing your quantum
application to be successfully deployed to a production environment.

Although production environments can vary widely between businesses, some common
components and processes can be identified as shown in
:numref:`Figure %s <QuantumAppProdArch>`. In fact, applications can be
easy to integrate into business operations in part because applications
typically run batch-based operations, submitting problems to and receiving
solutions from hybrid and quantum solvers via the Leap service.

.. _quantum_apps_prod_env:

Production Environment
======================

:numref:`Figure %s <QuantumAppProdArch>` illustrates an application acting as an
intermediary between various business systems and D-Wave's compute
infrastructure made available via the solver API and the Leap quantum cloud
service. To communicate with D-Wave's hybrid and quantum solvers, the
application uses D-Wave's Python-based and open-source software development kit
(SDK), the Ocean SDK. In this context, the Ocean SDK manages submitting problems
to and receiving solutions from hybrid and quantum solvers via the solver API
(SAPI) REST interface. ``Business System 1``, ``Business System 2``, and
``Data Storage`` represent various types of business systems, such as enterprise
content development systems (e.g., Microsoft Sharepoint), database management
systems, and data lakes.

.. figure:: ../_images/productizing_apps_business_infrastructure.png
    :name: QuantumAppProdArch
    :alt: Quantum-application infrastructure in production

    Quantum-application infrastructure in production.

.. _quantum_apps_design:

Application Design
==================

An application integrated with the Ocean SDK should provide the capability to
handle large-scale, long-running hybrid jobs in a heterogeneous environment
typical of many enterprise businesses. Within such an environment, an
application for running hybrid jobs could be part of a pipeline for
a business operation. For example, Pattison Food Group's
`production application <https://www.dwavequantum.com/resources/application/e-comm-driver-auto-scheduling-pattison-food-group>`_
uses D-Wave's hybrid solvers to optimize the weekly assignment
of drivers' work assignments, taking into account various constraints, such as
seniority or a minimum number of shifts per week.

Specifically, an application should be able to do the following:

*   Run long jobs. Hybrid problems can be configured to run
    for a few seconds or several hours.

*   Manage job requests in a reliable, industrial-grade queue,
    such as Redis, RabbitMQ, Amazon Elasticache, SQS, Kinesis, and so forth.

*   Horizontally scale queue workers to perform required preprocessing,
    retrieve additional data from datastores, transform the problem
    into the required format and upload it to a hybrid solver in the
    Leap service. Using a container orchestration platform, such as Kubernetes,
    can be key to scaling workers in a production environment. 

*   Easily keep up to date with Ocean SDK releases to help ensure the
    best performance and take advantage of new features.

Microservices can be a good choice for meeting the aforementioned guidelines.
:numref:`Figure %s <QuantumAppProdMicroserviceArch>` shows an example of a
microservice architecture.

.. figure:: ../_images/quantum_app_prod_microservice_arch.png
    :name: QuantumAppProdMicroserviceArch
    :alt: Microservice architecture for a quantum-application in production.

    Microservice architecture for a quantum-application in production.

In :numref:`Figure %s <QuantumAppProdMicroserviceArch>`, queue workers grab
problems off a queue of incoming problems. Each worker handles the following:

*   Preprocessing, which could include retrieving additional data from data
    sources, handling problem formulation, and storing the formulated problem.

*   Submitting the job and polling the hybrid solver for completion of the job.

*   Post-processing, which could include unpacking the solution, sending
    the solution to other business systems for further processing, and sending
    notifications.
    
.. _quantum_apps_performance_sizing:

Performance and Sizing
======================

Some performance and sizing requirements to consider are the following:

*   Desired throughput (i.e., solved problems per second).

*   Latency, size, and bandwidth for hybrid problems.

*   Problem sizes can range from about 10 MB to greater than 1 GB.

*   Asynchronous processing because jobs can be configured with potentially long
    runtimes.

.. _quantum_apps_security:

Security
========

In addition to implementing best practices for security and access control,
you should also consider the following best practices specific to interacting
with the D-Wave compute infrastructure:

*   Use a minimum-permission model for allowing application access to
    sensitive data, such as personally identifiable information (PII).

*   Ensure that access control to the application for submitting problems is
    limited to authorized users.

*   Keep your Leap API token secure as follows:

    *   Do not hardcode your API token into your application.

    *   Store your API token in a secure location and do not write it logs.

    *   Generate a new API token on a regular basis. 

.. _quantum_apps_prod_monitoring_metrics:

Monitoring and Logging
======================

The application should log metrics, including problem IDs, timestamps,
source, and timing information. A problem ID uniquely identifies each problem
and can be used to track your submissions and troubleshoot issues.
Logging as much metadata as is reasonably possible could help make
troubleshooting easier. Also, consider investing in structured logging solutions,
such as Elasticsearch, Datadog, and Splunk.

Consider building a dashboard to show important metrics, such as hybrid solver
usage, to your stakeholders.