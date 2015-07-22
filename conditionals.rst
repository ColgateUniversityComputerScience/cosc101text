****************
Making decisions
****************

Boolean expressions
===================

Solving almost any problem requires that we make *decisions*, and at the
heart of decision-making within programs are **Boolean** values and
expressions. A **boolean expression** is one that is either true or
false. The following examples use the operator ``==``, which compares
two operands and produces ``True`` if they are equal and ``False``
otherwise:

.. code-block:: python

    >>> 5 == 5
    True
    >>> 5 == 6
    False

``True`` and ``False`` are special values that belong to the type
``bool``; they are not strings:

.. code-block:: python

    >>> type(True)
    <type 'bool'>
    >>> type(False)
    <type 'bool'>

The ``==`` operator is one of the **relational operators**; the others
are:

.. code-block:: python

          x != y               # x is not equal to y
          x > y                # x is greater than y
          x < y                # x is less than y
          x >= y               # x is greater than or equal to y
          x <= y               # x is less than or equal to y

Although these operations are probably familiar to you, the Python
symbols are different from the mathematical symbols. A common error is
to use a single equal sign (``=``) instead of a double equal sign
(``==``). Remember that ``=`` is an assignment operator and ``==`` is a
relational operator. There is no such thing as ``=<`` or ``=>``.

You can use the relational operators to check whether a value is within
a numerical range:

.. code-block:: python

    >>> x = 4
    >>> 3 <= x < 5
    True

Besides applying these relational operators to numerical operands, they
can also be used with strings. To see if two strings are equal:

.. code-block:: python

    if word == 'banana':
        print  'All right, bananas.'

Other relational operations are useful for putting words in alphabetical
order:

.. code-block:: python

    if word < 'banana':
        print 'Your word,' + word + ', comes before banana.'
    elif word > 'banana':
        print 'Your word,' + word + ', comes after banana.'
    else:
        # must be equal!
        print 'All right, bananas.'

Python does not handle uppercase and lowercase letters the same way that
people do: all the uppercase letters come before all the lowercase
letters. When we look at strings in more detail in a later chapter,
we'll revisit this issue.

Lastly, there is a Boolean operator called ``in`` that can be used with
sequence types in Python to test whether one sequence is contained
within another. The most common use for in with strings is to test
whether a character or substring is contained within a string. For
example, both of the following Boolean expressions would evaluate to
``True``:

.. code-block:: python

    'a' in 'banana'
    'nana' in 'banana'

But this one would evaluate to ``False``:

.. code-block:: python

    'A' in 'banana'

Modulus operator
----------------

The **modulus operator** is not specifically related to Boolean
variables or making decisions, but will be useful in various problems
that we'll soon encounter. The modulus (or "mod") operator works on
integers and yields the remainder when the first operand is divided by
the second. In Python, the modulus operator is a percent sign (``%``).
The syntax is the same as for other operators:

.. code-block:: python

    >>> quotient = 7 / 3
    >>> print quotient
    2
    >>> remainder = 7 % 3
    >>> print remainder
    1

So 7 divided by 3 is 2 with 1 left over.

The modulus operator turns out to be surprisingly useful. For example,
you can check whether one number is divisible by another --- if
``x % y`` is zero, then ``x`` is divisible by ``y``.

Also, you can extract the right-most digit or digits from a number. For
example, ``x % 10`` yields the right-most digit of ``x`` (in base 10).
Similarly ``x % 100`` yields the last two digits.

Logical operators
-----------------

There are three **logical operators**: ``and``, ``or``, and ``not``. The
semantics (meaning) of these operators is similar to their meaning in
English. For example, ``x > 0 and x < 10`` is true only if ``x`` is
greater than 0 *and* less than 10.

``n%2 == 0 or n%3 == 0`` is ``True`` if *either* of the conditions is
``True``, that is, if the number is divisible by 2 *or* 3.

Finally, the ``not`` operator negates a boolean expression, so
``not (x > y)`` is ``True`` if ``x > y`` is ``False``, that is, if ``x``
is less than or equal to ``y``.

Strictly speaking, the operands of the logical operators should be
boolean expressions, but Python is not very strict. Any nonzero number
is interpreted as ``True``.

.. code-block:: python

    >>> 17 and True
    True

This flexibility can be useful, but there are some subtleties to it that
can be confusing. You should avoid exploiting this behavior as it tends
to make programs more difficult to read and understand.

Conditional execution
---------------------

In order to write useful programs, we almost always need the ability to
check conditions and change the behavior of the program accordingly.
**Conditional statements** give us this ability. The simplest form is
the ``if`` statement:

.. code-block:: python

    if x > 0:
        print 'x is positive'

The boolean expression after the ``if`` statement is called the
**condition**. If it is ``True``, then the indented statement gets
executed. If not, nothing happens.

``if`` statements have the same structure as the ``for`` statement: a
header with a colon at the end, followed by an indented body. Statements
like this are called **compound statements**. When ever you have a colon
at the end of a program statement, IDLE will automatically place your
cursor at a properly indented location on the next line. If you need to
do "manual" indentation, the convention in Python is to use 4 spaces
(and no tabs).

Again, for compound statements, there is no limit on the number of
statements that can appear in the body, but there has to be at least
one. Occasionally, it is useful to have a body with no statements
(usually as a place keeper for code you haven’t written yet). In that
case, you can use the ``pass`` statement, which does nothing.

.. code-block:: python

    if x < 0:
        pass          # need to handle negative values!

Alternative execution
---------------------

A second form of the ``if`` statement is **alternative execution**, in
which there are two possibilities and the condition determines which one
gets executed. The syntax looks like this:

.. code-block:: python

    if x%2 == 0:
        print 'x is even'
    else:
        print 'x is odd'

If the remainder when ``x`` is divided by 2 is 0, then we know that
``x`` is even, and the program displays a message to that effect. If the
condition is ``False``, the second set of statements is executed. Since
the condition must be ``True`` or ``False``, exactly one of the
alternatives will be executed. The alternatives are called **branches**,
because they are branches in the flow of execution.

Case study: simulating a coin toss
----------------------------------

Given the same inputs, most computer programs generate the same outputs
every time, so they are said to be **deterministic**. Determinism is
usually a good thing, since we expect the same calculation to yield the
same result. For some applications, though, we want the computer to be
unpredictable. Games are an obvious example, but there are more.

Making a program truly nondeterministic turns out to be not so easy, but
there are ways to make it at least *seem* nondeterministic. One of them
is to use algorithms that generate **pseudorandom** numbers.
Pseudorandom numbers are not truly random because they are generated by
a deterministic computation, but just by looking at the numbers it is
all but impossible to distinguish them from random.

The ``random`` module provides functions that generate pseudorandom
numbers (which we'll simply call "random" from now on).

The function ``random`` returns a random float between 0.0 and 1.0
(including 0.0 but not 1.0). Each time you call ``random``, you get the
next number in a long series. To see a sample, run this loop:

.. code-block:: python

    import random

    for i in range(10):
        x = random.random()
        print x

The function ``randint`` takes parameters ``low`` and ``high`` and
returns an integer between ``low`` and ``high`` (including both).

.. code-block:: python

    >>> random.randint(5, 10)
    5
    >>> random.randint(5, 10)
    9

So, one way to simulate tossing a fair coin (i.e., with equal chance it
comes up heads or tails), we could use the following program:

.. code-block:: python

    import random

    if random.randint(0,1) == 0:
        print "Heads!"
    else:
        print "Tails!"

The ``randint`` function will return 0 or 1 with equal probability, so
that will effectively simulate a coin toss. Alternatively, we could use
the ``random`` function to do the same thing:

.. code-block:: python

    import random

    if random.random() < 0.5:
        print "Heads!"
    else:
        print "Tails!"

Chained conditionals
--------------------

Sometimes there are more than two possibilities and we need more than
two branches. One way to express a computation like that is a **chained
conditional**:

.. code-block:: python

    if x < y:
        print 'x is less than y'
    elif x > y:
        print 'x is greater than y'
    else:
        print 'x and y are equal'

``elif`` is an abbreviation of "else if". Again, *exactly one branch
will be executed*. There is no limit on the number of ``elif``
statements. If there is an ``else`` clause, it has to be at the end, but
there doesn't have to be one.

.. code-block:: python

    import random

    rps = random.randint(1,3)
    if rps == 1:
        print "Rock!"
    elif rps == 2:
        print "Paper!"
    elif rps == 3:
        print "Scissors!"

Each condition is checked in order. If the first is ``False``, the next
is checked, and so on. If one of them is ``True``, the corresponding
branch executes, and the statement ends. Even if more than one condition
is ``True``, only the first ``True`` branch executes.

Nested conditionals
-------------------

One conditional can also be nested within another. We could have written
the trichotomy example like this:

.. code-block:: python

    if x == y:
        print 'x and y are equal'
    else:
        if x < y:
            print 'x is less than y'
        else:
            print 'x is greater than y'

The outer conditional contains two branches. The first branch contains a
simple statement. The second branch contains another ``if`` statement,
which has two branches of its own. Those two branches are both simple
statements, although they could have been conditional statements as
well.

Although the indentation of the statements makes the structure apparent,
**nested conditionals** become difficult to read very quickly. In
general, it is a good idea to avoid them when you can.

Logical operators often provide a way to simplify nested conditional
statements. For example, we can rewrite the following code using a
single conditional:

.. code-block:: python

    if 0 < x:
        if x < 10:
            print 'x is a positive single-digit number.'

The ``print`` statement is executed only if we make it past both
conditionals, so we can get the same effect with the ``and`` operator:

.. code-block:: python

    if 0 < x and x < 10:
        print 'x is a positive single-digit number.'

Debugging
---------

        *The most effective debugging tool is still careful thought,
        coupled* *with judiciously placed print statements.*

            Brian Kernighan, "Unix for Beginners" (1979)

Debugging problems can become a bit more complex when dealing with
conditional statements. To understand what is causing a problem in a
program, we often want to know which *branch* is being taken. To do
that, it can be helpful to insert ``print`` statements within ``if``,
``elif``, and ``else`` statement blocks. Adding ``print`` statements to
help reveal what the program is doing is often referred to as **trace
debugging**, **printf debugging**, or **caveman debugging**. (The term
"printf debugging" comes from the ``printf`` function in the C language,
which is fairly similar to the ``print`` statement in Python.) Although
the term "caveman" doesn't cast a particularly favorable light on this
technique, it is nonetheless an extremely useful and widely used method
for understanding what a program is doing.

Glossary
--------

modulus operator:
    An operator, denoted with a percent sign (``%``), that works on
    integers and yields the remainder when one number is divided by
    another.

boolean expression:
    An expression whose value is either ``True`` or ``False``.

relational operator:
    One of the operators that compares its operands: ``==``, ``!=``,
    ``>``, ``<``, ``>=``, and ``<=``.

logical operator:
    One of the operators that combines boolean expressions: ``and``,
    ``or``, and ``not``.

conditional statement:
    A statement that controls the flow of execution depending on some
    condition.

condition:
    The boolean expression in a conditional statement that determines
    which branch is executed.

compound statement:
    A statement that consists of a header and a body. The header ends
    with a colon (:). The body is indented relative to the header.

branch:
    One of the alternative sequences of statements in a conditional
    statement.

chained conditional:
    A conditional statement with a series of alternative branches.

nested conditional:
    A conditional statement that appears in one of the branches of
    another conditional statement.

deterministic:
    Pertaining to a program that does the same thing each time it runs,
    given the same inputs.

pseudorandom:
    Pertaining to a sequence of numbers that appear to be random, but
    are generated by a deterministic program.

.. rubric:: Exercises

1. Consider the following program:

.. code-block:: python

    i = input("Gimme a number: ")
    if i == 0:
        print "You entered zero"
    if i == 1:
        print "You entered one"
    else:
        print "You entered something other than zero or one"

..

   Given an input of ``0``, what will the program print? Why?


2. Write a program that asks for the number of a year (e.g., 1982)
   and prints whether that year was a leap year or not. A year is a
   leap year if it is evenly divisible by 4. If a year is also
   evenly divisible by 100 it is *not* a leap year, unless it is
   evenly divisible by 400 as well.

   For example, 1980 and 2012 were leap years. 1900 was *not* a leap
   year (evenly divisible by 100), but 2000 was (evenly divisible by
   100 *and* 400).

3. Write a short program to play one round of rock-paper-scissors.
   Ask the user to enter 0, 1, or 2 to correspond to rock, paper,
   and scissors. Use the ``random`` module to have the computer
   randomly choose rock, paper, or scissors. Print a message
   indicating who wins, or whether there was a tie.

   For those who haven't played rock, paper, scissors before (and
   even if you have), read the Wikipedia page for detail on related
   games, and programs (and robots) that have been built to play
   RPS: http://en.wikipedia.org/wiki/Rock-paper-scissors.

