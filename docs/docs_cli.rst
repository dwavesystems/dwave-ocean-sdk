.. _dwave_cli:

=========
dwave CLI
=========

As part of the installation of the
`dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
a `dwave` executable is installed; for example, in a virtual environment it might
be installed as `<virtual_environment>\\Scripts\\dwave.exe`. Running this file from
your system's console opens an interactive command line interface (CLI) that can
help you set up and configure your development environment, communicate with
D-Wave compute resources, and other useful actions.

Run :code:`dwave -- help` for information on all the CLI options. For **SDK
version 4.0.0** the CLI provided the following commands and options
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
      config   Create, update or inspect cloud client configuration file(s).
      install  Install optional non-open-source Ocean packages.
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

* :ref:`cli_example_setup`
* :ref:`cli_example_config`
* :ref:`cli_example_ping`
* :ref:`cli_example_solvers`

.. _cli_example_setup:

Setup
=====

The :code:`dwave setup` command optionally installs non-open-source packages
and configures your environment.

The output shown below includes the interactive prompts and placeholder replies
for a full setup.

.. cli-example-setup-start-marker

.. code-block:: bash

    $ dwave setup

    Optionally install non-open-source packages and configure your environment.

    Do you want to select non-open-source packages to install (y/n)? [y]:

    D-Wave Drivers
    These drivers enable some automated performance-tuning features.
    This package is available under the 'D-Wave EULA' license.
    The terms of the license are available online: https://docs.ocean.dwavesys.com/eula
    Install (y/n)? [y]:
    Installing: D-Wave Drivers
    Successfully installed D-Wave Drivers.

    D-Wave Problem Inspector
    This tool visualizes problems submitted to the quantum computer and the results returned.
    This package is available under the 'D-Wave EULA' license.
    The terms of the license are available online: https://docs.ocean.dwavesys.com/eula
    Install (y/n)? [y]:
    Installing: D-Wave Problem Inspector
    Successfully installed D-Wave Problem Inspector.

    Creating the D-Wave configuration file.
    Using the simplified configuration flow.
    Try 'dwave config create --full' for more options.

    Creating new configuration file: /home/jane/.config/dwave/dwave.conf
    Profile [defaults]:
    Updating existing profile: defaults
    Authentication token [skip]: ABC-1234567890abcdef1234567890abcdef
    Configuration saved.

.. cli-example-setup-end-marker

.. _cli_example_config:

Configure
=========

The :code:`dwave config` command configures your environment.

The output shown below includes the interactive prompts and placeholder replies.

.. cli-example-config-start-marker

.. code-block:: bash

    $ dwave config create
    Using the simplified configuration flow.
    Try 'dwave config create --full' for more options.

    Creating new configuration file: /home/jane/.config/dwave/dwave.conf
    Profile [defaults]:
    Updating existing profile: defaults
    Authentication token [skip]: ABC-1234567890abcdef1234567890abcdef
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

    $ dwave ping -s '{"qpu": true}'
    Using endpoint: https://cloud.dwavesys.com/sapi
    Using solver: My_DWAVE_2000Q

    Wall clock time:
     * Solver definition fetch: 2007.239 ms
     * Problem submit and results fetch: 1033.931 ms
     * Total: 3041.171 ms

    QPU timing:
     * total_real_time = 10493 us
     * anneal_time_per_run = 20 us
     * post_processing_overhead_time = 128 us
     * qpu_anneal_time_per_sample = 20 us
     # Snipped for brevity

.. cli-example-ping-end-marker

.. _cli_example_solvers:

Solvers
=======

The :code:`dwave solvers` command queries which D-Wave compute resources are
currently available to your account.

.. cli-example-solvers-start-marker

.. code-block:: bash

    $ dwave solvers
    Solver: DW_2000Q_33
       Parameters:
          anneal_offsets: A list of anneal offsets for each working qubit (NaN if u...
          anneal_schedule: A piecewise linear annealing schedule specified by a list...
          annealing_time: A positive integer that sets the duration (in microsecond...

          <Output snipped for brevity>

       Properties:
          anneal_offset_ranges: [[-0.18627387668142237, 0.09542224439071689], [-0.1836548...
          anneal_offset_step: 0.00426679499507194
          anneal_offset_step_phi0: 0.0002716837027763096
          annealing_time_range: [1, 150000]
          chip_id: W7-1_C16_4724854-02-G4_C5R9-device-cal-data-18-05-27-14:27
          couplers: [[0, 4], [1, 4], [2, 4], [3, 4], [0, 5], [1, 5], [2, 5], ...

          <Output snipped for brevity>

.. cli-example-solvers-end-marker

The example below lists which D-Wave compute resources are currently available 
to your account in a particular region (Europe).

.. code-block:: bash

    $ dwave solvers --region eu-central-1 --list --all
    Advantage_system5.1

