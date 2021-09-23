.. _example_cqm_stock_selling:

===========================================
Stock-Sales Strategy in a Simplified Market
===========================================

This example finds a stock-selling strategy for a simplified market model to
demonstrate using Leap's hybrid :term:`CQM` solver on a constrained problem 
with integer variables.

In this very simple market, you have some number of shares that you want to 
sell in daily parcels over a particular interval of days. Each sale of shares 
increases the price of the stock, 

.. math::

	p_i = p_{i-1} + \alpha s_{i-1}, 

where :math:`p_i` and :math:`s_i` are, respectively, the price and the number of 
shares sold on day :math:`i`, and :math:`\alpha` is some multiplier. 

The goal of this problem is to find the optimal number of shares to sell every 
day to maximize revenue from the total sales.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described
  in :ref:`sapi_access`.
* Ocean tools :doc:`dwave-system </docs_system/sdk_index>` and 
  :doc:`dimod </docs_dimod/sdk_index>`.

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

First define the simple market used in this model: 

* :code:`max_days` is the period over which you should sell all your shares.
* :code:`total_shares` is the number of shares you own (equal to :math:`\sum_i s_i`).
* :code:`price_day_0` is the stock price on the first day of the period.
* :code:`alpha` is a multiplier, :math:`\alpha`, that controls how much the stock 
  price increases for each share sold into the market. 
 
>>> max_days = 10
>>> total_shares = 100
>>> price_day_0 = 50
>>> alpha = 1

Instantiate a CQM: 

>>> from dimod import ConstrainedQuadraticModel
>>> cqm = ConstrainedQuadraticModel()

You can now formulate an :term:`objective function` to optimize and constraints
any feasible solution must meet, and set these in your CQM.


Objective Function
------------------

The objective function to maximize is the revenue from selling shares. Because
you own an integer number of shares, it is convenient to use integer variables
to indicate the number of shares sold each day, :code:`shares`. For simplicity,
this model assumes stock prices, :code:`price`, are also integers. 

Bounds on the range of values for integer variables shrink the solution space 
the solver must search, so it is helpful to set such bounds; for many problems, 
you can find bounds from your knowledge of the problem. In this case, 

* On any day, you cannot sell more than the total number of shares you start with 
* the maximum share price is the sum of the initial price and the entire price 
  increase that results from selling all your shares, 

  .. math::

	\max(p) = p_0 + \alpha * \sum_i s_i.      

>>> from dimod import Integer
>>> max_p = price_day_0 + alpha*total_shares
>>> shares = [Integer(f's_{i}', upper_bound=total_shares) for i in range(max_days)]
>>> price = [Integer(f'p_{i}', upper_bound=max_p) for i in range(max_days)]

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
   :math:`\sum_i s_i \le` :code:`total_shares`. 

>>> cqm.add_constraint(sum(shares) <= total_shares, label='Sell only shares you own')
'Sell only shares you own'

2. On the first day of the selling period, the stock has a particular price
   :math:`p_0 =` :code:`price_day_0`.

>>> cqm.add_constraint(price[0] == price_day_0, label='Initial share price')
'Initial share price'

3. The stock price increases in proprtion to the number of shares sold the 
   previous day:

   :math:`p_i = p_{i-1} + \alpha s_{i-1}`.

>>> for i in range(1, max_days):
...    pricing = cqm.add_constraint(price[i] - price[i-1] - alpha*shares[i-1] == 0, label=f'Sell at the price on day {i}')

For a sales period of ten days, this CQM has altogether 11 constraints: 

>>> len(cqm.constraints)
11

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
with a maximum allowed runtime of a minute, the CQM hybrid sampler 
returned 41 samples, out of which 24 were solutions that met all the 
constraints: 

>>> sampleset = sampler.sample_cqm(cqm, 
...                                time_limit=60, 
...                                label="SDK Examples - Stock-Selling Strategy")  # doctest: +SKIP
>>> print("{} feasible solutions of {}.".format(
...       sampleset.record.is_feasible.sum(), len(sampleset)))   # doctest: +SKIP
24 feasible solutions of 41.

Parse the best feasible solution:

>>> import itertools
>>> best = next(itertools.filterfalse(lambda d: not getattr(d,'is_feasible'),
...             list(sampleset.data())))
>>> s = [val for key, val in best.sample.items() if "s_" in key]
>>> p = [val for key, val in best.sample.items() if "p_" in key]
>>> r = [p*s for p, s in zip(p, s)]
>>> print("Revenue of {} found for selling {} daily.".format(sum(r), s))     # doctest: +SKIP
Revenue of 9499.0 found for selling [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 9.0, 11.0] daily.



