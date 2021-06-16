.. _install:

======================
Installing Ocean Tools
======================

Ocean software is supported on the following operating systems:

* Linux
* Windows (tested on 64-bit Windows 8, 10)
* Mac (tested on mac OS X 10.13)

Ocean software requires a :ref:`Python environment<pythonEnvironment>`. Python
versions 3.6 and higher are supported.

.. attention::
   D-Wave's Ocean software stopped supporting Python 2 at the end of 2019.

   For information on why many in the Python development community are
   requiring Python 3, see
   `the Python 3 statement <http://python3statement.org/>`_.


This section explains how to :ref:`install Ocean software<installOceanSoftware>`, either the entire suite of tools
or particular tools from the D-Wave GitHub repositories listed in the navigation bar.

Most Ocean tools require that you :ref:`configure a solver<sapi_access>` on your
system, which might be a D-Wave system or a classical sampler that runs on your local CPU.

.. _pythonEnvironment:

Python Virtual Environment
==========================

It's recommended that you work in a
`virtual environment <https://virtualenv.pypa.io/en/stable/>`_ on your local machine;
depending on your operating system, you may need to first install Python and/or
`virtualenv`.

1. `Download Python <https://www.python.org/downloads>`_ describes how to install Python
   on your local machine for supported operating system.

   For Unix-based systems, which often have Python pre-installed, installation
   might be as simple as:

   .. code-block:: bash

       sudo apt-get install python<version>

   .. attention::
      For Windows systems, note that only **64-bit** Python is supported.

#. `Install virtualenv <https://packaging.python.org/guides/installing-using-pip-and-virtualenv>`_
   describes how to install the `virtualenv` tool for creating isolated Python environments
   on your local machine for supported operating system.

   For Unix-based systems, installing virtualenv is typically done with a command such
   as this or similar:

   .. code-block:: bash

       sudo pip install virtualenv

#. Create a virtual environment for your Ocean work. For example, on Unix systems
   you might do:

   .. code-block:: bash

       virtualenv ocean
       source ocean/bin/activate

   (On Windows operating system, activating a virtual environment might be done with the
   :code:`Scripts\activate` command instead.)

Your machine is now ready to install Ocean software.

.. _installOceanSoftware:

Install Ocean Software
======================

The simplest way to start is to install `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
for the full suite of Ocean tools.

* You can :code:`pip install` the SDK inside your newly created virtual environment, typically
  with a command such as this or similar:

  .. code-block:: bash

      pip install dwave-ocean-sdk

* Alternatively, you can clone `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ repo
  and install the SDK to your virtual environment; for example:

  .. code-block:: bash

      git clone https://github.com/dwavesystems/dwave-ocean-sdk.git
      cd dwave-ocean-sdk
      python setup.py install

Note: To install a particular tool within the SDK only, follow the link to the GitHub repository for the tool,
as listed in the navigation bar, and follow the installation instructions on the
README file.

.. _dwave_setup:

Set Up Your Environment
=======================

For a full and easy development experience it is recommended that before you start
writing code, you complete the setup of your environment with two last steps:

* :ref:`setup_install`

  Adds non-open-source tools such as the :ref:`inspector`.
* :ref:`sapi_access`

  Sets defaults used for accessing D-Wave compute resources.

The `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
includes an :ref:`interactive CLI <dwave_cli>` that steps you through setup.

In the virtual environment you created as part of :ref:`install`, run the
:code:`dwave setup` command. The output shown below includes the interactive
prompts and placeholder replies for a full setup. The next sections explain
the details.

.. include:: ../docs_cli.rst
  :start-after: cli-example-setup-start-marker
  :end-before: cli-example-setup-end-marker

.. _setup_install:

Install Contributor Ocean Tools
-------------------------------

The interactive :code:`dwave setup` and :code:`dwave install` commands of the
the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ step
you through installation of non-open-source ("contrib") tools.

If you did not install contributor packages with the :code:`dwave setup` command
in the :ref:`dwave_setup` section, or want to add packages at a later time, you
can use it again then or use the :code:`dwave install` command.

.. code-block:: bash

    $ dwave install --help
    Usage: dwave install [OPTIONS] [PACKAGES]...

       Install optional non-open-source Ocean packages.

    Options:
      -l, --list     List available contrib (non-OSS) packages
      -a, --all      Install all contrib (non-OSS) packages
      -v, --verbose  Increase output verbosity
      --help         Show this message and exit.

Both commands describe the tools and enable you to select which if any to install.

Most Ocean tools solve problems on a :term:`solver`, which is a compute resource
such as a D-Wave system or CPU, and might require that you configure a default solver.
:ref:`sapi_access` describes the next step of setting up your environment, how to
configure your system to access D-Wave or other remote solvers.
