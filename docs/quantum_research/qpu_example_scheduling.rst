.. _qpu_example_scheduling:

=======================
Scheduling: Constraints
=======================

This example solves a binary *constraint satisfaction problem* (:term:`CSP`).
CSPs require that all a problem's variables be assigned values that result in
the satisfying of all :term:`constraints <constraint>`. Here, the constraints
are a company's policy for scheduling meetings:

*   Constraint 1: During business hours, all meetings must be attended in person
    at the office.
*   Constraint 2: During business hours, participation in meetings is mandatory.
*   Constraint 3: Outside business hours, meetings must be teleconferenced.
*   Constraint 4: Outside business hours, meetings must not exceed 30 minutes.

Solving such a CSP means finding arrangements of meetings that meet all the
constraints.

The purpose of this example is to help a new user to formulate a constraint
satisfaction problem using :ref:`Ocean software <index_ocean_sdk>` tools and
solve it on a |dwave_short| quantum computer. Other examples demonstrate
more-advanced steps that might be needed for complex problems.

Example Requirements
====================

.. include:: ../shared/examples.rst
    :start-after: start_requirements
    :end-before: end_requirements

Solution Steps
==============

.. |workflow_section| replace:: :ref:`qpu_workflow`

.. include:: ../shared/examples.rst
    :start-after: start_standard_steps
    :end-before: end_standard_steps

This example represents the problem's constraints as
:ref:`penalties <concept_penalty>` (small :term:`BQMs <bqm>` that have higher
values for variable assignments that violate constraints) and creates an
:term:`objective function` by summing all four penalty models. Solvers that seek
low-energy states are thus less likely to return meeting arrangements that
violate constraints.

Formulate the Problem
=====================

|dwave_short| quantum computers solve
:ref:`binary quadratic models <concept_models_bqm>`, so the first step is to
express the problem with binary variables (this example uses
:math:`\{0, 1\}`--valued binary variables):

.. list-table:: Problem Variables
    :widths: 15 25 25 35
    :header-rows: 1

    *   - **Variable**
        - **Represents**
        - **Value: 1**
        - **Value: 0**
    *   - :math:`t`
        - Time of day
        - Business hours
        - Non-business hours
    *   - :math:`v`
        - Venue
        - Office
        - Teleconference
    *   - :math:`l`
        - Length
        - Short (< 30 min)
        - Long
    *   - :math:`p`
        - Participation
        - Mandatory
        - Optional

.. note:: A slightly more complex problem might require variables with multiple
    values; for example, :code:`l` could have values :code:`{30, 60, 120}`
    representing the duration in minutes of meetings of several lengths. For
    such problems a :ref:`discrete quadratic model <concept_models_dqm>` (DQM)
    could be a better choice.

    In general, problems with constraints are more simply solved using a
    :ref:`nonlinear model <concept_models_nonlinear>` or a
    :ref:`constrained quadratic model <concept_models_cqm>` (CQM) and
    appropriate :term:`hybrid` nonlinear or :term:`CQM` solver, as demonstrated
    in the :ref:`opt_example_nl_cvrp` or :ref:`opt_example_cqm_binpacking`
    examples; however, the purpose of this example is to demonstrate solution
    directly on a |dwave_short| quantum computer.

For large numbers of variables and constraints, such problems can be hard. This
example has four binary variables, so only :math:`2^4=16` possible meeting
arrangements. As shown in the table below, it is a simple matter to work out all
the combinations by hand to find solutions that meet all the constraints.

.. table:: All Possible Meeting Options.
    :name: MeetingOptions

    ====================  =================  ==============  ==================  =================
    **Time of Day**       **Venue**          **Duration**    **Participation**   **Valid?**
    ====================  =================  ==============  ==================  =================
    Business hours        Office             Short           Mandatory           Yes
    Business hours        Office             Short           Optional            No (violates 2)
    Business hours        Office             Long            Mandatory           Yes
    Business hours        Office             Long            Optional            No (violates 2)
    Business hours        Teleconference     Short           Mandatory           No (violates 1)
    Business hours        Teleconference     Short           Optional            No (violates 1, 2)
    Business hours        Teleconference     Long            Mandatory           No (violates 1)
    Business hours        Teleconference     Long            Optional            No (violates 1, 2)
    Non-business hours    Office             Short           Mandatory           No (violates 3)
    Non-business hours    Office             Short           Optional            No (violates 3)
    Non-business hours    Office             Long            Mandatory           No (violates 3, 4)
    Non-business hours    Office             Long            Optional            No (violates 3, 4)
    Non-business hours    Teleconference     Short           Mandatory           Yes
    Non-business hours    Teleconference     Short           Optional            Yes
    Non-business hours    Teleconference     Long            Mandatory           No (violates 4)
    Non-business hours    Teleconference     Long            Optional            No (violates 4)
    ====================  =================  ==============  ==================  =================

Represent Constraints as Penalties
----------------------------------

You can represent constraints as BQMs using a :ref:`concept_penalty` in many
different ways.

*   Constraint 1: During business hours, all meetings must be attended in person
    at the office.

    This constraint requires that if :math:`t=1` (time of day is within business
    hours) then :math:`v = 1` (venue is the office). A simple penalty function,
    :math:`t-tv`, is shown in the truth table below:

    .. list-table:: Constraint 1: :math:`t-tv`
        :header-rows: 1

        *   - :math:`t`
            - :math:`v`
            - :math:`t-tv`
        *   - 0
            - 0
            - 0
        *   - 0
            - 1
            - 0
        *   - 1
            - 0
            - 1
        *   - 1
            - 1
            - 0

    Penalty function :math:`t-tv` sets a penalty of 1 for the the case
    :math:`t=1 \; \& \; v=0`, representing a meeting outside the office during
    business hours, which violates constraint 1. When incorporated in an
    objective function, solutions that violate constraint 1 do not yield minimal
    values.

    .. note:: One way to derive such a penalty function is to start with the
        simple case of a Boolean operator: the AND constraint, :math:`ab`,
        penalizes variable values :math:`a=b=1`. To penalize :math:`a=1, b=0`,
        you need the penalty function :math:`a \overline{b}`. For
        :math:`\{0, 1\}`--valued variables, you can substitute
        :math:`\overline{b} = 1-b` into the penalty and get
        :math:`a \overline{b} = a(1-b) = a - ab`.
        For more information on formulating such constraints, see the
        :ref:`qpu_reformulating` section.

*   Constraint 2: During business hours, participation in meetings is mandatory.

    This constraint requires that if :math:`t=1` (time of day is within
    business hours) then :math:`p=1` (participation is mandatory). A penalty
    function is :math:`t-tp`, analogous to constraint 1.

*   Constraint 3: Outside business hours, meetings must be teleconferenced.

    This constraint requires that if :math:`t=0` (time of day is outside
    business hours) then :math:`v=0` (venue is teleconference, not the office).
    A penalty function is :math:`v-tv`, a reversal of constraint 1.

*   Constraint 4: Outside business hours, meetings must not exceed 30 minutes.

    This constraint requires that if :math:`t=0` (time of day is outside
    business hours) then :math:`l=1` (meeting length is short). A simple penalty
    function is :math:`1+tl-t-l`, as shown in the truth table below:

    .. list-table:: Constraint 4: :math:`1+tl-t-l`
        :header-rows: 1

        *   - :math:`t`
            - :math:`l`
            - :math:`1+tl-t-l`
        *   - 0
            - 0
            - 1
        *   - 0
            - 1
            - 0
        *   - 1
            - 0
            - 0
        *   - 1
            - 1
            - 0

    Penalty function :math:`1+tl-t-l` sets a penalty of 1 for the the case
    :math:`t=0 \; \& \; l=0`, representing a lengthy meeting outside business
    hours, which violates constraint 4. When incorporated in an objective
    function, solutions that violate constraint 4 do not yield minimal values.

Create a BQM
------------

The total penalty for all four constraints is

.. math::

    t-tv + t-tp + v-tv + 1+tl-t-l

    = -2tv -tp +tl +t +v -l +1

Ocean's :ref:`dimod <index_dimod>` package enables the creation of BQMs. Below,
the first list of terms are the linear terms and the second are the quadratic
terms; the offset is set to 1; and the variable type is set to use
:math:`\{0, 1\}`--valued binary variables.

>>> from dimod import BinaryQuadraticModel
>>> bqm = BinaryQuadraticModel({'t': 1, 'v': 1, 'l': -1},
...                            {'tv': -2, 'tl': 1, 'tp': -1},
...                            1,
...                            'BINARY')

Solve the Problem by Sampling
=============================

For small numbers of variables, even your computer's CPU can solve CSPs quickly.
Here you solve both classically on your CPU and on the quantum computer.

Solving Classically on a CPU
----------------------------

Before using a |dwave_short| quantum computer, it can sometimes be helpful to
test code locally. Here, select one of Ocean software's test samplers to solve
classically on a CPU.
Ocean's :ref:`dimod <index_dimod>` package provides a sampler that simply
returns the BQM's value (energy) for every possible assignment of variable
values.

>>> from dimod.reference.samplers import ExactSolver
>>> sampler = ExactSolver()
>>> sampleset = sampler.sample(bqm)

Valid solutions---assignments of variables that do not violate
constraints---have the lowest value of the BQM (values of zero in the
:code:`energy` field below):

>>> print(sampleset.lowest(atol=.5))
   l  p  t  v energy num_oc.
0  1  0  0  0    0.0       1
1  1  1  0  0    0.0       1
2  1  1  1  1    0.0       1
3  0  1  1  1    0.0       1
['BINARY', 4 rows, 4 samples, 4 variables]

The code below prints all those solutions (assignments of variables) for which
the BQM has its minimum value.

>>> for sample, energy in sampleset.data(['sample', 'energy']): # doctest: +SKIP
...     if energy==0:
...         time = 'business hours' if sample['t'] else 'evenings'
...         venue = 'office' if sample['v'] else 'home'
...         length = 'short' if sample['l'] else 'long'
...         participation = 'mandatory' if sample['p'] else 'optional'
...         print("During {} at {}, you can schedule a {} meeting that is {}".format(time, venue, length, participation))
During evenings at home, you can schedule a short meeting that is optional
During evenings at home, you can schedule a short meeting that is mandatory
During business hours at office, you can schedule a short meeting that is mandatory
During business hours at office, you can schedule a long meeting that is mandatory

Solving on a Quantum Computer
-----------------------------

Now solve on a |dwave_short| quantum computer using the
:class:`~dwave.system.samplers.DWaveSampler` sampler from Ocean software's
:ref:`dwave-system <index_system>` package. Also use its
:class:`~dwave.system.composites.EmbeddingComposite` composite to map your
unstructured problem (variables such as :code:`t` etc.) to the sampler's
:ref:`graph structure <qpu_topologies>` (the QPU's numerically indexed qubits)
in a process known as :term:`minor-embedding`. The next code sets up a
|dwave_short| quantum computer as the sampler.

.. include:: ../shared/examples.rst
    :start-after: start_default_solver_config
    :end-before: end_default_solver_config

>>> from dwave.system import DWaveSampler, EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler())

Because the sampled solution is probabilistic, returned solutions may differ
between runs. Typically, when submitting a problem to a quantum computer, you
ask for many samples, not just one. This way, you see multiple “best” answers
and reduce the probability of settling on a suboptimal answer. Below, ask for
5000 samples.

>>> sampleset = sampler.sample(bqm, num_reads=5000, label='SDK Examples - Scheduling')

The code below prints all those :term:`solutions` (assignments of variables) for
which the BQM has its minimum value and the number of times it was found.

>>> print(sampleset.lowest(atol=.5))  # doctest: +SKIP
   l  p  t  v energy num_oc. chain_.
0  1  0  0  0    0.0    1238     0.0
1  0  1  1  1    0.0    1255     0.0
2  1  1  0  0    0.0    1212     0.0
3  1  1  1  1    0.0    1290     0.0
['BINARY', 4 rows, 4995 samples, 4 variables]

Summary
=======

In the terminology of the :ref:`ocean_stack` section, Ocean tools moved the
original problem through the following layers:

*   Application: scheduling under constraints. There exist many CSPs that are
    computationally hard problems; for example, the
    :ref:`map-coloring <qpu_example_mapcoloring>` problem is to color all
    regions of a map such that any two regions sharing a border have different
    colors. The
    `job-shop scheduling <https://github.com/dwave-examples/job-shop-scheduling-cqm>`_
    problem is to schedule multiple jobs done on several machines with
    constraints on the machines' execution of tasks.
*   Method: constraint compilation.
*   Sampler API: the Ocean tool builds a BQM with lowest values
    (:term:`ground states <ground state>`) that correspond to assignments of
    variables that satisfy all constraints.
*   Sampler: classical :class:`~dimod.reference.samplers.ExactSolver` and then
    quantum :class:`~dwave.system.samplers.DWaveSampler` samplers.
*   Compute resource: first a local CPU then a |dwave_short| quantum computer.
