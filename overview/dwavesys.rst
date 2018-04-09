.. _dwavesysk:

=======================
Using the D-Wave System
=======================

You access D-Wave :term:`solver` resources through the D-Wave Sampler API (SAPI).

Interacting with SAPI
---------------------

SAPI is an application layer built to provide resource discovery, permissions, and scheduling for
quantum annealing resources at D-Wave Systems. The requisite information for problem
submission through SAPI includes:

1. URL to the D-Wave system

   You need to specify a :term:`solver` when submitting a problem to the system.

2. API Token

   To submit a problem to the D-Wave system, you require an API token, which the system
   uses to authenticate the client session when connecting to the remote environment.
   Because we use tokens for authentication, user names and passwords are not required in code.

3. URL to the D-Wave system

   Obtain the URL you need to make a remote connection to the D-Wave system.

You can find all the above on the <<<web page>>>.

SAPI Communications Tool
------------------------

The `D-Wave Cloud Client <http://dwave-cloud-client.readthedocs.io/en/latest/index.html>`_
is a tool for communicating with SAPI.
