.. _install:

======================
Installing Ocean Tools
======================

Ocean software requires a Python environment.

You can install the entire suite of tools by installing the
`dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ or install particular
tools from the D-Wave GitHub repositories listed under :ref:`projects`.

Most Ocean tools require that you configure on your system a default :term:`solver`, which
might be a D-Wave system or a classical sampler that runs on your local CPU.

Python Virtual Environment
==========================

It's recommended that you work in a
`virtual environment <https://packaging.python.org/guides/installing-using-pip-and-virtualenv>`_ on
your local machine; depending on your operating system, you may need to first install Python and/or
`virtualenv`.

1. `Download Python <https://www.python.org/downloads>`_ describes how to install Python
   on your machine.

   For Unix-based systems, which often have Python pre-installed, installation
   might be as simple as :code:`sudo apt-get install python<version>`.
#. `Install virtualenv <https://virtualenv.pypa.io/en/stable/>`_ describes how to
   install the `virtualenv` tool for creating isolated Python environment.

   Installing virtualenv is typically done with a :code:`sudo pip install virtualenv`
   command or similar.
#. Create a virtual environment for your Ocean work. For example:

   .. code-block:: bash

       virtualenv ocean
       cd ocean
       source ./bin/activate

   (On Windows operating system, activating a virtual environment might be done with the
   :code:`Scripts\activate` command instead.)

Your machine is now ready to install Ocean software.

Install the SDK or a Tool
=========================

The simplest way to start is to install `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
for the full suite of OCean tools.

* You can pip install the SDK in your newly created virtual environment, typically
  with a :code:`pip install dwave-ocean-sdk` command or similar.
* Alternatively, you can clone (copy) `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
  to your virtual environment; for example:

  .. code-block:: bash

      git clone https://github.com/dwavesystems/dwave-ocean-sdk.git
      cd dwave-ocean-sdk
      python setup.py install

To install just a particular tool, follow the link to the GitHub repository for the tool,
as listed under :ref:`projects`, and follow the Installation instructions on the
README file.

Configure a Solver
==================

Most Ocean tools solve problems on a :term:`solver`, and might require that you configure
a default solver.

* :ref:`dwavesys` describes how to configure your system to solve problems on a D-Wave system.
* :ref:`cpu` describes how to configure your system to solve problems classically on your local CPU/GPU.
