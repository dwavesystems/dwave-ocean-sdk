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
`OAuth 2.0 <https://oauth.net/2/>`_ industry standard. The procedure described
in the :ref:`ocean_leap_authorization` section simplifies the retrieval and
storage of your Solver API (:term:`SAPI`) token for use in submitting problems
to :term:`solvers <solver>` in the Leap service from the third-party IDE of your
choice.

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
