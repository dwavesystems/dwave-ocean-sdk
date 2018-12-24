.. _dwavesys:

=====================
Using a D-Wave System
=====================

To use a D-Wave system as your :term:`solver` (the compute resource for solving problems),
you access it through the D-Wave Solver API (SAPI).

Interacting with SAPI
---------------------

SAPI is an application layer built to provide resource discovery, permissions, and scheduling for
quantum annealing resources at D-Wave. The requisite information for problem
submission through SAPI includes:

1. API endpoint URL

   A URL to the remote D-Wave system. By default, https://cloud.dwavesys.com/sapi is used to
   connect to resources provided by D-Wave's Leap Quantum Application Environment.

2. API Token

   An authentication token the D-Wave system uses to authenticate the client session when
   you connect to the remote environment. Because tokens provide authentication, user names and
   passwords are not required in your code.

3. Solver

   A D-Wave resource to be used to solve your submitted problems.

You can find all the above information when you log in to your D-Wave account. For
Leap users, select the Dashboard tab; for on-premises (Qubist) users, select the
Solver API tab and the API Tokens menu item under your user name.

You save your SAPI configuration (URL, API token, etc) in a
:std:doc:`D-Wave Cloud Client configuration file <cloud-client:index>`
that Ocean tools use unless overridden explicitly or with environment variables.
Your configuration file can include one or more solvers.


Configuring a D-Wave System as a Solver
---------------------------------------

The simplest way to configure a solver is to use the
:std:doc:`dwave-cloud-client <cloud-client:index>`
interactive CLI, which is installed as part of
the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ (or D-Wave Cloud
Client tool installation).

1. In the virtual environment you created as part of :ref:`install`, run the
   :code:`dwave config create` command (the output shown below
   includes the interactive prompts and placeholder replies).

.. code-block:: bash

    $ dwave config create
    Configuration file not found; the default location is: C:\\Users\\jane\\AppData\\Local\\dwavesystem\\dwave\\dwave.conf
    Confirm configuration file path (editable):
    Profile (create new): prod
    API endpoint URL (editable): https://my.dwavesys.url/
    Authentication token (editable): ABC-1234567890abcdef1234567890abcdef
    Client class (qpu or sw): qpu
    Solver (can be left blank): {"qpu": true, "vfyc": true}
    Proxy URL (can be left blank):
    Configuration saved.

2. Enter the SAPI information (e.g. your API token) found as described above. You can
   accept the command's defaults and in the future update the file if needed.

   To get started, Leap users can create a minimum configuration by entering only an API
   token; on-premises users should also set the URL to the on-premises system.

Alternatively, you can create and edit a
:std:doc:`D-Wave Cloud Client configuration file <cloud-client:index>`
manually or set the solver, API token, and URL directly in your code or as local environment
variables. For more information, see the examples in this document or
:std:doc:`D-Wave Cloud Client <cloud-client:index>`.

Verifying Your Solver Configuration
-----------------------------------

You can test that your solver is configured correctly and that you have access to a
D-Wave solver with the same
:std:doc:`dwave-cloud-client <cloud-client:index>`
interactive CLI installed as part of the SDK or D-Wave Cloud Client tool installation.

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
   problem to your configured solver (the output shown below is illustrative only).

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
--------------------------

The :std:doc:`dwave-cloud-client <cloud-client:index>`
interactive CLI can also show you the available solvers, their parameters, and
properties.

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
:std:doc:`dwave-cloud-client <cloud-client:index>` :meth:`~dwave.cloud.client.Client.get_solvers`
function. For example, the code below queries available solvers for your default SAPI URL and a
specified token.

.. code-block:: python

   >>> from dwave.cloud import Client
   >>> client = Client.from_config(token='ABC-123456789123456789123456789')
   >>> client.get_solvers()
   [Solver(id='2000Q_ONLINE_SOLVER1'),
    Solver(id='2000Q_ONLINE_SOLVER2')]

Typically, once you have selected and configured a solver, your code queries its parameters and
properties as attributes of the instantiated solver object. The code example below
sets a D-Wave system as the sampler, using the default SAPI configuration as set above,
and queries its parameters.

.. code-block:: python

   >>> from dwave.system.samplers import DWaveSampler
   >>> sampler = DWaveSampler()
   >>> sampler.parameters
   {u'anneal_offsets': ['parameters'],
   u'anneal_schedule': ['parameters'],
   u'annealing_time': ['parameters'],
   u'answer_mode': ['parameters'],
   u'auto_scale': ['parameters'],
   # Snipped above response for brevity

Descriptions of D-Wave system parameters and properties are in the :ref:`sysdocs`.

Submitting Problems to a D-Wave System
--------------------------------------

Once you have configured a
:std:doc:`D-Wave Cloud Client configuration file <cloud-client:index>`
your default solver configuration is used when you submit a problem without explicitly overriding it.
For example, the following code uses a
:std:doc:`dwave-system <system:index>`
structured sampler, :code:`EmbeddingComposite(DWaveSampler())`, as the sampler, which uses a
D-Wave system for the compute resource. Because no parameters (e.g., SAPI endpoint URL) are set
explicitly, the line :code:`sampler = EmbeddingComposite(DWaveSampler())` uses your default solver.

.. code-block:: python

   >>> from dwave.system.samplers import DWaveSampler
   >>> from dwave.system.composites import EmbeddingComposite
   >>> sampler = EmbeddingComposite(DWaveSampler())
   >>> response = sampler.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1})
   >>> response.data_vectors['energy']       # doctest: +SKIP
   array([-1.5])

The examples under :ref:`gs` demonstrate solving problems on the
D-Wave system, starting from very simple and gradually increasing the complexity.
