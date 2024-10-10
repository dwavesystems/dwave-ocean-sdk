.. _concept_samplesets:

==========
Samplesets 
==========

:term:`sampler`\ s sample from low-energy states of a problem’s 
:term:`objective function`\ ---\ :term:`BQM` samplers sample from low-energy 
states in models such as those defined by an :term:`Ising` equation or a 
:term:`QUBO` problem---and return an iterable of samples, in order of increasing 
energy.

When a D‑Wave quantum computer solves a problem, it uses quantum phenomena such 
as superposition and tunneling to explore all possible solutions simultaneously 
and find a set of the best ones. At the end of the computation (anneal), a single 
solution is sampled from a set of good solutions, with some probability, and 
returned. Because the sampled solution is probabilistic, different solutions may 
be returned in different runs. The standard way of submitting a problem to the 
system requests many samples, not just one. This not only returns multiple 
“best” answers but also reduces the probability of settling on a suboptimal 
answer.

Some classical samplers might return non-probabilistic solutions; for example, 
the :doc:`dimod <oceandocs:docs_dimod/sdk_index>` :class:`~.ExactSolver` 
deterministically returns the best solution or solutions to small problems by 
calculating the result for every configuration of variable values. Such samplers 
are called solvers.

Some Ocean functions might return a single best solution; for example, some 
:doc:`dwave-networkx <oceandocs:docs_dnx/sdk_index>` graph algorithms return 
only the lowest-energy sample.

.. include:: ../ocean/docs_dimod/sdk_content.rst
  :start-after: start_samplesets
  :end-before: end_samplesets
