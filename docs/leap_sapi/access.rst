.. the ocean_sapi_access_basic has a couple of xrefs in dwave-system

.. _leap_access:
.. _ocean_sapi_access_basic:

====================
Access Leap Services
====================

.. |config_file_env_var_solver_selection| replace:: The
    :ref:`leap_configuring_dev_env` section shows how to set up the
    :ref:`configuration files <leap_config_files>` and/or
    :ref:`environment variables <leap_access_env_vars>` that enable your solver
    selection.

The |cloud_tm| Solver API (:term:`SAPI`) provides access to the
:term:`solvers <solver>`---compute resources for solving problems, such as
|dwave_short| quantum computers and quantum-classical :term:`hybrid`
solvers---hosted in the `Leap <https://cloud.dwavesys.com/leap/>`_ quantum cloud
service.\ [#]_

This section describes how to authorize the Ocean software in your development
environment to access the Leap service, use your account's SAPI tokens to
authenticate your client sessions with its solvers, and configure your
environment to select solvers (e.g., which solver, from which geographical
:ref:`region <leap_access_multiregion>`, and using which project's
:ref:`SAPI token <leap_access_tokens>`) with
:ref:`configuration files <leap_config_files>` and/or
:ref:`environment variables <leap_access_env_vars>`.

.. [#] SAPI is used similarly for on-premises systems. Differences for such
    systems are noted below.

.. _leap_ocean_authorization:

Authorizing the Ocean SDK
=========================

Authentication using the secure `OAuth 2.0 <https://oauth.net/2/>`_ industry
standard is recommended. It enables the Ocean SDK in your development
environment to access your Leap service account for convenient access to solvers
and the SAPI tokens used to authenticate your client sessions with these
solvers.

.. dropdown:: OAuth Authorization Procedure

    Ocean's SDK
    `releases 6.6 <https://github.com/dwavesystems/dwave-ocean-sdk/releases/tag/6.6.0>`_
    and higher enable Leap authentication using the secure
    `OAuth 2.0 <https://oauth.net/2/>`_ industry standard.

    The following procedure authorizes the Ocean software access to your account
    in the Leap service and enables storing your SAPI token in your development
    environment. Ocean software authorization to access the Leap service
    persists across subsequent development sessions for this development
    environment.

    This procedure uses the :ref:`Ocean software CLI <ocean_dwave_cli>`
    ``dwave setup`` command, which also handles optional Ocean packages and the
    :ref:`configuration files <leap_config_files>` for you; the
    :ref:`CLI <cli_example_auth_leap>` page also describes alternative commands
    (e.g., ``dwave auth``) for more granular control.

    #.  For any new developer environment (for example, a Python
        `virtual environment <https://docs.python.org/3/library/venv.html>`_
        or a `GitHub Codespaces <https://docs.github.com/codespaces>`_
        *codespace*), run one of the following commands from your terminal. If
        your account has more than one project, the
        :ref:`tab_authorize_multiple_leap_projects` tab below shows how to
        select one.

        .. tab-set::

            .. tab-item:: Single Leap Project
                :name: tab_authorize_single_leap_project
                :selected:

                .. include:: ../shared/authorization.rst
                    :start-after: start_local_system
                    :end-before: end_local_system

                .. doctest::
                    :skipif: True

                    dwave setup --auth

                .. include:: ../shared/authorization.rst
                    :start-after: start_cloud_system
                    :end-before: end_cloud_system

                .. doctest::
                    :skipif: True

                    dwave setup --oob

            .. tab-item:: Multiple Leap Projects
                :name: tab_authorize_multiple_leap_projects

                You can log in to your |cloud|_ account, set the preferred
                project to be the active project (by selecting
                *your_user_name* > **Projects** > *project*) and then use the
                procedure described in the
                :ref:`tab_authorize_single_leap_project` tab.

                Alternatively, you can use the ``--project`` option to select a
                project as shown here (the example code below selects a project
                named ``PROJ3``):\ [#]_

                .. include:: ../shared/authorization.rst
                    :start-after: start_local_system
                    :end-before: end_local_system

                .. doctest::
                    :skipif: True

                    dwave setup --auth --project PROJ3

                .. include:: ../shared/authorization.rst
                    :start-after: start_cloud_system
                    :end-before: end_cloud_system

                .. doctest::
                    :skipif: True

                    dwave setup --oob --project PROJ3

                You can always switch your environment to use the SAPI token of
                another project later. For example, if you ran the procedure of
                the :ref:`tab_authorize_single_leap_project` tab with the
                ``PROJ2`` project set to active in Leap, you can at any time
                switch to the ``PROJ3`` project with the
                ``dwave config create --auto-token --project PROJ3`` command.

                .. [#]
                    If you have an existing environment, you can use the
                    ``dwave leap project ls`` command to retrieve the names and
                    codes of all your account's projects.

    #.  If you are not currently logged into the Leap service, you are asked to
        enter your credentials.

        :numref:`Figure %s <LeapLoginScreen>` shows the login screen.

        .. figure:: ../_images/leap_login_screen.png
            :name: LeapLoginScreen
            :alt: image
            :align: center
            :scale: 40%

            Login screen in the Leap service.

    #.  When you are logged into the Leap service, you are asked to grant the
        Ocean software permission to fetch an authorization code.

        :numref:`Figure %s <LeapIdeAuthLogin>` shows the authorization request.

        .. figure:: ../_images/leap_ide_auth_login.png
            :name: LeapIdeAuthLogin
            :alt: image
            :align: center
            :scale: 50%

            Authorization request screen.

        Click the ``Authorize`` button.

        For the OAuth *redirect* flow, the authorization code is now stored in
        your development environment; for the OAuth *out-of-band* flow, your
        browser displays the authorization code.

    #.  For the OAuth *out-of-band* flow only, copy the authorization code to
        your terminal's "``Authorization code:``" prompt, similar to the
        representative shell lines shown below::

            $ dwave setup --oob
            Optionally install non-open-source packages and configure your environment.

            All optional packages already installed.

            Authorizing Leap access.

            Please visit the following URL to authorize Ocean:
            https://cloud.dwavesys.com/leap/openid/authorize?response_type=code&client_id=80...

            Authorization code: 717983...

            Authorization completed successfully. You can now use "dwave auth get"
            to fetch your token.

            Creating the D-Wave configuration file.

            Using the simplified configuration flow.
            Try 'dwave config create --full' for more options.

            Creating new configuration file: /home/user/.config/dwave/dwave.conf
            Updating existing profile: defaults
            Fetched SAPI token for project 'Project 5' (PRJ5) from Leap API.
            Configuration saved.

        :numref:`Figure %s <LeapIdeAuthOobCode>` shows the authorization code
        returned in a browser tab for you to copy to the terminal prompt.

        .. figure:: ../_images/leap_ide_auth_oob_code.png
            :name: LeapIdeAuthOobCode
            :alt: image
            :align: center
            :scale: 50%

            Authorization code screen

    #.  Validate the configuration by running the following command in your
        terminal::

            dwave ping

    If you cloned a |dwave_short| example, you can now run it.

Alternatively, you can copy the SAPI token manually from the dashboard in the
Leap service.

.. _leap_access_tokens:

SAPI Tokens
-----------

An authentication token is used to authenticate the client session when you
connect to the `Leap <https://cloud.dwavesys.com/leap/>`_ service remote
environment.

.. dropdown:: Finding Your SAPI Token

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
            -   Requires that you authorize Leap access as described in the
                :ref:`leap_ocean_authorization` subsection.

    Example: using :ref:`dwave CLI <ocean_dwave_cli>` to see your SAPI token
    (the output shown below is illustrative only).

    .. code-block:: bash

        $ dwave leap project token --project Demo-Proj
        Solver API token for project Demo-Proj (ABC) is ABC-1234567890...12345.

.. dropdown:: Using Your API Token

    Typically, you create a configuration file and/or set environment variables
    in your work environment, as described in the
    :ref:`leap_configuring_dev_env` subsection, so that Ocean tools can
    automatically submit your SAPI token when interacting with SAPI. Because
    tokens provide authentication, user names and passwords are not required
    in your code. The :ref:`table_token_config` table shows various options
    of configuring and directly using your SAPI token.

    .. list-table:: Using Your SAPI Token
        :name: table_token_config
        :header-rows: 1

        *   -   Where
            -   How
            -   Usage Notes
        *   -   :ref:`Configuration file <leap_config_files>`
            -   Configure using the :ref:`dwave CLI <ocean_dwave_cli>` tool
                or edit the file manually.
            -   You can override this configuration by setting an
                environment variable or explicitly in your code.
        *   -   :ref:`Environment variables <leap_access_env_vars>`
            -   Configure :code:`DWAVE_API_TOKEN`. For example,
                :code:`export DWAVE_API_TOKEN=ABC-1234 ... 789` in
                a Unix shell.
            -   You can override this configuration explicitly in your code.
        *   -   Explicit parameters
            -   You can set your SAPI token directly in your code; for
                example,
                :code:`sampler = StrideHybridSolver(token="ABC-1234 ... 789")`
            -   Not recommended outside of testing (for security reasons).

    .. note:: For non-Ocean clients, you set your token in the HTTP header;
        see the :ref:`leap_sapi_rest` section for information.

.. _leap_selecting_solvers:

Selecting Solvers
=================

A *solver* is a  compute resource used to solve your submitted problems; for
example, a :term:`hybrid` :term:`solver` or quantum computer.

.. dropdown::  Viewing Available Solvers

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
                solvers accessible to the current SAPI token; switch to
                another project's SAPI token if needed.
            -   Solvers may be local to a region; see the
                :ref:`leap_access_multiregion` section to query solvers
                outside your default region.

    The following examples require that you create a configuration file and/or
    set environment variables in your work environment, as described in the
    :ref:`leap_configuring_dev_env` subsection.

    Example: using :ref:`dwave CLI <ocean_dwave_cli>` to see the available
    solvers, their parameters, and properties (the output shown below is
    illustrative only).

    .. include:: ../ocean/dwave_cli.rst
        :start-after: cli_example_solvers_start
        :end-before: cli_example_solvers_end

    Example: using :ref:`dwave-cloud-client <index_cloud>` to query for
    hybrid solvers.

    >>> from dwave.cloud import Client
    >>> with Client.from_config() as client:         # doctest: +SKIP
    ...    print(client.get_solvers(hybrid=True))
    [NLSolver(name='stride_hybrid_solver'),
    BQMSolver(name='hybrid_binary_quadratic_model'),
    DQMSolver(name='hybrid_discrete_quadratic_model'),
    CQMSolver(name='hybrid_constrained_quadratic_model')]

    .. note:: For non-Ocean clients, you can retrieve a list of supported
        remote solvers by sending an :code:`HTTP GET` request to the
        :code:`<SAPI base URL>/solvers/` endpoint; see the
        :ref:`leap_sapi_rest` section for information.

.. dropdown:: Selecting a Solver

    By default Ocean software selects solvers based on a set of preferred
    features; for example, by default a problem submitted to a quantum computer
    with the :class:`~dwave.system.samplers.DWaveSampler` class sampler might
    prefer the less busy of two available QPUs. The
    :ref:`table_solvers_selecting` table shows various options to configure
    solver selection.

    .. list-table:: Selecting a Solver
        :name: table_solvers_selecting
        :header-rows: 1

        *   -   Where
            -   How
            -   Usage Notes
        *   -   :ref:`Configuration file <leap_config_files>`
            -   Configure using the :ref:`dwave CLI <ocean_dwave_cli>` tool
                or edit the file manually.
            -   You can override this configuration by setting a solver in
                an environment variable or explicitly in your code.
        *   -   :ref:`Environment variables <leap_access_env_vars>`
            -   Configure :code:`DWAVE_API_SOLVER`. For example,
                :code:`export DWAVE_API_SOLVER='{"num_qubits__gt": 2000}'`
                in a Unix shell.
            -   You can override this configuration by selecting a solver
                explicitly in your code.
        *   -   Explicit parameter
            -   You can set your solver selection directly in your code; for
                example,
                :code:`sampler = DWaveSampler(solver=dict(topology__type='zephyr'))`
            -

|config_file_env_var_solver_selection|

.. _leap_access_multiregion:

Geographical Regions
--------------------

Leap quantum cloud service is distributed across multiple geographic regions.
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
                :func:`~dwave.cloud.regions.get_regions`
            -

    Example: using :ref:`dwave-cloud-client <index_cloud>` to query
    supported regions.

    >>> from dwave.cloud.regions import get_regions
    >>>
    >>> regions = get_regions() # doctest: +SKIP
    >>> for region in regions:  # doctest: +SKIP
    ...    print(f"{region.name}: {region.code}")
    North America (West): na-west-1
    Europe: eu-central-1
    North America (East): na-east-1

    .. note:: Users of on-premises systems should request the SAPI endpoint
        from the system administrator.

    .. note:: For non-Ocean clients, you can retrieve a list of supported
        regions by sending an :code:`HTTP GET` request to the
        :code:`https://cloud.dwavesys.com/metadata/v1/regions` endpoint.

.. dropdown::  Viewing a Region's Solvers

    You can use :ref:`interactive CLI <ocean_dwave_cli>` to query solvers in a
    particular region.

    .. code-block:: bash

        $ dwave solvers --list --region na-east-1
        Advantage2_system4
        Advantage2_research2

|config_file_env_var_solver_selection|

.. dropdown:: Selecting a Solver from a Particular Region

    You can set a preferred geographical region in a few ways.

    *   Select a default region in your
        :ref:`configuration file <leap_config_files>`. You can run the
        :ref:`dwave config <cli_example_config>` CLI command with the
        :code:`--full` option or edit an existing configuration file to set a
        preferred region.
    *   Set the appropriate environment variable (for example,
        :code:`export DWAVE_API_REGION=eu-central-1` in a Unix shell) for your
        current terminal or working session to select solvers from a preferred
        region.
    *   Explicitly select the region in your code. For example, the
        :code:`region` parameter in the code line
        :code:`sampler = DWaveSampler(region="na-west-1")` selects a
        |dwave_short| quantum computer located in North America.

    .. note:: Keep in mind the relative priorities of configurations set at
        various levels (in the above bullets, the configuration file,
        environment variables, and explicit parameters in your code), as
        described in the :ref:`dwave-cloud-client <index_cloud>` reference
        documentation. For example, while the setting of both an endpoint and
        region on the same level (either two lines in the configuration file or
        two environment variables or two explicit parameters) results in
        selection based on the endpoint, setting a region explicitly overrides
        an endpoint configured using an environment variable or in the
        configuration file.

.. dropdown::  Using Configuration-File Profiles for Multiple Regions

    You can set up your configuration file with profiles for multiple regions,
    as shown below.

    .. code-block:: bash

        [defaults]
        token = ABC-123456789123456789123456789

        [europe]
        region = eu-central-1

    You can then set the profile when instantiating a sampler, as below.

    >>> from dwave.system import DWaveSampler, EmbeddingComposite
    >>> sampler = EmbeddingComposite(DWaveSampler(profile="europe"))   # doctest: +SKIP

.. _leap_configuring_dev_env:

Configuring your Work Space
===========================

Typically, you use a configuration file to store tokens and select solvers.
You can always set or override your configurations in your code or with
:ref:`environment variables <leap_access_env_vars>`.

.. the ocean_sapi_access_advanced xref is in a couple of places in cloud client

.. _leap_config_files:
.. _ocean_sapi_access_advanced:

Configuration Files
-------------------

Configuration files conform to a standard
`Windows INI-style <https://en.wikipedia.org/wiki/INI_file>`_ format: profiles
are defined by sections such as, ``[profile-a]`` and ``[profile-b]``.

*   Default values for undefined profile keys are taken from the ``[defaults]``
    section if that exists.
*   If you do not specify a profile, the first profile is read, adding to (and
    possibly overwriting) keys of the ``[defaults]`` section if that exists.

.. _sapi_access_config_create:

.. dropdown::   Create a Configuration File

    The simplest way to configure solver access is to use the
    :ref:`interactive CLI <ocean_dwave_cli>`, which is installed as part of the
    :ref:`dwave-ocean-sdk <ocean_source_code>` installation.

    If you did not already do so with the :ref:`dwave setup <cli_example_setup>`
    command during installation, or want to make changes at a later time, you
    can use the :ref:`dwave config <cli_example_config>` command.

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

    Creating a configuration file using the
    :ref:`dwave config <cli_example_config>` command is done as follows (the
    :ref:`dwave setup <cli_example_setup>` command runs these same configuration
    steps):

    1.  In your Python environment, run the :code:`dwave config create`
        command\ [#]_ (the output shown below includes the interactive prompts
        and placeholder replies).

    .. include:: ../ocean/dwave_cli.rst
        :start-after: cli_example_config_start
        :end-before: cli_example_config_end

    2.  If needed, enter SAPI information (e.g. your SAPI token) found as
        described in the :ref:`leap_access_tokens` section. To get started,
        create a minimum configuration by accepting the command's defaults
        (pressing Enter) for all prompts\ [#]_. You can in the future update the
        file if needed.

    Alternatively, you can create and edit a configuration file manually (see
    the reference documentation for the :ref:`dwave-cloud-client <index_cloud>`
    package).

    .. [#] You can use the :code:`--auto-token` option if you have authorized
        Leap access as described in :ref:`leap_ocean_authorization`.

    .. [#] Users of on-premises systems should also enter the SAPI endpoint.
        Users interested in using solvers hosted outside their default region
        can also configure the SAPI endpoint (see the
        :ref:`leap_access_multiregion` section for the recommended way of
        configuring such access).

.. _sapi_access_config_verify:

.. dropdown::   Verify Your Configuration

    You can test that your solver access is configured correctly with the
    :ref:`interactive CLI <ocean_dwave_cli>`. The output shown below is
    illustrative only.

    1.  In your environment, run the :ref:`dwave ping <cli_example_ping>`
        command.

    .. include:: ../ocean/dwave_cli.rst
        :start-after: cli_example_ping_start
        :end-before: cli_example_ping_end

    2.  **Optionally**, run the
        :code:`dwave sample --random-problem --client qpu` command to submit a
        random problem to a remote solver. The truncated output shown below is
        illustrative only.

    .. code-block:: bash

        $ dwave sample --random-problem --client qpu
        Using endpoint: https://cloud.dwavesys.com/sapi/
        Using region: na-west-1
        Using solver: Advantage_system6
        ...
        Occurrences: [1]
        Energies: [-14243.244540499865]
        ...

.. dropdown:: Locating Your Configuration Files

    If a configuration file is not explicitly specified when instantiating a
    client or solver, auto-detection searches for candidate files in a number of
    standard directories, depending on your local system's operating system. You
    can see the standard locations with the
    :func:`~dwave.cloud.config.get_configfile_paths` method.

    For example, on a Unix system, depending on its flavor, these might include
    (in order)::

        /usr/share/dwave/dwave.conf
        /usr/local/share/dwave/dwave.conf
        ~/.config/dwave/dwave.conf
        ./dwave.conf

    On Windows 7+, configuration files are expected to be located under::

        C:\\Users\\<username>\\AppData\\Local\\dwavesystem\\dwave\\dwave.conf

    On Mac OS X, configuration files are expected to be located under::

        ~/Library/Application Support/dwave/dwave.conf

    (For details on the |dwave_short| API for determining platform-independent
    paths to user data and configuration folders see the homebase_ package.)

    .. _homebase: https://github.com/dwavesystems/homebase

    You can check the directories searched by the
    :func:`~dwave.cloud.config.get_configfile_paths` method from a console using
    the :ref:`interactive CLI utility <ocean_dwave_cli>`; for example::

        $ dwave config ls -m
        /etc/xdg/xdg-ubuntu/dwave/dwave.conf
        /usr/share/upstart/xdg/dwave/dwave.conf
        /etc/xdg/dwave/dwave.conf
        /home/jane/.config/dwave/dwave.conf
        ./dwave.conf

.. dropdown::   Configure Multiple Profiles

    A single configuration file can contain multiple profiles, each defining a
    separate combination of communication parameters such as the URL to the
    remote resource, SAPI token, solver, etc.

    For example, if the configuration file, ``~/.config/dwave/dwave.conf``,
    selected through auto-detection as the default configuration, contains the
    following profiles,\ ::

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

The reference documentation for the :ref:`dwave-cloud-client <index_cloud>`
package provides more examples.

.. _leap_access_env_vars:

Environment Variables
---------------------

In addition to files, you can set configuration information through environment
variables; for example:

*   ``DWAVE_CONFIG_FILE`` may select the configuration file path.
*   ``DWAVE_PROFILE`` may select the name of a profile (section).
*   ``DWAVE_API_TOKEN`` may select the SAPI token.

For details on supported environment variables and prioritizing between these
and values set explicitly or through a configuration file, see the
:mod:`dwave.cloud.config` module.