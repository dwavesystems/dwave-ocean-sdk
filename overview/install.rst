.. _install:

======================
Installing Ocean Tools
======================

Ocean software is supported on the following operating systems:

* Linux
* Windows (tested on 64-bit Windows 8, 10)
* Mac (tested on mac OS X 10.13)

Ocean software requires a :ref:`Python environment<pythonEnvironment>`. Supported Python versions are:

* 2.7.x
* 3.5 and higher

This section explains how to :ref:`install Ocean software<installOceanSoftware>`, either the entire suite of tools
or particular tools from the D-Wave GitHub repositories listed under :ref:`projects`.

Most Ocean tools require that you :ref:`configure a solver<configureSolver>` on your
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
as listed under :ref:`projects`, and follow the installation instructions on the
README file.

.. _configureSolver:

Configure a Solver
==================

Most Ocean tools solve problems on a :term:`solver`, which is a compute resources such as a D-Wave
system or CPU, and might require that you configure a default solver.

* :ref:`dwavesys` describes how to configure your system to solve problems on a D-Wave system.
* :ref:`cpu` describes how to configure your system to solve problems classically on your local CPU/GPU.
