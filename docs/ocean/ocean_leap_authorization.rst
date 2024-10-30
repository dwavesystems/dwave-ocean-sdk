.. _leap_auth:

======================================
Authorizing Access to the Leap Service
======================================

.. |TM| replace:: :sup:`TM`

Ocean's SDK `releases 6.6 <https://github.com/dwavesystems/dwave-ocean-sdk/releases/tag/6.6.0>`_   
and higher enable Leap\ |TM| authentication using the secure 
`OAuth 2.0 <https://oauth.net/2/>`_ industry standard. As described in the 
:std:doc:`oceandocs:overview/sapi` section, you require a Solver API (SAPI) 
token from your Leap account to submit problems to Leap solvers. 

.. note:: The `OAuth-based <https://oauth.net/2/>`_ authorization is 
    provided for convenience but you also have the option of manually copying 
    your SAPI token from Leap. 

For any new developer environment (for example, a Python 
`virtual environment <https://docs.python.org/3/library/venv.html>`_ or a 
`GitHub Codespaces <https://docs.github.com/codespaces>`_ *codespace*), 
authorize Ocean's access to your Leap account, using the secure
`OAuth 2.0 <https://oauth.net/2/>`_ code exchange, by running one of the 
following `Ocean CLI <https://docs.ocean.dwavesys.com/en/stable/docs_cli.html>`_ 
commands\ [#]_ from your terminal. Ocean authorization to access Leap is persisted 
across subsequent development sessions for this development environment. 

-   In an environment such as an **IDE installed on your system**, where you can 
    access `localhost <https://en.wikipedia.org/wiki/Localhost>`_ addresses 
    from your browser, initiate the OAuth *redirect* flow::

        dwave auth login

-   In an environment such as a **cloud IDE**, where access to 
    `localhost <https://en.wikipedia.org/wiki/Localhost>`_ addresses 
    from your browser might be blocked, you can initiate the alternative OAuth 
    *out-of-band* flow::

        dwave auth login --oob

A page opened in your browser will lead you through the authorization procedure. 

.. [#]
    You can see help documentation for 
    `Ocean CLI <https://docs.ocean.dwavesys.com/en/stable/docs_cli.html>`_ commands 
    and all their options with the CLI's ``--help`` option. 




