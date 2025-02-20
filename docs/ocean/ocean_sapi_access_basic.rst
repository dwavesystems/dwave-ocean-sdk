.. _ocean_sapi_access_basic:

==============================================
Configuring Access to the Leap Service (Basic)
==============================================

The |dwave_short_tm| Solver API (:term:`SAPI`) provides access to the
:term:`solvers <solver>`---compute resources for solving problems, such as
|dwave_short| quantum computers and quantum-classical :term:`hybrid`
solvers---hosted in the `Leap <https://cloud.dwavesys.com/leap/>`_ quantum cloud
service.\ [#]_

.. [#] SAPI is used similarly for on-premises systems. Differences for such
    systems are noted below.

This section provides the following information:

*   Section :ref:`sapi_access_interacting` provides information on viewing and
    configuring SAPI resources.
*   Section :ref:`sapi_access_config_create` steps you through creating a
    configuration file, which enables you to interact conveniently with SAPI.
*   Section :ref:`sapi_access_config_verify` ensures that your environment is
    set up correctly.
*   Section :ref:`sapi_intro_multiregion` provides information for users
    interested in using solvers hosted outside their default region.

.. _sapi_access_interacting:

Interacting with SAPI
=====================

SAPI is an application layer that provides resource discovery, permissions,
and scheduling for |dwave_short| :term:`solvers <solver>`. Problem submission
through SAPI requires the following information, typically provided by your work
environment from either Ocean's default values or your configuration.

*   **API Token** (required)

    An authentication token used to authenticate the client session when you
    connect to the remote environment.

    .. dropdown:: Finding your API Token

        The :ref:`table_token_viewing` table shows various options to view
        your SAPI token.

        .. list-table:: Viewing Your SAPI Token
            :name: table_token_viewing
            :header-rows: 1

            *   -   Where
                -   How
                -   Defaults
                -   Usage Notes
            *   -   `Leap <https://cloud.dwavesys.com/leap/>`_ dashboard
                -   Log in to your Leap account.
                -   For users that belong to multiple projects, your SAPI token
                    for the current project is displayed; switch the current
                    project if needed.
                -
            *   -   :ref:`dwave-cloud-client <index_cloud>`
                -   Use the :ref:`dwave CLI <ocean_dwave_cli>` tool.
                -   For users that belong to multiple projects, you can specify
                    the relevant project.
                -   Requires that you authorize
                    :ref:`Leap access <ocean_leap_authorization>`.

        Example: using :ref:`dwave CLI <ocean_dwave_cli>` to see your SAPI token
        (the output shown below is illustrative only).

        .. code-block:: bash

            $ dwave leap project token --project Demo-Proj
            Solver API token for project Demo-Proj (ABC) is ABC-1234567890...12345.

    .. dropdown:: Using your API Token

        Typically, you configure your work environment so Ocean tools can
        automatically submit your API token when interacting with SAPI. Because
        tokens provide authentication, user names and passwords are not required
        in your code. The :ref:`table_token_config` table shows various options
        of configuring and directly using your API token.

        .. list-table:: Using your API Token
            :name: table_token_config
            :header-rows: 1

            *   -   Where
                -   How
                -   Usage Notes
            *   -   :ref:`Configuration file <index_cloud>`
                -   Configure using the :ref:`dwave CLI <ocean_dwave_cli>` tool
                    or edit the file manually.
                -   You can override this configuration by setting an
                    environment variable or explicitly in your code.

                    .. todo:: check the link below

            *   -   :std:doc:`Environment variables <docs_cloud/reference/configuration>`
                -   Configure :code:`DWAVE_API_TOKEN`. For example,
                    :code:`export DWAVE_API_TOKEN=ABC-1234 ... 789` in
                    a Unix shell.
                -   You can override this configuration explicitly in your code.
            *   -   Explicit parameters
                -   You can set your API token directly in your code; for
                    example,
                    :code:`sampler = LeapHybridCQMSampler(token="ABC-1234 ... 789")`
                -   Not recommended outside of testing (for security reasons).

        .. note:: For non-Ocean clients, you set your token in the HTTP header;
            see the :ref:`leap_sapi_rest` section for information.

*   **Solver** (default: feature-based selection)

    A |dwave_short| resource to be used to solve your submitted problems; for
    example, a :term:`hybrid` :term:`solver` or an :term:`Advantage` quantum
    computer.

    .. dropdown:: Viewing Available Solvers

        The :ref:`table_solvers_viewing` table shows various options to view
        available solvers.

        .. list-table:: Viewing Available Solvers
            :name: table_solvers_viewing
            :header-rows: 1

            *   -   Where
                -   How
                -   Defaults
                -   Usage Notes
            *   -   `Leap <https://cloud.dwavesys.com/leap/>`_ dashboard
                -   Log in to your Leap account.
                -   For users that belong to multiple projects, solvers
                    accessible to the current project are displayed; switch the
                    current project if needed.
                -   Solvers may be local to a region.
            *   -   :ref:`dwave-cloud-client <index_cloud>`
                -   Use the :ref:`dwave CLI <ocean_dwave_cli>` tool or Ocean's
                    :meth:`~dwave.cloud.client.Client.get_solvers` method.
                -   For users that belong to multiple projects, queries return
                    solvers accessible to the current API token; switch to
                    another project's API token if needed.
                -   Solvers may be local to a region; see the
                    :ref:`sapi_intro_multiregion` subsection to query solvers
                    outside your default region.

        Example: using :ref:`dwave CLI <ocean_dwave_cli>` to see the available
        solvers, their parameters, and properties (the output shown below is
        illustrative only).

        .. include:: ocean_dwave_cli.rst
            :start-after: cli-example-solvers-start-marker
            :end-before: cli-example-solvers-end-marker

        Example: using :doc:`dwave-cloud-client <index_cloud>` to query for
        hybrid solvers.

        >>> from dwave.cloud import Client
        >>> with Client.from_config() as client:         # doctest: +SKIP
        ...    print(client.get_solvers(hybrid=True))
        [BQMSolver(id='hybrid_binary_quadratic_model_version2'),
        DQMSolver(id='hybrid_discrete_quadratic_model_version1'),
        CQMSolver(id='hybrid_constrained_quadratic_model_version1')]

        .. note:: For non-Ocean clients, you can retrieve a list of supported
            remote solvers by sending an :code:`HTTP GET` request to the
            :code:`<SAPI base URL>/solvers/` endpoint; see the
            :ref:`leap_sapi_rest` section for information.

    .. dropdown:: Selecting a Solver

        By default Ocean selects solvers based on a set of preferred features;
        for example, by default a problem submitted to a quantum computer with
        the :class:`~dwave.system.samplers.DWaveSampler` class sampler might
        prefer the less busy of two available QPUs. The
        :ref:`table_solvers_selecting` table shows various options to configure
        solver selection.

        .. list-table:: Selecting a Solver
            :name: table_solvers_selecting
            :header-rows: 1

            *   -   Where
                -   How
                -   Usage Notes
            *   -   :ref:`Configuration file <index_cloud>`
                -   Configure using the :ref:`dwave CLI <ocean_dwave_cli>` tool
                    or edit the file manually.
                -   You can override this configuration by setting a solver in
                    an environment variable or explicitly in your code.

                    .. todo:: check the link below

            *   -   :std:doc:`Environment variables <oceandocs:docs_cloud/reference/configuration>`
                -   Configure :code:`DWAVE_API_SOLVER`. For example,
                    :code:`export DWAVE_API_SOLVER='{"num_qubits__gt": 2000}'`
                    in a Unix shell.
                -   You can override this configuration by selecting a solver
                    explicitly in your code.
            *   -   Explicit parameter
                -   You can set your solver selection directly in your code; for
                    example,
                    :code:`sampler = DWaveSampler(solver=dict(topology__type='pegasus'))`
                -

*   **Region/Endpoint** (default: North American URL)

    A URL for a region's remote resources.

    By default, Ocean connects to North American (region :code:`na-west-1`) Leap
    quantum cloud resources at URL
    :code:`https://na-west-1.cloud.dwavesys.com/sapi/v2/`.

    .. dropdown:: Finding Supported Regions and Endpoints

        The :ref:`table_regions_viewing` table shows various options for viewing
        available regions and their URLs.

        .. list-table:: Viewing Available Regions and Endpoints
            :name: table_regions_viewing
            :header-rows: 1

            *   -   Where
                -   How
                -   Usage Notes
            *   -   `Leap <https://cloud.dwavesys.com/leap/>`_ dashboard
                -   Log in to your Leap account
                -   Solvers available to your account are grouped by region.
            *   -   :ref:`dwave-cloud-client <index_cloud>`
                -   Use the :ref:`Interactive CLI <ocean_dwave_cli>` or
                    :meth:`~dwave.cloud.client.Client.get_regions`
                -

        Example: using :doc:`dwave-cloud-client <index_cloud>` to query
        supported regions.

            >>> from dwave.cloud import Client
            >>> with Client.from_config() as client:          # doctest: +SKIP
            ...    regions = client.get_regions()
            ...    for code, info in regions.items():
            ...        print(f"{info['name']} ({code}): {info['endpoint']}")
            North America (na-west-1): https://na-west-1.cloud.dwavesys.com/sapi/v2/
            Europe (eu-central-1): https://eu-central-1.cloud.dwavesys.com/sapi/v2/

        .. note:: Users of on-premises systems should request the SAPI endpoint
            from the system administrator.

        .. note:: For non-Ocean clients, you can retrieve a list of supported
            regions by sending an :code:`HTTP GET` request to the
            :code:`https://cloud.dwavesys.com/metadata/v1/regions` endpoint.

    For information about using solvers in alternative geographical regions,
    see the :ref:`sapi_intro_multiregion` section below.

.. _sapi_access_config_create:

Create a Configuration File
===========================

The simplest way to configure solver access is to use the
:ref:`interactive CLI <ocean_dwave_cli>`, which is installed as part of the
:ref:`dwave-ocean-sdk <ocean_source_code>` installation.

If you did not already do so with the :ref:`dwave setup <cli_example_setup>`
command in the :ref:`ocean_install_setup_env` subsection, or want to make
changes at a later time, you can use the
:ref:`dwave config <cli_example_config>` command.

.. code-block:: bash

    $ dwave config --help
    Usage: dwave config [OPTIONS] COMMAND [ARGS]...

    Create, update or inspect cloud client configuration file(s).

    Options:
      --help  Show this message and exit.

    Commands:
      create   Create and/or update cloud client configuration file.
      inspect  Inspect existing configuration/profile.
      ls       List configuration files detected (and/or examined paths).

Creating a configuration file using the :ref:`dwave config <cli_example_config>`
is done as follows (the :ref:`dwave setup <cli_example_setup>` command of the
:ref:`ocean_install_setup_env` subsection runs these same configuration steps):

1.  In the virtual environment you created as part of :ref:`ocean_install`
    procedure, run the :code:`dwave config create` command\ [#]_ (the output
    shown below includes the interactive prompts and placeholder replies).

.. include:: ocean_dwave_cli.rst
    :start-after: cli-example-config-start-marker
    :end-before: cli-example-config-end-marker

.. [#] You can use the :code:`--auto-token` option if you have authorized
    :ref:`Leap access <ocean_leap_authorization>`.

2.  If needed, enter SAPI information (e.g. your API token) found as described
    in the :ref:`sapi_access_interacting` subsection above. To get started,
    create a minimum configuration by accepting the command's defaults (pressing
    Enter) for all prompts\ [#]_. You can in the future update the file if
    needed.

.. [#] Users of on-premises systems should also enter the SAPI endpoint. Users
   interested in using solvers hosted outside their default region can also
   configure the SAPI endpoint (see the :ref:`sapi_intro_multiregion` subsection
   for the recommended way of configuring such access).

Alternatively, you can create and edit a
:ref:`dwave-cloud-client configuration file <index_cloud>` manually.

You can always set or override your configurations in your code or with
environment variables. For more information, see the examples in this document
or the :ref:`dwave-cloud-client configuration file <index_cloud>` reference
documentation.

.. _sapi_access_config_verify:

Verify Your Configuration
=========================

You can test that your solver access is configured correctly with the
:ref:`interactive CLI <ocean_dwave_cli>`.

1.  In your virtual environment, run the :ref:`dwave ping <cli_example_ping>`
    command (the output shown below is illustrative only).

.. include:: ocean_dwave_cli.rst
    :start-after: cli-example-ping-start-marker
    :end-before: cli-example-ping-end-marker

2.  **Optionally**, run the :code:`dwave sample --random-problem` command to
    submit a random problem to a remote solver (the output shown below is
    illustrative only).

.. code-block:: bash

    $ dwave sample --random-problem
    Using endpoint: https://my.dwavesys.url/
    Using solver: My_DWAVE_2000Q
    Using qubit biases: {0: -1.0345257941434953, 1: -0.5795618633919246, 2: 0.9721956399428491, 3: 1....
    Using qubit couplings: {(1634, 1638): 0.721736584181423, (587, 590): 0.9611623181258304, (642, 64...
    Number of samples: 1
    Samples: [[1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1,...
    Occurrences: [1]
    Energies: [-2882.197791239335]

.. _sapi_intro_multiregion:

Accessing Solvers in Multiple Regions
=====================================

Leap quantum cloud service is distributed across multiple geographic regions.
You can see the supported regions and the solvers available in each for your
account in your `Leap <https://cloud.dwavesys.com/leap/>`_ dashboard. Ocean's
:ref:`dwave-cloud-client <index_cloud>` package enables you to select solvers
from a particular region using one or more of the following options:

*   Select a default region in your
    :ref:`dwave-cloud-client configuration file <index_cloud>`. You can run the
    :ref:`dwave config <cli_example_config>` CLI command with the :code:`--full`
    option or edit an existing configuration file to set a preferred region.
*   Set the appropriate environment variable (for example,
    :code:`export DWAVE_API_REGION=eu-central-1` in a Unix shell) for your
    current terminal or working session to select solvers from a preferred
    region.
*   Explicitly select the region in your code. For example, the :code:`region`
    parameter in the code line
    :code:`sampler = DWaveSampler(region="na-west-1")` selects a |dwave_short|
    quantum computer located in North America.

.. note:: Keep in mind the relative priorities of configurations set at various
    levels (in the above bullets, the configuration file, environment variables,
    and explicit parameters in your code), as described in the
    :ref:`dwave-cloud-client <index_cloud>` reference documentation. For
    example, while the setting of both an endpoint and region on the same level
    (either two lines in the configuration file or two environment variables or
    two explicit parameters) results in selection based on the endpoint, setting
    a region explicitly overrides an endpoint configured using an environment
    variable or in the configuration file.

Example: Viewing a Region's Solvers
-----------------------------------

You can use :ref:`interactive CLI <ocean_dwave_cli>` to query solvers in a
particular region.

.. code-block:: bash

    $ dwave solvers --list --region eu-central-1
    Advantage_system5.1

Example: Using Configuration-File Profiles for Multiple Regions
---------------------------------------------------------------

You can set up your configuration file with profiles for multiple regions, as
shown below.

.. code-block:: bash

    [defaults]
    token = ABC-123456789123456789123456789

    [europe]
    region = eu-central-1

You can then set the profile when instantiating a sampler, as below.

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler(profile="europe"))   # doctest: +SKIP