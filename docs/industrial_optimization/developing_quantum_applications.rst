.. _opt_developing_quantum_applications:

===============================
Developing Quantum Applications
===============================

This chapter provides some insight into the process used by |dwave_short| and
other companies to develop successful quantum applications.

Application development typically advances through the following steps.

#.  :ref:`app_dev_workflow_discovery` identifies problems in your company's
    processes that can benefit from quantum technology.
#.  :ref:`app_dev_workflow_description` describes a problem in a way that
    enables developers to model it.
#.  :ref:`app_dev_workflow_formulation` develops mathematical models of a
    problem.
#.  :ref:`app_dev_workflow_implementation` implements a mathematical model in
    code.
#.  :ref:`app_dev_workflow_testing` iteratively evaluates and improves the
    application.

.. _app_dev_workflow_discovery:

Problem Discovery
=================

The application-development process may start with your company looking to
benefit from quantum technology to improve existing business applications,
develop new applications, or add new features. How do you identify good
candidate problems for quantum-classical hybrid solutions? The following steps
can help.

1. .. dropdown:: Assess your applications.

    Search the company's processes for "bottlenecks", places where problem
    solving takes a lot of time or returns unsatisfactory results. These
    processes may be workhorses that have been in use for years, but over those
    years increases in input data, changing hardware (computers and new sensing
    technology) may have slowed processing or decreased efficacy.

    Bear in mind that a less obvious but possibly fruitful investigative route
    is to also question staff about unsolved problems for which the company may
    have never tried to implement processes.

#. .. dropdown:: Identify candidate problems.

    Typically, good candidates are optimization problems of the type described
    in the
    :ref:`Characteristics of candidate problems <app_dev_workflow_good_problems>`
    section below.

    Shortlist only the most promising problems, which should have these
    attributes:

    -   Important/valuable to the business; resist selecting lower-value
        problems that are tempting due to the ease of formulation.
    -   Hard: for well-known classes of problems you might know that your
        problem is formally hard (e.g., NP-hard) but for most problems it's
        sufficient that it lacks satisfactory solutions, contains many
        interacting choices that cannot be solved sequentially, would add value
        if solved more quickly, etc.

    Often these are problems that your company has previously attempted to
    solve, or has developed a solution for, but perhaps with less satisfactory
    results than desired, lower efficiency than needed, higher costs than
    acceptable, etc.

#. .. dropdown:: Select problems to solve.

    Successful development and introduction of an application as a company
    process might hinge on close collaboration with someone in the organization,
    a "problem owner", who has responsibility for the problem and authority over
    any changes to its solutions. Consider the following steps when selecting a
    problem:

    a.  Prepare an :ref:`elevator pitch <app_dev_workflow_elevator_pitch>`
        (see a possible format described below) for each candidate problem
        identified in the previous step.
    #.  Identify a problem owner for each candidate problem; support from such
        an invested owner may be a condition for advancing a new solution to the
        problem.
    #.  In collaboration with the problem owner, ensure you can access the
        problem's data (inputs, current solution runtimes and quality, etc).

    Proceed with only this curated set of problems.

Examples of Problem Discovery
-----------------------------

.. _app_dev_workflow_discovery_scheduling:

* .. dropdown:: Problem Discovery for a Large Retailer

    As an illustrative example, consider the following scenario of discovery:
    you work for a large retailer and are tasked with looking into applying new
    technologies to improve efficiency and cut costs of business operations.
    Following the steps in this section produces the following results.

    *   Assessing Applications

        You talk to representatives of each department and make a list of
        operational processes, which, for a large retailer, might include
        replenishing stocks of existing products, ordering optimum quantities of
        new products, routing deliveries from suppliers and to consumers, and
        many additional processes that occur daily, weekly, quarterly, etc.

    *   Identifying Candidate Problems

        Among these processes you note that your operations personnel are
        spending many hours per week scheduling shifts to staff the company's
        outlets. Is this a good candidate for new solutions?

        You look into the current scheduling process and find that it is
        implemented with in-house software plus some manual tuning on Excel
        sheets. Two decades ago a single manager used to spend a couple of hours
        on Fridays scheduling shifts for the company's single outlet but now,
        with additional outlets that employ many more workers, the task occupies
        the time of multiple managers on both generating an initial schedule and
        then on making adjustments during the week. Employees are often
        unsatisfied by the resulting schedules that fail to account for their
        preferences on shift times.

        You set up meetings with some of these managers, and they provide some
        very rough figures to help you estimate the business cost of remaining
        with the existing solution. You realize that over months and years, a
        better solution would yield significant savings for the company. It
        would also increase employee satisfaction, and thus retention. A quick
        internet search shows that scheduling can be a hard, discrete
        optimization problem. Such problems are good candidates for
        quantum-classical hybrid solutions.

        Perhaps you identify additional problems in a similar way.

    *   Selecting Problems

        For the identified scheduling problem, one of the involved managers
        agrees to act as the problem owner. Your manager allocates a senior
        developer for a couple of months to help you develop a proof of concept.

        (For the simplest of the additional candidate problems you identified,
        you are given approval to spend a few days jerry-rigging a proof of
        concept, by which you hope to demonstrate improved solution quality and
        justify a project budget. Your manager also considers another candidate
        you identified but suspects that changes there will require broad
        support in the company. You, your manager, and a problem owner create a
        short presentation on that problem's importance to the business, the
        difficulties and cost of the existing process, and the benefits of
        improving the process. Following this presentation, the company's Vice
        President of Operations sets up an ad-hoc "steering committee" with
        representatives of departments that would be effected by a change to
        this process and makes a budget request for developing an improved
        solution.)

* .. dropdown:: Elevator pitch for scheduling candidate problem.

    As an illustration example, the
    :ref:`elevator pitch <app_dev_workflow_elevator_pitch>` worksheet was
    used to create the following pitch points for the large retailer's
    employee-scheduling problem.

    .. list-table:: Scheduling: Business Value and Use Cases
        :widths: 40 60
        :header-rows: 1

        * - Question
          - Answer
        * - Why is this problem important to the business?
          - Given that meeting demand for staffing is imperative for our outlets
            to function, we currently over-allocate, at high cost; our current
            poor fit to employee requirements harms retainment of trained
            personnel;
            managers spend a lot of time scheduling; any changes due to
            same-day no-shows are disruptive.
        * - What improvements would most increase business value?
          - Speed of generating the schedule (reduce time managers spend
            scheduling), better fit to staff preferences, ability to scale for
            our expanding to more outlets next year.
        * - Who are the main users?
          - Outlet managers are responsible for weekly scheduling.
        * - What problem are they trying to solve?
          - Meet the weekly staffing demand while considering employee
            preferences, minimizing paid overtime, and meetings various hard and
            soft constraints.
        * - How do/will they interact with a solution?
          - Ideally the system reads in the staffing-demand and employee
            preference spreadsheets submitted by email/uploaded on website,
            reads employee schedule-data files in database, and at a preset
            weekly time generates up to half a dozen alternative schedules for
            managers to choose from, which can be presented online or emailed.
            If needed, the application can be manually updated and run.
        * - What is the overall process flow?
          - Outlet manager files the demand (requirements) for the week by
            Friday, staff file their preferred shifts for the week by noon
            Monday, the application runs automatically at 1:00 PM and presents
            schedules, managers select one or update parameters and run again,
            and by 4:00 PM the formal schedule is released.

    .. list-table:: Scheduling: Existing Solution
        :widths: 40 60
        :header-rows: 1

        * - Question
          - Answer
        * - How is the problem solved today?
          - In-house software plus manual tuning on Excel sheets. Tuning
            requires many hours and the results are a poor match to staff
            preferences. The schedule always meets demand but only because it
            includes an expensive 20% margin of over-staffing.
        * - What improvements are required for a new solution to displace the
            current one?
          - The main needs are reducing human work and improving the match to
            staff preferences. Any solution must be robust to the expected
            expansion of outlets set in the 5-year plan. An attempt was made to
            modernize the existing software but without success.
        * - Are there any known bottlenecks?
          - Scheduling is a known hard problem.
        * - What are the data inputs and outputs?
          - Inputs are staffing demand file, staff preference sheets, employee
            schedule-data files (exist in current process); output is the full
            schedule for each outlet.
        * - What are the required system and/or process integrations?
          - The new application must read the emailed/uploaded demand and
            preference sheets, and must have permission to access the database
            files of employee qualifications, training, hours, and pay rate.
            It should run automatically and allow managers with permission to
            run manually.
        * - How are results delivered/presented to users?
          - Ideally as an online schedule as shown in the attached PowerPoint.
        * - Is there historical data that can be used to test a new solution?
          - Yes, we can use the last year's filings and schedules.

Resources for Problem Discovery
-------------------------------

.. _app_dev_workflow_good_problems:

* .. dropdown:: Characteristics of candidate problems.

    What type of problems can benefit from quantum technology?

    Quantum computers can solve some hard problems more efficiently than any
    known algorithm for classical computers.\ [#]_

    A strong category of problems for quantum technology is *optimization*
    problems with *quadratic interactions* between *discrete* variables.\ [#]_

    *Optimization* problems are problems that require an assignment of variables
    that results in the best, or very good, solutions. For example, defining in
    what order a set of products be assembled to make the most efficient use of
    the manufacturing machines on a factory floor.

    *Discrete* variables include the following categories of variables:

    *   `Binary <https://en.wikipedia.org/wiki/Binary_data>`_ variables can be
        assigned two values, such as 0 and 1 or True and False.

        Problems with these variables can be recognized by the True or False
        judgments required from their solutions. For example,

        -   Scheduling: Did a task meet its deadline? Did the crew make it to
            the flight?
        -   Networks: Did a network node experience failure?
        -   Finance: Did a loan go into default?

    *   `Integer <https://en.wikipedia.org/wiki/Integer>`_ variables can be
        assigned whole numbers, such as those between -5 to 10.

        Problems with these variables optimize the number of something. For
        example,

        -   Delivery: How many 11" x 5" x 14"-sized boxes should be loaded onto
            the truck?

    *   `Categorical <https://en.wikipedia.org/wiki/Categorical_variable>`_
        (one-hot or "discrete") variables can be assigned a value from a set,
        such as ``green, red, blue``.

        Problems with these variables have several distinct options. For
        example,

        -   Scheduling: Which shift should employee :math:`X`` work?
        -   Map Coloring: Should the state be colored red, blue, green or
            yellow?

    *Quadratic interactions* represent relationships and correlations between
    the inputs of a problem. For example,

    *   Scheduling: A missed deadline affects other tasks, preventing gaps
        between consecutive machine usages saves costs.
    *   Networks: A failed network node changes the load on other nodes.
    *   Finance: Diverse stocks lowers risk, a defaulted loan affects the risk
        to other loans.

    .. [#]
        It can be helpful to have a little familiarity with the relevant
        terminology. Classical solution techniques often classify problems by
        their variable types and interactions:

        *   `ILP <https://en.wikipedia.org/wiki/Linear_programming>`_, integer
            linear programming, deals with problems that have integer variables
            that do not interact with each other.
        *   `MILP <https://en.wikipedia.org/wiki/Linear_programming#Integer_unknowns>`_,
            mixed integer linear programming, includes real (continuous)
            variables.
        *   `MIQP <https://en.wikipedia.org/wiki/Quadratic_programming>`_, mixed
            integer quadratic programming, allows for quadratic interactions
            between the variables.

        More academically,
        `complexity classes <https://en.wikipedia.org/wiki/Computational_complexity_theory>`_
        classify problems in terms of how solution times of algorithms scale
        with input size. For example, P, is a class of problems for which
        algorithms scale polynomially (considered efficient on classical
        computers) while for other classes there may not be classical algorithms
        that run in polynomial time; NP, nondeterministic polynomial-time, is a
        class of problems for which proposed solutions can be verified quickly
        but no known algorithms guarantee solutions in polynomial time.

    .. [#]
        |dwave_short|'s hybrid
        :ref:`constrained quadratic model <concept_models_cqm>`
        solver also performs well on problems with some real variables. Problems
        with real variables optimize over an uncountable set. For example, in a
        gaspipe-maintenance problem, you might ask, Where should the sensor be
        installed? And the answer might be 2.46 meters along some axis.

.. _app_dev_workflow_elevator_pitch:

* .. dropdown::  Elevator pitch for a candidate problem.

    You might use tables such as the following to create elevator pitches
    for each candidate problem:

    .. list-table:: Business Value and Use Cases
        :widths: 40 40 20
        :header-rows: 1

        * - Question
          - Answer
          - Comments
        * - Why is this problem important to the business?
          -
          -
        * - What improvements would most increase business value?
          -
          - Examples: Speed, quality, scalability, etc
        * - Who are the main users?
          -
          -
        * - What problem are they trying to solve?
          -
          -
        * - How do/will they interact with a solution?
          -
          -
        * - What is the overall process flow?
          -
          -

    .. list-table:: Existing Solution
        :widths: 40 40 20
        :header-rows: 1

        * - Question
          - Answer
          - Comments
        * - How is the problem solved today?
          -
          - What is working well? What is not?
        * - What improvements are required for a new solution to displace the
            current one?
          -
          - Have other approaches been tried?
        * - Are there any known bottlenecks?
          -
          -
        * - What are the data inputs and outputs?
          -
          - Are the necessary data inputs already in place?
        * - What are the required system and/or process integrations?
          -
          -
        * - How are results delivered/presented to users?
          -
          -
        * - Is there historical data that can be used to test a new solution?
          -
          -

*   The :ref:`qpu_stating_problems` section provides examples of good problems
    in many industries and verticals, as well as links to further examples.

.. _app_dev_workflow_description:

Problem Description
===================

For any selected problem, the first step in attempting to develop a new solution
or improve an existing solution is a clear and comprehensive description.

A good description specifies the following elements\ [#]_ of the problem:

.. [#]
    The following subsections provide simple examples that should make the
    abstract definitions given here concrete even to users with no prior
    optimization experience.

*   **Inputs**: the data needed to represent an instance of the problem.
*   **Outputs**: the preferred presentation of solutions to the problem.
*   **Parameters**: dependencies that configure problem instances and set
    preferences on solutions.
*   **Decision Variables**: the constituents of the problem to which the process
    attempts to assign good values.\ [#]_
*   **Objectives to be Optimized**: the goals the process attempts to accomplish
    by minimizing or maximizing certain aspects of the problem to the extent
    possible.
*   **Constraints**: aspects of the problem and/or process with limited or no
    flexibility, which must be satisfied for solutions to be considered
    feasible.\ [#]_

.. [#]
    This initial set of variables and their definitions often develops and
    changes during the :ref:`app_dev_workflow_formulation` step.

.. [#]
    Constraints are often categorized as either “hard” or “soft”. Any hard
    constraint must be satisfied for a solution of the model to qualify as
    feasible. Soft constraints may be violated to achieve an overall good
    solution.

The following steps can help guide you.

1. .. dropdown:: Write a plain-language description of the problem as you
    currently understand it.

    A good problem description has the following constituents for its inputs and
    outputs:

    *   Entities

        For example, in an employee-scheduling problem entities might include
        employees, time slots, supervisors, jobs, hourly rates, staffing
        demands, etc.
    *   Relations

        For example, relations in an employee-scheduling might include a
        requirement that one supervisor be present for every three new hires,
        that no more than 20% of staff in any time slot be new hires, that two
        senior staff should not staff a small department simultaneously, etc.
    *   Quantity being optimized

        For example, minimizing the
        `makespan <https://en.wikipedia.org/wiki/Makespan>`_ of a scheduling
        problem or selection of some number :math:`k` of features in a
        machine-learning problem.

#. .. dropdown:: In collaboration with the problem owner, revise your initial
    description.

    *   Describe the problem using the business/domain language, explained for
        non-specialist developers; that means, the description is immediately
        recognizable to experts in the field, with all domain-specific
        terminology clarified for the application developers who may not be
        knowledgeable in the problem's domain or the company's business.
    *   Clear up any ambiguities and inconsistencies.
    *   Ensure that the problem owner approves of the revised description.

#. Attempt to acquire at least one complete instance of the problem, including
   input data, runtime, solutions, tuning parameters, etc.

Examples of Problem Description
-------------------------------

.. dropdown::  Description of a Large Retailer's Scheduling Problem

    As an illustrative example, consider the following scenario of problem
    description.

    *   Candidate Problem

        You are tasked with developing a new solution to the
        :ref:`scheduling problem <app_dev_workflow_discovery_scheduling>`
        of the :ref:`app_dev_workflow_discovery` section.

    *   Plain-Language Description

        Based on your initial work of problem discovery you know enough about
        the employee-scheduling problem to write a draft description. It might
        look something like this:

        "Our employee-scheduling problem is to generate a weekly schedule for
        our Madrid employees that optimally matches demand and scheduled shifts,
        with preference given to senior and full-time employees. The schedule
        should not include back-to-back shifts or more than 48 weekly hours per
        employee..."

    *   Revised Description

        After a few iterations with the problem owner, your final description
        might look like this:

        "Our employee-scheduling problem is to release every Monday by 4:00PM to
        all employees of our five Madrid outlets a schedule of their allocated
        shifts for the following week. Because employees have until noon Monday
        to file their availability and preferences for the following week, the
        scheduling application must generate a schedule within 1 hour to allow
        staff time to make adjustments and rerun once or twice if needed.
        Preferably, the application generates more than a single schedule per
        run, allowing staff discretion to select one.

        The optimal schedule should, to the extent possible, achieve the
        following objectives:\ [#]_

        *   Minimize the differences between our anticipated demand for work
            hours and scheduled hours.
        *   Maximally account for seniority in selecting employees for available
            hours.
        *   Maximally account for employees' stated schedule preferences.
        *   Minimize the number of employees needed to meet the anticipated
            work.
        *   Maximize the number of employees with full-time schedules.
        *   Minimize overtime.
        *   Minimize the variance in overtime across our employees.

        The schedule must also take into consideration the following
        constraints:

        *   Overtime must be in 4-hour blocks.
        *   Full-time employees should not be alloted more than 48 hours per
            week.
        *   Employees must not work back-to-back shifts.
        *   Full-time employees must have two consecutive rest days each week.
        *   Week-end shifts can be allocated only to eligible employees.

    *   Problem Instance

        You also collect one, or preferably a few, problem instances that
        developers can use when designing a replacement application and testing
        it. These might include artifacts such as the following:

        *   File with shift start and end hours for May, July, and October.
        *   Currently used input data files on employees with the following
            details:
            name, employee ID number, rank, minimum and maximum available weekly
            hours, flag specifying full or part time, training (what roles the
            employee is qualified to fill).
        *   Excel sheet with anticipated demand per outlet per role per day from
            several weeks in the previous year.
        *   Scanned copies of the sheets employees file with the weekly
            availability and preferred hours.
        *   Schedules for the last 6 weeks as generated by the current process.

    .. [#]

        When formulating a problem with multiple desired objective, such as
        here, it can be helpful to reduce the final objective to a weighted sum
        of just two or three objectives and reformulate the remainder as (soft)
        constraints. Often these objectives represent costs to the business or
        opportunities to profit, and can be costed; that costing can be used as
        the weightings between these various objectives, combining them into a
        single objective of improving profits. For example, you might define the
        objective to minimize overtime as a constraint on overtime not exceeding
        some threshold.

Resources for Problem Description
---------------------------------

*   `Domain-driven design <https://en.wikipedia.org/wiki/Domain-driven_design>`_

* .. dropdown::  Work Sheet for Problem Description

    This worksheet can aid you in writing a problem description. You can print
    it and, in collaboration with the problem owner, fill in the Description
    column with answers to the question asked for each section, plus any
    additional pertinent information.

    .. list-table:: Problem Description
        :widths: 25 35 40
        :header-rows: 1

        * - Section
          - Description
          - Questions Answered
        * - General statement of the problem in business/domain language
          -
          -
            - What are the decision variables?
            - What is the objective?
            - What are the constraints?
        * - Timing goals and restrictions
          -
          -
            - How frequently is the problem solved?
            - What is the expected solution runtime?
            - Are problem instances independent or a series where one instance
              needs the previous solution as an input?
            - Do other business processes depend on the output of the
              optimization?
        * - Scale of production problems
          -
          -
            - Is the company already solving problem instances at the desired
              scale?
            - What is the largest problem instance currently solved?
            - Is solving large instances more important than quality
              solutions\ [#]_?
        * - Quality of solutions
          -
          -
            - What are the requirements for solution quality?
            - Is optimality a requirement?
            - How important is solution quality?
            - How important is optimality versus feasibility\ [#]_?
            - Is the company satisfied with the quality of current solutions?
        * - Existing model
          -
          - Is there an existing mathematical formulation for the problem?

    .. [#] Does the problem owner prefer to find higher-quality solutions for
        a smaller-than-desired problem instance over good solutions for a
        larger problem instance?

    .. [#] Finding the global optimal (best possible solution, which corresponds
        to the solver returning the lowest possible energy) versus finding a
        good, feasible solution.

.. _app_dev_workflow_formulation:

Problem Formulation
===================

A comprehensive problem description is a prerequisite for developing your
initial model.\ [#]_

The standard approach to problem formulation is to translate the problem
description generated in the previous section into mathematical equations,
specifically an objective subject to constraints.

.. admonition:: Doing the Math

    Although users with high-school mathematics can understand these models,
    depending on your previous experience this step may be challenging.
    |dwave_short|'s training courses provided in the |dwave_learn|_ program can
    reduce learning time but if developing mathematical models is outside your
    company's expertise, it can make solid business sense to have
    |dwave_short|'s Professional Services organization handle this step for you
    via the |dwave_launch_tm|_ program.

Some developers find it best to directly represent the equations in code rather
than in writing. You can try and see what works best for you.

The model you develop in this stage typically has the following elements:

*   Variables: can be binary\ [#]_, integer, and real
*   Objective: the quantity being optimized (formulated as a quadratic/linear
    model to be minimized)
*   Constraints: linear and quadratic relationships between variables that must
    or should\ [#]_ be satisfied

Such a model is called a
:ref:`constrained quadratic model <concept_models_cqm>`,a
:ref:`nonlinear model <concept_models_nonlinear>`, or sometimes a
:ref:`binary quadratic model <concept_models_bqm>`.

Performance is sensitive to the model. As you develop your model consider
various formulations: developing a few different models can be beneficial in
that some might significantly outperform others.

.. [#]
    Typically there are additional prerequisites such as managerial approvals,
    budgets, possibly reviews in your company's legal and human-resources
    departments, input from your IT department, etc. For some applications,
    where change is disruptive, it can be helpful to discuss the process with
    someone in your company that has experience in project and change
    management. Updating established processes can have wide-ranging
    implications; understanding these early on enables you to initiate any
    needed administrative work in parallel to your application development.

.. [#]
    Including "one hot"
    :meth:`discrete <oceandocs:dimod.ConstrainedQuadraticModel.add_discrete>`
    variables.

.. [#]
    Constraints are often categorized as either “hard” or “soft”. Any hard
    constraint must be satisfied for a solution of the model to qualify as
    feasible. Soft constraints may be violated to achieve an overall good
    solution.

Examples of Problem Formulation
-------------------------------

*   The
    `Employee Scheduling example <https://github.com/dwave-examples/employee-scheduling>`_
    in |dwave_short|'s
    `collection of code examples <https://github.com/dwave-examples>`_ is a
    pedagogic example of formulating a small employee-scheduling problem.
*   Ocean software's
    `collection of code examples <https://github.com/dwave-examples>`_ on GitHub
    contains many examples of formulation.

Resources for Problem Formulation
---------------------------------

*   The :ref:`qpu_index_examples_beginner` section walks you through some basic
    examples of mathematical formulation, using very simple objectives and
    constraints, which can be a gentle introduction to the concepts and a series
    of code examples, for different levels of experience, which include such
    formulations.
*   The :ref:`qpu_stating_problems` section provides references to examples
    categorized by field and the :ref:`qpu_reformulating` section describes
    various techniques to mathematically formulate parts of your problem.
*   The |dwave_short|_ website provides links to user applications.
*   `Building a Quantum Hybrid Application <https://www.youtube.com/watch?v=UzTIsoXPnek>`_
    is a video recording of an August 2023 |dwave_short| webinar.
*   There is a vast literature on operational optimization.
*   |dwave_learn|_ program: |dwave_short|'s online, instructor-supported
    training.
*   |dwave_launch|_ program: |dwave_short|'s Professional Services organization,
    which works with customers to accelerate their progress from getting started
    through production implementation.

.. _app_dev_workflow_implementation:

Software Implementation
=======================

Your application will likely have multiple parts, including the following:

*   Core optimization code

    This is the part that implements your formulation of the problem and submits
    it to a |dwave_short| solver for solution. It is recommended that you
    implement the :ref:`model <concept_models>` representing your
    problem, formulated as described in the previous section, and manage the
    submission using the
    `Ocean SDK <index_ocean_sdk>`.

*   Handling inputs and presenting results

    Your application may have rigidly defined inputs and expected outputs or, as
    part of your work, you may have freedom to define input formats and how to
    present solutions. Close collaboration with the problem owner and intended
    users of the application on these parts can prevent mistaken presumptions
    that might risk the project's ultimate success.

*   Integration with other applications

    Try to identify any needed integrations early: some might have long
    procurement or development schedules.

It is recommended that you manage and schedule your application development over
multiple iterations of learning and improvement, as described in the next
section.

.. _app_dev_workflow_testing:

Test and Iterate
================

.. admonition:: Getting it Right

    Many users, even those experienced in
    `operations research <https://en.wikipedia.org/wiki/Operations_research>`_,
    find it challenging to finesse a working model into a performant one. If
    your results fall short, especially on your first attempt to develop a
    quantum application,
    `professional help <https://www.dwavesys.com/solutions-and-products/professional-services>`_
    might be key to your project's success.

A useful approach to implementing your formulated problem as a software
application includes the following steps of iterative development:

1. .. dropdown:: Build an initial prototype

    For your initial prototype, start with small problem inputs and use
    :ref:`symbolic math <concept_symbolic_math>`, simple loops, etc to
    build a model without worrying much about construction performance.

    This prototype, which may also be considered a
    `proof of concept <https://en.wikipedia.org/wiki/Proof_of_concept>`_, might
    be the first point in your development process that provides feedback on its
    feasibility and likelihood of success. As such, you may be balancing
    multiple conflicting needs; for example:

    *   Speed to show initial results versus sufficient research to enable
        success
    *   Demonstrating advantage on large problem instances versus minimal
        software work on small instances
    *   Clear presentation of results versus minimal coding work on outputs
    *   Ease of troubleshooting versus performance

    It can be helpful to define in advance the minimal requirements for the
    initial prototype to ensure timely delivery and successful completion of
    this important step. Take into consideration the complexity of the model,
    the experience of the developers in the relevant fields (both the problem
    and the quantum programming model), and the company's scheduling
    requirements, and aim for the achievable.

#. .. dropdown:: Increase scale, complexity, performance

    *   Iteratively increase problem inputs up to the size expected in your
        production environment. Input size affects not just solution times but
        also the time and memory usage required to build the model. As your
        model's size increases, so does the importance of optimally building the
        model.
    *   Consider various :ref:`decomposition techniques <qpu_decomposing>` when
        dealing with extremely large problems.
    *   Consider various techniques to reduce problem size:
        :class:`presolve techniques <oceandocs:dwave.preprocessing.presolve.pypresolve.Presolver>`,
        dropping (or even adding) constraints, using native discrete variables
        for the hybrid CQM solver, etc.

#. .. dropdown:: Test outputs, update model, and repeat the previous step

    Model validation includes many aspects; for example:

    *   Comparisons with the current solution, between constrained and
        unconstrained models (i.e. representing one or more constraints as
        :ref:`penalty models <concept_penalty>` in the objective), between
        different solvers, and for varying solver
        :ref:`runtimes <opt_best_practices_runtimes>`.
    *   Various inputs, preferably inputs similar to those expected in your
        production environment.
    *   Multiple runs: results from heuristic solvers vary over executions for
        the same input, so the performance of a single execution is
        inconclusive.

    Often, initial models do not perform well and, before you can begin
    increasing the problem scale, you may need to further simplify your model.
    It might be that at this point your immediate goal is to just to achieve
    some "base model" that produces results that are not wrong.

    There are many options for simplifying your model to attain a working base
    from which to then build up the needed, comprehensive model. For example,

    *   Relax some of the constraints
    *   Drop some components of the problem formulation
    *   Explore some alternative formulations for at least some parts of the
        model

        Bear in mind that there are often multiple ways you can view a problem;
        for example, you  could represent an input toggle switch as either a
        binary variable (True or False) or a one-hot variable (ON or OFF) and
        you might represent the
        `satisfiability (SAT) <https://en.wikipedia.org/wiki/Boolean_satisfiability_problem>`_
        problem :math:`(x_1 \vee \overline{x}_2 ) \wedge (\overline{x}_1 \vee x_2)`
        of the :ref:`qpu_example_sat_unconstrained` section as either an
        objective to be minimized, :math:`0.1 x_1 + 0.1 x_2 - 0.2 x_1 x_2`, or a
        constraint to be met, :math:`x_1=x_2`.

Resources for Test Iterations
-----------------------------

*   `Model Validation and Scaling <https://youtu.be/MNdhUtmsbus?t=2180>`_
    tutorial video from |dwave_short|'s Qubits 2023 conference.
*   The :ref:`opt_scaling` section.
*   |dwave_short| provides the |dwave_launch|_ program to accelerate
    enterprises' path from problem discovery through production implementation.
*   The `Leap <https://cloud.dwavesys.com/leap>`_ service hosts a community
    where developers help each other.
