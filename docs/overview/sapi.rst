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

   A URL to the remote resources. By default, 
   ``https://na-west-1.cloud.dwavesys.com/sapi/v2`` is used to connect to 
   resources provided by D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ 
   quantum cloud service in North America, including D-Wave quantum computers.\ [#]_

2. API Token

   An authentication token used to authenticate the client session when
   you connect to the remote environment. Because tokens provide authentication, user names and
   passwords are not required in your code.

3. Solver

   A D-Wave resource to be used to solve your submitted problems; for example, a
   hybrid solver or an Advantage quantum computer.

You can find all the above information when you log in to your D-Wave account. For
Leap users, select the Dashboard tab; for on-premises (Qubist) users, select the
Solver API tab and the API Tokens menu item under your user name.

You save your SAPI configuration (URL, API token, etc) in a
:doc:`D-Wave Cloud Client configuration file </docs_cloud/sdk_index>`
that Ocean tools use unless overridden explicitly or with environment variables.
Your configuration file can include one or more solvers.

.. [#]
   For information about using solvers in alternative geographical regions,
   see the :ref:`sapi_intro_multiregion` section below.    

.. note:: When you work in D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ IDE,
   SAPI information such as your API token is pre-configured in the default
   workspace's environment variables.

Creating a Configuration File
=============================

The simplest way to configure solver access is to use the :ref:`interactive CLI <dwave_cli>`, which
is installed as part of
the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
installation.

If you did not already do so with the :ref:`dwave setup <cli_example_setup>` command
in the :ref:`dwave_setup` section, or want to make changes at a later time, you
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

Creating a configuration file using the :ref:`dwave config <cli_example_config>` is done
as follows (the :ref:`dwave setup <cli_example_setup>` command of the :ref:`dwave_setup` section
runs these same configuration steps):

1. In the virtual environment you created as part of :ref:`install`, run the
   :code:`dwave config create` command (the output shown below
   includes the interactive prompts and placeholder replies).

.. include:: ../docs_cli.rst
  :start-after: cli-example-config-start-marker
  :end-before: cli-example-config-end-marker

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

You can test that your solver access is configured correctly with the
:ref:`interactive CLI <dwave_cli>`.

1. In your virtual environment, run the :ref:`dwave ping <cli_example_ping>` command (the output shown
   below is illustrative only).

.. include:: ../docs_cli.rst
  :start-after: cli-example-ping-start-marker
  :end-before: cli-example-ping-end-marker

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
:ref:`interactive CLI <dwave_cli>` to see the available solvers, their parameters, and properties.

1. Run the :ref:`dwave solvers <cli_example_solvers>` command (the output shown below is illustrative only).

.. include:: ../docs_cli.rst
  :start-after: cli-example-solvers-start-marker
  :end-before: cli-example-solvers-end-marker

Alternatively, from within your code or a Python interpreter you can query solvers available for
a SAPI URL and API token using
:doc:`dwave-cloud-client </docs_cloud/sdk_index>` :meth:`~dwave.cloud.client.Client.get_solvers`
function. For example, the code below queries available solvers for your default SAPI URL and a
specified token.

>>> from dwave.cloud import Client        
>>> client = Client.from_config(token='ABC-123456789123456789123456789')     # doctest: +SKIP
>>> client.get_solvers()       # doctest: +SKIP
[Solver(id='2000Q_ONLINE_SOLVER1'),
 UnstructuredSolver(id='hybrid_binary_quadratic_model_version2')]

Typically, once you have selected and configured a solver, your code queries its parameters and
properties as attributes of the instantiated solver object. The code example below
(with output snipped for brevity) sets a D-Wave system as the sampler, using the default 
SAPI configuration as set above, and queries its parameters.

>>> from dwave.system import DWaveSampler
>>> sampler = DWaveSampler(solver={'qpu': True})
>>> sampler.parameters            # doctest: +SKIP
{u'anneal_offsets': ['parameters'],
 u'anneal_schedule': ['parameters'],
 u'annealing_time': ['parameters'],
 u'answer_mode': ['parameters'],
 u'auto_scale': ['parameters'], ...

Descriptions of D-Wave system parameters and properties are in the
:std:doc:`system documentation <sysdocs_gettingstarted:index>`.

.. _sapi_intro_multiregion:

Accessing Solvers in Multiple Regions
=====================================

Leap quantum cloud service is distributed across multiple geographic regions.
You can see the supported regions and the solvers available in each for your 
account in your `Leap <https://cloud.dwavesys.com/leap/>`_ dashboard. To 
specify a preferrence for solver selection from a particular region, you can 
use the standard selection methods supported by Ocean's :ref:`sdk_index_cloud`: 

* Select a default region in your 
  :ref:`dwave-cloud-client configuration file <sdk_index_cloud>`. You can run 
  the :ref:`dwave config <cli_example_config>` CLI command with the 
  :code:`--full` option or edit an existing configuration file to set a 
  preferred region.  
* Set the appropriate environment variable (for example, 
  :code:`export DWAVE_API_REGION=eu-central-1` in a Unix shell) for your current 
  terminal or working session to select solvers from a preferred region. 
* Explicitly select the region in your code. For example, the :code:`region`
  parameter in the code line :code:`sampler = DWaveSampler(region="na-west-1")` 
  selects a D-Wave quantum computer located in North America. 

.. note:: Keep in mind the relative priorities of configurations set at 
   various levels (in the above bullets, the configuration file, environment 
   variables, and explicit parameters in your code), as described in the 
   :ref:`sdk_index_cloud` documentation. For example, while the setting of both 
   an endpoint and region on the same level (either two lines in the configuration 
   file or two environment variables or two explicit parameters) results in 
   selection based on the endpoint, setting a region explicitly overrides an 
   endpoint configured using an environment variable or in the configuration
   file. 

