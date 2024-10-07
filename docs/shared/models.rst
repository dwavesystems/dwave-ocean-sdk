
.. start_models_intro

To express your problem as an objective function and submit to a |dwave_short| 
sampler for solution, you typically use one of the quadratic models\ [#]_ or 
nonlinear model\ [#]_ provided by :std:doc:`Ocean software <oceandocs:index>`:

*   :ref:`concept_models_bqm` are unconstrained\ [#]_ and have binary variables.

    BQMs are typically used for applications that optimize over decisions that could
    either be true (or yes) or false (no); for example, should an antenna transmit,
    or did a network node experience failure?

*   :ref:`concept_models_cqm` can be constrained and have binary, integer and real variables.

    CQMs are typically used for applications that optimize problems that might
    include real, integer and/or binary variables and one or more constraints.

*   :ref:`concept_models_dqm` are unconstrained and have discrete variables.

    DQMs are typically used for applications that optimize over several distinct
    options; for example, which shift should employee X work, or should the state
    on a map be colored red, blue, green or yellow?

*   :ref:`concept_models_nonlinear` can be constrained and have binary and integer variables.

    This model is especially suited for use with decision variables that represent 
    a common logic, such as subsets of choices or permutations of ordering. For 
    example, in a 
    `traveling salesperson problem <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_, 
    permutations of the variables representing cities can signify the order of the 
    route being optimized, and in a 
    `knapsack problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_, the 
    variables representing items can be divided into subsets of packed and not 
    packed. 

.. [#]
    Quadratic functions have one or two variables per term. A simple example of a

    quadratic function is,

    .. math::


        D = Ax + By + Cxy


    where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable
    terms---:math:`Ax` and :math:`By` here---are linear with the constant biasing

    the term's variable. Two-variable terms---:math:`Cxy` here---are quadratic with
    a relationship between the variables.


    Ocean also provides support for
    :ref:`higher order models <oceandocs:higher_order>`, which are typically

    reduced to quadratic for sampling.

.. [#]

    The nonlinear model represents a general optimization problem with an 
    :term:`objective function` and/or constraints over variables of various 

    types.

.. [#]

    Constraints for such models are typically represented by adding
    :ref:`penalty models <sysdocs:cb_techniques>` to the objective, as shown
    in the :ref:`getting_started_formulation_constraints` section.
    
.. end_models_intro
