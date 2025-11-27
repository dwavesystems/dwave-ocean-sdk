.. _opt_productizing_quantum_apps:

=========================
Productizing Applications
=========================

This section provides insight into successfully deploying your application to a
production environment.

Although production environments can vary widely between businesses, some common
components and processes can be identified as shown in a
:ref:`typical production environment <prod_env>`. In fact, applications can be
easy to integrate into business operations in part because applications
typically run batch-based operations, submitting problems to and receiving
solutions from hybrid solvers via the Leap service. While both your business
case and production environment can dictate the production application that you
build, a microservice design can be an optimal solution for many enterprise
businesses; thus, the production environment and application design described
in this section are based on a microservice architecture.

.. _prod_env:

Production Environment
======================

:numref:`Figure %s <QuantumAppProdArch>` illustrates a microservice based on D-Wave’s
Python-based open-source software development kit (SDK), Ocean SDK. The Ocean
SDK is a suite of tools for using D-Wave's quantum computers and hybrid solvers,
including managing the submission of problems to and reception of problem
solutions from quantum processing unit (QPU) and hybrid solvers. 

.. figure:: ../_images/quantum_app_prod_arch.png
    :name: QuantumAppProdArch
    :alt: Quantum-application architecture in production

    Quantum-application architecture in production.

.. _quantum_app_prod_design:

Application Design
==================

A microservice based on the Ocean SDK can provide the capability to handle
large-scale, long-running hybrid-solver jobs in a heterogeneous,
service-oriented architecture typical for many enterprise businesses.
A microservice enables the following benefits:

*   Ensure efficient usage by centralizing both preprocessing and postprocessing,
    system notifications, logging, metrics, security, and so forth.

*   Ability to run long jobs. Hybrid problems can be configured to run for as
    little as a few seconds to many hours.

*   Service requests from other internal business systems.

    *   Requests could be stored in a reliable, industrial-grade queue, such as
        Redis, RabbitMQ, Amazon Elasticache, SQS, Kinesis, and so forth.

    *   Horizontally scalable queue workers could perform required preprocessing,
        retrieve additional data from datastores; and transform the hybrid problem
        into the required format and upload it to a hybrid solver in the
        Leap service.

*   Enable easily keeping up to date with Ocean SDK releases to help ensure the
    best performance and get new features.

:numref:`Figure %s <QuantumAppProdMicroserviceArch>` shows an example of a
microservice architecture.

.. figure:: ../_images/quantum_app_prod_microservice_arch.png
    :name: QuantumAppProdMicroserviceArch
    :alt: Microservice architecture for a quantum-application architecture in
          production

    Microservice architecture for a quantum-application architecture in
    production.

In :ref:`QuantumAppProdMicroserviceArch`, queue workers grab problems off a
queue of incoming problems. Each worker handles the following:

*   Preprocessing, which could include retrieving additional data from databases,
    handling problem formulation, storing the formulated problem.

*   Submitting the job and polling the hybrid solver for completion of the job.

*   Post-processing, which could include unpacking the solution, sending
    solution to other business systems for further processing, sending
    notifications.

.. _quantum_apps_prod_security_access_control:

Security and Access Control
===========================

*   Use a minimum-permission model for access to sensitive data, such as
    personally identifiable information (PII).

*   Ensure that access control to the application for submitting problems is
    limited to authorized users.

*   Keep your Leap API token secure.

    *   Do not hardcode your API token into your application.

    *   Store your API token in a secure location and do not write it logs.

    *   Generate a new API token on a regular basis. 

.. _quantum_apps_prod_performance:

Performance
===========

Some performance requirements to consider are the following:

*   Initial desired throughput (i.e., solved problems per second).

*   Analyze latency, size, and bandwidth considerations for hybrid solvers;
    their runtime is configurable, from seconds to hours, depending on solution
    requirements.

*   Your application must be designed around asynchronous processing.

*   Problem size can range from about 10 MB to greater than 1 GB.

.. _quantum_apps_pre_post_processing:

Preprocessing and Postprocessing
================================

*   Preprocessing of data used in problem submission. For example, data such as
    words or amounts may need to be extracted from databases or unstructured
    sources, such as internal Web pages or documents, and converted to the
    appropriate data type.

*   Postprocessing of solution data returned from the hybrid solvers.
    For example, solution data is returned as QUBOs and if the final output
    of the solution were to be employee schedules, then the QUBOs would need to
    be converted to a Web page or PDFs showing those schedules.
    
.. _quantum_apps_prod_monitoring_metrics:

Monitoring and Metrics
======================

Each step should log metrics, including hybrid problem IDs, timestamps,
source, and timing information. Logging as much metadata as is reasonably
possible could help make troubleshooting easier. Also, consider investing in
structured logging solutions, such as Elasticsearch, Datadog, Splunk, and so
forth.

Although hybrid solvers have a high SLA, you should ensure that your
application can handle situations in which such solvers or the QPU solvers that
back them become unavailable. For example, during scheduled maintenance,
sometimes problems are paused in a queue until solvers are back online.

Finally, consider building a dashboard to show important metrics, such as hybrid
solver usage, to your stakeholders.