dwavesystems/docs

This repo is the source of the D-Wave open-source tools documentation located at http://dw-docs.readthedocs.io/en/latest/

Making a simple change
===============================
If you spot something in the docs that needs to be fixed, the fastest way to get the change in is to edit 
the file on the GitHub web site. 

To do this, click on the [edit on GitHub] link at the top of the page you want to edit. The link takes you 
to that topic's GitHub page. In GitHub, click the pencil icon and make your changes. You can preview how 
they'll look right on the page (use the "Preview Changes" tab).

When you are finished editing, click "Propose file change" at the bottom of the page and confirm your 
pull request (PR). The system will do some checks and add a comment to your PR with the results.

The D-Wave team can normally merge pull requests within a couple of days. We will fix build errors before we merge, 
so you don't have to worry about passing all of the checks, but merge issues might add an extra few days. The important 
part is submitting your change.

Making more extensive changes
===============================
If your change involves edits to multiple topics, or if you contribute frequently, consider forking this repo 
in GitHub, cloning it on your workstation, and making pull requests from commits you push to your forked repo. After 
you fork, clone the forked repo to your workstation.

Contributing this way requires some set-up, but once this is done, you can contribute frequently from your own GitHub repo. 

Our docs have the following dependencies:
- Sphinx version 1.6.2 
- Python version 3

After making your changes but before submitting a PR, run the shell command *make* at the root of your local 
repo to check for errors and build a local version of the doc set in HTML for testing. Before running make for 
the first time, install Sphinx, the documentation generator, possibly using sudo:

  pip install -r requirements.txt

Note: The default target directory is *docs*. This is the target that creates the appropriate build directory on 
your local machine and references in the source files of your local repo.

The docs build in a minute or two. To view the local version you built, either:
- Open the build/<filename> file in your browser. 
- Use a local web server like the SimpleHTTPServer Python module. 

Viewing your content using the SimpleHTTPServer module allows you to navigate through the documentation 
as if you were browsing it on http://dw-docs.readthedocs.io. To use the SimpleHTTPServer module:

1. Navigate to the build directory.
2. Run python -m SimpleHTTPServer. After the server starts up, connect to your docs through your loopback IP address (http://127.0.0.1:8000).


Sending feedback
============================
We love getting feedback. You can use:

- Email --- Send an email to docs@dwavesys.com for documentation bugs, ideas, thoughts, and suggestions. Be aware that this email address is not a support email address, however. If you need support, contact D-Wave support at dwsupport@dwavesys.com.
- Pull request --- Submit a PR to this repo using either of the two methods described above.



License
=============
Creative Commons Attribution 3.0 Unported License

