.. _opt_example_cqm_stockselling:

===========
Stock Sales
===========

This example finds a stock-selling strategy for a simplified market model to
demonstrate using a `Leap <https://cloud.dwavesys.com/leap/>`_ :term:`hybrid`
:term:`CQM` solver on a :term:`constrained <constraint>` problem with integer
and binary variables.

In this very simple market, you have some number of shares that you want to sell
in daily blocks over a defined interval of days. Each sale of shares affects the
market price of the stock,

.. math::

    p_i = p_{i-1} + \alpha s_{i-1},

where :math:`p_i` and :math:`s_i` are, respectively, the price and the number of
shares sold on day :math:`i`, and :math:`\alpha` is some multiplier.

The goal of this problem is to find the optimal number of shares to sell per day
to maximize revenue from the total sales.

The :ref:`opt_example_cqm_stockselling_tax` subsection adds a tax to the market
model to demonstrate the incorporation of binary variables into the CQM.

Example Requirements
====================

.. include:: ../shared/examples.rst
    :start-after: start_requirements
    :end-before: end_requirements

Solution Steps
==============

.. |workflow_section| replace:: :ref:`opt_workflow`

.. include:: ../shared/examples.rst
    :start-after: start_standard_steps
    :end-before: end_standard_steps

This example formulates this problem as a
:ref:`constrained quadratic model <concept_models_cqm>` and uses the
:class:`~dwave.system.samplers.LeapHybridCQMSampler` class to find good
solutions.

Formulate the Problem
=====================

First, define the market parameters.

*   :code:`max_days` is the period over which you should sell all your shares.
*   :code:`total_shares` is the number of shares you own (equal to
    :math:`\sum_i s_i`).
*   :code:`price_day_0` is the stock price on the first day of the period.
*   :code:`alpha` is a multiplier, :math:`\alpha`, that controls how much the
    stock price increases for each share sold into the market.

>>> max_days = 10
>>> total_shares = 100
>>> price_day_0 = 50
>>> alpha = 1

Instantiate a CQM.

>>> from dimod import ConstrainedQuadraticModel
>>> cqm = ConstrainedQuadraticModel()

You can now formulate an :term:`objective function` to optimize and constraints
any feasible solution must meet, and set these in your CQM.

Objective Function
------------------

The objective function to maximize is the revenue from selling shares. Because
you own an integer number of shares, it is convenient to use integer variables
to indicate the number of shares sold each day, :code:`shares`. For simplicity,
this model assumes stock prices, :code:`price`, are also integers\ [#]_.

.. [#]
    One could use integer variables to model stock prices in dollars and cents
    by multiplying the values by 100; however, this greatly increases the search
    space. One could also create a compromise model with somewhat greater
    resolution and search space by rounding to the nearest dime and multiplying
    prices by 10, for example.

Bounds on the range of values for integer variables shrink the solution space
the solver must search, so it is helpful to set such bounds; for many problems,
you can find bounds from your knowledge of the problem. In this case,

*   On any day, you cannot sell more than the total number of shares you start
    with.
*   The maximum share price is the sum of the initial price and the total price
    increase that would result from selling all your shares,

    .. math::

        \max(p) = p_0 + \alpha * \sum_i s_i.

>>> from dimod import Integer
>>> max_p = price_day_0 + alpha*total_shares
>>> shares = [Integer(f's_{i}', upper_bound=total_shares) for i in range(max_days)]
>>> price = [Integer(f'p_{i}', upper_bound=max_p) for i in range(max_days)]

Daily revenue is the number of shares sold multiplied by the price on each sales
day.

>>> revenue = [s*p for s, p in zip(shares, price)]

To maximize the total revenue, :math:`\sum_i s_ip_i`, is to minimize the
negative of that same revenue:

>>> cqm.set_objective(-sum(revenue))

.. note::

    As noted in the :ref:`example_cqm_binpacking` example, keep in mind that
    these "variables" are actually class :class:`dimod.QuadraticModel` objects,

    >>> price[0]
    QuadraticModel({'p_0': 1.0}, {}, 0.0, {'p_0': 'INTEGER'}, dtype='float64')

    with a single variable with the requested label, :code:`p_0` or :code:`s_0`.
    This means, for example, that multiplying these models to create a
    :code:`revenue[0]` "variable" actually creates a new quadratic model,

    >>> revenue[0]                               # doctest: +SKIP
    QuadraticModel({'s_0': 0.0, 'p_0': 0.0},
    ...            {('p_0', 's_0'): 1.0},
    ...            0.0,
    ...            {'s_0': 'INTEGER', 'p_0': 'INTEGER'}, dtype='float64')

    with a quadratic bias between :code:`p_0` and :code:`s_0`.

Constraints
-----------

The simplified market in this problem has the following constraints:

1.  In total you can sell only the number of shares you own, no more,
    :math:`\sum_i s_i \le` :code:`total_shares`.

>>> cqm.add_constraint(sum(shares) <= total_shares, label='Sell only shares you own')
'Sell only shares you own'

2.  On the first day of the selling period, the stock has a particular price
    :math:`p_0 =` :code:`price_day_0`.

>>> cqm.add_constraint(price[0] == price_day_0, label='Initial share price')
'Initial share price'

3.  The stock price increases in proportion to the number of shares sold the
    previous day:

    :math:`p_i = p_{i-1} + \alpha s_{i-1}`.

>>> for i in range(1, max_days):
...    pricing = cqm.add_constraint(price[i] - price[i-1] - alpha*shares[i-1] == 0, label=f'Sell at the price on day {i}')

For a sales period of ten days, this CQM has altogether 11 constraints:

>>> len(cqm.constraints)
11

Solve the Problem by Sampling
=============================

Instantiate a :class:`~dwave.system.samplers.LeapHybridCQMSampler` class
sampler,

>>> from dwave.system import LeapHybridCQMSampler
>>> sampler = LeapHybridCQMSampler()     # doctest: +SKIP

and submit the CQM to the selected\ [#]_ solver.

.. [#]
    You can see the selected solver using the
    :attr:`~dwave.cloud.solver.BaseSolver.name` property; for example,

    >>> sampler.solver.name                          # doctest: +SKIP
    'hybrid_constrained_quadratic_model_version1'

    and use :ref:`feature-based solver selection <index_cloud>` to select a
    particular solver.

For one particular execution, with a maximum allowed runtime of a minute, the
CQM hybrid solver returned 41 samples, out of which 24 were solutions that met
all the constraints:

>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=60,
...                                label="SDK Examples - Stock-Selling Strategy")  # doctest: +SKIP
>>> print("{} feasible solutions of {}.".format(
...       sampleset.record.is_feasible.sum(), len(sampleset)))   # doctest: +SKIP
24 feasible solutions of 41.

The small function below extracts from the returned sampleset the best feasible
solution and parses it.

>>> def parse_best(sampleset):
...    best = sampleset.filter(lambda row: row.is_feasible).first
...    s = [val for key, val in best.sample.items() if "s_" in key]
...    p = [val for key, val in best.sample.items() if "p_" in key]
...    r = [p*s for p, s in zip(p, s)]
...    return r, s, best

Parse and print the best feasible solution:

>>> r, s, _ = parse_best(sampleset)                # doctest: +SKIP
>>> print("Revenue of {} found for daily sales of: \n{}".format(sum(r), s))     # doctest: +SKIP
Revenue of 9499.0 found for daily sales of:
[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 9.0, 11.0]

.. _opt_example_cqm_stockselling_tax:

Market with Taxation
====================

The previous sections made use of only integer variables. Quadratic models also
accept binary variables. This section models a market in which you pay an
additional tax on early sales and uses a binary variable to incorporate that
update into the CQM created in the previous sections.

Consider a market in which you pay a tax in amount, :code:`tax_payment`, for
selling shares during the first :code:`taxed_period` days of the period in which
you can sell your shares.

>>> taxed_period = 3
>>> tax_payment = 225

Because you either pay this tax or do not pay it, you can use a binary variable,
:code:`t`, to indicate payment. You can update the previous objective by
reducing the revenue from share sales by the tax payment (adding it to the
negative revenue) if the :code:`t` binary variable is 1:

>>> from dimod import Binary
>>> t = Binary('t')
>>> cqm.set_objective(tax_payment*t - sum(revenue))

Binary variable :code:`t` should be True (1) if sales in the first
:code:`taxed_period` days of the period are greater than zero; otherwise it
should be False (0):

.. math::

    \sum_{i < \text{taxed_period}} s_i > 0 \longrightarrow t=1

    \sum_{i < \text{taxed_period}} s_i = 0 \longrightarrow t=0

One way to set such an indicator variable is to create a pair of linear
constraints:

.. math::

    \frac{\sum_{i < \text{taxed_period}} s_i}{\sum_i s_i}
    \le t \le \sum_{i < \text{taxed_period}} s_i

To show that this pair of inequalities indeed sets the desired binary indicator,
the table below shows, **bolded**, the binary values :math:`t` must take to
simultaneously meet both inequalities for
:math:`\sum_{i < \text{taxed_period}} s_i` with sample values 0, 1, and 5 for
the previous configured :code:`total_shares = 100`.

.. list-table:: Binary Indicator Variable :math:`t` for :math:`\sum_i s_i = 100`
    :widths: auto
    :header-rows: 1

    *   - :math:`\frac{\sum_{i < \text{taxed_period}} s_i}{\sum_i s_i}`
        - :math:`\sum_{i < \text{taxed_period}} s_i`
        - :math:`\pmb{t}`
        - :math:`\frac{\sum_{i < \text{taxed_period}} s_i}{\sum_i s_i}
          \le \pmb{t} \le \sum_{i < \text{taxed_period}} s_i`
    *   - 0
        - 0
        - :math:`\pmb{0}`
        - :math:`0 = \pmb{0} = 0`
    *   - :math:`\frac{1}{100}`
        - 1
        - :math:`\pmb{1}`
        - :math:`\frac{1}{100} < \pmb{1} = 1`
    *   - :math:`\frac{5}{100}`
        - 5
        - :math:`\pmb{1}`
        - :math:`\frac{5}{100} < \pmb{1} < 5`

Add these two constraints to the previously created CQM:

>>> cqm.add_constraint(t - sum(shares[:taxed_period]) <= 0, label="Tax part 1")
'Tax part 1'
>>> cqm.add_constraint(1/total_shares*sum(shares[:taxed_period]) - t <= 0, label="Tax part 2")
'Tax part 2'

Submit the CQM to the selected solver. For one particular execution,
with a maximum allowed runtime of a minute, the CQM hybrid sampler
returned 50 samples, out of which 33 were solutions that met all the
constraints:

>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=60,
...                                label="SDK Examples - Stock-Selling Strategy")  # doctest: +SKIP
>>> print("{} feasible solutions of {}.".format(
...       sampleset.record.is_feasible.sum(), len(sampleset)))   # doctest: +SKIP
33 feasible solutions of 50.

Parse and print the best feasible solution:

>>> r, s, best = parse_best(sampleset)                  # doctest: +SKIP
>>> income = sum(r) - best.sample['t']*tax_payment      # doctest: +SKIP
>>> print("Post-tax income of {} found for daily sales of: \n{}".format(income, s))     # doctest: +SKIP
Post-tax income of 9283.0 found for daily sales of:
[0.0, 0.0, 0.0, 13.0, 14.0, 14.0, 14.0, 16.0, 15.0, 14.0]

Notice that the existence of this tax, though avoided in the sales strategy
found above, has reduced your income by a little less than the tax fee (the
maximum income if you had paid the tax would be 9275). If the tax is slightly
reduced, it is more profitable to sell during the taxation period and pay the
tax:

>>> tax_payment = 220
>>> cqm.set_objective(tax_payment*t - sum(revenue))
>>> sampleset = sampler.sample_cqm(cqm,
...                                time_limit=60,
...                                label="SDK Examples - Stock-Selling Strategy")  # doctest: +SKIP
>>> r, s, best = parse_best(sampleset)                        # doctest: +SKIP
>>> income = sum(r) - best.sample['t']*tax_payment            # doctest: +SKIP
>>> print("Post-tax income of {} found for daily sales of: \n{}".format(income, s))     # doctest: +SKIP
Post-tax income of 9276.0 found for daily sales of:
[10.0, 10.0, 10.0, 11.0, 9.0, 10.0, 12.0, 9.0, 10.0, 9.0]
