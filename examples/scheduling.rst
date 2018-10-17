.. _scheduling:

======================
Constrained Scheduling
======================

This example solves a binary *constraint satisfaction problem* (CSP). CSPs require that all
a problem's variables be assigned values that result in the satisfying of all constraints.
Here, the constraints are a company's policy for scheduling meetings:

* Constraint 1: During business hours, all meetings must be attended in person at the office.
* Constraint 2: During business hours, participation in meetings is mandatory.
* Constraint 3: Outside business hours, meetings must be teleconferenced.
* Constraint 4: Outside business hours, meetings must not exceed 30 minutes.

Solving such a CSP means finding meetings that meet all the constraints.

The purpose of this example is to help a new user to formulate a constraint satisfaction problem
using Ocean tools and solve it on a D-Wave system.
Other examples demonstrate more advanced steps that might be needed for
complex problems.

Example Requirements
====================

To run the code in this example, the following is required.

* The requisite information for problem submission through SAPI, as described in :ref:`dwavesys`.
* Ocean tools :std:doc:`dwave-binarycsp <binarycsp:index>`,
  :std:doc:`dwave-system <system:index>`,
  and :std:doc:`dimod <dimod:index>`.

If you installed `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_
and ran :code:`dwave config create`, your installation should meet these requirements.

Solution Steps
==============

Section :ref:`solving_problems` describes the process of solving problems on the quantum
computer in two steps: (1) Formulate the problem as a :term:`binary quadratic model` (BQM)
and (2) Solve the BQM with a D-wave system or classical :term:`sampler`. In this example,
Ocean's *dwavebinarycsp* tool builds the BQM based on the constraints we formulate.

Formulate the Problem
=====================

D-Wave systems solve binary quadratic models, so the first step is to express the problem
with binary variables.

* Time of day is represented by binary variable :code:`time` with value :math:`1` for business hours
  and :math:`0` for hours outside the business day.
* Venue is represented by binary variable :code:`location` with value :math:`1` for office
  and :math:`0` for teleconference.
* Meeting duration is represented by variable :code:`length` with value :math:`1` for short meetings
  (under 30 minutes) and :math:`0` for meetings of longer duration.
* Participation is represented by variable :code:`mandatory` with value :math:`1` for mandatory
  participation and :math:`0` for optional participation.

For large numbers of variables and constraints, such problems can be hard.
This example has four binary variables, so only :math:`2^4=16` possible meeting arrangements.
As shown in the table below, it is a simple matter to work out all the combinations by hand to
find solutions that meet all the constraints.

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

Ocean's :std:doc:`dwavebinarycsp <binarycsp:index>` enables the
definition of constraints in different ways, including by defining functions that evaluate
True when the constraint is met. The code below defines a function that returns True when
all this example's constraints are met.

.. code-block:: python

   def scheduling(time, location, length, mandatory):
       if time:                                 # Business hours
           return (location and mandatory)      # In office and mandatory participation
       else:                                    # Outside business hours
           return ((not location) and length)   # Teleconference for a short duration

The next code lines create a constraint from this function and adds it to CSP instance,
:code:`csp`, instantiated with binary variables.

>>> import dwavebinarycsp
>>> csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)
>>> csp.add_constraint(scheduling, ['time', 'location', 'length', 'mandatory'])

This tool, :std:doc:`dwavebinarycsp <binarycsp:index>`, can also convert the binary CSP to a BQM. The following code does so and
displays the BQM's linear and quadratic coefficients, :math:`q_i` and :math:`q_{i,j}` respectively in
:math:`\sum_i^N q_ix_i + \sum_{i<j}^N q_{i,j}x_i  x_j`, which are the inputs for programming
the quantum computer.

>>> bqm = dwavebinarycsp.stitch(csp)
>>> bqm.linear   # doctest: +SKIP
{'length': -2.0, 'location': 2.0, 'mandatory': 0.0, 'time': 2.0}
>>> bqm.quadratic          # doctest: +SKIP
{('location', 'length'): 2.0,
 ('mandatory', 'length'): 0.0,
 ('mandatory', 'location'): -2.0,
 ('time', 'length'): 0.0,
 ('time', 'location'): -4.0,
 ('time', 'mandatory'): 0.0}

Solve the Problem by Sampling
=============================

For small numbers of variables, even your computer's CPU can solve CSPs
quickly. Here we solve both classically on your CPU and on the quantum computer.

Solving Classically on a CPU
----------------------------

Before using the D-Wave system, it can sometimes be helpful to test code locally.
Here we select one of Ocean software's test samplers to solve classically on a CPU.
Ocean's :std:doc:`dimod <dimod:index>` provides a sampler that
simply returns the BQM's value (energy) for every possible assignment of variable values.

>>> from dimod.reference.samplers import ExactSolver
>>> sampler = ExactSolver()
>>> solution = sampler.sample(bqm)

Valid solutions---assignments of variables that do not violate any constraint---should
have the lowest value of the BQM, and *ExactSolver()* orders its assignments
of variables by ascending order, so the first solution has the lowest value (lowest
energy state). The code below sets variable :code:`min_energy` to the BQM's
lowest value, which is in the first record of the returned result.

>>> min_energy = next(solution.data(['energy']))[0]
>>> print(min_energy)
-2.0

The code below prints all those solutions (assignments of variables) for which the BQM has
its minimum value.

>>> for sample, energy in solution.data(['sample', 'energy']):
...     if energy == min_energy:
...         time = 'business hours' if sample['time'] else 'evenings'
...         location = 'office' if sample['location'] else 'home'
...         length = 'short' if sample['length'] else 'long'
...         mandatory = 'mandatory' if sample['mandatory'] else 'optional'
...         print("During {} at {}, you can schedule a {} meeting that is {}".format(time, location, length, mandatory))
...
During evenings at home, you can schedule a short meeting that is optional
During evenings at home, you can schedule a short meeting that is mandatory
During business hours at office, you can schedule a short meeting that is mandatory
During business hours at office, you can schedule a long meeting that is mandatory

Solving on a D-Wave System
--------------------------

We now solve on a D-Wave system using sampler *DWaveSampler()* from Ocean software's
:std:doc:`dwave-system <system:index>`. We also use
its *EmbeddingComposite()* composite to map our unstructured problem (variables
such as :code:`time` etc.) to the sampler's graph structure (the QPU's numerically
indexed qubits) in a process known as :term:`minor-embedding`. The next code sets up
a D-Wave system as the sampler.

.. note:: In the code below, replace sampler parameters in the third line. If
      you configured a default solver, as described in :ref:`dwavesys`, you
      should be able to set the sampler without parameters as
      :code:`sampler = EmbeddingComposite(DWaveSampler())`.
      You can see this information by running :code:`dwave config inspect` in your terminal.

>>> from dwave.system.samplers import DWaveSampler
>>> from dwave.system.composites import EmbeddingComposite
>>> sampler = EmbeddingComposite(DWaveSampler(endpoint='https://URL_to_my_D-Wave_system/', token='ABC-123456789012345678901234567890', solver='My_D-Wave_Solver'))

Because the sampled solution is probabilistic, returned solutions may differ between runs. Typically,
when submitting a problem to the system, we ask for many samples, not just one. This way, we see multiple
“best” answers and reduce the probability of settling on a suboptimal answer. Below, we
ask for 5000 samples.

>>> response = sampler.sample(bqm, num_reads=5000)

The code below prints all those solutions (assignments of variables) for which the BQM has
its minimum value and the number of times it was found.

>>> total = 0
... for sample, energy, occurrences in response.data(['sample', 'energy', 'num_occurrences']):
...     total = total + occurrences
...     if energy == min_energy:
...         time = 'business hours' if sample['time'] else 'evenings'
...         location = 'office' if sample['location'] else 'home'
...         length = 'short' if sample['length'] else 'long'
...         mandatory = 'mandatory' if sample['mandatory'] else 'optional'
...         print("{}: During {} at {}, you can schedule a {} meeting that is {}".format(occurrences, time, location, length, mandatory))
... print("Total occurrences: ", total)
...
1676: During business hours at office, you can schedule a long meeting that is mandatory
1229: During business hours at office, you can schedule a short meeting that is mandatory
1194: During evenings at home, you can schedule a short meeting that is optional
898: During evenings at home, you can schedule a short meeting that is mandatory
Total occurrences:  5000

Summary
=======

In the terminology of :ref:`oceanstack`\ , Ocean tools moved the original problem through the
following layers:

* Application: scheduling under constraints. There exist many CSPs that are computationally hard problems; for example, the
  map-coloring problem is to color all regions of a map such that any two regions sharing a border
  have different colors. The job-shop scheduling problem is to schedule multiple jobs done on several
  machines with constraints on the machines' execution of tasks.
* Method: constraint compilation.
* Sampler API: the Ocean tool builds a BQM with lowest values ("ground states") that
  correspond to assignments of variables that satisfy all constraints.
* Sampler: classical *ExactSolver()* and then *DWaveSampler()*.
* Compute resource: first a local CPU then a D-Wave system.
