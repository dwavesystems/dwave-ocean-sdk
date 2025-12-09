.. _opt_deploying_quantum_apps_prod:

=======================
Deploying in Production
=======================

This section provides insight into designing and preparing a hybrid application
to be successfully deployed in a production environment. Hybrid applications
can be easy to integrate with a business's technology stack, in part, because
such applications typically run batch-based, asynchronous operations, submitting
problems to and receiving results from hybrid solvers in the Leap service.

.. _quantum_apps:

Application
===========

A hybrid application acts as an intermediary between the systems of
a business's technology stack and D-Wave's compute infrastructure made available
via the solver API (SAPI) and the Leap service.
:numref:`Figure %s <HybridAppPipeline>` provides a high-level illustration of a
typical hybrid application integrated with a business's technology
stack. A business's technology stack can involve many different business
systems such as a user interface, enterprise-content development systems
(e.g., Microsoft Sharepoint), database management systems, and data lakes.
A hybrid application receives input data from various systems in the business's
technology stack and uses D-Wave's Python-based and open-source software
development kit (SDK), the Ocean SDK, to submit problems via SAPI REST calls to
the hybrid solvers in D-Wave's Leap service. The hybrid solvers return problem
results and, again using the Ocean SDK, the hybrid application receives such
results; the hybrid application postprocesses the results and returns solutions
to the appropriate business systems.

.. figure:: ../_images/hybrid_app_pipeline.png
    :name: HybridAppPipeline
    :alt: Hybrid application integrated with a business's technology stack

    Hybrid application integrated with a business's technology stack.\ [#]_

.. [#] QPU solvers are not shown in this figure, but the solver API is also
    used to call them.

The following process illustrates a basic, hybrid application, which
can be used as a model for more complex ones.

#.  Authenticate and authorize access to the Leap service via a solver API
    token and configuration of the Ocean SDK's :ref:`dwave-cloud-client <index_cloud>`
    package. For information, see :ref:`ocean_sapi_access_advanced`.

#.  Preprocess input data, which includes handling problem and model
    formulation, storing the formulated problem, and, optionally, retrieving
    additional data from data sources.

#.  Submit the problem to a hybrid solver.

    When a problem is submitted, it is also uploaded. Sometimes, for example,
    if you want to solve it again or clearly separate uploading from solving,
    you may want to upload it separately.

#.  (Optional) Although polling the hybrid solver for completion of hybrid
    problems is automatically performed by the Ocean SDK, you may want to
    implement polling yourself; if you do so, you must explicitly download each
    problem's results (i.e., the answer).

#.  Handle solver errors as follows:

    *   You do not need to retry idempotent requests because, by default, the
        Ocean SDK retries them.

    *   You should handle the errors raised when falling back to another
        QPU solver is recommended or required.

    *   You may retry on timeouts to non-idempotent endpoints. For example, you
        could retry a problem submission, being aware that duplicate problems
        could be submitted.

    *   It is highly recommended that you never automatically retry on
        authentication and authorization errors as well as HTTP 5xx errors.
        Although an exception could be made for retrying on these errors while
        polling, you should ensure that you back off or stop retrying during
        long solver outages.
    
#.  Post-process the problem results, which typically includes the following:

    *   Unpacking the problem results.

    *   Interpreting and converting the problem results into a form suitable for
        the appropriate business system and users.

    *   Sending notifications to business systems and users.
    
A real-world example of an enterprise-level hybrid application is
Pattison Food Group's
`production application <https://www.dwavequantum.com/resources/application/e-comm-driver-auto-scheduling-pattison-food-group>`_,
which uses D-Wave's hybrid solvers to optimize the weekly assignment
of drivers' work assignments, taking into account various constraints, such as
seniority and the required number of drivers for each shift.

.. _quantum_apps_guidelines:

Application Guidelines
======================

An application should be capable of handling large-scale, long-running
hybrid problems in a heterogeneous environment typical of many enterprise-level
businesses.

.. _quantum_apps_performance_scaling:

Performance and Scaling
-----------------------

Some performance and scaling considerations are the following:

*   Desired throughput (i.e., solved problems per second). Also take into
    account concurrency limits to provision your workloads effectively.

*   Internet connection latency and bandwidth.

*   Size of problems, which can range from about 10 MB to greater than 1 GB.

*   Long and asynchronous jobs; hybrid problems can be configured to run for a
    few seconds or several hours.

*   CPU and memory requirements for hardware and virtual compute: How you model
    your problems can impact these requirements.

You should also keep up to date with Ocean SDK releases to help ensure the best
performance and take advantage of the newest features.

.. _quantum_apps_security:

Security
--------

In addition to implementing best practices for security and access control,
you should also consider the following best practices specific to interacting
with D-Wave's compute infrastructure:

*   Use a minimum-permission model for allowing application access to
    sensitive data, such as personally identifiable information (PII).

*   Ensure that access control to the application for submitting problems is
    limited to authorized users.

*   Rotate your solver API token on a regular basis, and change them immediately
    before deploying to production, just in case they have been saved outside of
    your codebase during development. In addition, ensure that your solver API
    token is secure as follows:

    *   Store your solver API token in a single secure location.
    
    *   Do not hardcode your solver API token in your application.

    *   Do not write your solver API token to logs nor save it to your version
        control system.

.. _quantum_apps_monitoring_logging:

Monitoring and Logging
----------------------

The application should log metrics, including problem IDs, timestamps,
source, and timing information. A problem ID uniquely identifies each problem
and can be used to track your submissions and troubleshoot issues.
Logging as much metadata as is reasonably possible could help make
troubleshooting easier. Also, consider investing in structured logging solutions,
such as Elasticsearch, Datadog, and Splunk.

Consider building a dashboard to show important metrics, such as hybrid solver
usage, to your stakeholders.