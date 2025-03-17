.. _ocean_sapi_access_advanced:

===================================================
Configuring Access to the Leap's Service (Advanced)
===================================================

The :ref:`dwave-cloud-client <index_cloud>` package is a minimal implementation
of the `REST <https://en.wikipedia.org/wiki/REST>`_ interface used to
communicate with |dwave_short|'s Solver API (:term:`SAPI`) servers.

SAPI is an application layer built to provide resource discovery, permissions,
and scheduling for quantum computers and quantum-classical :term:`hybrid`
solvers at |dwave_short|. The :ref:`dwave-cloud-client <index_cloud>` package
provides a minimal Python interface to that layer without compromising the
quality of interactions and workflow.

The package's :class:`~dwave.cloud.solver.Solver` class enables low-level
control of problem submission. It is used, for example, by the
:ref:`dwave-system <index_system>` package's
:class:`~dwave.system.samplers.DWaveSampler`, which enables quick incorporation
of a |dwave_short| quantum computer as a :term:`sampler` in your code.

It's recommended you set up your Cloud Client configuration through the
:ref:`interactive CLI utility <ocean_dwave_cli>`.

As described in the :ref:`ocean_sapi_access_basic` section, for your code to
access remote |dwave_short| compute resources, you must configure communication
through SAPI; for example, your code needs your API token for
:ref:`authentication <ocean_leap_authorization>`. The Cloud Client provides
multiple options for configuring the required information:

*   One or more locally saved
    :ref:`configuration files <sapi_access_config_files>`
*   :ref:`Environment variables <sapi_access_env_vars>`
*   Direct setting of key values in functions

These options can be flexibly used together.

.. _sapi_access_config_files:

Configuration Files
===================

If a Cloud Client configuration file is not explicitly specified when
instantiating a client or solver, auto-detection searches for candidate files in
a number of standard directories, depending on your local system's operating
system. You can see the standard locations with the
:func:`~dwave.cloud.config.get_configfile_paths` method.

For example, on a Unix system, depending on its flavor, these might include (in
order)::

    /usr/share/dwave/dwave.conf
    /usr/local/share/dwave/dwave.conf
    ~/.config/dwave/dwave.conf
    ./dwave.conf

On Windows 7+, configuration files are expected to be located under::

    C:\\Users\\<username>\\AppData\\Local\\dwavesystem\\dwave\\dwave.conf

On Mac OS X, configuration files are expected to be located under::

    ~/Library/Application Support/dwave/dwave.conf

(For details on the |dwave_short| API for determining platform-independent paths
to user data and configuration folders see the homebase_ package.)

.. _homebase: https://github.com/dwavesystems/homebase

You can check the directories searched by the
:func:`~dwave.cloud.config.get_configfile_paths` method from a console using the
:ref:`interactive CLI utility <ocean_dwave_cli>`; for example::

    $ dwave config ls -m
    /etc/xdg/xdg-ubuntu/dwave/dwave.conf
    /usr/share/upstart/xdg/dwave/dwave.conf
    /etc/xdg/dwave/dwave.conf
    /home/jane/.config/dwave/dwave.conf
    ./dwave.conf

A single Cloud Client configuration file can contain multiple profiles, each
defining a separate combination of communication parameters such as the URL to
the remote resource, authentication token, solver, etc. Configuration files
conform to a standard Windows INI-style format: profiles are defined by sections
such as, `[profile-a]` and `[profile-b]`. Default values for undefined profile
keys are taken from the `[defaults]` section.

For example, if the configuration file, `~/.config/dwave/dwave.conf`, selected
through auto-detection as the default configuration, contains the following
profiles,\ ::

    [defaults]
    token = ABC-123456789123456789123456789

    [default-solver]
    client = qpu
    solver = {"num_qubits__gt": 5000}

    [hybrid]
    client = hybrid

    [europe]
    region = eu-central-1

    [secondary-project]
    token = DEF-987654321987654321987654321

    [test-advantage2]
    solver = {"topology__type": "zephyr"}

you can instantiate clients for a |dwave_short| quantum computer and a
quantum-classical :term:`hybrid` solver with::

    >>> from dwave.cloud import Client
    >>> client_qpu = Client.from_config()   # doctest: +SKIP
    >>> client_hybrid = Client.from_config(profile='hybrid')   # doctest: +SKIP

.. _sapi_access_env_vars:

Environment Variables
=====================

In addition to files, you can set configuration information through environment
variables; for example:

*   ``DWAVE_CONFIG_FILE`` may select the configuration file path.
*   ``DWAVE_PROFILE`` may select the name of a profile (section).
*   ``DWAVE_API_TOKEN`` may select the API token.

For details on supported environment variables and prioritizing between these
and values set explicitly or through a configuration file, see the
:mod:`dwave.cloud.config` module.

.. _sapi_access_workflow:

Work Flow
=========

A typical workflow may include the following steps:

1.  Instantiate a :class:`~dwave.cloud.client.Client` class to manage
    communication with remote :term:`solver` resources, selecting and
    authenticating access to available solvers; for example, you can list all
    solvers available to a client with its
    :func:`~dwave.cloud.client.Client.get_solvers` method and select and return
    one with its :func:`~dwave.cloud.client.Client.get_solver` method.

    Preferred use is with a context manager---a
    :code:`with Client.from_config(...) as` construct---to ensure proper closure
    of all resources. The following example snippet creates a client based on an
    auto-detected configuration file and instantiates a solver.

    >>> with Client.from_config() as client:   # doctest: +SKIP
    ...     solver = client.get_solver(qpu=True)

    Alternatively, the following example snippet creates a client for software
    resources that it later explicitly closes.

    >>> client = Client.from_config(client='hybrid')   # doctest: +SKIP
    >>> # code that uses client
    >>> client.close()    # doctest: +SKIP

2.  Instantiate a selected :class:`~dwave.cloud.solver.Solver` class, a resource
    for solving problems. Solvers are responsible for:

    -   Encoding submitted problems
    -   Checking submitted parameters
    -   Adding problems to a client's submission queue

    Solvers that provide sampling for solving :term:`Ising` and :term:`QUBO`
    problems, such as an :term:`Advantage`
    :class:`~dwave.system.samplers.DWaveSampler` :term:`sampler`, or constrained
    quadratic models, such as a quantum-classical :term:`hybrid`
    :class:`~dwave.system.samplers.LeapHybridCQMSampler` solver, might be remote
    resources.

3.  Submit your problem, using your solver, and then process the returned
    :class:`~dwave.cloud.computation.Future` class, instantiated by your solver
    to handle remotely executed problem solving.