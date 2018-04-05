=================
How to Contribute
=================

The goal of this document is to establish a common understanding among software contributors to D-Wave's Ocean software
projects based on the code conventions and best practices used at D-Wave.

This document is intended to be a living document, and is not complete. Feedback is welcome.

Testing
=======

A feature or bugfix is complete only when the code has been unit-tested. Part of the pull-request process is to test
your branch against `master`, and so the more tests you provide, the easier the pull-request process.

Submitting Changes
==================

When contributing to a D-Wave project, fork the repository using the `Github fork
<https://guides.github.com/activities/forking/>`_ button and work in a feature branch in your own repository. In your
feature branch, commit and push often, you can always rebase locally to edit your commit history and make it readable.
To start a discussion, initiate a pull request. The sooner you start the pull request, the better. This allows early
discussion on your feature and saves time and effort when you are ready to merge. When you are ready to merge, notify
the repository owner and they will merge your code in.

Follow the commit conventions described here:

* https://chris.beams.io/posts/git-commit/
* http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

TL;DR:

* Separate subject from body with a blank line
* Limit the subject line to 50 characters
* Capitalize the subject line
* Do not end the subject line with a period
* Use the imperative mood in the subject line
* Wrap the body at 72 characters
* Use the body to explain what and why vs. how

If your branch is long-lived, rebase off of `master` periodically.

If you're already familiar with Git, but rebasing is still scary, try this `think like a Git guide
<http://think-like-a-git.net/>`_.

The master branch in a `dwavesystems` repository reflects the bleeding-edge developments of the project. Significant old
versions forked from `master` are kept in version branches. For example, we might keep version branches `2.x` and `3.x`
while `master` tracks the latest `4.x` version. We try to minimize the number of version branches kept alive/maintained.

Stable releases are tracked using tags. These tagged snapshots are deployed to PyPI after successfully passing the test
cases during continuous integration.

Coding Conventions
==================

* Variable naming should follow the well-known conventions of a language. Avoid uninformative or needlessly terse
  variable names.
* Code is read more often than written.
* Functions should do one thing.
* Early pull requests and code reviews.
* Early architecting/design. Code reviews can happen before any code has been written.
* Use a consistent character width of 120.
* Use 4 spaces instead of tabs.
* End all files with a newline.

Documentation and Comments
--------------------------

* Do a good job of commenting. Read this `Coding Horror article
  <https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/>`_.
* Comments should add, not repeat: avoid repeating in English or pseudo-code what the code does. Rather, discuss what
  the block is trying to achieve.
* Side effects should be visible on screen; if not in code, then in comments.
* Remember, **the best documentation is clean, simple code with good variable names**. When this is not possible, you
  must use a comment to explain the purpose of a functional block.

  Example:

  The following code

  .. code-block:: python

    # z must not be greater than 255.
    if z > 255:
        raise RuntimeError('z must be <= 255!')

  would be much more informative as

  .. code-block:: python

    # if z is greater than 255, this universe will collapse. See https://url.to.issue.tracker/IS-42
    if z > 255:
        raise RuntimeError('z must be <= 255!')

  or even better:

  .. code-block:: python

    # See https://url.to.issue.tracker/IS-42
    if z > 255:
        raise RuntimeError('z cannot be greater than 255, or this universe will collapse.')

Python
------

pep8
~~~~

As a baseline, follow the `pep8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide for python.

Python 2/3
~~~~~~~~~~

All code should be both Python 2 and 3 compatible.


Documentation
~~~~~~~~~~~~~

* Google docstrings convention (`definition <https://google.github.io/styleguide/pyguide.html>`_, `example
  <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_) on all public-facing functions. The
  following are exceptions:

  * For D-Wave extensions of third-party projects, we match the existing convention (e.g. the `D-Wave NetworkX
    <https://github.com/dwavesystems/dwave_networkx>`_ project follows `NumPy <http://scipy.org>`_ conventions).
  * Argument defaults are written "default=x" rather than "default x".

* Private functions should include some sort of docstring.
* If your module has more than one public unit, it should have a module docstring with a table of contents.
* The docstring for the :code:`__init__` method goes on the class.
* All docstrings should be parsable by the `Sphinx <http://www.sphinx-doc.org/en/stable/#>`_ documentation generation
  tool (i.e. reStructuredText) The sphinx theme should be `readthedocs <https://docs.readthedocs.io/en/latest/>`_.

C++
---

.clang-format
~~~~~~~~~~~~~

* When starting a new C++ project, copy the .clang-format file included here.
* Our style is based on Google (as opposed to LLVM, Chromium, Mozilla, or Webkit) with minor differences.
* :code:`ColumnLimit` is set to :code:`120`, as specified in `Coding Conventions`_.
* :code:`NamespaceIndentation` is set to :code:`Inner` as a middle ground between :code:`None` (Google) and :code:`All`,
  such that every line in a file defining a namespace isn't indented, but nested namespaces are easily spotted.
* Various indent-width specifiers are scaled by a factor of 2 such that the base indent is :code:`4`, as specified in
  `Coding Conventions`_, instead of :code:`2` (Google). This is especially helpful for readibility in cases like

  .. code-block:: c++

    if (condition) {
        foo();
    } else {
        bar();
    }

  as opposed to

  .. code-block:: c++

    if (condition) {
      foo();
    } else {
      bar();
    }

Additional Style
~~~~~~~~~~~~~~~~

Favor the use of the optional braces for single-line control statements, which enhance consistency and extensibility.

Example:

Use the following format

.. code-block:: c++

  if (a) {
      return;
  }

as opposed to

.. code-block:: c++

  if (a) return;

This could potentially be enforced by :code:`clang-tidy`.

Versioning Scheme
-----------------

Our code follows `Semantic Versioning <http://semver.org/>`_ conventions: major.minor.patch.

A change that breaks backwards compatibility must increment the major version. Anything below version 1.0.0 can break
backwards compatibility.

Readme File
-----------

If you are creating a repository, don't forget to include a :code:`README.rst` containing
a reasonable description of your project.
