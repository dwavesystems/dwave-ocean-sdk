.. _example_cqm_stock_selling:

===========================================
Stock-Sales Strategy in a Simplified Market
===========================================

This example finds a stock-selling strategy for a simplified market model to
demonstrate using Leap's hybrid :term:`CQM` solver on a constrained problem 
with integer variables.

In this very simple market, you have some number of shares that you want to 
sell in daily parts over a particular interval. Each sale of shares increases
the price of the stock, :math:`p_i = p_{i-1} + \alpha s_{i-1}`, where 
:math:`p_i` and :math:`s_i` are, respectively, the price and the number of 
shares sold on day :math:`i`, and :math:`\alpha` is some multiplier. 
You want to find the optimal number of shares to sell every day over the interval
to maximize your revenue from the total sales.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described
  in :ref:`sapi_access`.
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>` and 
  :doc:`dimod </docs_dimod/sdk_index>`.
* :std:doc:`NumPy <numpy:index>` for some mathematical calculations.

.. example-requirements-start-marker

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
and ran :code:`dwave setup`, your installation should meet these requirements.
In D-Wave's `Leap <https://cloud.dwavesys.com/leap/>`_ IDE, the default workspace
meets these requirements.

.. example-requirements-end-marker

Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems on 
the quantum computer in two steps: (1) Formulate the problem as a 
:term:`quadratic model` (QM) and (2) Solve the QM with a D-Wave solver. This
example formulates this problem as a :ref:`constrained quadratic model <cqm_sdk>` 
and uses the :class:`~dwave.system.samplers.LeapHybridCQMSampler` to find good 
solutions.

Formulate the Problem
=====================

First set some values for the simple market used in this model: 

* :code:`max_days` is the period over which you should sell all your shares
* :code:`total_shares` is the number of shares you own
* :code:`price_day_1` is the stock price on the first day of the period
* :code:`alpha` is a multiplier that controls how much the stock price increases
  for each share sold into the market. 
 
>>> max_days = 10
>>> total_shares = 100
>>> price_day_1 = 50
>>> alpha = 1

Instantiate a CQM: 

>>> from dimod import ConstrainedQuadraticModel, Binary
>>> cqm = ConstrainedQuadraticModel()

You can now formulate an :term:`objective function` to optimize and constraints
any feasible solution must meet, and set these in your CQM.


Objective Function
------------------

The objective function to maximize is the revenue from selling shares. Because
you own an integer number of shares, it is convenient to use integer variables
to indicate the number of shares sold each day, :code:`shares`. For simplicity,
stock prices too are integers in this model, :code:`price`. 

Bounds on the range of values for integer variables reduces the solution space 
the solver to search, so it is helpful to set such bounds; for many problems, 
you can find bounds from your knowledge of the problem. In this case, you can 
never sell more than the total number of shares you have and the maximum share 
price is the sum of the initial price and the maximum price increase, 
:math:`\text{price_day_1} + \alpha * \text{total_shares}`.      

>>> shares = [Integer(f's_{i}', upper_bound=total_shares) for i in range(max_days)]
>>> price = [Integer(f'p_{i}', upper_bound=price_day_1 + alpha*total_shares) for i in range(max_days)]

Daily revenue is the number of shares sold multiplied by the price on each sales
day.

>>> revenue = [s*p for s, p in zip(shares, price)]

To maximize the total revenue, :math:`\sum_i s_ip_i`, is to minimize the negative
of that same revenue:  

>>> cqm.set_objective(-sum(revenue))

Constraints
-----------

The simplified market in this problem has the following constraints:

1. In total you can sell only the number of shares you own, no more, 
   :math:`\sum_i s_i = \text{total_shares}`. 

>>> cqm.add_constraint(sum(shares) <= total_shares, label='Sell only shares you own')

2. Each day you can sell zero or more shares, :math:`s_i >= 0`.

>>> for i in range(max_days):
...    positive_shares = cqm.add_constraint(shares[i] >= 0, label=f'Sell positive numbers of shares {i}')

3. On the first day of the selling period, the stock has a particular price
   :math:`p_0 = \text{price_day_1}`.

>>> pricing_day0 = cqm.add_constraint(price[0] == price_day_1, label='Initial share price')

4. The stock price increases in proprtion to the number of shares sold the 
   previous day:

   :math:`p_i = p_{i-1} + \alpha s_{i-1} \Longrightarrow p_i - p_{i-1} - s_{i-1} = 0` 
   for :math:`\alpha=1`.

>>> for i in range(1, max_days):
...    pricing = cqm.add_constraint(price[i] - price[i-1] - shares[i-1] == 0, label=f'Sell at the price on day {i}')

For a sales period of ten days, this CQM has altogether 21 constraints: 

>>> len(cqm.constraints)
21

Solve the Problem by Sampling
=============================

D-Wave's quantum cloud service provides cloud-based hybrid solvers you can
submit arbitrary QMs to. These solvers, which implement state-of-the-art 
classical algorithms together with intelligent allocation of the quantum 
processing unit (QPU) to parts of the problem where it benefits most, are 
designed to accommodate even very large problems. Leap's solvers can 
relieve you of the burden of any current and future development and optimization
of hybrid algorithms that best solve your problem.

Ocean software's :doc:`dwave-system </docs_system/sdk_index>`
:class:`~dwave.system.samplers.LeapCQMHybridSampler` class enables you to 
easily incorporate Leap's hybrid CQM solvers into your application:

>>> from dwave.system import LeapHybridCQMSampler
>>> sampler = LeapHybridCQMSampler()     # doctest: +SKIP

Submit the CQM to the selected solver. For one particular execution, 
with a maximum allowed runtime of 3 minutes, the CQM hybrid sampler 
returned 47 samples, out of which 31 were solutions that met all the 
constraints: 

>>> sampleset = sampler.sample_cqm(cqm, time_limit=180)  # doctest: +SKIP
>>> print("{} feasible solutions of {}.".format(
...       sampleset.record.is_feasible.sum(), len(sampleset)))   # doctest: +SKIP
31 feasible solutions of 47.

Parse the best feasible solution:

>>> import itertools
>>> best = next(itertools.filterfalse(lambda d: not getattr(d,'is_feasible'),
...             list(sampleset.data())))
>>> s = [val for key, val in best.sample.items() if "s_" in key]
>>> p = [val for key, val in best.sample.items() if "p_" in key]
>>> r = [p*s for p, s in zip(p, s)]
>>> print("Revenue of {} found for selling {} daily.".format(sum(r), s))     # doctest: +SKIP
Revenue of 9496.0 found for selling [9.0, 10.0, 9.0, 10.0, 9.0, 11.0, 11.0, 11.0, 11.0, 9.0] daily.

