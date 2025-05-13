.. _ocean_leap_authorization:

======================================
Authorizing Access to the Leap Service
======================================

Ocean's SDK
`releases 6.6 <https://github.com/dwavesystems/dwave-ocean-sdk/releases/tag/6.6.0>`_
and higher enable Leap\ |tm| authentication using the secure
`OAuth 2.0 <https://oauth.net/2/>`_ industry standard. As described in the
:ref:`ocean_sapi_access_basic` section, you require a Solver API (:term:`SAPI`)
token from your Leap account to submit problems to Leap
:term:`solvers <solver>`.

Authorization Procedure
=======================

The following procedure authorizes the Ocean software access to your account in
the Leap service and enables storing your SAPI token in your development
environment. Ocean software authorization to access the Leap service persists
across subsequent development sessions for this development environment.

This procedure uses the :ref:`Ocean software CLI <ocean_dwave_cli>`
``dwave setup`` command, which also handles optional Ocean packages and the
configuration file for you; the :ref:`CLI <cli_example_auth_leap>` page also
describes alternative commands (e.g., ``dwave auth``) for more granular control.

#.  For any new developer environment (for example, a Python
    `virtual environment <https://docs.python.org/3/library/venv.html>`_
    or a `GitHub Codespaces <https://docs.github.com/codespaces>`_ *codespace*),
    run one of the following commands from your terminal. If your account has
    more than one project, the :ref:`tab_authorize_multiple_leap_projects` tab
    below shows how to select one.

    .. tab-set::

        .. tab-item:: Single Leap Project
            :name: tab_authorize_single_leap_project
            :selected:

            .. include:: ../shared/authorization.rst
                :start-after: start_local_system
                :end-before: end_local_system

            .. doctest::
                :skipif: True

                dwave setup --auth

            .. include:: ../shared/authorization.rst
                :start-after: start_cloud_system
                :end-before: end_cloud_system

            .. doctest::
                :skipif: True

                dwave setup --oob

        .. tab-item:: Multiple Leap Projects
            :name: tab_authorize_multiple_leap_projects

            You can log in to your |cloud|_ account, set the preferred
            project to be the active project (by selecting
            *your_user_name* > **Projects** > *project*) and then use the
            procedure described in the :ref:`tab_authorize_single_leap_project`
            tab.

            Alternatively, you can use the ``--project`` option to select a
            project as shown here (the example code below selects a project
            named ``PROJ3``):\ [#]_

            .. include:: ../shared/authorization.rst
                :start-after: start_local_system
                :end-before: end_local_system

            .. doctest::
                :skipif: True

                dwave setup --auth --project PROJ3

            .. include:: ../shared/authorization.rst
                :start-after: start_cloud_system
                :end-before: end_cloud_system

            .. doctest::
                :skipif: True

                    dwave setup --oob --project PROJ3

            You can always switch your environment to use the API token of
            another project later. For example, if you ran the procedure of the
            :ref:`tab_authorize_single_leap_project` tab with the ``PROJ2``
            project set to active in Leap, you can at any time switch to the
            ``PROJ3`` project with the
            ``dwave config create --auto-token --project PROJ3`` command.

            .. [#]
                If you have an existing environment, you can use the
                ``dwave leap project ls`` command to retrieve the names and
                codes of all your account's projects.

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

        $ dwave setup --oob
        Optionally install non-open-source packages and configure your environment.

        All optional packages already installed.

        Authorizing Leap access.

        Please visit the following URL to authorize Ocean:
        https://cloud.dwavesys.com/leap/openid/authorize?response_type=code&client_id=80...

        Authorization code: 717983...

        Authorization completed successfully. You can now use "dwave auth get"
        to fetch your token.

        Creating the D-Wave configuration file.

        Using the simplified configuration flow.
        Try 'dwave config create --full' for more options.

        Creating new configuration file: /home/user/.config/dwave/dwave.conf
        Updating existing profile: defaults
        Fetched SAPI token for project 'Project 5' (PRJ5) from Leap API.
        Configuration saved.

    :numref:`Figure %s <LeapIdeAuthOobCode>` shows the authorization code
    returned in a browser tab for you to copy to the terminal prompt.

    .. figure:: ../_images/leap_ide_auth_oob_code.png
        :name: LeapIdeAuthOobCode
        :alt: image
        :align: center
        :scale: 50%

        Authorization code screen

#.  Validate the configuration by running the following command in your
    terminal::

        dwave ping

If you cloned a |dwave_short| example, you can now run it.

Manual Authorization
====================

The `OAuth-based <https://oauth.net/2/>`_ procedure of the previous section is
provided for convenience but you also have the option of manually copying your
SAPI token from the dashboard in the Leap service. The
:ref:`ocean_sapi_access_basic` section provides more information.