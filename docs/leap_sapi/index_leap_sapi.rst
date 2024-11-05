.. _index_leap_sapi:

============
Leap Service
============

.. toctree::
  :hidden:
  :maxdepth: 1

  leap_index_rns
  leap_dev_env
  doc_admin
  doc_rest_api

The |cloud_tm| quantum cloud service from 
`D-Wave Quantum Inc. <https://dwavesys.com>`_, launched in 2018, provides 
real-time access to quantum computing.

.. sections-start-marker

.. grid:: 3
    :gutter: 2

    .. grid-item-card:: :ref:`leap_index_rns` 
         
        System release notes, fixed and open issues. 

    .. grid-item-card:: :ref:`leap_dev_env` 
         
        Description of Leap support for third-party IDEs. 

    .. grid-item-card:: |doc_leap_admin|_ 
         
        Description of how project administrators manage access
        to projects in Leap.

    .. grid-item-card:: |doc_rest_api|_ 
         
        Reference documentation for the :term:`Solver API <SAPI>` (SAPI) 
        REST interface.

.. sections-end-marker


.. figure:: ../../_images/network-leap-simple.png
  :alt: network diagram showing a laptop connecting to a |dwave_short| quantum computer through the cloud.
  :scale: 50 %

You use Leap to do the following:

* Submit problems to |dwave_short_tm| quantum computers,
  including `hybrid solvers <https://docs.dwavesys.com/docs/latest/doc_leap_hybrid.html>`_,
  which use a combination of classical and quantum
  resources and can accept extremely large problems.

* Get started quickly and write your quantum applications
  using an integrated development environment (IDE)
  that is compliant with the 
  `Development Containers specification <https://containers.dev/supporting>`_,
  for example, cloud-based 
  `GitHub Codespaces <https://docs.github.com/codespaces>`_.

* Run demos and interactive coding examples
  in `Resources <https://cloud.dwavesys.com/leap/resources/demos/>`_.

* Get involved in
  `our community of like-minded users <https://support.dwavesys.com/hc/en-us/community/topics>`_.

* `Administer projects <https://cloud.dwavesys.com/leap/admin>`_,
  including managing solvers and users together
  and setting access to solvers for those users.

Sign up for Leap here: https://cloud.dwavesys.com/leap.

Leap Dashboard
--------------

The Leap dashboard is the home for your Leap experience and contains
a considerable amount of useful information. For example,
you can manage your account settings and
see the status of problems you have submitted, usage statistics,
solver status, a summary of your account, and your active project
and its associated API token.

You might be a member of multiple projects, but the information displayed
on the dashboard is only for the active project; for example, the solvers
that have been assigned to the active project.

Leap supports solvers in multiple regions (for example, North America
and Europe). The dashboard displays the solvers that are available by region.

.. note::

   * If you have a Trial or Developer Plan, you have only one project.

   * You can make a different project active by selecting
     *your_user_name* > **Projects** > *project*.

Solvers
-------

You submit problems to solvers.
Solvers are either quantum processing units (QPUs), classical,\ [#]_ or hybrid;
hybrid solvers use a combination of quantum and classical resources.

.. [#] Classical solvers can be used to test your code during development.

Problem Submission and API Tokens
---------------------------------

To submit a problem, an API token is required.
Instead of a user name and password, an API token is used to authenticate
your client session when it connects to Leap.
A unique and secure API token is generated for each of your projects
and is available on the Leap dashboard.

To learn about authorizing the Ocean software access to your Leap account 
and enabling it to store your API token in your development environment, 
see :ref:`doc_leap_dev_env`.

If your API token is shared or compromised in any way,
you should reset it via the Leap dashboard.

Customer Plans and Access to Solvers  
------------------------------------

Your customer plan and :ref:`seat type <seat_type>` in a project, 
together with your customer contract (where applicable),
determine your degree of access to solvers. 
You can view your solver access and usage for a project
on the dashboard. 

Users with :ref:`limited solver access <solver_access_limit>` 
can submit problems to the solvers in a project 
while their remaining solver-access time\ [#]_\ [#]_
for that project is sufficient.

.. [#] A user's solver-access time for a project is renewed monthly;
       the renewal date is displayed on the dashboard.

.. [#] Solver access for a Trial Plan expires on the date displayed 
       in the **Access Expiry** field; for upgrade options, 
       click **Expand Your Access**.

.. _leap_support_for_dev_env:

Support for IDEs
----------------

|dwave_short| Leap supports third-party integrated development environments (IDEs)
that are compliant with the Development Containers specification.
Examples of popular, compliant IDEs are cloud-based GitHub Codespaces
and locally installed VS Code.

For more information, see :ref:`doc_leap_dev_env`.

Leap Administration
-------------------

Leap Admin is an easy-to-use cloud-based administration tool.\ [#]_ You use
Leap Admin to invite users and manage their access to projects
in the Leap quantum cloud service, view the status of problems
submitted to solvers, troubleshoot submission issues,
and generate solver usage reports.

For more information, see the |doc_leap_admin|_.

..  [#] To administer projects, you must be a project administrator.

Leap Community, Resources, and Help
-----------------------------------

Leap has many learning resources available as follows:

* `Community <https://support.dwavesys.com/>`_

  A community space where you can pose questions and provide answers
  to other users of the service.

* `Resources <https://cloud.dwavesys.com/leap/resources/demos/>`_

  Includes Leap demos and a searchable collection of examples
  and Jupyter notebooks.

* `Help <https://support.dwavesys.com/>`_

  Includes a frequently asked questions (FAQ) section and a knowledge base.
