SwarmOps - Heuristic Optimization for Python.
=============================================

SwarmOps for Python implements the following heuristic optimizers which do not
use the gradient of the problem being optimized:

* Particle Swarm Optimization (PSO)
* Differential Evolution (DE)
* Many Optimizing Liaisons (MOL) - A simple variant of PSO
* Pattern Search (PS)
* Local Unimodal Sampling (LUS)

All these optimizers perform minimization. If you need to maximize a problem
then you simply return the negated value in your fitness function (aka. cost-
or error-function).

The PS and LUS optimizers only require few iterations and are therefore useful
for problems that are very time-consuming to compute. PSO, MOL and DE usually
require many more iterations but can also sometimes find better solutions.

Multiple optimization runs can be performed using the MultiRun-class, which
also supports printing various statistics, plotting a trace of the fitness,
and refining the best-found solution using the
[L-BFGS-B](https://en.wikipedia.org/wiki/Limited-memory_BFGS) optimizer from SciPy.

Parallel execution is also supported in different ways, see below.

Installation
------------

SwarmOps for Python can be installed in different ways.

### Zip-file

To install the source-code manually, download the
[Zip-file](https://github.com/Hvass-Labs/swarmops/archive/master.zip)
and unpack it into a directory of your choice.

### pip

To install swarmops using pip, type the following in the Linux terminal:

    pip install git+https://github.com/Hvass-Labs/swarmops.git

This installs swarmops in the current Python environment.

### virtualenv

You may want to install swarmops in a virtual environment so it does
not interfere with other parts of your Python installation. Type
the following in a Linux terminal:

    virtualenv ~/dev/swarmops-env/
    cd ~/dev/swarmops-env/
    pip install git+https://github.com/Hvass-Labs/swarmops.git

Now you can import swarmops in Python files from inside the directory
~/dev/swarmops-env/

### Github

To install directly from Github type the following in a Linux terminal:

    git clone https://github.com/Hvass-Labs/swarmops.git

This creates a directory named swarmops which contains all the source-code.

Importing in Your Project
----------------------

There are different ways of importing and using swarmops in your own project.

Assume you have installed swarmops in the directory ~/dev/swarmops/
and you want to use it in a project located in ~/dev/my-project/

### Symbolic Link

A simple way of including swarmops in your project is to create
a symbolic link by typing the following in a Linux terminal:

    ln -s ~/dev/swarmops/swarmops/ ~/dev/my-project/swarmops/

This creates ~/dev/my-project/swarmops/ which really points
to the directory ~/dev/swarmops/swarmops/ and allows you to
import swarmops from Python source-code files inside ~/dev/my-project/ 

### Environment Path

A simple way of making swarmops available to Python in general,
is to add the directory to the PYTHONPATH environment variable,
by typing the following in a Linux terminal:

    export PYTHONPATH=~/dev/swarmops/:$PYTHONPATH

This allows you to import swarmops from any Python source-code.
The line can be added to ~/.bashrc so it works permanently.

### virtualenv

If you want to use a virtual environment, you write the following
in a Linux terminal:

    virtualenv ~/dev/my-project/
    cd ~/dev/my-project/
    pip install git+https://github.com/Hvass-Labs/swarmops.git

This allows you to use swarmops from Python source-code inside
the directory ~/dev/my-project/

### Importing

Whichever of the above methods you used, you can now import swarmops
from inside the my-project directory.

For example, you can make a file called ~/dev/my-project/test.py
with the following content:

    from swarmops.DE import DE
    from swarmops.Problem import Rosenbrock

    print(DE.name_full)

    problem = Rosenbrock(dim=3)

    result = DE(problem=problem, max_evaluations=10000)

    print(result.best)
    print(result.best_fitness)

This is supposed to execute a single optimization run using
Differential Evolution (DE) on the Rosenbrock problem in 3
dimensions, using 10000 fitness evaluations.

You can run the program by entering:

    python test.py

The output should be something like this (the numbers may be somewhat
different because they are random):

    Differential Evolution (DE/Rand/1/Bin)
    [ 1.00000295  1.00000462  1.00000635]
    1.02338996528e-09

Optimization Demo
-----------------

A short demo for optimizing benchmark problems is found in demo-optimize.py
The easiest way to learn how to use SwarmOps for optimizing a problem is to
study and modify this file. The source-code is generally well-documented.

To execute the file, type the following in a Linux terminal in the directory
where you installed swarmops:

    python demo-optimize.py

Meta-Optimization Demo
----------------------

Meta-optimization is the tuning of an optimizer's control / behavioural
parameters by using another overlaying optimizer. This may greatly
improve optimization performance. SwarmOps supports meta-optimization
and a short demo is found in the file demo-meta-optimize.py

To execute the file, type the following in a Linux terminal in the directory
where you installed swarmops:

    python demo-meta-optimize.py

Requirements
------------

SwarmOps requires NumPy. Additionally, if you want to use L-BFGS-B to refine
the best-found solution, then you also need SciPy. And if you want to plot
the fitness-trace, then you also need matplotlib.

SwarmOps was developed using
[Anaconda 3.X](https://www.continuum.io/downloads) but it should also
work with other Python installations as long as you have at least NumPy
installed, and SciPy and matplotlib if you require them.

However, the parallel execution apparently does not work with Python 2.7,
so you must use Python 3.X if you want to use parallel execution in SwarmOps.

Unit Tests
----------

Unit-tests / nose-tests are found in test_all.py which test the optimizers
with thousands of different configurations. The purpose is to test whether
exceptions are raised somewhere and if the output is of the expected data-type.
The optimization results are not tested for correctness because these
optimizers are stochastic in nature and will always give different results.
This is discussed in more detail in the test_all.py file. This means you should
also manually inspect the output of demo-optimize.py and demo-meta-optimize.py
so as to assess whether the optimization results are satisfactory.

Parallel Execution
------------------

SwarmOps supports parallel execution in 3 ways depending on your needs:

1.  The MultiRun-class can execute several optimization runs in parallel. This is
    usually the best way because the overhead of the parallel execution is very
    low so there is a near-linear speed-up depending on the number of CPU cores.
    However, if you only want to perform a single optimization run then you cannot
    use this way of making the execution parallel.

2.  The optimizers PSO, MOL and DE can execute in parallel. This is done by
    running the fitness evaluations in parallel for each iteration of the optimizer.
    However, the overhead is significant, especially on Windows, so this way of
    doing parallel execution should only be used if
    (A) you only want to perform a single optimization run, and
    (B) your fitness function is slow to compute.

3.  You can make your fitness function execute in parallel by yourself and then
    use the optimizers from SwarmOps in non-parallel mode.

Parallel execution apparently does not work in Python 2.7, please use Python 3.x.

Parallel Meta-Optimization
--------------------------

SwarmOps supports running meta-optimization in parallel with some limitations.
The list of the best control parameters found during meta-optimization will be empty.
Similarly the best-found solutions for the optimization problems will also be empty.

If these results are important to you, then you should run meta-optimization in non-parallel
mode, and instead run several instances of your program at the same time. Then you
will get parallel execution (assuming your CPU has multiple cores) and you will
still get the list of the best-found control parameters and solutions to the problems.

This design choice was made because Python's parallel implementation is a bit peculiar
and it would have required significant changes to MetaOptimize.py to make it work,
which would have made the source-code much more complicated, while the work-around is
quite simple.

Constraints
-----------

SwarmOps for Python only implements boundary constraints. If this is insufficient
for your needs, then a suggestion is to 'repair' the candidate solutions before
you calculate the fitness of a problem. For example, if your fitness function is
called with x, and you must ensure that the elements of x sum to one, then you
would simply 'repair' x inside your fitness function by calculating
z = x / np.sum(x) and then calculating the fitness for z instead of x, and use a
special case if x sums to zero.

SwarmOps for C# supports more general constraints.

Convergence Tests
-----------------

SwarmOps does not implement convergence tests. The reason is that the optimizers
may appear to have stagnated for hundreds or even thousands of iterations, and
then suddenly they find an improvement. Instead you should set the max number of
fitness evaluations and optimization runs that you can afford to run in the available
time.

Other Programming Languages
---------------------------

SwarmOps is also implemented in other programming languages such as
C#, C, Java, and Matlab. Especially the C# and Java versions have more
features than the Python version and will execute much faster for
meta-optimization.

[www.hvass-labs.org/projects/swarmops](http://www.hvass-labs.org/projects/swarmops/)

License
-------

Copyright (C) 2003-2016 Magnus Erik Hvass Pedersen. See LICENSE.txt for details.

Version History
---------------

V. 1.0  - First release (April 12, 2016)