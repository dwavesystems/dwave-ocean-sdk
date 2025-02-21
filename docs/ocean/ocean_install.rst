.. _ocean_install:

========================
Installing the Ocean SDK
========================

Ocean software is supported on the following operating systems:

*   **Linux:** tested on 64-bit OS
*   **Windows:** tested on 64-bit Windows 8, 10
*   **Mac:** tested on macOS 10.15.5 (Xcode 12.2)

Ocean software requires a :ref:`Python environment <ocean_install_python_env>`.
Python versions |python_requires| are supported.

This section explains how to install Ocean software.

.. _ocean_install_python_env:

Python Virtual Environment
==========================

It's recommended that you work in a
:std:doc:`virtual environment <python:library/venv>` on your local machine;
depending on your operating system, you may need to first install Python.

1.  `Download Python <https://www.python.org/downloads>`_ describes how to
    install Python on your local machine for supported operating system.

    .. attention::
        For Windows systems, note that only **64-bit** Python is supported.

#.  Create a virtual environment for your Ocean work. For example, on Unix
    systems you might do:

    .. code-block:: bash

        python -m venv ocean
        . ocean/bin/activate

    (On Windows operating system, activating a virtual environment might be done
    with the :code:`Scripts\\activate` command instead.)

Your machine is now ready to install Ocean software.

.. _ocean_install_software:

Install Ocean Software
======================

The simplest way to start is to install
:ref:`dwave-ocean-sdk <ocean_source_code>` for the full suite of Ocean tools.

You can :code:`pip install` the SDK inside your newly created virtual
environment.

*   For a standard installation of the latest released version from the
    `Python Package Index (PyPI) <https://pypi.org/>`_ repository:

    .. code-block:: bash

        pip install dwave-ocean-sdk

*   Advanced users might directly install the latest (development) SDK from the
    `D-Wave GitHub <https://github.com/dwavesystems/dwave-ocean-sdk>`_
    repository using a command such as,

    .. code-block:: bash

        pip install git+https://github.com/dwavesystems/dwave-ocean-sdk

Alternatively, you can clone the :ref:`dwave-ocean-sdk <ocean_source_code>` repo
and install the SDK to your virtual environment; for example:

.. code-block:: bash

    git clone https://github.com/dwavesystems/dwave-ocean-sdk.git
    cd dwave-ocean-sdk
    python setup.py install

Note: To install a particular tool within the SDK only, follow the
:ref:`link <ocean_source_code>`  to the GitHub repository for the tool, and
follow the installation instructions on the README file.

.. _ocean_install_setup_env:

Set Up Your Environment
=======================

For a full and easy development experience it is recommended that before you
start writing code, you complete the setup of your environment with these last
steps:

*   :ref:`ocean_leap_authorization`

    Optionally authorize Ocean to access your Leap account to facilitate
    token management.

*   :ref:`ocean_install_contrib`

    Adds non-open-source tools such as the
    :ref:`problem inspector <dwave_inspector>`.

*   :ref:`ocean_sapi_access_basic`

    Sets defaults used for accessing |dwave_short| compute resources.

The :ref:`dwave-ocean-sdk <ocean_source_code>` includes an
:ref:`interactive CLI <ocean_dwave_cli>` that steps you through setup.

In the virtual environment you created as part of :ref:`ocean_install` above,
run the :code:`dwave setup` command. The output shown below includes the
interactive prompts and placeholder replies for a full setup.

.. tip:: New users can accept the :code:`dwave setup` command's defaults (press
    Enter) for all prompts except the authentication token, which is displayed
    on the `Leap <https://cloud.dwavesys.com/leap/>`_ dashboard for your
    account. The :ref:`ocean_sapi_access_basic` section explains how you can
    update your work environment's configuration at any time.

.. include:: ocean_dwave_cli.rst
    :start-after: cli_example_setup_start
    :end-before: cli_example_setup_start_end

.. _ocean_install_contrib:

Install Contributor Ocean Tools
-------------------------------

The interactive :code:`dwave setup` and :code:`dwave install` commands of the
the :ref:`dwave-ocean-sdk <ocean_source_code>` step you through installation of
non-open-source ("contrib") tools.

If you did not install contributor packages with the :code:`dwave setup` command
in the :ref:`ocean_install_setup_env` subsection, or want to add packages at a
later time, you can use it again then or use the :code:`dwave install` command.

.. code-block:: bash

    $ dwave install --help
    Usage: dwave install [OPTIONS] [PACKAGES]...

       Install optional non-open-source Ocean packages.

    Options:
      -l, --list     List available contrib (non-OSS) packages
      -a, --all      Install all contrib (non-OSS) packages
      -v, --verbose  Increase output verbosity
      --help         Show this message and exit.

Both commands describe the tools and enable you to select which if any to
install.

Most Ocean tools solve problems on a :term:`solver`, which is a compute resource
such as a |dwave_short| quantum computer or CPU, and might require that you
configure a default solver. The :ref:`ocean_sapi_access_basic` describes the
next step of setting up your environment, how to configure your system to access
|dwave_short| or other remote solvers.
