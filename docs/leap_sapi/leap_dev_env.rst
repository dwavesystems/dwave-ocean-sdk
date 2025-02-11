.. _leap_dev_env:

================
Support for IDEs
================

The Leap quantum cloud service supports third-party IDEs, both local and
cloud-based, that implement the
`Development Containers specification <https://containers.dev/supporting>`_
(aka "devcontainers"). Although any IDE that implements devcontainers
is supported, |dwave_short| recommends
`GitHub Codespaces <https://docs.github.com/codespaces>`_.

The Ocean SDK
`releases 6.6 <https://github.com/dwavesystems/dwave-ocean-sdk/releases/tag/6.6.0>`_
and higher enable authentication using the secure
`OAuth 2.0 <https://oauth.net/2/>`_ industry standard. The
:ref:`leap_dev_env_authorization` procedure described here simplifies the
retrieval and storage of your Solver API (SAPI) token for use in submitting
problems to solvers in the Leap service from the third-party IDE of your choice.

For an overview about developing quantum applications, see the
:ref:`opt_developing_quantum_applications` section; for a beginner's
introduction, see the :ref:`opt_index_get_started` section. Also see end-to-end
`examples of D-Wave quantum applications in GitHub <https://github.com/dwave-examples>`_.

Requirements
============

*   Ocean SDK
    `releases 6.6 <https://github.com/dwavesystems/dwave-ocean-sdk/releases/tag/6.6.0>`_
    or higher.

If you configure your IDE to use
`Ocean-Dev Docker Images <https://github.com/dwavesystems/ocean-dev-docker>`_,
your development environment is updated with a recent Ocean SDK release.
You can see an example `here <https://github.com/dwave-examples/sudoku>`_.

.. _leap_dev_env_authorization:

Authorizing Access to the Leap Service
======================================

As described in the :ref:`ocean_sapi_access_basic` section for Ocean software,
you require a SAPI token to submit problems to solvers in the Leap service. The
following procedure authorizes the Ocean software access to your account in the
Leap service and enables storing your SAPI token in your development
environment. Ocean software authorization to access the Leap service persists
across subsequent development sessions for this development environment.

.. note:: The following `OAuth-based <https://oauth.net/2/>`_ procedure is
    provided for convenience but you also have the option of manually copying
    your SAPI token from the dashboard in the Leap service. The
    :ref:`ocean_sapi_access_basic` section provides more information.

This procedure uses the :ref:`Ocean software CLI <ocean_dwave_cli>` commands
that you enter into your terminal. You can see help documentation for these
commands and all their options with the CLI's ``--help`` option.\ [#]_

#.  For any new developer environment (for example, a Python
    `virtual environment <https://docs.python.org/3/library/venv.html>`_
    or a `GitHub Codespaces <https://docs.github.com/codespaces>`_ *codespace*),
    authorize the Ocean software access to your account in the Leap service,
    using the secure `OAuth 2.0 <https://oauth.net/2/>`_ code exchange, by
    running one of the following commands from your terminal.

    -   In an environment such as an **IDE installed on your system**, where you
        can access `localhost <https://en.wikipedia.org/wiki/Localhost>`_
        addresses from your browser, initiate the OAuth *redirect* flow::

            dwave auth login

    -   In an environment such as a **cloud IDE**, where access to
        `localhost <https://en.wikipedia.org/wiki/Localhost>`_ addresses from
        your browser might be blocked, you can initiate the alternative OAuth
        *out-of-band* flow::

            dwave auth login --oob

#.  If you are not currently logged into the Leap service, you are asked to
    enter your credentials.

    :numref:`Figure %s <LeapLoginScreen>` shows the login screen.

    .. figure:: ../_images/leap_login_screen.png
        :name: LeapLoginScreen
        :alt: image
        :align: center
        :scale: 40%

        Login screen in the Leap service.

#.  When you are logged into the Leap service, you are asked to grant the Ocean
    software permission to fetch an authorization code.

    :numref:`Figure %s <LeapIdeAuthLogin>` shows the authorization request.

    .. figure:: ../_images/leap_ide_auth_login.png
        :name: LeapIdeAuthLogin
        :alt: image
        :align: center
        :scale: 50%

        Authorization request screen.

    Click the ``Authorize`` button.

    For the OAuth *redirect* flow, the authorization code is now stored in your
    development environment; for the OAuth *out-of-band* flow, your browser
    displays the authorization code.

#.  For the OAuth *out-of-band* flow only, copy the authorization code to your
    terminal's "``Authorization code:``" prompt, similar to the representative
    shell lines shown below::

        $ dwave auth login --oob
        Please visit the following URL to authorize Ocean:
        https://leap.dwavesystems.com/leap/openid/authorize?response_type=code&client_id=96...

        Authorization code: 717983...

    :numref:`Figure %s <LeapIdeAuthOobCode>` shows the authorization code
    returned in a browser tab for you to copy to the terminal prompt.

    .. figure:: ../_images/leap_ide_auth_oob_code.png
        :name: LeapIdeAuthOobCode
        :alt: image
        :align: center
        :scale: 50%

        Authorization code screen

#.  Create a :ref:`dwave-cloud-client <index_cloud>`
    :ref:`configuration file <configurationFiles>` to manage your SAPI access
    by running the following command from your terminal::

        dwave config create --auto-token

#.  Validate the configuration by running the following command in your
    terminal::

        dwave ping

If you cloned a |dwave_short| example, you can now run it.

.. [#] Below are some examples of displaying commands, options, and help
    documentation for the :ref:`dwave-cloud-client <index_cloud>` CLI (produced
    on version ``0.11.0``). For more information, see the
    :ref:`Ocean software CLI <ocean_dwave_cli>` section.

    *   Display all commands::

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

    *   Display help on a particular command::

            $ dwave auth --help
            Usage: dwave auth [OPTIONS] COMMAND [ARGS]...

            Authorize access to the Leap service and fetch API tokens.

            Options:
                --help  Show this message and exit.

            Commands:
                get      Fetch Leap API token.
                login    Authorize Ocean to access Leap API on user's behalf.
                refresh  Refresh Leap API access token.

    *   Display the options available to a particular command::

            $ dwave auth login --help
            Usage: dwave auth login [OPTIONS]

            Authorize Ocean to access Leap API on user's behalf.

            Options:
                -p, --profile TEXT      Connection profile (section) name
                -f, --config-file FILE  Configuration file path
                --oob                   Run OAuth 2.0 Authorization Code flow
                                        out-of-band, without the use of locally
                                        hosted redirect URL.
                --help                  Show this message and exit.