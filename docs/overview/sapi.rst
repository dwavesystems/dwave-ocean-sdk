.. _sapi_access:

====================================
Configuring Access to D-Wave Solvers
====================================

D-Wave's Solver API (SAPI) provides access to :term:`solver`\ s, remote compute resources
for solving problems such as a D-Wave system or `Leap <https://cloud.dwavesys.com/leap/>`_\ 's
quantum-classical hybrid solvers.

Interacting with SAPI
=====================

SAPI is an application layer built to provide resource discovery, permissions, and
scheduling for D-Wave compute resources. The requisite information for problem
submission through SAPI includes:

1. API endpoint URL

   A URL to the remote resources. By default, ``https://cloud.dwavesys.com/sapi``
   is used to connect to resources provided by
   D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ quantum cloud service,
   including D-Wave quantum computers.

2. API Token

   An authentication token used to authenticate the client session when
   you connect to the remote environment. Because tokens provide authentication, user names and
   passwords are not required in your code.

3. Solver

   A D-Wave resource to be used to solve your submitted problems; for example, a
   hybrid solver or a D-Wave 2000Q quantum computer.

You can find all the above information when you log in to your D-Wave account. For
Leap users, select the Dashboard tab; for on-premises (Qubist) users, select the
Solver API tab and the API Tokens menu item under your user name.

You save your SAPI configuration (URL, API token, etc) in a
:doc:`D-Wave Cloud Client configuration file </docs_cloud/sdk_index>`
that Ocean tools use unless overridden explicitly or with environment variables.
Your configuration file can include one or more solvers.

.. note:: When you work in D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ IDE,
   SAPI information such as your API token is pre-configured in the default
   workspaces' environment variables.

Creating a Configuration File
=============================

The simplest way to configure solver access is to use the interactive CLI, which
is installed as part of
the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
installation.

If you did not already do so with the :code:`dwave setup` command
in the :ref:`dwave_setup` section, or want to make changes at a later time, you
can use the :code:`dwave config` command.

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

Creating a configuration file using the :code:`dwave config` is done
as follows (the :code:`dwave setup` command of the :ref:`dwave_setup` section
runs these same configuration steps):

1. In the virtual environment you created as part of :ref:`install`, run the
   :code:`dwave config create` command (the output shown below
   includes the interactive prompts and placeholder replies).

.. code-block:: bash

    $ dwave config create
    Configuration file not found; the default location is: /home/jane/.config/dwave/dwave.conf
    Confirm configuration file path [/home/jane/.config/dwave/dwave.conf]:
    Profile (create new) [prod]:
    API endpoint URL [skip]:
    Authentication token [skip]: ABC-1234567890abcdef1234567890abcdef
    Default client class (qpu or sw) [qpu]:
    Default solver [skip]:
    Configuration saved.

2. Enter the SAPI information (e.g. your API token) found as described in the section
   above. To get started, create a minimum configuration by accepting the command's
   defaults (pressing Enter) for all prompts except the API token (Leap users) or
   API token and endpoint (on-premises users). You can in the future update the
   file if needed.

Alternatively, you can create and edit a
:doc:`D-Wave Cloud Client configuration file </docs_cloud/sdk_index>`
manually.

You can always set or override the solver, API token, and URL directly in your code
or as local environment variables. For more information, see the examples in this
document or :doc:`D-Wave Cloud Client </docs_cloud/sdk_index>`.

Verifying Your Configuration
----------------------------

You can test that your solver access is configured correctly with the same
interactive CLI installed as part of the SDK installation.

1. In your virtual environment, run the :code:`dwave ping` command (the output shown
   below is illustrative only).

.. code-block:: bash

    $ dwave ping
    Using endpoint: https://my.dwavesys.url/
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

2. **Optionally**, run the :code:`dwave sample --random-problem` command to submit a random
   problem to a remote solver (the output shown below is illustrative only).

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

Querying Available Solvers
==========================

.. note:: `Leap <https://cloud.dwavesys.com/leap/>`_ accounts can see accessible solvers
   on the dashboard.

From your terminal, you can use the 
interactive CLI to see the available solvers, their parameters, and properties.

1. Run the :code:`dwave solvers` command (the output shown below is illustrative only).

.. code-block:: bash

    $ dwave solvers
    Solver: My_DWAVE_2000Q
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

Alternatively, from within your code or a Python interpreter you can query solvers available for
a SAPI URL and API token using
:doc:`dwave-cloud-client </docs_cloud/sdk_index>` :meth:`~dwave.cloud.client.Client.get_solvers`
function. For example, the code below queries available solvers for your default SAPI URL and a
specified token.

.. code-block:: python

   >>> from dwave.cloud import Client
   >>> client = Client.from_config(token='ABC-123456789123456789123456789')
   >>> client.get_solvers()
   [Solver(id='2000Q_ONLINE_SOLVER1'),
    UnstructuredSolver(id='hybrid_v1')]

Typically, once you have selected and configured a solver, your code queries its parameters and
properties as attributes of the instantiated solver object. The code example below
sets a D-Wave system as the sampler, using the default SAPI configuration as set above,
and queries its parameters.

.. code-block:: python

   >>> from dwave.system import DWaveSampler
   >>> sampler = DWaveSampler(solver={'qpu': True})
   >>> sampler.parameters
   {u'anneal_offsets': ['parameters'],
   u'anneal_schedule': ['parameters'],
   u'annealing_time': ['parameters'],
   u'answer_mode': ['parameters'],
   u'auto_scale': ['parameters'],
   # Snipped above response for brevity

Descriptions of D-Wave system parameters and properties are in the
:std:doc:`system documentation <sysdocs_gettingstarted:index>`.
