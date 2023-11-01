.. _dwave_cli:

===
CLI
===

As part of the installation of the
`dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
a `dwave` executable is installed; for example, in a virtual environment it might
be installed as `<virtual_environment>\\Scripts\\dwave.exe`. Running this file from
your system's console opens an interactive command line interface (CLI) that can
help you set up and configure your development environment, communicate with
D-Wave compute resources, interact with your 
`Leap <https://cloud.dwavesys.com/leap/>`_ account, and other useful actions.

Run :code:`dwave --help` for information on all the CLI options.\ [#]_  For 
**SDK version 6.7.0** the CLI provided the following commands and options
(see the output in your installation for the latest):

.. code-block:: bash

    $ dwave

    Usage: dwave [OPTIONS] COMMAND [ARGS]...

      D-Wave Cloud Client interactive configuration tool.

    Options:
      --version    Show the version and exit.
      --debug      Enable debug logging.
      --trace      Enable trace-level debug logging.
      --log LEVEL  Set custom numeric or symbolic log level.
      --platform   Show the platform tags and exit.
      --help       Show this message and exit.

    Commands:
      auth     Authorize Leap access and fetch Leap/Solver API tokens.
      config   Create, update or inspect cloud client configuration file(s).
      install  Install optional non-open-source Ocean packages.
      leap     Interact with Leap API.
      ping     Ping the QPU by submitting a single-qubit problem.
      sample   Submit Ising-formulated problem and return samples.
      setup    Setup optional Ocean packages and configuration file(s).
      solvers  Get solver details.
      upload   Multipart problem upload with cold restart support.

.. note:: If you work in a Bash shell and want command completion for `dwave`, add

          .. code-block:: bash

             eval "$(_DWAVE_COMPLETE=source <path>/dwave)"

          to your shell's `.bashrc` configuration file, where `<path>` is the absolute
          path to the installed `dwave` executable, for example `/home/Mary/my-quantum-app/env/bin`.

Below are shown example sessions for some of the commands:

* :ref:`cli_example_auth_leap`
* :ref:`cli_example_setup`
* :ref:`cli_example_config`
* :ref:`cli_example_ping`
* :ref:`cli_example_solvers`

.. _cli_example_auth_leap:

Leap 
====

The :code:`dwave auth` and :code:`dwave leap` commands enable Ocean to access 
and interact with your `Leap <https://cloud.dwavesys.com/leap/>`_ account.

For example, in your developer environment (e.g., a Python 
`virtual environment <https://docs.python.org/3/library/venv.html>`_ or a 
`GitHub Codespaces <https://docs.github.com/codespaces>`_ *codespace*), 
you can authorize Ocean's access to your Leap account, using the secure
`OAuth 2.0 <https://oauth.net/2/>`_ code exchange, by running one of the 
following Ocean CLI commands from your terminal. 
    
-   In an environment such as an **IDE installed on your system**, where you can 
    access `localhost <https://en.wikipedia.org/wiki/Localhost>`_ addresses 
    from your browser, initiate the OAuth *redirect* flow::

        dwave auth login

-   In an environment such as a **cloud IDE**, where access to 
    `localhost <https://en.wikipedia.org/wiki/Localhost>`_ addresses 
    from your browser might be blocked, you can initiate the alternative OAuth 
    *out-of-band* flow::

        dwave auth login --oob

With Ocean now authorized to access your Leap account, you can create a 
:ref:`dwave-cloud-client <sdk_index_cloud>` 
:ref:`configuration file <configurationFiles>` to manage your Solver API (SAPI) access
with the SAPI token retrieved from your account as shown in the 
:ref:`cli_example_config` command.

.. _cli_example_setup:

Setup
=====

The :code:`dwave setup` command optionally installs non-open-source packages
and configures your environment.

The output shown below includes the interactive prompts and placeholder replies
for a full setup. The :code:`--auth` authorizes Ocean to 
:ref:`access your Leap account <cli_example_auth_leap>` to fetch your SPI token. 

.. cli-example-setup-start-marker

.. code-block:: bash

    $ dwave setup --auth

    Optionally install non-open-source packages and configure your environment.

    Do you want to select non-open-source packages to install (y/n)? [y]: ↵

    D-Wave Drivers
    These drivers enable some automated performance-tuning features.
    This package is available under the 'D-Wave EULA' license.
    The terms of the license are available online: https://docs.ocean.dwavesys.com/eula
    Install (y/n)? [y]: ↵
    Installing: D-Wave Drivers
    Successfully installed D-Wave Drivers.

    D-Wave Problem Inspector
    This tool visualizes problems submitted to the quantum computer and the results returned.
    This package is available under the 'D-Wave EULA' license.
    The terms of the license are available online: https://docs.ocean.dwavesys.com/eula
    Install (y/n)? [y]: ↵
    Installing: D-Wave Problem Inspector
    Successfully installed D-Wave Problem Inspector.

    Authorizing Leap access.

    Creating the D-Wave configuration file.

    Using the simplified configuration flow.
    Try 'dwave config create --full' for more options.

    Creating new configuration file: /home/jane/.config/dwave/dwave.conf
    Updating existing profile: defaults
    Fetched SAPI token for project 'My-Proj' (ABC) from Leap API.
    Configuration saved.

.. cli-example-setup-end-marker

.. _cli_example_config:

Configure
=========

The :code:`dwave config` command configures your environment.

The output shown below is for a development environment where the user has 
first enabled Ocean's :ref:`Leap access <cli_example_auth_leap>`.

.. cli-example-config-start-marker

.. code-block:: bash

    $ dwave config create --auto-token
    Using the simplified configuration flow.
    Try 'dwave config create --full' for more options.

    Creating new configuration file: /home/jane/.config/dwave/dwave.conf
    Updating existing profile: defaults 
    Access token expired (or expires soon), refreshing it.
    Fetched SAPI token for project 'ABC' (ABC) from Leap API.
    Configuration saved.

.. cli-example-config-end-marker

.. _cli_example_ping:

Ping
====

The :code:`dwave ping` command tests communications with the quantum computer
configured using the :code:`dwave setup` or :code:`dwave config` commands.

.. cli-example-ping-start-marker

The example below, for a Bash Unix shell, pings only QPU solvers.

.. code-block:: bash

    $ dwave ping --client qpu
    Using endpoint: https://cloud.dwavesys.com/sapi
    Using solver: DW_2000Q_6
    Submitted problem ID: 34f773f7-77dc-7fa5-a7d5-7e397d90fc4a

    Wall clock time:
     * Solver definition fetch: 1888.499 ms
     * Problem submit and results fetch: 1038.042 ms
     * Total: 2926.541 ms

    QPU timing:
     * post_processing_overhead_time = 307.0 us
     * qpu_access_overhead_time = 1185.96 us
     * qpu_access_time = 10995.04 us
     * qpu_anneal_time_per_sample = 20.0 us
     * qpu_delay_time_per_sample = 20.54 us
     * qpu_programming_time = 10756.1 us
     * qpu_readout_time_per_sample = 198.4 us
     * qpu_sampling_time = 238.94 us
     * total_post_processing_time = 307.0 us

.. cli-example-ping-end-marker

.. _cli_example_solvers:

Solvers
=======

The :code:`dwave solvers` command queries which D-Wave compute resources are
currently available to your account.

.. cli-example-solvers-start-marker

.. code-block:: bash

    $ dwave solvers  --list --all
    DW_2000Q_6
    hybrid_binary_quadratic_model_version2
    hybrid_discrete_quadratic_model_version1
    Advantage_system4.1

.. cli-example-solvers-end-marker

The example below lists which D-Wave compute resources are currently available
to your account in a particular region (Europe).

.. code-block:: bash

    $ dwave solvers --region eu-central-1 --list --all
    Advantage_system5.1


..  [#] Below are some examples of using the :code:`--help` option 
    to see documentation at different levels of commands and options (produced 
    on SDK version 6.6.0). 
    
    * See all CLI commands:: 

        $ dwave --help
        Usage: dwave [OPTIONS] COMMAND [ARGS]...

            D-Wave Cloud Client interactive configuration tool.

        Options:
            --version    Show the version and exit.    

        ... <Snipped above for brevity>

        Commands:
            auth     Authorize Leap access and fetch Leap/Solver API tokens.
            config   Create, update or inspect cloud client configuration file(s).
            install  Install optional non-open-source Ocean packages.
            leap     Interact with Leap API.
            ping     Ping the QPU by submitting a single-qubit problem.
            ... <Snipped here due to length>

    * See help on a particular CLI command:: 

        $ dwave auth --help
        Usage: dwave auth [OPTIONS] COMMAND [ARGS]...

        Authorize Leap access and fetch Leap/Solver API tokens.

        Options:
            --help  Show this message and exit.

        Commands:
            get      Fetch Leap API token.
            login    Authorize Ocean to access Leap API on user's behalf.
            refresh  Refresh Leap API access token.    

    * See the options available to a particular CLI command:: 

        $ dwave auth login --help
        Usage: dwave auth login [OPTIONS]

        Authorize Ocean to access Leap API on user's behalf.

        Options:
            -p, --profile TEXT      Connection profile (section) name
            -f, --config-file FILE  Configuration file path
            --oob                   Run OAuth 2.0 Authorization Code flow out-of-band,
                                    without the use of locally hosted redirect URL.
            --help                  Show this message and exit.

 