.. _oceanstack:

====================
Ocean Software Stack
====================

The Ocean software stack provides a chain of tools that implements the computations needed
to transform an arbitrarily posed problem to a form solvable on a quantum solver.

Abstraction Layers
------------------

.. _fig_stack:

.. figure:: ../_static/stack.PNG
  :name: stack
  :scale: 70 %
  :alt: Overview of the software stack.

  Ocean Software Stack

As shown in :ref:`fig_stack`, it is helpful to think of the Ocean tools and the context
in which they operate as being divided into in the following layers of functionality:

* Compute Resources

  The hardware on which the problem is solved. This might be a D-Wave quantum processor but
  it can also be the CPU of your laptop computer.
* Samplers

  Abstraction layer of the :term:`sampler` functionality. Ocean tools implement several D-Wave samplers and
  classical sampler. You can use the Ocean tools to customize a D-Wave sampler, create your own
  sampler, or use existing (classical) samplers.
* Sampler API

  Abstraction layer that represents the problem in a form that can access the selected ; for example,
  a `dimod <http://dimod.readthedocs.io/en/latest/>`_ (`repo <https://github.com/dwavesystems/dimod>`_)
  sampler method such as Ising that provides an Ising problem for solution.
* Methods

  Tools that pose a problem in binary quadratic model (BQM) form; for example
  `dwave_networkx <http://dwave-networkx.readthedocs.io/en/latest/index.html>`_ (`repo <https://github.com/dwavesystems/dwave_networkx>`_\ ) for graph-related problems.
* Application

  Original problem context; for example, factoring as a problem of finding two integers
  that factor a third integer.

Problem-to-Solution Tool Chain
------------------------------

A problem can be posed in a variety of formulations; the D-Wave system solves Ising problems.
The Ocean tools assist you in converting the problem from its original form to a
form native to the D-Wave system and sending the compatible problem for solving.
