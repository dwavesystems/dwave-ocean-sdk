.. _ocean_leap_authorization:

======================================
Authorizing Access to the Leap Service
======================================

.. |TM| replace:: :sup:`TM`

Ocean's SDK
`releases 6.6 <https://github.com/dwavesystems/dwave-ocean-sdk/releases/tag/6.6.0>`_
and higher enable Leap\ |TM| authentication using the secure
`OAuth 2.0 <https://oauth.net/2/>`_ industry standard. As described in the
:ref:`ocean_sapi_access_basic` section, you require a Solver API (:term:`SAPI`)
token from your Leap account to submit problems to Leap
:term:`solvers <solver>`.

.. note:: The `OAuth-based <https://oauth.net/2/>`_ authorization is provided
    for convenience but you also have the option of manually copying your SAPI
    token from the Leap service's dashboard.

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
commands and all their options with the CLI's ``--help`` option.

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
    :ref:`configuration file <sapi_access_config_files>` to manage your SAPI
    access by running the following command from your terminal::

        dwave config create --auto-token

#.  Validate the configuration by running the following command in your
    terminal::

        dwave ping

If you cloned a |dwave_short| example, you can now run it.