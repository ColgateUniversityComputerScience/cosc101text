*********
Recursion
*********

Chicken, meet egg
-----------------

It is legal for one function to call another; it is also legal for a
function to call itself. It may not be obvious why that is a good thing,
but it turns out to be one of the most magical things a program can do.
A function that calls itself is **recursive**; the process is called
**recursion**.

A recursive definition is similar to a circular definition, in the sense
that the definition contains a reference to the thing being defined. A
truly circular definition is not very useful:

frabjous:
    An adjective used to describe something that is frabjous.

If you saw that definition in the dictionary, you might be annoyed (in
which case, you might want to check out "recursive acronyms"!
http://en.wikipedia.org/wiki/Recursive_acronym). On the other hand, if
you looked up the definition of the factorial function, denoted with the
symbol :math:`!`, you might get something like this:

  * :math:`0! = 1`
  * :math:`n! = n * (n-1)!` 

This definition says that the factorial of 0 is 1, and the factorial of
any other value, :math:`n`, is :math:`n` multiplied by the factorial of
:math:`n-1`.

So :math:`3!` is 3 times :math:`2!`, which is 2 times :math:`1!`, which
is 1 times :math:`0!`. Putting it all together, :math:`3!` equals 3
times 2 times 1 times 1, which is 6.

If you can write a recursive definition of something, you can usually
write a Python program to evaluate it. The first step is to decide what
the parameters should be. In this case it should be clear that
``factorial`` takes an integer:

.. code-block:: python

    def factorial(n):

If the argument happens to be 0, all we have to do is return 1:

.. code-block:: python

    def factorial(n):
        if n == 0:
            return 1

Otherwise, and this is the interesting part, we have to make a recursive
call to find the factorial of :math:`n-1` and then multiply it by
:math:`n`:

.. code-block:: python

    def factorial(n):
        if n == 0:
            return 1
        else:
            recurse = factorial(n-1)
            result = n * recurse
            return result

If we call ``factorial`` with the value 3:

    Since 3 is not 0, we take the second branch and calculate the
    factorial of ``n-1``...

        Since 2 is not 0, we take the second branch and calculate the
        factorial of ``n-1``...

            Since 1 is not 0, we take the second branch and calculate
            the factorial of ``n-1``...

                Since 0 *is* 0, we take the first branch and return 1
                without making any more recursive calls.

            The return value (1) is multiplied by :math:`n`, which is 1,
            and the result is returned.

        The return value (1) is multiplied by :math:`n`, which is 2, and
        the result is returned.

    The return value (2) is multiplied by :math:`n`, which is 3, and the
    result, 6, becomes the return value of the function call that
    started the whole process.

Here is what the stack diagram looks like for this sequence of function
calls:

.. figure:: figs/stack3.png
   :align: center
   :alt: Stack diagram for ``factorial(3)``

   Stack diagram for ``factorial(3)``

The four frames have different values for the parameter ``n``. The
return values are shown being passed back up the stack. In each frame,
the return value is the value of ``result``, which is the product of
``n`` and ``recurse``.

The bottom of the stack, where ``n = 0``, is referred to as the **base
case**. It does not make a recursive call, so there are no more stack
frames. Also, in the last frame, the local variables ``recurse`` and
``result`` do not exist, because the branch that creates them does not
execute.

Decrease and conquer
--------------------

Recursion as a programming technique lends itself well to a problem
solving strategy called **decrease and conquer**. The basic idea is to
consider how a problem can be formulated in terms of "smaller" versions
of itself. In the case of the ``factorial`` function, we directly use
the mathematical definition to accomplish this:

.. code-block:: python

    factorial(n) = n * factorial(n-1)

The right-hand side of the statement *decreases* the problem size
(``n``) by one, and recursively invokes the ``factorial`` function.
Since this statement recursively reduces the problem size, we eventually
reach the **base case** (i.e., ``n == 0``), at which point the recursion
stops.

The strategy discussed earlier, *divide and conquer* is also useful when
thinking about solving problems recursively. If a problem can be divided
into smaller, non-overlapping versions of itself, a recursive approach
may be appropriate. In the searching and sorting chapters, we'll see an
examples of two problems that fit this approach.

Infinite recursion
------------------

If a recursion never reaches a base case, it goes on making recursive
calls forever, and the program never terminates. This is known as
**infinite recursion**, and it is generally not a good idea. Here is a
minimal program with an infinite recursion:

.. code-block:: python

    def recurse():
        recurse()

In most programming environments, a program with infinite recursion does
not really run forever. Python reports an error message when the maximum
recursion depth is reached:

.. code-block:: python

      File "<stdin>", line 2, in recurse
      File "<stdin>", line 2, in recurse
      File "<stdin>", line 2, in recurse
                      .   
                      .
                      .
      File "<stdin>", line 2, in recurse
    RuntimeError: Maximum recursion depth exceeded

This traceback is a little bigger than the one we saw in the previous
chapter. When the error occurs, there are 1000 ``recurse`` frames on the
stack!

Leap of faith
-------------

Following the flow of execution is one way to read programs, but it can
quickly become labyrinthine. An alternative approach is what might be
considered the "leap of faith." When you come to a function call,
instead of following the flow of execution, you *assume* that the
function works correctly and returns the right result.

In fact, you are already practicing this leap of faith when you use
built-in functions. When you call ``math.cos`` or ``math.exp``, you
don’t examine the bodies of those functions. You just assume that they
work because the people who wrote the built-in functions were good
programmers.

The same is true when you call one of your own functions. For example,
we previously wrote a function called ``is_divisible`` that determines 
whether one number is divisible by another. Once we have convinced ourselves 
that this function is correct—by examining the code and testing—we can 
use the function without looking at the body again.

The same is true of recursive programs. When you get to the recursive
call, instead of following the flow of execution, you should assume that
the recursive call works (yields the correct result) and then ask
yourself, “Assuming that I can find the factorial of :math:`n-1`, can I
compute the factorial of :math:`n`?” In this case, it is clear that you
can, by multiplying by :math:`n`.

Of course, it’s a bit strange to assume that the function works
correctly when you haven’t finished writing it, but that’s why it’s
called a leap of faith!

Two more examples
-----------------

Factorial
~~~~~~~~~

After ``factorial``, the most common example of a recursively defined
mathematical function is ``fibonacci``. Similar to the ``factorial``
function, it follows a *decrease and conquer* approach. The
``fibonacci`` function has the following definition [1]_:


  * :math:`fibonacci(0) = 0`

  * :math:`fibonacci(1) = 1`

  * :math:`fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`


Translated into Python, it looks like this:

.. code-block:: python

    def fibonacci (n):
        if n == 0:
            return 0
        elif  n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

Notice that in the last line, the "problem size" (``n``) is reduced by
one or two. Eventually, we decrease the problem size to ``n = 0`` or
``n = 1``. If you try to follow the flow of execution here, even for
fairly small values of :math:`n`, your head explodes. But according to
the leap of faith, if you assume that the two recursive calls work
correctly, then it is clear that you get the right result by adding them
together.

Palindromes
~~~~~~~~~~~

Another problem that can solved with a recursive "reduce and conquer"
approach is to determine whether a string is a palindrome or not. A
string is a palindrome if it is spelled the same way backward and
forward. For example, the following words are palindromes:

-  racecar
-  civic
-  kayak
-  rotator
-  testset

The following phrase is also palindromic (assuming the punctuation is
removed, and we convert all characters to the same case):

    A man, a plan, a canal, Panama!

This problem is a little bit different than the others we've seen, but
the idea of reducing the problem to a smaller size still holds. First,
we'll define a base case:

    A string of length 1 or less is a palindrome.

Nothing very controversial there, right? And it suggests an approach:
try to reduce the size of the string until we have a string of length 1
or less.

The main bit of insight we need is to realize that for a string to be a
palindrome, *the first and last characters must be the same*. If they
are, we can slice off the first and last characters, thus reducing the
problem size! We can then check if the remaining string is a palindrome
--- recursion! If the first and last characters aren't the same, there's
no chance the string is a palindrome. Translating all that to a
function:

.. code-block:: python

    def isPalindrome(s):
        # string of 1 or fewer characters
        # is necessarily a palindrome
        if len(s) <= 1:
            return True

        # if first and last characters are
        # the same, reduce the problem size,
        # and make recursive call
        elif s[0] == s[-1]:
            newstring = s[1:-1]
            return isPalindrome(newstring)

        # no chance that we've got a palindrome.
        # just return in abject failure.
        else:
            return False

Checking types
--------------

What happens if we call ``factorial`` and give it 1.5 as an argument?

.. code-block:: python

    >>> factorial(1.5)
    RuntimeError: Maximum recursion depth exceeded

It looks like an infinite recursion. But how can that be? There is a
base case—when ``n == 0``. But if ``n`` is not an integer, we can *miss*
the base case and recurse forever.

In the first recursive call, the value of ``n`` is 0.5. In the next, it
is -0.5. From there, it gets smaller (more negative), but it will never
be 0.

We have two choices. We can try to generalize the ``factorial`` function
to work with floating-point numbers, or we can make ``factorial`` check
the type of its argument. The first option is called the gamma
function [2]_ and it’s a little beyond the scope of this book. So we’ll
go for the second.

We can use the built-in function ``isinstance`` to verify the type of
the argument. While we’re at it, we can also make sure the argument is
positive:

.. code-block:: python

    def factorial (n):
        if not isinstance(n, int):
            print 'Factorial is only defined for integers.'
            return None
        elif n < 0:
            print 'Factorial is not defined for negative integers.'
            return None
        elif n == 0:
            return 1
        else:
            return n * factorial(n-1)

The first base case handles nonintegers; the second catches negative
integers. In both cases, the program prints an error message and returns
``None`` to indicate that something went wrong:

.. code-block:: python

    >>> factorial('fred')
    Factorial is only defined for integers.
    None
    >>> factorial(-2)
    Factorial is not defined for negative integers.
    None

If we get past both checks, then we know that :math:`n` is positive or
zero, so we can prove that the recursion terminates.

This program demonstrates a pattern sometimes called a **guardian**. The
first two conditionals act as guardians, protecting the code that
follows from values that might cause an error. The guardians make it
possible to prove the correctness of the code.

A theoretical aside
-------------------

We have only covered a subset of Python, but you might be interested to
know that this subset is a *complete* programming language, which means
that anything that can be computed can be expressed in this language.
Any program ever written could be rewritten using only the language
features you have learned so far (actually, you would need a few
commands to control devices like the keyboard, mouse, disks, etc., but
that’s all).

Proving that claim is a nontrivial exercise first accomplished by Alan
Turing, one of the first computer scientists (some would argue that he
was a mathematician, but a lot of early computer scientists started as
mathematicians). Accordingly, it is known as the Turing Thesis. For a
more complete (and accurate) discussion of the Turing Thesis, I
recommend Michael Sipser’s book *Introduction to the Theory of
Computation*.

Debugging
---------

Adding print statements at the beginning and end of a function can help
make the flow of execution more visible, especially when debugging
recursive functions. For example, here is a version of ``factorial``
with print statements:

.. code-block:: python

    def factorial(n):
        space = ' ' * (4 * n)
        print space, 'factorial', n
        if n == 0:
            print space, 'returning 1'
            return 1
        else:
            recurse = factorial(n-1)
            result = n * recurse
            print space, 'returning', result
            return result

``space`` is a string of space characters that controls the indentation
of the output. Here is the result of ``factorial(5)`` :

::

                         factorial 5
                     factorial 4
                 factorial 3
             factorial 2
         factorial 1
     factorial 0
     returning 1
         returning 1
             returning 2
                 returning 6
                     returning 24
                         returning 120

If you are confused about the flow of execution, this kind of output can
be helpful. It takes some time to develop effective scaffolding, but a
little bit of scaffolding can save a lot of debugging.

Glossary
--------

recursion:
    The process of calling the function that is currently executing.

base case:
    A conditional branch in a recursive function that does not make a
    recursive call.

infinite recursion:
    A recursion that doesn’t have a base case, or never reaches it.
    Eventually, an infinite recursion causes a runtime error.

.. rubric:: Exercises


1. Write a function that takes a possibly empty list of integers as
   a parameter, and recursively computes and returns the sum of the
   list of numbers. You can not use any built-in Python functions
   except for ``len``.

2. Write a function that takes a possibly empty string as a
   parameter and recursively produces a reversed copy of the string.

3. Similar to the last problem, write a function that takes a
   possibly empty *list* as a parameter (the list may contain *any*
   Python data types), and recursively produces a reversed copy of
   the list.

4. Read the following function and see if you can figure out what it
   does, then run it.

.. code-block:: python

   import turtle

   def draw(length, n):
       if n == 0:
           return
       angle = 50
       turtle.forward(length*n)
       turtle.left(angle)
       draw(length, n-1)
       turtle.right(2*angle)
       draw(length, n-1)
       turtle.left(angle)
       turtle.backward(length*n)

   draw(10, 4)
   turtle.done()

..

5. The Koch curve is a fractal that looks something like this:

.. figure:: figs/koch.png
   :align: center
   :alt: Koch curve fractal.

   Koch curve fractal.

..

   To draw a Koch curve with length :math:`x`, all you have to do is

   1. Draw a Koch curve with length :math:`x/3`.

   2. Turn left 60 degrees.

   3. Draw a Koch curve with length :math:`x/3`.

   4. Turn right 120 degrees.

   5. Draw a Koch curve with length :math:`x/3`.

   6. Turn left 60 degrees.

   7. Draw a Koch curve with length :math:`x/3`.

   The only exception is if :math:`x` is less than 3. In that case,
   you can just draw a straight line with length :math:`x`.

     a. Write a function called ``koch`` that takes a turtle and a
        length as parameters, and that uses the turtle to draw a Koch
        curve with the given length.

     b. Write a function called ``snowflake`` that draws three Koch
        curves to make the outline of a snowflake.

     c. The Koch curve can be generalized in several ways. See
        http://wikipedia.org/wiki/Koch_snowflake for examples and
        implement your favorite.

6. The Ackermann function, :math:`A(m, n)`, is defined [3]_ as:

   :math:`A(m,n) =`
       
   * :math:`n+1` if :math:`m = 0`
   * :math:`A(m-1,1)` if :math:`m > 0 and n = 0`
   * :math:`A(m-1, A(m, n-1))` if :math:`m > 0` and :math:`n > 0`

..

   Write a function named `ack` that evaluates Ackerman’s function.
   Use your function to evaluate `ack(3, 4)`, which should be 125. What
   happens for larger values of `m` and `n`?

7. A number, :math:`a`, is a power of :math:`b` if it is divisible
   by :math:`b` and :math:`a/b` is a power of :math:`b`. Write a
   function called ``is_power`` that takes parameters ``a`` and
   ``b`` and returns ``True`` if ``a`` is a power of ``b``.

8. The greatest common divisor (GCD) of :math:`a` and :math:`b` is
   the largest number that divides both of them with no
   remainder [4]_.

   One way to find the GCD of two numbers is Euclid’s algorithm,
   which is based on the observation that if :math:`r` is the
   remainder when :math:`a` is divided by :math:`b`, then
   :math:`gcd(a, b) = gcd(b, r)`. As a base case, we can consider
   :math:`gcd(a, 0) = a`.

   Write a function called ``gcd`` that takes parameters ``a`` and
   ``b`` and returns their greatest common divisor. If you need
   help, see http://wikipedia.org/wiki/Euclidean_algorithm.

.. rubric:: Footnotes

.. [1]
   See http://wikipedia.org/wiki/Fibonacci_number.

.. [2]
   See http://wikipedia.org/wiki/Gamma_function.

.. [3]
   See http://wikipedia.org/wiki/Ackermann_function.

.. [4]
   This exercise is based on an example from Abelson and Sussman’s
   *Structure and Interpretation of Computer Programs*.
