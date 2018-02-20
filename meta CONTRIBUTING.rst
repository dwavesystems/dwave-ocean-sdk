How to contribute
=================

This page discusses the code conventions and best practices used in the Application Development, Technologies, and Tools
team at D-Wave. This document is intended as a living document, and is not complete. Feedback is welcome.

The goal of this guide is to provide a common understanding within the group and between D-Wave software contributors.

Testing
-------

Your feature or bugfix is only complete when your code has been unittested. Part of the pull request process will be to
test your branch against master, and so the more tests you can provide, the easier the pull request process will become.

Submitting changes
------------------

Versioning scheme
~~~~~~~~~~~~~~~~~

Semantic versioning (`major.minor.patch <http://semver.org/>`_). A change that breaks backwards compatibility must
include a major version change.

Git
~~~

Commits
*******

TL;DR:

* Separate subject from body with a blank line
* Limit the subject line to 50 characters
* Capitalize the subject line
* Do not end the subject line with a period
* Use the imperative mood in the subject line
* Wrap the body at 72 characters
* Use the body to explain what and why vs. how

Sources:

* https://chris.beams.io/posts/git-commit/
* http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

Git-Flow
********

When contributing to a D-Wave project, fork the repository using the `Github fork
<https://guides.github.com/activities/forking/>`_ button and work in a feature branch in your own repository. In your
feature branch, commit and push often, you can always rebase locally to edit your commit history and make it readable.
To start a discussion, initiate a pull request. The sooner you start the pull request, the better. This will allow
everyone to communicate on your feature early and will save time and effort when you are ready to merge. If your branch
is long lived, remember to rebase off of master periodically. When you are ready to merge, notify the repository owner
and they will merge your code in.

If you're already familiar with git, but rebasing is still scary, try this `think like a git guide
<http://think-like-a-git.net/>`_.

In our ``dwavesystems`` repos, we keep only the master branch. This branch reflects the bleeding edge developments of
the project. Exceptionally, significant old versions that forked from the master branch will be kept in a version
branch. For example, we might keep version branches ``2.x`` and ``3.x`` while the ``master`` branch tracks the latest
``4.x`` version. We'll try to minimize the number of version branches we keep alive/maintain.

Stable releases are tracked using tags. These tagged snapshots are deployed to PyPI after successfully passing the test
cases during continuous integration.

Readme file
***********

If you are creating a repository, don't forget to include a :code:`README.rst` containing a reasonable description of
your project.

Coding Conventions
------------------

Documentation and comments
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Do a good job of commenting. Read this CodingHoror `article <https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/>`_.
* Comments should add, not repeat: avoid repeating in english or pseudo-code what the code does. Rather, discuss what the block is trying to achieve.
* Side effects should be visible on screen, if not in code, then in comments.
* Remember, **the best documentation is clean, simple code with good variable names**. When this is not possible, you must use a comment to explain the purpose of a functional block.

  e.g.:

  .. code-block:: python

    # z must not be greater than 255.
    if z > 255:
        raise RuntimeError('z must be <= 255!')

  would be much more informative as:

  .. code-block:: python

    # if z is greater than 255, this universe will collapse. See https://url.to.issue.tracker/IS-42
    if z > 255:
        raise RuntimeError('z must be <= 255!')

  or even better:

  .. code-block:: python

    # See https://url.to.issue.tracker/IS-42
    if z > 255:
        raise RuntimeError('z cannot be greater than 255, or this universe will collapse.')

General programming
~~~~~~~~~~~~~~~~~~~

* Variable naming should follow the well know conventions of a language and avoid uninformative or needlessly terse variable names.
* Code is read more often than written.
* Functions should do one thing.
* Early pull requests and code reviews.
* Early architecting/design. Code reviews can happen before any code has been written.
* Use a consistent character width with an upper bound of 120.
* Use 4 spaces instead of tabs.

Python specific
~~~~~~~~~~~~~~~

pep8
****
* As a baseline, follow the `pep8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide for python.

python2/3
*********

* All code should be both Python 2 and 3 compatible.


Documentation
*************

* Google docstrings convention (`definition <https://google.github.io/styleguide/pyguide.html>`_, `example <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_) on all public facing functions.
* Private functions should include some sort of docstring.
* If your module has more than one public unit, it should have a module docstring with a table of contents.
* The docstring for the :code:`__init__` method goes on class.
* All docstrings should be parsable by the `Sphinx <http://www.sphinx-doc.org/en/stable/#>`_ documentation generation tool (i.e. restructured text) The sphinx theme should be `readthedocs <https://docs.readthedocs.io/en/latest/>`_

C++ specific
~~~~~~~~~~~~

.clang-format
*************

* When starting a new C++ project, copy the .clang-format file included here.
* Our style is based on Google (as opposed to LLVM, Chromium, Mozilla, or Webkit) with minor differences.
* :code:`ColumnLimit` is set to :code:`120`, as specified in `General programming`_.
* :code:`NamespaceIndentation` is set to :code:`Inner` as a middle ground between :code:`None` (Google) and :code:`All`, such that every line in a file defining a namespace isn't indented, but nested namespaces are easily spotted.
* Various indent width specifiers are scaled by a factor of 2 such that the base indent is :code:`4`, as specified in `General programming`_, instead of :code:`2` (Google). This is especially helpful for readibility in cases like

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

Additional style
****************

* Favor the use of the optional braces for single-line control statements, for consistency and extensibility.

  e.g.,

  .. code-block:: c++

    if (a) {
        return;
    }

  as opposed to

  .. code-block:: c++

    if (a) return;

  This could potentially be enforced by :code:`clang-tidy`.
