**************
Program design
**************

Why functions?
--------------

It may not be clear why it is worth the trouble to divide a program into
functions. There are several reasons:

-  Creating a new function gives you an opportunity to name a group of
   statements, which makes your program easier to read and debug.

-  Functions can make a program smaller by eliminating repetitive code.
   Later, if you make a change, you only have to make it in one place.

-  Dividing a long program into functions allows you to test and debug
   the parts one at a time and then assemble them into a working whole.

-  Well-designed functions are often useful for many programs. Once you
   write and debug one, you can reuse it.

Solving a problem by writing and composing functions also lends itself
well to a fundamental problem solving tactic: **divide and conquer**.
The basic idea is to break down a problem into smaller, and more easily
solved problems, until each subproblem can be solved directly. Many
problems can be complex and difficult to try to solve as a whole, but if
they are broken down into smaller subtasks, hopefully the subtasks are
more manageable.

The main challenge with a divide-and-conquer approach to problem solving
is *how to decompose the problem*: it isn't always apparent how to break
a problem down into smaller components. As we work through more
challenging problems, we will gain practice with this technique and
learn different strategies for applying it.

Incremental development
-----------------------

Assuming you've figured out how to break down a problem into smaller
subtasks, you are still faced with the challenge of writing larger and
more complex functions. As a result, you might find yourself spending
more time debugging.

To deal with writing increasingly complex programs, you might want to
try a process called **incremental development**. The goal of
incremental development is to avoid long debugging sessions by adding
and testing only a small amount of code at a time.

As an example, suppose you want to find the distance between two points,
given by the coordinates :math:`(x_1, y_1)` and :math:`(x_2, y_2)`. By
the Pythagorean theorem, the distance is:

.. math::

   \mathrm{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

The first step is to consider what a ``distance`` function should look
like in Python. In other words, what are the inputs (parameters) and
what is the output (return value)?

In this case, the inputs are two points, which you can represent using
four numbers. The return value is the distance, which is a
floating-point value.

Already you can write an outline of the function:

.. code-block:: python

    def distance(x1, y1, x2, y2):
        return 0.0

Obviously, this version doesn’t compute distances; it always returns
zero. But it is syntactically correct, and it runs, which means that you
can test it before you make it more complicated.

To test the new function, call it with sample arguments:

.. code-block:: python

    >>> distance(1, 2, 4, 6)
    0.0

I chose these values so that the horizontal distance is 3 and the
vertical distance is 4; that way, the result is 5 (the hypotenuse of a
3-4-5 triangle). When testing a function, it is useful to know the right
answer.

At this point we have confirmed that the function is syntactically
correct, and we can start adding code to the body. A reasonable next
step is to find the differences :math:`x_2 - x_1` and :math:`y_2 - y_1`.
The next version stores those values in temporary variables and prints
them.

.. code-block:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        print('dx is', dx)
        print('dy is', dy)
        return 0.0

If the function is working, it should display ``'dx is 3'`` and
``'dy is 4'``. If so, we know that the function is getting the right
arguments and performing the first computation correctly. If not, there
are only a few lines to check.

Next we compute the sum of squares of ``dx`` and ``dy``:

.. code-block:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        print('dsquared is: ', dsquared)
        return 0.0

Again, you would run the program at this stage and check the output
(which should be 25). Finally, you can use ``math.sqrt`` to compute and
return the result:

.. code-block:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = math.sqrt(dsquared)
        return result

If that works correctly, you are done. (Even better, you could construct
additional test cases to verify that the function *really* works.)
Otherwise, you might want to print the value of ``result`` before the
return statement.

.. sidebar:: The ``print`` function and **keyword arguments**

   The ``print`` function is a bit more powerful than we've shown or
   used so far.  It can take several different **keyword arguments**
   that can be used to control how output to the screen gets generated.
   Two specific keyword arguments are ``sep`` and ``end``.

   The ``sep`` keyword argument can be used to specify a string that
   should be printed *between* each argument to the print function call.
   By default, a single space is printed::

       >>> print(1, 2, 3)
       1 2 3

   But if you call ``print`` with the ``sep`` keyword, you can change
   that behavior::
   
       >>> print(1, 2, 3, sep="!!!")
       1!!!2!!!3
       >>> print(1, 2, 3, sep="")
       123
       >>> print(1, 2, 3, sep="+")
       1+2+3
   
   With keyword arguments you *must* use the syntax ``parametername=value``.
   For the ``print`` function, this should be somewhat obvious: if we did 
   not specify ``sep='value'`` the function wouldn't know whether to just
   print the argument or use it in a special way to control how output
   should be created.

   Another keyword argument to ``print`` is ``end``, which can be used
   to specify a string that should be printed at the end of each line.
   The default ``end`` string is ``\n'`` (the "newline" character), which
   causes the output of ``print`` to appear on its own line.  By using
   the ``end`` keyword argument, this behavior can be changed.  With
   the following code::

       print(1, 2, end='')
       print(3)

   The output would be::

       1 23

   Think about why the 2 and 3 have no space between them.  As an exercise,
   rewrite the two lines of code above so that the output is ``1 2 3`` on
   one line.


The final version of the function doesn’t display anything when it runs;
it only returns a value. The ``print`` function calls we wrote are useful
for debugging, but once you get the function working, you should remove
them. Code like that is called **scaffolding** because it is helpful for
building the program but is not part of the final product.

When you start out, you should add only a line or two of code at a time.
As you gain more experience, you might find yourself writing and
debugging bigger chunks. Either way, incremental development can save
you a lot of debugging time.

The key aspects of the process are:

1. Start with a working program and make small incremental changes. At
   any point, if there is an error, you should have a good idea where it
   is.

2. Use temporary variables to hold intermediate values so you can
   display and check them.

3. Once the program is working, you might want to remove some of the
   scaffolding or consolidate multiple statements into compound
   expressions, but only if it does not make the program difficult to
   read.

    **Example**:

    1. Use incremental development to write a function called
       ``hypotenuse`` that returns the length of the hypotenuse of a
       right triangle given the lengths of the two legs as arguments.
       Record each stage of the development process as you go.

Composition
-----------

As you should expect by now, you can call one function from within
another.  This ability is called **composition**.

As an example, we’ll write a function that takes two points, the center
of the circle and a point on the perimeter, and computes the area of the
circle.

Assume that the center point is stored in the variables ``xc`` and ``y`c`,
and the perimeter point is in ``xp`` and ``yp``. The first step is to find
the radius of the circle, which is the distance between the two points.
We just wrote a function, ``distance``, that does that:

.. code-block:: python

    radius = distance(xc, yc, xp, yp)

The next step is to find the area of a circle with that radius; we just
wrote that, too:

.. code-block:: python

    result = area(radius)

Encapsulating these steps in a function, we get:

.. code-block:: python

    def circle_area(xc, yc, xp, yp):
        radius = distance(xc, yc, xp, yp)
        result = area(radius)
        return result

The temporary variables ``radius`` and ``result`` are useful for development
and debugging, but once the program is working, we can make it more
concise by composing the function calls:

.. code-block:: python

    def circle_area(xc, yc, xp, yp):
        return area(distance(xc, yc, xp, yp))


A development plan
------------------

A **development plan** is a process for writing programs. The process we
used in this case study is “encapsulation and generalization.” The steps
of this process are:

1. Start by writing a small program with no function definitions.

2. Once you get the program working, encapsulate it in a function and
   give it a name.

3. Generalize the function by adding appropriate parameters.

4. Repeat steps 1–3 until you have a set of working functions. Copy and
   paste working code to avoid retyping (and re-debugging).

5. Look for opportunities to improve the program by **refactoring**.  
   Refactoring simply means changing a program's structure without
   modifying its behavior. Examples of refactoring might be to
   improve a program by reducing (or eliminating) repeated statements,
   or improving abstraction by creating a new function.  For
   example, if you have similar code in several places, consider
   factoring it into an appropriately general function.

This process has some drawbacks, but it can be useful if you don’t know
ahead of time how to divide the program into functions. This approach
lets you design as you go along.

Guidelines for functions: SOFA
------------------------------

A somewhat goofy but useful acronym for thinking about what makes a "good" 
function is SOFA.  The meaning of the acronym is this:

   Functions should be:

    * **S**\ hort,
    * Do **O**\ ne thing,
    * Take **F**\ ew arguments, and
    * Implement a single level of **A**\ bstraction




.. todo:: Make reference to uncle bob's book

docstrings
----------

A **docstring** is a string at the beginning of a function that explains
the interface ("doc" is short for "documentation"). Here is an example:

.. code-block:: python

    def circle_area(xc, yc, xp, yp):
        '''
        (float, float, float, float) -> float

        Compute the area of a circle.
        '''
        return area(distance(xc, yc, xp, yp))

This docstring is a triple-quoted string, also known as a multiline
string because the triple quotes allow the string to span more than one
line.  

It is terse, but it contains the essential information someone would
need to use this function. It explains concisely what the function does
(without getting into the details of how it does it).  The first line
is traditionally a representation of the parameter types that the function
accepts, and the data type that the function returns.  The explanation
of the function should give enough detail for a user of the function
to know how to use it and any details he or she should be aware of.

Writing this kind of documentation is an important part of interface
design. A well-designed interface should be simple to explain; if you
are having a hard time explaining one of your functions, that might be a
sign that the interface could be improved.

.. index:: debugging

Debugging
---------

An interface is like a contract between a function and a caller. The
caller agrees to provide certain parameters and the function agrees to
do certain work.

For example, ``polyline`` requires three arguments. The first has to be
a number, and it should probably be positive, although it turns out that
the function works even if it isn’t. The second argument should be an
integer; ``range`` complains otherwise (depending on which version of
Python you are running). The third has to be a number, which is
understood to be in degrees.

These requirements are called **preconditions** because they are
supposed to be true before the function starts executing. Conversely,
conditions at the end of the function are **postconditions**.
Postconditions include the intended effect of the function (like drawing
line segments) and any side effects (like moving the turtle).

Preconditions are the responsibility of the caller. If the caller
violates a (properly documented!) precondition and the function doesn’t
work correctly, the bug is in the caller, not the function.

Note that the ``assert`` function described in the last chapter can be
incredibly helpful for verifying pre- or post-conditions.

Glossary
--------

divide and conquer:
    A problem solving strategy that proceeds by breaking down a problem
    into smaller and smaller subtasks, until a subtask can be solved
    directly.

incremental development:
    A program development plan intended to avoid debugging by adding and
    testing only a small amount of code at a time.

scaffolding:
    Code that is used during program development but is not part of the
    final version.

encapsulation:
    The process of transforming a sequence of statements into a function
    definition.

generalization:
    The process of replacing something unnecessarily specific (like a
    number) with something appropriately general (like a variable or
    parameter).

keyword argument:
    An argument that includes the name of the parameter as a "keyword."

interface:
    A description of how to use a function, including the name and
    descriptions of the arguments and return value.

refactoring:
    The process of modifying a working program to improve function
    interfaces and other qualities of the code.

development plan:
    A process for writing programs.

docstring:
    A string that appears in a function definition to document the
    function's interface.

precondition:
    A requirement that should be satisfied by the caller before a
    function starts.

postcondition:
    A requirement that should be satisfied by the function before it
    ends.

.. rubric:: Exercises

.. todo:: hangperson, run-length encoding, 

.. rubric:: Footnotes

