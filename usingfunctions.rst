Using functions
***************

In this chapter we'll learn about how to use functions that are built in
to Python. Python contains hundreds, if not thousands, of *modules* that
contain many functions that you can use in your programs. Over the span
of this course we will use quite a few different modules and functions.
This chapter is about how to tap into these features.

Function calls
--------------

In the context of programming, a **function** is a named sequence of
statements that performs a computation. When you define a function, you
specify the name and the sequence of statements. Later, you can "call"
the function by name. We have already seen one example of a **function
call**:

::

    >>> type(32)
    <type 'int'>

The name of the function is ``type``. The expression in parentheses is
called the **argument** of the function. The result, for this function,
is the type of the argument.

It is common to say that a function "takes" an argument and "returns" a
result. The result is called the **return value**.

Type conversion functions
-------------------------

Python provides built-in functions that convert values from one type to
another. The ``int`` function takes any value and converts it to an
integer, if it can, or complains otherwise:

::

    >>> int('32')
    32
    >>> int('Hello')
    ValueError: invalid literal for int(): Hello

``int`` can convert floating-point values to integers, but it doesn't
round off; it chops off the fraction part:

::

    >>> int(3.99999)
    3
    >>> int(-2.3)
    -2

``float`` converts integers and strings to floating-point numbers:

::

    >>> float(32)
    32.0
    >>> float('3.14159')
    3.14159

Finally, ``str`` converts its argument to a string:

::

    >>> str(32)
    '32'
    >>> str(3.14159)
    '3.14159'

Getting user input: the ``input`` and ``raw_input`` functions
-------------------------------------------------------------

The programs we have written so far are a bit rude in the sense that
they accept no input from the user. They just do the same thing every
time.

Python provides a built-in function called ``raw_input`` that gets input
from the keyboard. When this function is called, the program stops and
waits for the user to type something. When the user presses ``Return``
or ``Enter``, the program resumes and ``raw_input`` returns what the
user typed as a string.

::

    >>> response = raw_input()
    What are you waiting for?
    >>> print response
    What are you waiting for?

Before getting input from the user, it is a good idea to print a prompt
telling the user what to input. ``raw_input`` can take a prompt as an
argument:

::

    >>> name = raw_input('What...is your name?\n')
    What...is your name?
    Arthur, King of the Britons!
    >>> print name
    Arthur, King of the Britons!

The sequence ``\n`` at the end of the prompt represents a **newline**,
which is a special character that causes a line break. That’s why the
user’s input appears below the prompt.

If you expect the user to type an integer, you can try to convert the
return value to ``int``:

::

    >>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
    >>> speed = raw_input(prompt)
    What...is the airspeed velocity of an unladen swallow?
    17
    >>> int(speed)
    17

But if the user types something other than a string of digits, you get
an error:

::

    >>> speed = raw_input(prompt)
    What...is the airspeed velocity of an unladen swallow?
    What do you mean, an African or a European swallow?
    >>> int(speed)
    ValueError: invalid literal for int()

We will see how to handle this kind of error later.

More on strings
---------------

A string is a **sequence** of characters. You can access the characters
one at a time with the bracket operator:

::

    >>> fruit = 'apple'
    >>> letter = fruit[1]

The second statement selects character number 1 from ``fruit`` and
assigns it to ``letter``.

The expression in brackets is called an **index**. The index indicates
which character in the sequence you want (hence the name).

But you might not get what you expect:

::

    >>> print letter
    p

For most people, the first letter of ``'apple'`` is ``a``, not ``p``.
But for computer scientists, the index is an offset from the beginning
of the string, and the offset of the first letter is zero.

::

    >>> letter = fruit[0]
    >>> print letter
    a

So ``a`` is the 0\ :sup:`th` letter (“zero-eth”) of ``'apple'``, ``p``
is the 1\ :sup:`th` letter (“one-eth”), and ``p`` is the 2\ :sup:`th`
(“two-eth”) letter.

Since indices start at 0, we can see that the last valid index of the
string ``'apple'`` is 4, which is one less than the length of the string
(which is 5 characters).

    +----------+--------+--------+--------+--------+--------+
    |          | ``a``  | ``p``  | ``p``  | ``l``  | ``e``  |
    +----------+--------+--------+--------+--------+--------+
    | index    | 0      | 1      | 2      | 3      | 4      |
    +----------+--------+--------+--------+--------+--------+

To get the last letter of a string, you might be tempted to try
something like this:

::

    >>> fruit = 'apple'
    >>> length = len(fruit)
    >>> print length
    5
    >>> last = fruit[length]
    IndexError: string index out of range

The reason for the ``IndexError`` is that there is no letter in
``'apple'`` with the index 5. To get the last character, you have to
subtract 1 from the length of the string.

A built-in Python function that we'll use frequently with sequence types
like strings is ``len``. This function returns the number of items in
the sequence as an integer. It can conveniently be used to access the
last character of a string, no matter the length of the string:

::

    >>> fruit = 'coconut'
    >>> fruitlen = len(fruit)
    >>> print fruitlen
    7
    >>> print fruit[fruitlen-1]
    't'

You can use any expression, including variables and operators, as an
index, but the value of the index has to be an integer. Otherwise you
get:

::

    >>> letter = fruit[1.5]
    TypeError: string indices must be integers

Also, strings are *immutable*, which means that you cannot modify them
once they're created. For example, if you try to modify one character of
a string using an assignment statement, you'll get an error:

::

    >>> fruit[0] = 'x'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment    

In addition to using indices from 0 to one less than the length of a
string, you can use negative indices, which count backward from the end
of the string. The expression ``fruit[-1]`` yields the last letter,
``fruit[-2]`` yields the second to last, and so on. The following table
shows both *positive* and *negative* indices, and how they can be used
to access characters of a string.

    +---------------------+--------+--------+--------+--------+--------+
    |                     | ``a``  | ``p``  | ``p``  | ``l``  | ``e``  |
    +---------------------+--------+--------+--------+--------+--------+
    | positive indices    | 0      | 1      | 2      | 3      | 4      |
    +---------------------+--------+--------+--------+--------+--------+
    | negative indices    | -5     | -4     | -3     | -2     | -1     |
    +---------------------+--------+--------+--------+--------+--------+

Case study 1: printing out the characters of a string
-----------------------------------------------------

As we've learned, *a string is a sequence of characters*. Sometimes,
solving a problem requires us to inspect each character of a string, one
by one. In other words, to inspect each character *in sequence*. Python
includes the ``for`` statement to help with repetitive tasks like this.
Here is an example that simply prints out each character by itself, in
sequence:

::

    fruit = "kiwi"
    for char in fruit:
        print char
    print "done!"

There are quite a few new syntactical elements to this example, so let's
go through it in detail.

First, we see the ``for`` statement, which can be read in English as
"for every item in the sequence", or "for every character in the string
fruit". The last item of a ``for`` statement must, therefore, be a
sequence type, like a string.

The ``for`` statement is usually called a "``for`` loop", because of its
repetitive nature. The effect of the program is to assign each letter of
the string ``fruit`` to the variable ``char``, one by one. For each
assignment, the indented statement block underneath the ``for``
statement consisting of the line ``print char`` is executed. That is,
the statement block is *repeated* for each character in the string. As a
result, each letter of the string is printed by itself on separate
lines. The complete output of the program is shown below:

So, the word ``char`` in the ``for`` statement is a variable that is
assigned each item of the sequence, one-by-one. (Note that the variable
name ``char`` is *just a variable name*, and has no inherent meaning to
the ``for`` loop: we could have just as easily used ``seed`` or some
other valid variable name.)

Also, notice that a colon (``:``) appears at the end of the ``for``
statement, and that the next line is indented. Whenever you encounter a
colon at the end of a statement in Python, the next statement **must**
be indented in order for the code to be syntactically correct. There can
be more than one indented statement, but *at least* one must be present;
these indented statements are referred to as a **statement block**.

::

    k
    i
    w
    i
    done!

The sequence of operations that are executed by the 4-line program is
not especially obvious just from glancing at the program. In order to be
able to understand the output, we need to think about the meaning of the
``for`` statement, and trace each action that the Python interpreter
would make. Learning to read a program is an important skill to develop,
and one that you will need to work on throughout this course.

In detail, the way that this program is sequentially executed by the
Python interpreter is as follows:

1. The variable fruit is assigned the string ``'kiwi'``
2. We encounter the ``for`` loop. The variable ``char`` is assigned the
   *first* letter of the string referred to by ``fruit`` (``'k'``)

   -  We print ``char``, which is just ``'k'``

3. We go back to the top of the ``for`` loop; the next letter, ``'i'``,
   is assigned to ``char``

   -  We print ``char``, which is ``'i'``

4. We go back to the top of the ``for`` loop; the next letter, ``'w'``,
   is assigned to ``char``

   -  We print ``char``, which is ``'w'``

5. We go back to the top of the ``for`` loop; the last letter, ``'i'``,
   is assigned to ``char``

   -  We print ``char``, which is ``'i'``

6. We exit the for loop since we have traversed every element in the
   sequence (string) ``'kiwi'``. We print ``'done!'`` since that is the
   next statement in the program.

Math functions
--------------

Python has a math module that provides most of the familiar mathematical
functions. A **module** is a file that contains a collection of related
functions.

Before we can use the module, we have to import it:

::

    >>> import math

This statement creates a **module object** named math. If you print the
module object, you get some information about it:

::

    >>> print math
    <module 'math' (built-in)>
    >>> 

The module object contains the functions and variables defined in the
module. To access one of the functions, you have to specify the name of
the module and the name of the function, separated by a dot (also known
as a period). This format is called **dot notation**.

::

    >>> ratio = signal_power / noise_power
    >>> decibels = 10 * math.log10(ratio)

    >>> radians = 0.7
    >>> height = math.sin(radians)

The first example computes the logarithm base 10 of the signal-to-noise
ratio. The math module also provides a function called ``log`` that
computes logarithms base ``e``.

The second example finds the sine of ``radians``. The name of the
variable is a hint that ``sin`` and the other trigonometric functions
(``cos``, ``tan``, etc.) take arguments in radians. To convert from
degrees to radians, divide by 360 and multiply by :math:`2 \pi`:

::

    >>> degrees = 45
    >>> radians = degrees / 360.0 * 2 * math.pi
    >>> math.sin(radians)
    0.707106781187

The expression ``math.pi`` gets the variable ``pi`` from the math
module. The value of this variable is an approximation of :math:`\pi`,
accurate to about 15 digits.

If you know your trigonometry, you can check the previous result by
comparing it to the square root of two divided by two:

::

    >>> math.sqrt(2) / 2.0
    0.707106781187

A few last notes about importing modules:

#. By convention any ``import`` statements should always go at the *top*
   of your programs.

#. There are a huge number of modules built-in to Python (take a look at
   http://docs.python.org/library/ if you wish). We'll really just
   scratch the surface on these built-in capabilities. As we proceed
   through the course, you'll learn how to decipher the online Python
   documentation to be able to take advantage of more of these modules.

#. There are other ways to import modules, which you'll see later in the
   course (and which you'll likely encounter if you look at Python code
   examples on the web).

Composition
-----------

So far, we have looked at the elements of a program—variables,
expressions, and statements—in isolation, without talking about how to
combine them.

One of the most useful features of programming languages is their
ability to take small building blocks and **compose** them. For example,
the argument of a function can be any kind of expression, including
arithmetic operators:

::

    x = math.sin(degrees / 360.0 * 2 * math.pi)

And even function calls:

::

    x = math.exp(math.log(x+1))

Almost anywhere you can put a value, you can put an arbitrary
expression, with one exception: the left side of an assignment statement
has to be a variable name. Any other expression on the left side is a
syntax error.

::

    >>> minutes = hours * 60                 # right
    >>> hours * 60 = minutes                 # wrong!
    SyntaxError: can't assign to operator

Case study 2: string traversal using ``range``, ``len``, and a for loop
-----------------------------------------------------------------------

In the next two case studies, we'll get practice with function
composition and learn two new built-in Python functions: ``range`` and
``round``.

We already know that we can use a for loop to access each character of a
string, one by one. We also know that we can use an *index* to access
individual characters in a string by position. What if we wanted to
combine these two ideas, and cycle through the valid indices of a
string? For example, if we wanted to go through the integer values 0..4
to access each character of the string ``apple`` by index. Well, Python
has a built-in function named ``range`` that can help with exactly that
task. For example:

::

    >>> range(4)
    [0, 1, 2, 3]
    >>>

The ``range`` function takes an integer as a parameter, and returns a
sequence of integers from 0 through the supplied argument minus 1. (The
sequence of integers that ``range`` returns is called a ``list`` in
Python. A ``list`` is a sequence type with some similarities to strings.
We'll learn more about lists soon.)

We can use the ``range`` function in a ``for`` loop to print the
integers from 0 through 3 as follows:

::

    for index in range(4):
        print index

::

    0
    1
    2
    3

Now, to solve the problem of printing the characters of a string *by
index*, we can *compose* the ``range`` and ``len`` functions in a
``for`` loop, as follows:

::

    fruit = 'kiwi'
    for index in range(len(fruit)):
        print index, fruit[index]

In the statement block inside the ``for`` loop, we print both the value
of the variable ``index``, and the character at the given index in the
string. Thus, the output should be:

::

    0 k
    1 i
    2 w
    3 i

The composition of ``range`` and ``len`` in a ``for`` loop is quite
powerful! It's also a good Pythonic idiom to understand: we'll use it
often in ``for`` loop construction.

One last note about the ``range`` function: it can actually take more
than one argument to flexibly construct a variety of different numeric
sequences. We'll learn about this more complex use of ``range`` a bit
later.

Case study 3: making a table of square roots
--------------------------------------------

In the last case study of this chapter, we'll again use ``range`` in a
``for`` loop to print tables of numeric values. Say, for example, that
we want to make a table of square roots, like:

::

    The square root of 0 is 0
    The square root of 1 is 1
    The square root of 2 is ?!
    ...

I don't remember a good approximation to the square root of two off the
top of my head, but I bet we can coerce Python into telling us! Here's
one way how:

::

    import math

    print "My amazing table of square roots!"
    for number in range(5):
        print "The square root of", number, "is", math.sqrt(number)

The output of our program should be:

::

    My amazing table of square roots!
    The square root of 0 is 0.0
    The square root of 1 is 1.0
    The square root of 2 is 1.41421356237
    The square root of 3 is 1.73205080757
    The square root of 4 is 2.0

Make sure you understand how Python produces the above output.

Hmm... we've got a table of square roots, but some of the values are a
little unwieldy because of so many decimal places. To make the output
look a little nicer, we can use the built-in Python ``round`` function.
``round`` takes two arguments: a value to round, and the number of
decimal places to which to round the number. If we want to round to 2
decimal places, we can modify the above program to compose the ``round``
and ``math.sqrt`` functions:

::

    import math

    print "My super-amazing table of square roots!"
    for number in range(5):
        print "The square root of", number, "is", round(math.sqrt(number),2)

::

    My super-amazing table of square roots!
    The square root of 0 is 0.0
    The square root of 1 is 1.0
    The square root of 2 is 1.41
    The square root of 3 is 1.73
    The square root of 4 is 2.0

Ah. That's better. Later, we'll learn ways to make our output look even
nicer, but for now, ``round`` does a pretty good job.

Debugging
---------

There are a few common error patterns and issues to be aware of related
to functions and new syntax we've seen in this chapter.

1. Using a function in an external module, but forgetting to use
   ``import``:

   ::

        >>> print math.sqrt(10)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'math' is not defined     

   To fix this problem, just be sure to say ``import math`` at the top
   of your program.

2. Constructing a for loop that results in the statement block not being
   executed.

   ::

        mystring = ''
        for char in mystring:
            print "The new phone books are here!"

   The result of this program is ... nothing! The reason is that the
   string, while valid, is "empty". Thus, there are no characters to be
   assigned to the variable ``char``, and we won't execute the statement
   block within the ``for`` loop. Nothing will happen.

   Some other questions for you to consider along the same lines as this
   error pattern: what happens if you call ``len`` with an empty string?
   What happens if you use ``range`` with a negative number?

   Thankfully, it's *impossible* to create a ``for`` loop that never
   stops. We will, however, encounter another *iteration* mechanism in
   Python where "infinite loops" are possible.

3. Using a non-sequence type for the last part of the ``for`` statement.

   The last part of the ``for`` statement has to be a sequence type, or
   something that is *iterable*. If not, you'll get an error like the
   following:

   ::

        >>> for value in 5:
        ...     print value
        ... 
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: 'int' object is not iterable
        >>> 

   All this error says is that the integer value 5 isn't a sequence
   type, so the ``for`` loop blew up.

More generally, when Python crashes, the "Traceback" message that it
shows contains a lot of information. The most useful parts are usually:

-  What kind of error it was, and
-  Where it occurred.

Syntax errors are usually easy to find, but there are a few gotchas.
Whitespace errors can be tricky because spaces and tabs are invisible
and we are used to ignoring them.

::

    >>> x = 5
    >>>  y = 6
      File "<stdin>", line 1
        y = 6
        ^
    SyntaxError: invalid syntax

In this example, the problem is that the second line is indented by one
space. But the error message points to ``y``, which is misleading. In
general, error messages indicate where the problem was discovered, but
the actual error might be earlier in the code, sometimes on a previous
line.

The same is true of runtime errors. Suppose you are trying to compute a
signal-to-noise ratio in decibels. The formula is

.. math:: SNR_{db} = 10 \times \log_{10} (P_{signal} / P_{noise})

In Python, you might write something like this:

::

    import math
    signal_power = 9
    noise_power = 10
    ratio = signal_power / noise_power
    decibels = 10 * math.log10(ratio)
    print decibels

But when you run it, you get an error message:

::

    Traceback (most recent call last):
      File "snr.py", line 5, in ?
        decibels = 10 * math.log10(ratio)
    OverflowError: math range error

The error message indicates line 5, but there is nothing wrong with that
line. To find the real error, it might be useful to print the value of
``ratio``, which turns out to be 0. The problem is in line 4, because
dividing two integers does floor division. The solution is to represent
signal power and noise power with floating-point values.

So in general, error messages tell you where the problem was discovered,
but that is often not where it was caused.

Glossary
--------

function:
    A named sequence of statements that performs some useful operation.
    Functions may or may not take arguments and may or may not produce a
    result.

function call:
    A statement that executes a function. It consists of the function
    name followed by an argument list.

argument:
    A value provided to a function when the function is called. This
    value is assigned to the corresponding parameter in the function.

module:
    A file that contains a collection of related functions and other
    definitions.

import statement:
    A statement that reads a module file and creates a module object.

module object:
    A value created by an ``import`` statement that provides access to
    the values defined in a module.

dot notation:
    The syntax for calling a function in another module by specifying
    the module name followed by a dot (period) and the function name.

sequence:
    An ordered set; that is, a set of values where each value is
    identified by an integer index.

item:
    One of the values in a sequence.

index:
    An integer value used to select an item in a sequence, such as a
    character in a string.

loop:
    A part of a program that can execute repeatedly.

composition:
    Using an expression as part of a larger expression, or a statement
    as part of a larger statement.

Exercises
---------

    #. Ask for a three-character string from a user, then construct and
       print a new string by swapping the first and last characters of
       the string entered by the user. (You can assume that the user
       always types a string consisting of 3 letters.) For example, if
       the user types ``'box'``, your program should print ``'xob'``.
       Note: using the ``if`` statement (discussed in the next chapter)
       is off limits!

    #. Ask for a string from the user. Print the string right-justified
       within a page width of 40 characters. For example, if a user
       types ``'abecedarian'``, which is 11 characters long, your
       program should print exactly 29 spaces followed by
       ``'abecedarian'`` (i.e., the total width of what you print should
       be exactly 40 characters). You can assume that the string entered
       by the user is at most 40 characters long.

    #. Construct a short program with a ``for`` loop to print the values
       of the sequence 25, 50, 75, ... 175, 200. Your ``for`` loop
       should use ``range`` with just one argument.

    #. Write a program that asks a user for a positive integer, then
       prints a table of cubes from 1 through that number. Make the
       table output as nice as you can using what we've covered so far.
       For example, if a user enters the number 3, your program should
       print the numbers 1, 8, and 27 (1\ :sup:`3`, 2\ :sup:`3`, and
       3\ :sup:`3`) in a nice table.

    #. Write a program that asks a user for a string, then prints the
       characters of the string *in reverse*, one on each line. For
       example, if a user enters the string ``'magic'``, your program
       should print:

       ::

            c
            i
            g
            a
            m

    #. Modify the program to make a table of square roots by asking the
       user for the largest number for which to compute the square root.
       For example, if the user types ``11``, your table should show the
       square roots from 0 through 11, including both end points.

    #. Write a program to compute the square root of the sum of numbers
       from 1 to 1000. You should use a ``for`` loop to compute the sum,
       and the ``sqrt`` function in the ``math`` module to compute the
       square root.

    #. The interest earned on an investment can be computed as
       ``interest = principal * rate``.

       Write a program that asks a user for an interest rate as a
       floating point number, an investment amount as a floating point
       number, and the number of years. Your program should print, for
       each year, the current amount of the principal. Note to
       economists and mathematicians: you should *not* use the
       exponential formula for this problem.

       ::

           What is the interest rate? 0.05
           What is the principal (amount invested)? 100
           How many years? 5
           After 1 years, the principal is 105.0
           After 2 years, the principal is 110.25
           After 3 years, the principal is 115.76
           After 4 years, the principal is 121.55
           After 5 years, the principal is 127.63

.. raw:: html

   <!-- make this section end! -->



