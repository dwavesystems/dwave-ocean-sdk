.. start_general_steps

To map a problem to a quadratic or nonlinear model, you can try the following
steps.

1.  Write out the objective and constraints.

    This should be written out in terms of your problem domain, not necessarily
    in math format.

    -   The *objective* of a problem is what you are looking to
        minimize\ [#]_.
    -   A *constraint* in a problem is a rule that you must follow; an
        answer that does not satisfy a given constraint is called *infeasible*,
        it's not a good answer, and might not be usable at all. For example, a
        travelling salesperson cannot be in two cities at once or the trucks in
        your problem may not be able to hold more than 100 widgets.

    There may be more than one way to interpret your problem in terms of
    objectives and constraints.

2.  Convert objective and constraints into math expressions.

    Decide on the type of variables to best formulate it:

    *   **Binary**

        Does your application optimize over decisions that could either be true
        (or yes) or false (no)? For example,

        -   Should the antenna transmit or no?
        -   Did a network node experience failure?

    *   **Discrete**

        Does your application optimize over several distinct options? For
        example,

        -   Which shift should employee X work?
        -   Should the state be colored red, blue, green or yellow?

    *   **Integer**

        Does your application optimize the number of something? For example,

        -   How many widgets should be loaded onto the truck?

    *   **Continuous**

        Does your application optimize over an uncountable set? For example,

        -   Where should the sensor be built?

    Once you think of a problem in these terms, you can assign a variable for
    each question.

    Next ask about the degree the problem can likely be formulated as:

    *   **Quadratic**

        Are its relationships defined pairwise? For example,

        -   In the
            `structural imbalance example <https://github.com/dwave-examples/structural-imbalance-notebook>`_
            each pair of people in the network is either friendly or hostile.

    *   **Higher-Order**

        Does your application have relationships between multiple variables at
        once? For example,

        -   Simulating an AND gate

    Next, transform objective and constraints into math expressions. For binary
    variables, this can often be done with truth tables if you can break the
    problem down into two- or three-variable relationships. For other variables
    and non-quadratic degrees, you can try techniques such as
    :ref:`qpu_reformulating_higher_degree` and Ocean tools such as
    :ref:`higher order models <dimod_higher_order_models>`.

3.  Reformulate as a model.

    Different types of expressions require different strategies. Expressions
    derived from truth tables may not need any adjustments. The
    :ref:`qpu_reformulating` section provides a variety of reformulation
    techniques; some common reformulations are:

    *   **Squared terms:** QUBO and Ising models do not have squared binary
        variables. In QUBO format, its 0 and 1 values remain unchanged when
        squared, so you can replace any term :math:`x_i^2` with :math:`x_i`. In
        Ising format, its -1 and +1 values always equal 1 when squared, so you
        can replace any term :math:`s_i^2` with the constant 1.

    *   **Maximization to minimization:** if your objective function is a
        maximization function (for example, maximizing profit), you can convert
        this to a minimization by multiplying the entire expression by -1. For
        example:

        .. math::
            \mbox{arg max} (3v_1+2v_1v_2) = \mbox{arg min} (-3v_1-2v_1v_2)

    *   **Equality to minimization:** if you have a constraint that is an
        equality, you can convert it to a minimization expression by moving all
        arguments and constants to one side of the equality and squaring the
        non-zero side of the equation. This leaves an expression that is
        satisfied at its smallest value (0) and unsatisfied at any larger value
        (>0). For example, the equation :math:`x+1=2` can be converted to
        :math:`\min_x[2-(x+1)]^2`, which has a minimum value of zero for the
        solution of the equation, :math:`x=1`.

        This approach is useful also for :math:`n \choose k` constraints
        (selection of exactly :math:`k` of :math:`n` variables), where you
        disfavor selections of greater or fewer than :math:`k` variables with
        the penalty :math:`P = \alpha (\sum_{i=1}^n x_i - k)^2`, where
        :math:`\alpha` is a weighting coefficient (see the
        :ref:`concept_penalty` section) used to set the penalty's strength.

4.  Combine expressions.\ [#]_

    Once you have written all of the components (objective and constraints) as
    models, for example BQMs, make a final model by adding all of the
    components. Typically you multiply each expression by a constant that
    weights the different constraints against each other to best reflect the
    requirements of your problem. You may need to tune these multipliers through
    experimentation to achieve good results. You can see examples in Ocean
    software's
    `collection of code examples <https://github.com/dwave-examples>`_ on
    GitHub.

.. [#]
    For maximization see step 3.
.. [#]
    When using penalty models for constraints.

.. end_general_steps
