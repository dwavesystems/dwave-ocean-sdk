.. _qpu_stating_problems:

===================
Stating the Problem
===================

Once properly stated, a problem can be formulated as an objective function to be
solved on a |dwave_short| solver.

|dwave_short| provides several resources containing many reference examples:

*   Ocean software's
    `collection of code examples <https://github.com/dwave-examples>`_ on
    GitHub.
*   `D-Wave papers <https://www.dwavesys.com/learn/publications>`_
    (for example, [dwave2]_) and links to
    `user applications <https://www.dwavesys.com/learn/featured-applications/>`_.

This section provides a sample of problems in various fields, and the available
resources for each (at the time of writing); having a relevant reference problem
may enable you to use similar solution steps when solving your own problems on
|dwave_short| solvers.

Many of these are discrete optimization, also known as combinatorial
optimization, which is the optimization of an objective function defined over a
set of discrete values such as Booleans.

Keep in mind that there are different ways to model a given problem; for
example, a :term:`constraint satisfaction problem` (CSP) can have various
domains, variables, and constraints. :term:`Model` selection can affect solution
performance, so it may be useful to consider various approaches.

.. list-table:: A Sample of Reference Problems in |dwave_short|'s Resources
    :widths: 40 20 20 20
    :header-rows: 1

    *   - **Problem**
        - **Beginner Content Available?**
        - **Solvers**
        - **Content**
    *   - :ref:`qpu_stating_problems_fault_diagnosis`
        -
        - QPU, hybrid
        - Code, papers
    *   - :ref:`qpu_stating_problems_computer_vision`
        -
        - QPU
        - Papers
    *   - :ref:`qpu_stating_problems_database_queries`
        -
        - QPU
        - Papers
    *   - :ref:`qpu_stating_problems_factoring`
        - Yes
        - QPU
        - Code, papers
    *   - :ref:`qpu_stating_problems_finance`
        -
        - QPU, hybrid
        - Papers
    *   - :ref:`qpu_stating_problems_graph_partitioning`
        - Yes
        - QPU, hybrid
        - Code, papers
    *   - :ref:`qpu_stating_problems_machine_learning`
        -
        - QPU
        - Papers
    *   - :ref:`qpu_stating_problems_map_coloring`
        - Yes
        - QPU, hybrid
        - Code, paper
    *   - :ref:`qpu_stating_problems_protein_folding`
        -
        - QPU
        - Papers
    *   - :ref:`qpu_stating_problems_scheduling`
        - Yes
        - QPU, hybrid
        - Code, papers
    *   - :ref:`qpu_stating_problems_traffic_flow`
        -
        - QPU, hybrid
        - Papers

Whether or not you see a relevant problem here, it's recommended you check out
the examples in |dwave_short|'s
`collection of code examples <https://github.com/dwave-examples>`_ and
`corporate website <https://www.dwavesys.com>`_ for the latest examples of
problems from all fields of study and industry.

.. _qpu_stating_problems_fault_diagnosis:

Circuits & Fault Diagnosis
==========================

Fault diagnosis attempts to quickly localize failures as soon as they are
detected in systems such as sensor networks, process monitoring, and safety
monitoring. Circuit fault diagnosis attempts to identify failed gates during
manufacturing, under the assumption that gate failure is rare enough that the
minimum number of gates failing is the most likely cause of the detected
problem.

The :ref:`qpu_reformulating_example_cfd` section in the :ref:`qpu_reformulating`
chapter shows the steps of solving a circuit fault diagnosis problem on a
|dwave_short| QPU.

Code Examples
-------------

*   :ref:`qpu_example_multigate`

    Solves a logic circuit problem using Ocean tools to demonstrate solving a
    CSP on a |dwave_short| QPU solver.
*   `Circuit-Fault-Diagnosis <https://github.com/dwave-examples/circuit-fault-diagnosis>`_

    Demonstrates the use of |dwave_short| solvers to solve a three-bit
    multiplier circuit.
*   `Circuit Equivalence <https://github.com/dwave-examples/circuit-equivalence>`_

    Verifies equivalence of two representations of electronic circuits using a
    discrete quadratic model (DQM).

Papers
------

*   [Bia2016]_ discusses embedding fault diagnosis CSPs on the |dwave_short|
    system.
*   [Bis2017]_ discusses a problem of diagnosing faults in an electrical
    power-distribution system.
*   [Pap1976]_ discusses decomposing complex systems for the problem of
    generating tests for digital-faults detection.
*   [Per2015]_ maps fault diagnosis to a QUBO and embeds onto a QPU.

.. _qpu_stating_problems_computer_vision:

Computer Vision
===============

`Computer vision <https://en.wikipedia.org/wiki/Computer_vision>`_ develops
techniques to enable computers to analyse digital images, including video. The
field has applications in industrial manufacturing, healthcare, navigation,
miltary, and many other areas.

Papers
------

*   [Arr2022]_ compares quantum and classical approaches to motion segmentation.
*   [Bir2021]_ discusses a quantum algorithm for solving a synchronization
    problem, specifically permutation synchronization, a non-convex optimization
    problem in discrete variables.
*   [Gol2019]_ derive an algorithm for correspondence problems on point sets.
*   [Li2020]_ translates detection scores from bounding boxes and overlap ratio
    between pairs of bounding boxes into QUBOs for removing redundant object
    detections.
*   [Ngu2019]_ demonstrates good prediction performance of a regression
    algorithm for a lattice quantum chromodynamics simulation data using a
    |dwave_2kq| system.

.. _qpu_stating_problems_database_queries:

Database Queries (SAT Filters)
==============================

A satisfiability (SAT) filter is a small data structure that enables fast
querying over a huge dataset by allowing for false positives (but not false
negatives).

Papers
------

*   [Bia2017]_ discusses solving SAT and MaxSAT with a quantum annealer.
*   [Dou2015]_ discusses uses of SAT filters with a quantum annealer.
*   [Jue2016]_ discusses quantum annealing for Boolean satisfiability problems.
*   [Wea2014]_ describes the SAT filter.

.. _qpu_stating_problems_factoring:

Factoring
=========

The factoring problem is to decompose a number into its factors. There is no
known method to quickly factor large integers---the complexity of this problem
has made it the basis of public-key cryptography algorithms.

Code Examples
-------------

*   `Factoring <https://github.com/dwave-examples/factoring>`_

    Demonstrates the use of |dwave_short| QPU solvers to solve a small factoring
    problem.
*   `Factoring Notebook <https://github.com/dwave-examples/factoring-notebook>`_

    Demonstrates the use of |dwave_short| QPU solvers to solve a small factoring
    problem.

Papers
------

*   [Dri2017]_ investigates prime factorization using quantum annealing and
    computational algebraic geometry, specifically Grobner bases.
*   [Dwave3]_ discusses integer factoring in the context of using the
    |dwave_short| Anneal Offsets feature; see also the
    :ref:`qpu_config_anneal_offset` section.
*   [Bur2002]_ discusses factoring as optimization.
*   [Jia2018]_ develops a framework to convert an arbitrary integer
    factorization problem to an executable Ising model.
*   [Lin2021]_ applies deep reinforcement learning to configure adiabatic
    quantum computing on prime factoring problems.

.. _qpu_stating_problems_finance:

Finance
=======

Portfolio optimization is the problem of optimizing the allocation of a budget
to a set of financial assets.

Papers
------

*   [Coh2020]_ investigates the use of quantum computers for building an optimal
    portfolio.
*   [Coh2020b]_ analyzes 3,171 US common stocks to create an efficient
    portfolio.
*   [Das2019]_ provides a quantum annealing algorithm in QUBO form for a dynamic
    asset allocation problem using expected shortfall constraint.
*   [Din2019]_ seeks the optimal configuration of a supply chain's
    infrastructures and facilities based on customer demand.
*   [Els2017]_ discusses using Markowitz's optimization of the financial
    portfolio selection problem on the |dwave_short| system.
*   [Gra2021]_ uses portfolio optimization as a case study by which to benchmark
    quantum annealing controls.
*   [Kal2019]_ explores how commercially available quantum hardware and
    algorithms can solve real world problems in finance.
*   [Mug2020]_ implements dynamic portfolio optimization on quantum and
    quantum-inspired algorithms and compare with |dwave_short| hybrid solvers.
*   [Mug2021]_ proposes a hybrid quantum-classical algorithm for dynamic
    portfolio optimization with minimal holding period.
*   [Oru2019]_ looks at forecasting financial crashes.
*   [Pal2021]_ implement in a simple way some complex real-life constraints on
    the portfolio optimization problem
*   [Phi2021]_ selects a set of assets for investment such that the total risk
    is minimised, a minimum return is realised and a budget constraint is met.
*   [Ros2016a]_ discusses solving a portfolio optimization problem on the
    |dwave_short| system.
*   [Ven2019]_ investigates a hybrid quantum-classical solution method to the
    mean-variance portfolio optimization problems.

.. _qpu_stating_problems_graph_partitioning:

Graph Partitioning
==================

`Graph partition <https://en.wikipedia.org/wiki/Graph_partition>`_ is the
problem of reducing a graph into mutually exclusive sets of nodes.

Code Examples
-------------

*   `Graph Partitioning <https://github.com/dwave-examples/graph-partitioning>`_

    Solves a graph partitioning problem on a QPU.
*   `Graph-Partitioning DQM <https://github.com/dwave-examples/graph-partitioning-dqm>`_

    Solves a graph partitioning problem using the DQM solver in the Leap
    service.
*   `Maximum Cut <https://github.com/dwave-examples/maximum-cut>`_

    Solves a maximum cut problem on a QPU.
*   `Clustering <https://github.com/dwave-examples/clustering>`_

    Identifies clusters in a data set.
*   `Immunization Strategy <https://github.com/dwave-examples/immunization-strategy>`_

    Fragments a population into separate groups via a "separator" using the DQM
    solver in the Leap service.

Papers
------

*   [Bod1994]_ investigates the complexity of the maximum cut problem.
*   [Gue2018]_ performs simulations of the Quantum Approximate Optimization
    Algorithm (QAOA) for maximum cut problems.
*   [Hig2022]_ computes core-periphery partition for an undirected network
    formulated as a QUBO problem.
*   [Jas2019]_ proposes a using quantum annealing on extreme clustering
    problems.
*   [Ush2017]_ discusses unconstrained graph partitioning as community
    clustering.
*   [Zah2019]_ proposes an algorithm to detect multiple communities in a signed
    graph.

.. _qpu_stating_problems_machine_learning:

Machine Learning
================

Artificial intelligence (AI) is transforming the world. You see it every day at
home, at work, when shopping, when socializing, and even when driving a car.
Machine learning algorithms operate by constructing a model with parameters that
can be learned from a large amount of example input so that the trained model
can make predictions about unseen data.

Most of the transformation that AI has brought to-date has been based on
deterministic machine learning models such as feed-forward neural networks. The
real world, however, is nondeterministic and filled with uncertainty.
*Probabilistic* models explicitly handle this uncertainty by accounting for gaps
in our knowledge and errors in data sources.

A *probability distribution* is a mathematical function that assigns a
probability value to an event. Depending on the nature of the underlying event,
this function can be defined for a continuous event (e.g., a normal
distribution) or a discrete event (e.g., a Bernoulli distribution). In
probabilistic models, probability distributions represent the unobserved
quantities in a model (including noise effects) and how they relate to the data.
The distribution of the data is approximated based on a finite set of *samples*.
The model infers from the observed data, and learning occurs as it transforms
the *prior* distributions, defined before observing the data, into *posterior*
distributions, defined afterward. If the training process is successful, the
learned distribution resembles the actual distribution of the data to the extent
that the model can make correct predictions about unseen situations---correctly
interpreting a previously unseen handwritten digit, for example.

In short, probabilistic modeling is a practical approach for designing machines
that:

*   Learn from noisy and unlabeled data
*   Define confidence levels in predictions
*   Allow decision making in the absence of complete information
*   Infer missing data and latent correlations in data

Machine learning algorithms operate by constructing a model with parameters that
can be learned from a large amount of example input so that the trained model
can make predictions about unseen data.

Boltzmann Distribution
----------------------

A *Boltzmann distribution* is an energy-based discrete distribution that defines
probability, :math:`p`, for each of the states in a binary vector.

Assume :math:`\vc{x}` represents a set of :math:`N` binary random variables.
Conceptually, the space of :math:`\vc{x}` corresponds to binary representations
of all numbers from 0 to :math:`2^N - 1`. You can represent it as a column
vector, :math:`\vc{x}^T = [x_1, x_2, \dots, x_N]`, where
:math:`x_n \in \{0, 1\}` is the state of the :math:`n^{th}` binary random
variable in :math:`\vc{x}`.

The Boltzmann distribution defines a probability for each possible state that
:math:`\vc{x}` can take using\ [#]_

.. [#]
    :math:`\beta` is omitted from this equation because usually, in the context
    of machine learning, it is assumed to be 1.

.. math::
    :nowrap:

    \begin{equation}
        p(\vc{x}) = \frac{1}{Z} \exp(-E(\vc{x};\theta))
    \end{equation}

where :math:`E(\vc{x};\theta)` is an energy function parameterized by
:math:`\theta`, which contains the biases, and

.. math::
    :nowrap:

    \begin{equation}
        Z = \sum_x{\exp(-E(\vc{x};\theta))}
    \end{equation}

is the *normalizing coefficient*, also known as the *partition function*, that
ensures that :math:`p(\vc{x})` sums to 1 over all the possible states of
:math:`x`; that is,

.. math::
    :nowrap:

    \begin{equation}
        \sum_x p(\vc{x}) = 1.
    \end{equation}

Note that because of the negative sign for energy, :math:`E`, the states with
high probability correspond to states with low energy.

The energy function :math:`E(\vc{x};\theta)` can be represented as a QUBO:
the linear coefficients bias the probability of individual binary variables
in :math:`\vc{x}` and the quadratic coefficients represent the correlation
weights between the elements of :math:`\vc{x}`. The |dwave_short| architecture,
which natively processes information through the Ising/QUBO models (linear
coefficients are represented by qubit biases and quadratic coefficients by
coupler strengths), can help discrete energy-based machine learning.

Sampling from the |dwave_short| QPU
-----------------------------------

Sampling from energy-based distributions is a computationally intensive task
that is an excellent match for the way that the |dwave_short| system solves
problems; that is, by seeking low-energy states. Samples from the |dwave_short|
QPU can be obtained quickly and provide an advantage over sampling from
classical distributions.

When training a probabilistic model, you need a well-characterized distribution;
otherwise, it is difficult to calculate gradients and you have no guarantee of
convergence. While both classical Boltzmann and quantum Boltzmann distributions
are well characterized, all but the smallest problems solved by the QPU should
undergo postprocessing to bring them closer to a Boltzmann distribution; for
example, by running a low-treewidth postprocessing algorithm.

Temperature Effects
^^^^^^^^^^^^^^^^^^^

As in statistical mechanics, :math:`\beta` represents inverse temperature:
:math:`1/(k_B T)`, where :math:`T` is the thermodynamic temperature in kelvin
and :math:`k_B` is Boltzmann's constant.

The |dwave_short| QPU operates at cryogenic temperatures, nominally
:math:`15`\ |nbsp|\ mK, which can be translated to a scale parameter
:math:`\beta`. The effective value of :math:`\beta` varies from QPU to QPU and
in fact from problem to problem since the |dwave_short| QPU samples are not
Boltzmann and time-varying phenomena may affect samples. Therefore, to attain
Boltzmann samples, run the Gibbs chain for a number of iterations starting from
quantum computer samples. The objective is to further anneal the samples to the
correct temperature of interest :math:`T = 1/{\beta}`, where
:math:`\beta = 1.0`.

In the |dwave_short| software, postprocessing refines the returned solutions to
target a Boltzmann distribution characterized by :math:`\beta`, which is
represented by a floating point number without units. When choosing a value for
:math:`\beta`, be aware that lower values result in samples less constrained to
the lowest energy states. For more information on :math:`\beta` and how it is
used in the sampling postprocessing algorithm, see the :ref:`qpu_postprocessing`
section.

*   Probabilistic Sampling: RBM

    A *restricted Boltzmann machine* (RBM) is a special type of Boltzmann
    machine with a symmetrical *bipartite* structure; see
    :numref:`Figure %s <bipartite>`.

    .. figure:: ../_images/bipartite_new.png
        :name: bipartite
        :alt: Two-layer neural net comprising a layer of visible units and one
            of hidden units. Visible units are numbered V 0 through V 3. Hidden
            units are labeled H 0 through H 2. There are connections between the
            visible and hidden units, but none between units in the same layer.

        Bipartite structure of an RBM, with a layer of visible variables
        connected to a layer of hidden variables.

    It defines a probability distribution over a set of binary variables that
    are divided into visible (input), :math:`\vc{v}`, and hidden,
    :math:`\vc{h}`, variables, which are analogous to the retina and brain,
    respectively.\ [#]_
    The hidden variables allow for more complex dependencies among visible
    variables and are often used to learn a stochastic generative model over a
    set of inputs. All visible variables connect to all hidden variables, but no
    variables in the same layer are linked. This limited connectivity makes
    inference and therefore learning easier because the RBM takes only a single
    step to reach thermal equilibrium if you *clamp* the visible variables to
    particular binary states.

    .. [#]
        Analogy courtesy of Pedro Domingos in *The Master Algorithm: How the
        Quest for the Ultimate Learning Machine Will Remake Our World.*
        Basic Books, 2015.

    During the learning process, each visible variable is responsible for a
    feature from an item in the dataset to be learned. For example, images from
    the famous MNIST dataset of handwritten digits\ [#]_ have 784 pixels, so the
    RBMs that are training from this dataset require 784 visible variables. Each
    variable has a *bias* and each connection between variables has a *weight*.
    These values determine the energy of the output.

    .. [#]
        http://yann.lecun.com/exdb/mnist/

    Without the introduction of hidden variables, the energy function
    :math:`E(\vc{x})` by itself is not sufficiently flexible to give good
    models. You can write :math:`\vc{x}=[\vc{v},\vc{h}]` and denote the energy
    function as :math:`E(\vc{v},\vc{h})`.

    Then,

    .. math::
        :nowrap:

        \begin{equation}
            p(\vc{x};\theta) = p(\vc{v},\vc{h};\theta)
        \end{equation}

    and of interest is

    .. math::
        :nowrap:

        \begin{equation}
            p(\vc{v};\theta) = \sum_\vc{h} p(\vc{v},\vc{h};\theta),
        \end{equation}

    which you can obtain by marginalizing over the hidden variables,
    :math:`\vc{h}`.

    A standard training criterion used to determine the energy function is to
    *maximize* the log likelihood (LL) of the training data---or, equivalently,
    to *minimize* the negative log likelihood (NLL) of the data. Training data
    is repetitively fed to the model and corresponding improvements made to the
    model.

    When training a model, you are given :math:`D` training (visible) examples
    :math:`\vc{v}^{(1)}, ..., \vc{v}^{(D)}`, and would like to find a setting
    for :math:`\theta` under which this data is highly likely. Note that
    :math:`n^{th}` component of the :math:`d^{th}` training example is
    :math:`v_n^{(d)}`.

    To find :math:`\theta`, maximize the likelihood of the training data:

    *   The likelihood is :math:`L(\theta) = \prod_{d=1}^D p(v^{(d)};\theta)`
    *   It is more convenient, computationally, to maximize the log likelihood:

    .. math::
        :nowrap:

        \begin{equation}
            LL(\theta)=log(L(\theta))=\sum_{d=1}^D {\log}p(v^{(d)};\theta).
        \end{equation}

    You can use the *gradient descent* method to minimize the
    :math:`NLL(\theta)`:

    *   Starting at an initial guess for :math:`\theta` (say, all zero values),
        calculate the gradient (the direction of fastest improvement) and then
        take a step in that direction.
    *   Iterate by taking the gradient at the new point and moving downhill
        again.

    To calculate the gradient at a particular :math:`\theta`, evaluate some
    expected values: :math:`E_{p(\vc{x};\theta)} f(\vc{x})` for a set of
    functions :math:`f(\vc{x})` known as the sufficient statistics. The expected
    values cannot be determined exactly, because you cannot sum over all
    :math:`2^N` configurations; therefore, approximate by only summing over the
    most probable configurations, which you can obtain by sampling from the
    distribution given by the current :math:`\theta`.

*   Energy-Based Models

    Machine learning with energy-based models (EBMs) minimizes an objective
    function by lowering scalar energy for configurations of variables that best
    represent dependencies for probabilistic and nonprobabilistic models.

    For an RBM as a generative model, for example, where the gradient needed to
    maximize log-likelihood of data is intractable (due to the partition
    function for the energy objective function), instead of using the standard
    Gibbs's sampling, use samples from the |dwave_short| system. The training
    will have steps like these: a. Initialize variables. b. Teach visible nodes
    with training samples. c. Sample from the |dwave_short| system. d. Update
    and repeat as needed.

*   Support Vector Machines

    Support vector machines (SVM) find a hyperplane separating data into classes
    with maximized margin to each class; structured support vector machines
    (SSVM) assume structure in the output labels; for example, a beach in a
    picture increases the chance the picture is of a sunset.

*   Boosting

    In machine learning, *boosting* methods are used to combine a set of simple,
    "weak" predictors in such a way as to produce a more powerful, "strong"
    predictor.

Generative and Discriminative Modeling
--------------------------------------

*Generative* modelling is concerned with the modeling the joint distribution of
random variables :math:`X, Y`, whereas *discriminative* modeling is concerned
with the conditional distribution of :math:`X \mid Y`.

Generative modelling with annealing quantum computers is modeled by Boltzmann
machines and quantum Boltzmann machines [Ami2018]_, [Ack1985]_---families of
learnable probability models over binary data.\ [#]_

Discriminative modelling with annealing quantum computers can be modelled using
both Boltzmann machines and quantum neural networks [Kak1995]_, [Chr1995]_.

.. [#]
    Closely related to Boltzmann machines are the exponential family [Wai2008]_
    Markov random fields [Dob1968]_, and Ising models [Isi1925]_.

.. _boltzmann_machines_quantum_generalization:

Boltzmann Machines and its Quantum Generalization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Boltzmann machines model high-dimensional binary data. A Boltzmann machine is
defined by its probability mass function,

.. math::

    \begin{align}
        P_\theta(x) &= \frac{1}{Z(\theta)}\exp\{\langle T(x) ,
            \theta \rangle \} \\
        Z(\theta) & = \sum_{s \in \{\pm 1\} ^n}\exp\{\langle T(s) ,
            \theta \rangle \},
    \end{align}

where :math:`x \in \{\pm 1\}^n` for some dimension
:math:`n`, :math:`\theta \in \mathbb{R}^{n+n(n-1)/2}` are the model parameters,
and :math:`T: \{\pm 1\}^n \mapsto \{\pm 1\}^{n+n(n-1)/2}` is the sufficient
statistic [Wai2008]_ of the model; i.e.,

.. math::

    \begin{equation}
        T(x) = \begin{bmatrix}
            x_1 & x_2 & \dots & x_n & x_1x_2 & x_1 x_3 & \dots & x_2 x_3 &
            \dots & x_{n-1} x_n
        \end{bmatrix}^\intercal.
    \end{equation}

More generally, given a graph :math:`G=(V, E)`, define a graph-restricted
Boltzmann machine specified by :math:`G` to have sufficient statistics defined
by,

.. math::

    \begin{align}
        T(x) & =
        \begin{bmatrix}
            x_{v_1} & \dots & x_{n} & z_{e_1} & \dots & z_{e_m},
        \end{bmatrix}^\intercal,
    \end{align}

where :math:`v_i \in V` for :math:`i \in \{1, \dots, \lvert V\rvert\}`,
and :math:`z_{e_i} = x_{e_{i_1}}x_{e_{i_2}}`,
:math:`e_i = (e_{i_1}, e_{i_2}) \in E` for
:math:`i \in \{1, \dots, \lvert E \rvert \}`, and
:math:`\theta \in \mathbb{R}^{\lvert V \rvert + \lvert E \rvert}`.

When only a subset of variables are observed, denoted :math:`v`, the remaining
unobserved variables are referred to as *hidden units* :math:`h`.

The marginal distribution of observed variables can be far more expressive due
to the marginalization of hidden units, i.e.,

.. math::

    \begin{align}
        P_\theta^\text{m}(v) & = \sum_{h} P_\theta(x=(v, h)).
    \end{align}

The inclusion of hidden units can potentially introduce challenges to be
discussed in the :ref:`generative_discriminative_conclusion` section.

Given a binary dataset, one can fit a Boltzmann machine to the model using, for
example, maximum likelihood estimates [Cas2002]_.

However, the maximum likelihood estimate for a Boltzmann machine is nontrivial
to evaluate. The standard approach [Hin2002]_, [Ack1985]_ is to optimize the
model using stochastic gradient descent [Boy2004]_.

The gradient of the log likelihood function itself is intractable:

.. math::

    \begin{align}
        \nabla_\theta \log P_\theta(v) & = T(v) - \mathbb{E}\left[ T(X)\right].
    \end{align}

Its intractability stems from the expectation term, with respect to the model,
which requires an evaluation of the partition function :math:`Z(\theta)`.

This motivates the need for Monte Carlo algorithms [Rob2004]_; i.e., sample
approximations of the expectation.

Sampling from Boltzmann machines is notoriously difficult and is where the
annealing quantum computer excels.

The restricted Boltzmann machine [Hin2002]_, [Smo1986]_ is a special case of the
graph-restricted Boltzmann machine in which the graph is a complete bipartite
graph. Furthermore, partial observations are restricted to be on one and only
one partite set of the graph. These modelling constraints were motivated by the
need for an efficient training algorithm [Hin2002]_, [Hin2010]_.

Quantum Boltzmann machines offer a generalization of Boltzmann machines and are
defined by Hamiltonians.

In practice today (2026, the time of writing), at D-Wave the annealing quantum
computer is utilized as an approximate sampler of quantum Boltzmann machines.
Thus the following introductory definition only serves to satisfy one's
curiosity. Refer to [Ami2018]_ for a complete treatment.

In D-Wave's implementation, these Hamiltonians take the form:\ [#]_

.. math::

    \begin{align}
        H   & = \sum_{i \in V} h_i Z_i + \sum_{(i, j)\in E} J_{i,j} Z_i Z_j +
                \sum_{i\in V} \gamma_i X_i \\
        Z_i & = \left( \bigotimes_{j=1}^{j=i-1} I_2 \right)
                Z \left( \bigotimes_{j=i+1}^{j=\lvert V \rvert} I_2 \right) \\
        X_i & = \left( \bigotimes_{j=1}^{j=i-1} I_2 \right)
                X \left( \bigotimes_{j=i+1}^{j=\lvert V \rvert} I_2 \right) \\
        I_2 & = \begin{bmatrix}
                    1 & 0 \\ 0 & 1
                \end{bmatrix} \\
        X   & = \begin{bmatrix}
                    0 & 1 \\ -1 & 0
                \end{bmatrix} \\
        Z   & = \begin{bmatrix}
                    1 & 0 \\ 0 & -1
                \end{bmatrix}.
    \end{align}

The product :math:`\bigotimes` denotes the Kronecker product [Str2012]_.
The probability measure is now defined by the diagonal elements of the density
matrix,

.. math::

    \begin{align}
        \rho & = \frac{1}{\mathcal{Z}}\exp\{-H\} \\
        \mathcal{Z} & = \Tr\left[\exp\{-H\}\right].
    \end{align}

For intuition, consider a diagonal Hamiltonian---diagonal Hamiltonian
(:math:`\gamma_i = 0` for all :math:`$i`) corresponds to the classical definition of a
Boltzmann machine. By construction of the Hamiltonian, the summation over
:math:`Z_i` and :math:`Z_iZ_j` matrices result in a matrix whose diagonal
entries correspond to each of the :math:`2^{\lvert V\rvert}` binary strings'
probability (when normalized).
When qubits are measured in the :math:`z`-basis, or with respect to each
:math:`Z_i`, binary strings are observed with their corresponding probabilities.
The quantum Boltzmann machine can be trained using the same expressions or
quantities as in classical Boltzmann machines, albeit based on a lower bound of
the log likelihood [Ami2018]_.

.. [#]

    The Hamiltonian is time-dependent but, motivated by ease of exposition, the
    dependence on time has been omitted here. For a more complete treatment,
    see, for example, the :ref:`qpu_quantum_annealing_intro` section.

Quantum Boltzmann Machines: Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applying arbitrary graph-restricted Boltzmann machines to real-world
applications raises at least two challenges.

1)  Data are seldom natively binary. For example, image data are continuous and
    text data are categorical.
2)  Correlations are not guaranteed to be local and quadratic even when data are
    binary, thereby limiting the expressivity and goodness-of-fit of
    graph-restricted Boltzmann machines.

Identifying a mapping of input variables to model variables is at least as
difficult as the quadratic assignment problem [Law1963]_---an NP-hard problem.
The problem can be formulated as maximizing the likelihood function over both
mappings and parameters.

Both challenges can be addressed via several approaches.
One solution is to leverage variants of (variational) autoencoders [Sch2015]_,
[Bal1987]_, [Kin2013]_, for example, [Rol2016]_, [Li2016]_, [Zha2017]_,
[Van2017]_, [Jan2016]_, [Kho2018]_.
The idea underpinning these approaches is to enforce a discrete-latent-space
constraint in the model.

Defining variational autoencoders [Kin2013]_ with discrete latent variables is
not a problem because the reparameterization trick [Kin2013]_ is not limited to
real-valued random variables [Rol2016]_.
However, a problem arises in training such a discrete model via gradient
descent: gradients are zero for discrete random variables. [Rol2016]_ addresses
this training problem by augmenting binary latent variables with real-valued
random variables. The auxiliary variables are equipped with distributions
conditioned on the binary variables, resulting in nonzero gradients in
backpropagation [Sch2015]_.

For example, consider the random variable :math:`Z \mid B` where :math:`B` is a
Bernoulli random variable and :math:`Z \mid B = 0` is :math:`0`, and
:math:`Z \mid B = 1 \sim \text{Exponential}(1)`.

Using the inverse conditional distribution function (CDF) sampling method
[Rob2004]_, you have,

.. math::

    \begin{align}
        u & \sim \text{Uniform}(0, 1) \\
        x & \in [0, 1] \\
        f(x, u) & = \begin{cases}
                        0  & u > x \\
                        \log \left[ \frac{u+x-1}{x}(e-1) +1	\right] & u \leq x
                    \end{cases},
    \end{align}

where :math:`u` is the *noise variable*, :math:`x` is the encoded data input,
and the second case for :math:`f` comes from the inverse CDF of the exponential
distribution. Because :math:`f` is differentiable with nonzero gradients, one
can meaningfully backpropagate through the discretization layer.

Another approach to modelling data with binary random variables is to use
approximations proposed by [Jan2016]_, [Mad2016]_. The approach is based on a
limiting argument with annealed Gumbel distributions combined with a
straight-through estimator [Ben2013]_,

.. math::

    \begin{align}
        z_i & = \frac{\exp (\frac{\log (\pi_i ) + g_i}{\tau})}
        {\sum_j \exp (\frac{\log (\pi_j ) + g_j}{\tau})} \\
        z & = \begin{bmatrix}
                z_1 & z_2 & \dots & z_K
              \end{bmatrix} \\
        i & \in \{1, \dots, K\},
    \end{align}

where :math:`K` represents the number of discrete values (:math:`K=2` for
binary) and :math:`\tau` is an annealing parameter. When :math:`\tau \to 0`,
:math:`z` becomes a one-hot vector; i.e., :math:`z_i = 1` for some index
:math:`i` and :math:`0` for all other indices not equal to :math:`i`.

In a recent molecular-design application, [Kun2026]_ leveraged ideas from the
neural hash function of [Eri2015]_ to discretize data. The binarization strategy
applied in [Eri2015]_ penalizes the encoding network, during training, when
latent variables deviate from :math:`\pm 1`. That is, the following loss
function is added as a regularizer to the neural network training objective:

.. math::

    \begin{equation}
        L_\text{quant}(z) = \lvert \lvert z - \text{sign}(z)\rvert \rvert ^2.
    \end{equation}

Finally, *REINFORCE* [Wil1992]_, [Gly1990]_ can also be used to backpropagate
gradients through discretization layers,

.. math::

    \begin{equation}
        \nabla_x \mathbb{E}_Z[f(Z)] = \mathbb{E}_Z[f(Z)\nabla_x \log p_x(Z)].
    \end{equation}

A drawback of REINFORCE is that the estimator is effectively computed by
expressions akin to finite differences, resulting in high variance. Bespoke
variance-reduction techniques [Rob2004]_ are often required to stabilize the
estimator. See [Jan2016]_ for a summary of relevant variance-reduction
techniques based on control variates.

Boltzmann machines can also be used as discriminative models or, equivalently,
used for modelling conditional distributions :math:`Y \mid X`. See [Cal2019]_
for an applied example using annealing quantum computers. Training of Boltzmann
machines for discriminative tasks is no different from training generative
models. Variables :math:`X` and :math:`Y` are both assigned to variables of a
Boltzmann machine during training.\ [#]_

At inference, however, only variables associated with :math:`X` are fixed at
their observed value and predictions are computed by sampling :math:`Y\mid X`.
In practice, discriminative modelling with sparse graph-restricted Boltzmann
machines poses a subtle variable-assignment problem to be discussed in the
:ref:`generative_discriminative_conclusion` section.

.. [#]
    This assignment or mapping of variables can be performed via an encoder or
    by manual assignment.

Quantum Neural Networks
^^^^^^^^^^^^^^^^^^^^^^^

Quantum neural networks [Kak1995]_, [Chr1995]_ are families of functions
evaluated via parameterized quantum systems.\ [#]_
That is, a quantum neural network, :math:`f_\theta`, parameterized by
:math:`\theta` is defined as,

.. math::

    \begin{equation}
        f_\theta(x) = \langle \psi_0 \lvert U^\dagger_\theta(x) \hat F
            U_\theta(x) \rvert \psi_0 \rangle,
    \end{equation}

where :math:`x \in \mathbb{R}^d` represents input data, :math:`U_\theta`
represents a unitary transformation, :math:`U_\theta^\dagger` its conjugate
transpose, :math:`\lvert \psi_0 \rangle` is an initial state of the system,
:math:`\langle \psi_0 \rvert` its conjugate transpose, and :math:`\hat F` is a
quantum observable.

Essentially, a quantum neural network is a parameterized function whose outputs
are expected values of the quantum system. A difficulty in applying quantum
neural networks to real-world applications is in training.

Evaluating or even approximating gradients of a loss function with respect to
the network parameters is nontrivial due to the intractability of densities and
expectations. Much of the literature on training quantum neural networks has
been dedicated to gate-model systems, using, for example, the parameter-shift
rule and its generalizations [Mit2018]_, [Wie2022]_.

A more relevant approach to training quantum annealing-based neural networks is
via equilibrium propagation [Sce2017]_, a gradient-estimation technique
originally introduced in the context of training energy-based models [teh2003]_.
Generalizations to quantum equilibrium propagation have been proposed in
[Mas2025]_, [Sce2024]_. The parameter update rule can be described as follows.

Consider an example Hamiltonian of the form,

.. math::

    \begin{equation}
        H(x) = \sum_{i, j} J_{i,j}(x) Z_iZ_j + \sum_i h_i(x) Z_i,
    \end{equation}

where :math:`Z_i` are as defined in the
:ref:`boltzmann_machines_quantum_generalization` section, :math:`J_{i,j}, h_i`
are scalar functions of the input data :math:`x`; that is
:math:`h_i: \mathbb{R}^d \mapsto \mathbb{R}` and
:math:`J_{i, j}:\mathbb{R}^d \mapsto \mathbb{R}`. Note, :math:`h_i` and
:math:`J_{i, j}` include constant functions independent of :math:`x`.
Equilibrium propagation approximates the gradients by introducing another
Hamiltonian, a nudge Hamiltonian, defined as,

.. math::

    \begin{equation}
        H_\text{nudge}(x, y) = H(x) - \sum_i \tilde h_i(y) Z_i,
    \end{equation}

where :math:`y \in \mathbb{R}^{d_2}` are the desired network outputs, and
:math:`\tilde h_i` is similarly defined to :math:`h`,
:math:`\tilde h_i: \mathbb{R}^d \mapsto \mathbb{R}`. The gradient is expressed
as,

.. math::

    \begin{equation}
        \nabla_\theta C(\theta, (x, y)) = \mathbb{E}_S[T(S)] -
        \mathbb{E}_{S'}[T(S')],
    \end{equation}

where :math:`S, S'` are spin-valued random vectors with distribution prescribed
by :math:`H(x), H_\text{nudge}(x, y)` respectively, :math:`\theta = (h, J)` (as
defined in the :ref:`boltzmann_machines_quantum_generalization` section),
:math:`T` is the sufficient statistic of :math:`H` (as defined in the
:ref:`boltzmann_machines_quantum_generalization` section), and
:math:`C: \mathbb{R}^{|V| + |E|} \times \mathbb{R}^d \times \mathbb{R}^{d_2} \mapsto \mathbb{R}`
is a differentiable cost function (with respect to the first argument).
The gradient, expressed as a difference of expectations, can be readily
estimated by sampling from a quantum computer.

An inefficiency of the approach is the need to sample from two separate
distributions for one gradient computation.

The applicability of quantum annealing-based neural networks has been
demonstrated in MNIST [Den2012]_ image classification tasks [Zha2025]_,
[Lay2024]_. Notably, [Lay2024]_ exploited the hardware topology of quantum
annealers [Boo2019]_ ,[Boo2021]_ to implement a convolutional neural network
[Fuk1979]_, [Sch2015]_.

A closely related approach is quantum reservoir computing [Kor2024]_.
Informally but practically, quantum reservoir computing equates to evaluating an
untrained quantum neural network, as an activation function, followed by a
trained linear function. The difficulty in applying quantum reservoirs is the
domain-expertise required in defining a base Hamiltonian and a mapping of inputs
to the base Hamiltonian.

.. [#]
    "Quantum neural networks" are often used synonymously with "variational quantum circuits" or
    "parameterized quantum circuits".

.. _generative_discriminative_conclusion:

Opportunities and Limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Boltzmann machines and quantum neural networks provide powerful frameworks for
generative and discriminative modelling using annealing quantum computers.
Naturally, these models can be readily inserted
into---or substitute for---subcomponents of existing models: for example,
linear layers, activation functions, and attention modules. Thus there is
interest in identifying areas for which practical benefits can be realized with
quantum annealing-based machine learning methods.

This section considers three performance indicators in which a annealing quantum
computer has potential to improve upon classical baselines.

1)  Runtime
2)  Model complexity
3)  Power consumption

First, a description of timing information of D-Wave's annealing quantum
computers at a coarsened but practically relevant granularity.

Quantum annealing protocols can operate in time spans as short as nanoseconds to
as long as milliseconds. Once the protocol has run its course, reading out the
classical states takes on the order of hundreds of microseconds. The bottleneck
in this protocol is in programming the Hamiltonian to the annealing quantum
computer, which is on the order of tens of milliseconds.

Because D-Wave's annealing quantum computers are accessed via |cloud_tm|_, a
quantum cloud platform, there may be additional network latencies in the order
of hundreds of milliseconds. In principle, communication latency can be
mitigated and programming time optimized such that the effective processing time
is on the order of tens of milliseconds.
A comprehensive breakdown of timing information is in the
:ref:`qpu_operation_timing` section.

To put this timing into context, consider both generative and discriminative
modelling tasks.

In a generative model setup where annealing quantum computers are utilized as
Boltzmann machine samplers, the natural comparators are Monte Carlo samplers
such as the Metropolis algorithm [Met1953]_ [Rob2004]_. Metropolis algorithm
sampling times can range from hundreds of milliseconds to seconds when sampling
from the same Boltzmann machine as the annealing quantum computer for an
equivalent effective sample size [Vat2021]_.

For complex models, more sophisticated and compute-intensive methods such as
parallel tempering [Gey1991]_ and annealed importance sampling [nea2001]_ are
required.

Other alternatives include autoregressive models [Van2016]_, [Vas2017]_,
[Gu2024]_, which are model-dependent but generally slow due to repeated neural
network evaluations.

In a discriminative model where an annealing quantum computer is utilized as a
quantum Boltzmann machine or a quantum neural network, it is sensible to
consider classical neural network module runtimes for reference. For example, a
self-attention [Vas2017]_ module requires approximately half a millisecond
to evaluate a sequence of length :math:`1024` by :math:`1024` dimensions using a
modern graphical processing unit (GPU; NVIDIA L4).\ [#]_

Flash attention [Dao2022]_---a hardware-optimized attention module---reported
runtimes of :math:`1`\--\ :math:`10`\ s of milliseconds (including
backpropagation) for inputs of length ranging from :math:`1000`\ s to
:math:`8000`\ s. If, however, one insists on sampling from the quantum neural
network via, say, classical simulations and approximations, then annealing
quantum computers are likely to perform favorably.

While restricted Boltzmann machines are universal approximators [Ler2008]_,
[Mon2020]_, D-Wave's annealing quantum computers are implemented with sparse
connectivity and are thus limited in their expressivity.
The |dwave_5kq_tm| system and |adv2_tm| system's topologies are defined by the
:term:`Pegasus` and :term:`Zephyr` family of graphs respectively [Boo2019]_,
[Boo2021]_. Each vertex represents a qubit, and each edge represents a coupler.
In other words, these graphs are used to define graph-restricted Boltzmann
machines described in the :ref:`boltzmann_machines_quantum_generalization`
section.

The two families of graphs are visualized in the :ref:`qpu_topologies` section.
A key observation relevant to the discussion of expressivity is the locality of
interactions. In both family of graphs, edges are locally connected in a
two-dimensional plane; long range interactions do not exist. These locality
constraints motivate techniques for maximizing expressivity, which are discussed
next.

Several approaches exist to increase model expressivity.

1)  Minor embeddings [Cho2008]_: represent logical variables by chaining
    multiple physical qubits through strong pairwise interaction terms.
2)  Hidden units: marginalize a distribution over its hidden units.
3)  Optimize variable-to-qubit mappings.

Minor embedding can increase connectivity and introduce long-range interactions,
but introduces its own challenges such as early freezeout and chain
breakages.\ [#]_

Hidden units can be interpreted similarly to embeddings where the embeddings are
learned implicitly. However, this also introduces complexity to training
methods. For example, when using tractable closed-form expressions for
marginalization, the effective inverse temperature must be estimated [Ray2016]_.
When using sample approximations for marginalization, multiple invocations of
the annealing quantum computer will be required.

The competitive runtime and model expressivity is further complemented by a
constant power consumption [Dwave8]_ independent of model complexity.
This constant power consumption is because almost all power drawn from D-Wave's
systems goes toward cryogenic refrigeration; the bulk of the computation is
analog. This suggests model complexity can be further enhanced through a liberal
composition of quantum Boltzmann machines and quantum neural networks.

.. [#]
    The implementation is a compiled PyTorch module [Pas2019]_.

.. [#]
    See the :ref:`qpu_qa_freezeout` and
    :ref:`chain breaks <qpu_embedding_intro_chains>` sections.

Code Examples
-------------

*   `Qboost <https://github.com/dwave-examples/qboost>`_ is an example of
    formulating boosting as an optimization problem for solution on a QPU.

Papers
------

General machine learning and sampling:

*   [Bia2010]_ discusses using quantum annealing for machine learning
    applications in two modes of operation: zero-temperature for optimization
    and finite-temperature for sampling.
*   [Ben2017]_ discusses sampling on the |dwave_short| system.
*   [Inc2022]_ presents a QUBO formulation of the Graph Edit Distance problem
    and uses quantum annealing and variational quantum algorithms on it.
*   [Muc2022]_ proposes and evaluates a feature-selection algorithm based on
    QUBOs.
*   [Per2022]_ presents a systematic literature review of 2017--21 published
    papers to identify, analyze and classify different algorithms used in
    quantum machine learning and their applications.
*   [Vah2017]_ discusses label noise in neural networks.

RBMs:

*   [Ada2015]_  describes implementing an RBM on the |dwave_short| system to
    generate samples for estimating model expectations of deep neural networks.
*   [Dum2013]_ discusses implementing an RBM using physical computation.
*   [Hin2012]_ is a tutorial on training RBMs.
*   [Kor2016]_ benchmarks quantum hardware on Boltzmann machines.
*   [Mac2018]_ discusses mutual information and renormalization group using
    RBMs.
*   [Rol2016]_ describes discrete variational autoencoders.
*   [Sal2007]_ describes RBMs used to model tabular data, such as users' ratings
    of movies.
*   [Vin2019]_ describes using |dwave_short| quantum annealers as Boltzmann
    samplers to perform quantum-assisted, end-to-end training of QVAE.

Energy-Based Models:

*   [Lec2006]_ describes EBMs.

Support Vector Machines:

*   [Boy2007]_ gives a concise introduction to subgradient methods.
*   [Wil2019]_ gives a method to train SVMs on a |dwave_2kq| system, and applies
    it to data from biology experiments.

Boosting:

*   [Nev2012]_ describes the Qboost formulation.

.. _qpu_stating_problems_map_coloring:

Map Coloring
============

Map coloring is an example of a :ref:`concept_constraint_satisfaction_problem`
(CSP). CSPs require that all a problem’s variables be assigned values, out of a
finite domain, that result in the satisfying of all constraints. The
map-coloring CSP is to assign a color to each region of a map such that any two
regions sharing a border have different colors.

The :ref:`qpu_reformulating_example_map` section in the :ref:`qpu_reformulating`
section is an example of map coloring on the |dwave_short| system.

Code Examples
-------------

*   :ref:`opt_example_kerberos_map`

    Demonstrates an out-of-the-box use of a hybrid sampler solving a problem of
    arbitrary structure and size.
*   :ref:`opt_example_dqm_map`

    Demonstrates the hybrid discrete quadratic model (DQM) solver available in
    the Leap service.
*   :ref:`qpu_example_mapcoloring`

    Demonstrates solving a map-coloring CSP on a QPU.
*   `Map-Coloring CSP <https://github.com/dwave-examples/map-coloring>`_

    Demonstrates the use of |dwave_short| QPU solvers to solve a map-coloring
    problem.

Papers
------

[Dwave4]_ describes solving a map coloring problem on a QPU.

.. _qpu_stating_problems_protein_folding:

Material Simulation
===================

One promise of quantum computing lies in harnessing programmable quantum devices
for practical applications such as efficient simulation of quantum materials and
condensed matter systems; for example, simulation of geometrically frustrated
magnets in which topological phenomena can emerge from competition between
quantum and thermal fluctuations.

Protein folding refers to the way protein chains structure themselves in the
context of providing some biological function. Although their constituent
amino acids enable multiple configurations, proteins rarely misfold (such
proteins are a cause of disease) because the standard configuration
has lower energy and so is more stable.

Papers
------

*   [Kin2021]_ report on experimental observations of equilibration in
    simulation of geometrically frustrated magnets.
*   [Mni2021]_ reduces the molecular Hamiltonian matrix in Slater determinant
    basis to determine the lowest energy cluster.
*   [Per2012]_ discusses using the |dwave_short| system to find the
    lowest-energy configuration for a folded protein.
*   [Tep2021]_ uses a quantum-classical solver to calculate excited electronic
    states of molecular systems. Note that the paper uses the
    `qbsolv <https://docs.ocean.dwavesys.com/projects/qbsolv>`_ package, which
    has since been discontinued in favor of the hybrid solvers available in the
    Leap service and the
    :ref:`dwave-hybrid <index_hybrid>` package.

.. _qpu_stating_problems_scheduling:

Scheduling
==========

The well-known
`job-shop schedule <https://en.wikipedia.org/wiki/Job_shop_scheduling>`_
problem is to maximize priority or minimize schedule length (known as a
*makespan*\ , the time interval between starting the first job and finishing the
last) of multiple jobs done on several machines, where a job is an ordered
sequence of tasks performed on particular machines, with constraints that a
machine executes one task at a time and must complete started tasks.

Code Examples
-------------

*   :ref:`Constrained Scheduling <qpu_example_scheduling>`

    Shows new users how to formulate a constraint satisfaction problem (CSP)
    using Ocean tools and solve it on a |dwave_short| QPU solver.
*   `Job-Shop Scheduling <https://github.com/dwave-examples/job-shop-scheduling>`_

    An implementation of [Ven2015]_ for |dwave_short| QPU solvers.
*   `Employee Scheduling <https://github.com/dwave-examples/employee-scheduling>`_

    A formulation of a discrete quadratic model (DQM) for solution using the
    hybrid DQM solver in the Leap service.
*   `Nurse Scheduling <https://github.com/dwave-examples/nurse-scheduling>`_

    An implementation of [Ike2019]_ that forms a QUBO for solution by the hybrid
    BQM solver in the Leap service.

Papers
------

*   [Ike2019]_ describes an implementation of nurse scheduling.
*   [Kur2020]_ describes an implementation of job-shop scheduling on a
    |dwave_short| QPU solver.
*   [Liu2020]_ proposes to use deep reinforcement learning on job-shop
    scheduling.
*   [Ven2015]_ describes an implementation of job-shop scheduling on the
    |dwave_short| system, which includes formulating the problem, translating to
    QUBO, and applying variable reduction techniques. It also talks about direct
    embedding of local constraints.

.. _qpu_stating_problems_traffic_flow:

Traffic Flow
============

One form of the traffic-flow optimization problem is to minimize the travel time
of a group of vehicles from their sources to destinations by minimizing
congestion on the roads being used.

Papers
------

*   [Flo2017]_ describes work done by Volkswagen to map a traffic-flow
    optimization problem on the |dwave_short| system.
*   [Tam2022]_ formulates a vehicle-routing problem as a QUBO to solve
    traffic-congestion problems.

