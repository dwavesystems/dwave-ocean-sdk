.. _nl_model_sdk:

================
Nonlinear Models
================

The nonlinear model represents a general optimization problem with an 
:term:`objective function` and/or constraints over variables of various 
types.

This model is especially suited for use with decision variables that represent 
a common logic, such as subsets of choices or permutations of ordering. For 
example, in a 
`traveling salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_ 
permutations of the variables representing cities can signify the order of the 
route being optimized and in a 
`knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_ the 
variables representing items can be divided into subsets of packed and not 
packed. 

The :class:`~dwave.optimization.model.Model` class encodes this model and 
its methods provide convenient utilities for constructing such models.


