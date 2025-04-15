.. _index_leap_sapi:

============
Leap Service
============

.. toctree::
    :hidden:
    :maxdepth: 1

    dev_env
    admin
    sapi_rest
    Leap Service Release Notes <https://docs.dwavequantum.com/projects/leap_sapi/en/latest/index.html>

The |cloud_tm| quantum cloud service provides real-time cloud access to
|dwave_short|_ quantum computers and :term:`hybrid` :term:`solvers <solver>`.

.. sections-start-marker

.. grid:: 2 2 3 3
    :gutter: 2

    .. grid-item-card:: :ref:`leap_dev_env`
        :img-top: /_images/ide_icon.svg
        :link: leap_dev_env
        :link-type: ref

        Description of Leap support for third-party IDEs.

    .. grid-item-card:: :ref:`leap_admin`
        :img-top: /_images/leap_admin_icon.svg
        :link: leap_admin
        :link-type: ref

        Description of how project administrators manage access
        to projects in Leap.

    .. grid-item-card:: :ref:`leap_sapi_rest`
        :img-top: /_images/rest_api_icon.svg
        :link: leap_sapi_rest
        :link-type: ref

        Reference documentation for the :term:`Solver API <SAPI>` (SAPI)
        REST interface.

    .. grid-item-card:: Leap Service Release Notes
        :img-top: /_images/release_notes_icon.svg
        :link: https://docs.dwavequantum.com/projects/leap_sapi/en/latest/index.html
        :link-type: url

        Leap service release notes, fixed and open issues.

About the Service
=================

.. figure:: ../_images/network-leap-simple.png
    :alt: network diagram showing a laptop connecting to a |dwave_short| quantum
        computer through the cloud.
    :scale: 50 %
    :figwidth: 25%
    :align: right

The Leap service hosts |dwave_short|'s :term:`solvers <solver>`, including
quantum computers and :term:`hybrid` solvers. It enables you to do the
following:

*   Submit problems and view results and usage statistics
*   Administer projects
*   Find learning resources: a `Community page <https://support.dwavesys.com/>`_
    where you can pose questions and provide answers to other users,
    a `Resources page <https://cloud.dwavesys.com/leap/resources/demos/>`_ with
    interactive demos and a searchable collection of examples, and a
    `Help Center <https://support.dwavesys.com/>`_ for frequently asked
    questions (FAQ) section and a searchable knowledge base

Sign up for the Leap service here: https://cloud.dwavesys.com/leap.

Dashboard
---------

The dashboard is the home for your experience using the Leap service and
contains a considerable amount of useful information, some of which you can also
update; for example:

*   Your account settings and a summary of your account
*   Your active project and its associated API token
*   Status of problems you have submitted and usage statistics
*   Solver status

You might be a member of multiple projects, but the information displayed on the
dashboard is only for the active project; for example, the solvers that have
been assigned to the active project. You can make a different project active by
selecting *your_user_name* > **Projects** > *project*.

The Leap service supports solvers in multiple regions (for example, North
America and Europe). The dashboard displays the solvers that are available by
region.

Solver Access
=============

Your customer plan\ [#]_ and :ref:`seat type <admin_def_seat_type>` in a
project, together with your customer contract (where applicable), determine your
degree of access to solvers; for example, you may not have access to all solvers
that are available in the Leap service. You can view your solver access and
usage for a project on the dashboard.

Users with :ref:`limited solver access <admin_def_solver_access_limit>` can
submit problems to the solvers in a project while their remaining solver-access
time\ [#]_ for that project is sufficient.

.. [#] For information about customer plans, see the
    `Leap Customer Plans <https://cloud.dwavesys.com/leap/plans>`_ page.

.. [#] A user's solver-access time for a project is renewed monthly, subject to
    the customer contract; the renewal date is displayed on the dashboard.

Your API Token
--------------

To submit a problem, an API token is required. Instead of a user name and
password, an API token is used to authenticate your client session when it
connects to the Leap service. A unique and secure API token is generated
for each of your projects, excluding those with the **Trial Plan** account
type,\ [#]_ and is available on the dashboard. If your API token is shared or
compromised in any way, you should reset it via the dashboard.

.. [#]  Projects with the **Trial Plan** account type do not include the use of
    API tokens required to submit arbitrary problems to solvers and thus users
    in those projects can only run some demos.

Ocean SDK Access
================

you can authorize Ocean software to access your account in the Leap service and
store your API token in your development environment; see the
:ref:`ocean_leap_authorization` section for details.

(For information on configuring Ocean software to access preferred solvers or
use one of multiple API tokens, see the :ref:`ocean_index_get_started` page.)

Problem Storage
===============

Up to 1000 of your most recent problems are stored and accessible in the Leap
service for up to 365 days; if the number of your problems exceeds 1000, the
Leap service begins to delete the oldest ones.