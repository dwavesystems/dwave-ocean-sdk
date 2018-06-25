.. _dwavesys:

=====================
Using a D-Wave System
=====================

You access D-Wave :term:`solver` resources through the D-Wave Sampler API (SAPI).

Interacting with SAPI
---------------------

SAPI is an application layer built to provide resource discovery, permissions, and scheduling for
quantum annealing resources at D-Wave Systems. The requisite information for problem
submission through SAPI includes:

1. API endpoint URL

   A URL to the remote D-Wave system.

2. API Token

   An authentication token the D-Wave system uses to authenticate the client session when
   you connect to the remote environment. Because tokens provide authentication, user names and
   passwords are not required in your code.

3. Solver

   Name of the D-Wave resource to be used to solve your submitted problems.

You can find all the above information when you log in to your D-Wave account.

Setting a D-Wave System as Your Default Solver
----------------------------------------------

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_\ ,
the simplest way to configure a default solver is to use the
`dwave-cloud-client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_ interactive CLI,
which is installed as part of the SDK or D-Wave Cloud Client tool installation.

For example, to use the interactive CLI to create a `D-Wave Cloud Client configuration file <http://dwave-cloud-client.readthedocs.io/en/latest/#module-dwave.cloud.config>`_ that
sets a D-Wave system as your default solver, running the :code:`dwave config create`
interactive command in the virtual environment you created as part of :ref:`install` does
something similar to the following:

.. code-block:: bash

    dwave config create
    Configuration file not found; the default location is: C:\\Users\\jane\\AppData\\Local\\dwavesystem\\dwave\\dwave.conf
    Confirm configuration file path (editable):
    Profile (create new): prod
    API endpoint URL (editable): https://my.dwavesys.url/
    Authentication token (editable): ABC-1234567890abcdef1234567890abcdef
    Client class (qpu or sw): qpu
    Solver (can be left blank): My_DWAVE_2000Q
    Proxy URL (can be left blank):
    Configuration saved.

Alternatively, you can create and edit a `D-Wave Cloud Client configuration file <http://dwave-cloud-client.readthedocs.io/en/latest/#module-dwave.cloud.config>`_
manually or set the solver, API token, and URL directly in your code or as local environment
variables. For more information, see the examples in this document or `D-Wave Cloud Client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_\ .

Verifying Your Solver Configuration
-----------------------------------

You can test that your solver is configured correctly and that you have access to a
D-Wave solver with the same `dwave-cloud-client <http://dwave-cloud-client.readthedocs.io/en/latest/>`_
interactive CLI installed as part of the SDK or D-Wave Cloud Client tool installation.
Running the :code:`dwave config create` interactive command in the virtual environment you
created as part of :ref:`install` does something similar to the following:

.. code-block:: bash

    dwave ping
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

Similarly, you can use the interactive CLI to try submitting a random problem to your
configured solver. Running the :code:`dwave sample --random-problem` command does
something similar to the following:

.. code-block:: bash

    dwave sample --random-problem
    Using endpoint: https://my.dwavesys.url/
    Using solver: My_DWAVE_2000Q
    Using qubit biases: {0: -1.0345257941434953, 1: -0.5795618633919246, 2: 0.9721956399428491, 3: 1....
    Using qubit couplings: {(1634, 1638): 0.721736584181423, (587, 590): 0.9611623181258304, (642, 64...
    Number of samples: 1
    Samples: [[1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1,...
    Occurrences: [1]
    Energies: [-2882.197791239335]

Submitting Problems to a D-Wave System
--------------------------------------

Once you have configured a default solver, it is used when you submit a problem
without explicitly overriding it. For example, setting
:code:`solver = EmbeddingComposite(DWaveSampler())` in the
following code uses your default solver as the computation resource for the
`dwave-system <http://dwave-system.readthedocs.io/en/latest/>`_  structured sampler
that solves problems on the D-Wave system.

.. code-block:: python

   >>> from dwave.system.samplers import DWaveSampler
   >>> from dwave.system.composites import EmbeddingComposite
   >>> sampler = EmbeddingComposite(DWaveSampler())
   >>> response = sampler.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1})
   >>> response.data_vectors['energy']       # doctest: +SKIP
   array([-1.5])

The examples under :ref:`getting_started` demonstrate solving problems on the
D-Wave system, starting from very simple and gradually increasing the complexity.
