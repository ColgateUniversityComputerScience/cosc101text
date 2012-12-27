
# Functions in depth

## Adding new functions

So far, we have only been *using* the functions that come with Python,
but it is also possible to add new functions. A **function definition**
specifies the name of a new function and the sequence of statements to
execute when the function is called.

Here is an example:

    def print_lyrics():
        print "I'm a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."

`def` is a keyword that indicates that this is a function definition.
The name of the function is `print_lyrics`. The rules for function names
are the same as for variable names: letters, numbers and some
punctuation marks are legal, but the first character can’t be a number.
You can’t use a keyword as the name of a function, and you should avoid
having a variable and a function with the same name.

The empty parentheses after the name indicate that this function doesn’t
take any arguments. 

The first line of the function definition is called the **header**; the
rest is called the **body**.  The header has to end with a colon and the
body has to be indented.  By convention, the indentation is always four
spaces.  The body can contain any number of statements.  We've now seen
three *compound statements* that can include indented statement blocks:
the `for` statement, the `if` statement, and now the `def` statement.

If you type a function definition in interactive mode, the interpreter
prints ellipses (*...*) to let you know that the definition isn’t
complete:

    >>> def print_lyrics():
    ...     print "I'm a lumberjack, and I'm okay."
    ...     print "I sleep all night and I work all day."
    ...

To end the function, you have to enter an empty line (this is not
necessary in a script).

Defining a function creates a variable with the same name.

    >>> print print_lyrics
    <function print_lyrics at 0xb7e99e9c>
    >>> print type(print_lyrics)
    <type 'function'>

The value of `print_lyrics` is a **function object**, which has type
`'function'`.  The output from the `print print_lyrics` statement shows
a number in hexadecimal format (the number starting `"0x..."`).  The
number refers to the *memory location* of the function object (i.e.,
where that function exists in Python's memory space).

The syntax for calling the new function is the same as for built-in
functions:

    >>> print_lyrics()
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.

Once you have defined a function, you can use it inside another
function. For example, to repeat the previous refrain, we could write a
function called `repeat_lyrics`:

    def repeat_lyrics():
        print_lyrics()
        print_lyrics()

And then call `repeat_lyrics`:

    >>> repeat_lyrics()
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.
    I'm a lumberjack, and I'm okay.
    I sleep all night and I work all day.

But that’s not really how the song goes.

## Definitions and uses

Pulling together the code fragments from the previous section, the whole
program looks like this:

    def print_lyrics():
        print "I'm a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."

    def repeat_lyrics():
        print_lyrics()
        print_lyrics()

    repeat_lyrics()

This program contains two function definitions: `print_lyrics` and
`repeat_lyrics`.  Function definitions get executed just like other
statements, but the effect is to create function objects. The statements
inside the function do not get executed until the function is called,
and the function definition generates no output.

As you might expect, you have to create a function before you can
execute it.  In other words, the function definition has to be executed
before the first time it is called.

> **Examples**:
>
> 1. Move the last line of this program to the top, so the function call
>    appears before the definitions. Run the program and see what error
>    message you get.
>
> 1. Move the function call back to the bottom and move the definition of
>    `print_lyrics` after the definition of `repeat_lyrics`.  What happens
>    when you run this program?  Why?

## Flow of execution

In order to ensure that a function is defined before its first use, you
have to know the order in which statements are executed, which is called
the **flow of execution**.

Execution always begins at the first statement of the program.
Statements are executed one at a time, in order from top to bottom.

Function definitions do not alter the flow of execution of the program,
but remember that statements inside the function are not executed until
the function is called.

A function call is like a detour in the flow of execution. Instead of
going to the next statement, the flow jumps to the body of the function,
executes all the statements there, and then comes back to pick up
exactly where it left off.

That sounds simple enough, until you remember that one function can call
another. While in the middle of one function, the program might have to
execute the statements in another function. But while executing that new
function, the program might have to execute yet another function!

Fortunately, Python is good at keeping track of where it is, so each
time a function completes, the program picks up where it left off in the
function that called it. When it gets to the end of the program, it
terminates.

What’s the moral of this sordid tale?  When you read a program, you
don’t always want to read from top to bottom.  Usually, you want to
follow the flow of execution and read the program as Python would
interpret it.

## Parameters and arguments

Some of the built-in functions we have seen require arguments. For
example, when you call `math.sin` you pass a number as an argument. Some
functions take more than one argument: `math.pow` takes two, the base
and the exponent.

Inside the function, the arguments are assigned to variables called
**parameters**. Here is an example of a user-defined function that takes
an argument:

    def print_twice(bruce):
        print bruce
        print bruce

This function assigns the argument to a parameter named `bruce`. When
the function is called, it prints the value of the parameter (whatever
it is) twice.

This function works with any value that can be printed.

    >>> print_twice('Spam')
    Spam
    Spam
    >>> print_twice(17)
    17
    17
    >>> print_twice(math.pi)
    3.14159265359
    3.14159265359

The same rules of composition that apply to built-in functions also
apply to user-defined functions, so we can use any kind of expression as
an argument for `print_twice`:

    >>> print_twice('Spam '*4)
    Spam Spam Spam Spam
    Spam Spam Spam Spam
    >>> print_twice(math.cos(math.pi))
    -1.0
    -1.0

The argument is evaluated before the function is called, so in the
examples the expressions `'Spam '*4` and `math.cos(math.pi)` are only
evaluated once.

You can also use a variable as an argument:

    >>> michael = 'Eric, the half a bee.'
    >>> print_twice(michael)
    Eric, the half a bee.
    Eric, the half a bee.

The name of the variable we pass as an argument (`michael`) has nothing
to do with the name of the parameter (`bruce`). It doesn’t matter what
the value was called back home (in the caller); here in `print_twice`,
we call it `bruce`.

## Variables and parameters are local

When you create a variable inside a function, it is **local**, which
means that it only exists inside the function. For example:

    def cat_twice(part1, part2):
        cat = part1 + part2
        print_twice(cat)

This function takes two arguments, concatenates them, and prints the
result twice. Here is an example that uses it:

    >>> line1 = 'Bing tiddle '
    >>> line2 = 'tiddle bang.'
    >>> cat_twice(line1, line2)
    Bing tiddle tiddle bang.
    Bing tiddle tiddle bang.

When `cat_twice` terminates, the variable `cat` is destroyed. If we try
to print it, we get an exception:

    >>> print cat
    NameError: name 'cat' is not defined

Parameters are also local.  For example, outside `print_twice`, there is
no such thing as `bruce`.

## Return values

### The special type `None`

Some of the built-in functions we have used, such as the math functions,
produce results.  When you call a function that returns a result, like
`math.sqrt`, you almost always want to do something with the result; for
example, you might assign it to a variable or use it as part of an
expression:

    x = math.cos(radians)
    golden = (math.sqrt(5) + 1) / 2

When you call a function in interactive mode, Python displays the
result:

    >>> math.sqrt(5)
    2.2360679774997898

But in a script, if you call a function that returns a result all by
itself, the return value is lost forever, and does not even show up
in the console as output!

    math.sqrt(5)

This script computes the square root of 5, but since it doesn’t store or
display the result (i.e., there is no `print` statement), it is not very
useful.

Functions that do not return anything (also called "void functions")
might display something on the screen or have some other effect, but
they don’t explicitly pass back a result.  However, Python will
implicitly return the special value `None`.  Say `print_twice` is
defined as follows:

    def print_twice(s):
        print s
        print s
        # nothing returned from this function

In the interactive interpreter, we call the function and assign its
result to the variable `result`:

    >>> result = print_twice('Bing')
    Bing
    Bing
    >>> print result
    None

The value `None` is not the same as the string `'None'`.  It is a
special value that has its own type:

    >>> print type(None)
    <type 'NoneType'>

### Functions with return values

If we want a function to hand back a result to the caller of the
function, we can use the `return` statement with an expression.  For
example, the following function `area` returns the area of a circle with
a given radius:

    import math
    
    def area(radius):
        temp = math.pi * radius**2
        return temp

The `return` statement means: *"Return immediately from this function
and use the following expression as a return value."*  The expression
can be arbitrarily complicated, so we could have written this function
more concisely:

    def area(radius):
        return math.pi * radius**2

On the other hand, **temporary variables** like `temp` often make
debugging easier.

Sometimes it is useful to have multiple return statements, one in each
branch of a conditional:

    def absolute_value(x):
        if x < 0:
            return -x
        else:
            return x

Since these `return` statements are in an alternative conditional, only
one will be executed.

As soon as a return statement executes, the function terminates without
executing any subsequent statements.  Code that appears after a `return`
statement, or any other place the flow of execution can never reach, is
called **dead code**.

In a function that returns a result, it is a good idea to ensure that
every possible path through the program hits a `return` statement. For
example:

    # warning: this is problematic code!
    def absolute_value(x):
        if x < 0:
            return -x
        if x > 0:
            return x

This function is incorrect because if `x` happens to be 0, neither
condition is true, and the function ends without hitting a `return`
statement. If the flow of execution gets to the end of a function, the
return value is `None`, which is not the absolute value of 0.

    >>> print absolute_value(0)
    None

By the way, Python provides a built-in function called `abs` that
computes absolute values.

> **Example**:
>
> 1. Write a `compare` function that returns `1` if `x > y`, `0` if
>    `x == y`, and `-1` if `x < y`.
>

## Stack diagrams

To keep track of which variables can be used where, it is sometimes
useful to draw a **stack diagram**.  Like state diagrams, stack diagrams
show the value of each variable, but they also show the function each
variable belongs to.

Each function is represented by a **frame** (or "stack frame").  A frame
is a box with the name of a function beside it and the parameters and
variables of the function inside it.  The stack diagram for the previous
example looks like this:

![Example stack diagram.](figs/stack.png) 

The frames are arranged in a stack that indicates which function called
which, and so on.  In this example, `print_twice` was called by
`cat_twice`, and `cat_twice` was called by `__main__`, which is a
special name for the topmost frame. When you create a variable outside
of any function, it belongs to `__main__`.

Each parameter refers to the same value as its corresponding argument.
So, `part1` has the same value as `line1`, `part2` has the same value as
`line2`, and `bruce` has the same value as `cat`.

If an error occurs during a function call, Python prints the name of the
function, and the name of the function that called it, and the name of
the function that called *that*, all the way back to `__main__`.

For example, if you try to access `cat` from within `print_twice`, you
get a `NameError`:

    Traceback (innermost last):
      File "test.py", line 13, in __main__
        cat_twice(line1, line2)
      File "test.py", line 5, in cat_twice
        print_twice(cat)
      File "test.py", line 9, in print_twice
        print cat
    NameError: name 'cat' is not defined

This list of functions is called a **traceback**.  It tells you what
program file the error occurred in, and what line, and what functions
were executing at the time.  It also shows the line of code that caused
the error (i.e., line 9, in the function `print_twice`).

The order of the functions in the traceback is the same as the order of
the frames in the stack diagram.  The function that is currently running
is at the bottom.^[Stack diagrams can either be drawn starting from the
top, working down, or from the bottom, working up.  It depends which
hemisphere (northern or southern) you come from.  (Just kidding.  As
long as you're consistent, it doesn't matter which way you draw it.)]


\label{sec:booleanfn}
<a name="sec:booleanfn"></a>

## Boolean functions

Functions can return booleans, which is often convenient for hiding
complicated tests inside functions. For example:

    def is_divisible(x, y):
        if x % y == 0:
            return True
        else:
            return False

It is common to give boolean functions names that sound like yes/no
questions; `is_divisible` returns either `True` or `False` to indicate
whether `x` is divisible by `y`.

Here is an example:

    >>> is_divisible(6, 4)
    False
    >>> is_divisible(6, 3)
    True

The result of the `==` operator is a boolean, so we can write the
function more concisely by returning it directly:

    def is_divisible(x, y):
        return x % y == 0

Boolean functions are often used in conditional statements:

    if is_divisible(x, y):
        print 'x is divisible by y'

It might be tempting to write something like:

    if is_divisible(x, y) == True:
        print 'x is divisible by y'

But the extra comparison is unnecessary.

> **Example**:
>
> 1. Write a function `is_between(x, y, z)` that returns `True` if
> $x \le y \le z$ or `False` otherwise.

## Debugging

### Adding `print` statements

Breaking a large program into smaller functions creates natural
checkpoints for debugging.  If a function is not working, there are three
possibilities to consider: 

-   There is something wrong with the arguments the function is getting.
-   There is something wrong with the function.
-   There is something wrong with the return value or the way it is
    being used.

To rule out the first possibility, you can add a `print` statement at
the beginning of the function and display the values of the parameters
(and maybe their types). Or you can write code that checks the
preconditions explicitly.

If the parameters look good, add a `print` statement before each
`return` statement that displays the return value. If possible, check
the result by hand. Consider calling the function with values that make
it easy to check the result.

If the function seems to be working, look at the function call to make
sure the return value is being used correctly (or used at all!).

### Unit testing and `assert`

After you think you've solved a problem, *how do you know your program
behaves as intended?* You've probably run it once or twice to make sure
it does *something*, and maybe you've even tested it out with a few
different inputs.  But we can do better.

Especially when writing functions that perform a specific task, it is
common to create **test cases** to call the function with specific
inputs to ensure that the function works correctly and returns the "right"
thing.  This approach to testing is called **unit testing** because of the focus on testing individual functional units (i.e., the functions!) in a program.

You can think of testing your program in this way as something of an
*experiment*.  First, you decide on the inputs (parameters) you want to pass to your function.  The output you expect from the function is
basically a hypothesis which can easily be tested by running the
function with your chosen input: if it produces the expected output,
then your hypothesis was correct.  If not, then there is probably
something wrong with the function.  (There may also be something wrong
with the output you expected --- for this reason you need to be very
careful when devising tests!)

There is a built-in function called `assert` that can help with
developing unit tests to ensure a function works as expected.  The
`assert` function takes a Boolean expression as a parameter.  If the
expression evaluates to `False`, the `assert` function will cause your
program to crash.  This is a good thing!  The crash lets you know that
something is wrong and needs to be fixed!  If the expression in the
`assert` function call evaluates to `True`, essentially nothing happens
--- the next line in the program will be executed.

Here's an example.  The following function is supposed to take one
string as a parameter, and count up and return the number of upper- and
lower-case `'A'`s in the string.  It has two bugs.  Before you read on,
see if you can figure out what they are.

    # function should count up all the lower- and upper-case
    # A's in a string and return the count.
    def count_As(mystring):
        count = 0
        for char in mystring:
            if char == 'a':
                count += 1

Let's think of four test cases for our unit test of this function:

 * If we call `count_As` with `'xyz'` (or an empty string), it should return 0.
 * If we call `count_As` with `'abc'`, it should return 1.
 * If we call `count_As` with `'ABC'`, it should also return 1.
 * If we call `count_As` with `'Abracadabra'`, it should return 5.
 
We can construct calls to `assert` by including a Boolean expression that
calls the function, and compares the return value to the expected output.  In the 
`assert` calls, we are making assertions (duh!) about what the output should be:

    def unit_tests():
        # three test cases using three different
        # strings to test whether the count_As
        # function works correctly
        assert(count_As("xyz") == 0)
        assert(count_As("abc") == 1)
        assert(count_As("ABC") == 1)
        assert(count_As("Abracadabra") == 5)

    unit_tests()

When we run this program, we'll first call `unit_tests`, then we'll call
each of the `assert` statements, in order.  Because of the bugs in `count_As`,
we'll crash on the first `assert` call:

    Traceback (most recent call last):
      File "test2.py", line 16, in <module>
        unit_tests()
      File "test2.py", line 11, in unit_tests
        assert(count_As("xyz") == 0)
    AssertionError

We see from the function stack traceback that the program died on line
11, which was the first call to `assert`.  The program crashes because
the return value of calling `count_As("xyz")` is not 0 (although it
should be!)  If we look carefully at the `count_As` function, we'll see
one problem: there's no `return` statement!  The function currently
*always* returns `None`. Easy to fix:

    def count_As(mystring):
        count = 0
        for char in mystring:
            if char == 'a':
                count += 1
        return count # added a return statement!

When we run the program now, we hit another `AssertionError`:

    Traceback (most recent call last):
      File "test2.py", line 17, in <module>
        unit_tests()
      File "test2.py", line 14, in unit_tests
        assert(count_As("ABC") == 1)
    AssertionError

Now, the program crashes on the `assert` on line 14.  If we carefully
examine the code (and perhaps add a `print` statement or two to help us
to see what's going on in the function), we can see that we're only
counting lower case `'a'`s, not upper case.  Once we fix that problem,
all the Boolean expressions in the `assert` calls will evaluate to
`True`, and the program will finish without crashing.  This will
indicate that all our tests passed successfully.

Interestingly, an increasingly common practice within the software industry is to specify a set of
test cases *before* writing a function.  The idea is that the activity
of specifying a set of test cases helps to clarify what a function
should do. Once the test cases are specified, the function can be
written.  Once all the test cases successfully pass, the function is
done.

The hard part of testing a program is figuring out what a good set of
test cases should be.  Here are some rules of thumb:

 * Pick one or two "normal" inputs and expected outputs.  Think of
   parameters you expect to be commonly passed to the function and ensure
   that the function works for those parameters.

 * Think about any "corner cases" --- parameters that are just outside
   any "normal" or expected values.  For example, if you usually expect to
   get the integers 1-10 as parameters to a function, write a tests for the
   valid bounds (1 and 10) as well as values just outside those bounds (0 and
   11).
   
 * Think deviously.  What sorts of inputs might cause problems for a
   function?  For example, if a function expects a string as input, what
   happens if an empty string (`""`) gets passed in?

You can also read more about unit testing on Wikipedia:
<http://en.wikipedia.org/wiki/Unit_testing>.

## Glossary

function:
  ~ A named sequence of statements that performs some useful operation.
    Functions may or may not take arguments and may or may not produce a
    result.

function definition:
  ~ A statement that creates a new function, specifying its name,
    parameters, and the statements it executes.

function object:
  ~ A value created by a function definition. The name of the function
    is a variable that refers to a function object.

function header:
  ~ The first line of a function definition.

function body:
  ~ The sequence of statements inside a function definition.

parameter:
  ~ A name used inside a function to refer to the value passed as an
    argument.

function call:
  ~ A statement that executes a function. It consists of the function
    name followed by an argument list.

argument:
  ~ A value provided to a function when the function is called. This
    value is assigned to the corresponding parameter in the function.

local variable:
  ~ A variable defined inside a function. A local variable can only be
    used inside its function.

return value:
  ~ The result of a function. If a function call is used as an
    expression, the return value is the value of the expression.

flow of execution:
  ~ The order in which statements are executed during a program run.

stack diagram:
  ~ A graphical representation of a stack of functions, their variables,
    and the values they refer to.

frame:
  ~ A box in a stack diagram that represents a function call. It
    contains the local variables and parameters of the function.

traceback:
  ~ A list of the functions that are executing, printed when an
    exception occurs.

temporary variable:
  ~ A variable used to store an intermediate value in a complex
    calculation.

dead code:
  ~ Part of a program that can never be executed, often because it
    appears after a `return` statement.

`None`:
  ~ A special value returned by functions that have no return statement
    or a return statement without an argument.

test case:
  ~ A set of parameters (inputs) and expected outputs for a function that 
    can test whether the function behaves as expected.
  
unit testing:
  ~ The idea of testing smaller pieces of a program, like a function, rather
    than testing the whole program at once.

assertion:
  ~ A propositional statement that you expect to be `True` at some point in a
    program.  The built-in `assert` function can be used to test Boolean 
    propositional statements.
   
## Exercises

> 1. Fix the last bug in the `count_As` function.  Can you think of any
>    additional test cases that should be added for this function?
>
> 1. Write a function named `compare_ab` that takes one string as parameters,
>    and counts the occurrences of `'a'`s and `'b'`s in the string.  The function
>    should return `True` if the number of `'a'`s and `'b'`s is the same, and
>    `False` otherwise.  Think of a set of test cases for this function, and
>    write them.
> 
> 1. Write a function named `right_justify` that takes a string named `s`
>    as a parameter and prints the string with enough leading spaces so
>    that the last letter of the string is in column 60 of the display.
> 
>            >>> right_justify('allen')
>                                                        allen
> 
> 1. Write a function called `is_leap` that takes a year value as a
>    parameter, and returns `True` if the year is a leap year or `False` if
>    it is not.  Refer to one of the exercises from the last chapter for the
>    definition of a leap year.
> 
> 
> 1. A function object is a value you can assign to a variable or pass as
>    an argument. For example, `do_twice` is a function that takes a
>    function object as an argument and calls it twice:
> 
>            def do_twice(f):
>                f()
>                f()
> 
>     Here's an example that uses `do_twice` to call a function named
>     `print_spam` twice.
> 
>            def print_spam():
>                print 'spam'
>         
>            do_twice(print_spam)
> 
>        a. Type this example into a script and test it.
>      
>        b. Modify `do_twice` so that it takes two arguments, a function
>           object and a value, and calls the function twice, passing the
>           value as an argument.
>      
>        c. Write a more general version of `print_spam`, called
>           `print_twice`, that takes a string as a parameter and prints it
>           twice.
>      
>        d. Use the modified version of `do_twice` to call `print_twice`
>           twice, passing `'spam'` as an argument.
>      
>        e. Define a new function called `do_four` that takes a function
>           object and a value and calls the function four times, passing the
>           value as a parameter. There should be only two statements in the
>           body of this function, not four.
> 
>  1. This exercise^[Based on an exercise in Oualline, *Practical C
>     Programming, Third Edition*, O'Reilly (1997)] can be done using 
>     only the statements and other features we have learned so far.
> 
>     Write a function that draws a grid like the following:
> 
>             + - - - - + - - - - +
>             |         |         |
>             |         |         |
>             |         |         |
>             |         |         |
>             + - - - - + - - - - +
>             |         |         |
>             |         |         |
>             |         |         |
>             |         |         |
>             + - - - - + - - - - +
> 
>     Hint: to print more than one value on a line, you can print a
>     comma-separated sequence:
> 
>             print '+', '-'
> 
>     If the sequence ends with a comma, Python leaves the line
>     unfinished, so the value printed next appears on the same line.
> 
>             print '+', 
>             print '-'
> 
>     The output of these statements is `'+ -'`.
> 
>     A `print` statement all by itself ends the current line and goes
>     to the next line.
>
> 
> 1. Use the previous function to draw a similar grid with four rows
>    and four columns.
> 
> 1. Write a function that takes one integer named `size` as a parameter
>    and prints an equilateral triangle composed of asterisks of length `size`.
>    For example, the call `make_triangle(4)` should result in the following
>    triangle printed:
> 
>               *
>              * *
>             * * *
>            * * * *
> 
> 1. Draw a stack diagram for the following program. What does the program
>    print?
> 
>            def b(z):
>                prod = a(z, z)
>                print z, prod
>                return prod
>           
>            def a(x, y):
>                x = x + 1
>                return x * y
>           
>            def c(x, y, z):
>                sum = x + y + z
>                pow = b(sum)**2
>                return pow
>           
>            x = 1
>            y = x + 1
>            print c(x, y+3, x+y)
>
>
> 1. Fermat’s Last Theorem says that there are no integers $a$, $b$, and
>    $c$ such that: $$a^n + b^n = c^n $$ for any values of $n$ greater than
>    2.
> 
>      a.  Write a function named `check_fermat` that takes four
>          parameters---`a`, `b`, `c` and `n`---and that checks to see if
>          Fermat’s theorem holds. If $n$ is greater than 2 and it turns out
>          to be true that $$a^n + b^n = c^n $$, the function should return
>          `True`.  Otherwise, the function should return `False`.
>  
>      b.  Write a function that prompts the user to input values for `a`,
>          `b`, `c` and `n`, converts them to integers, and uses
>          `check_fermat` to check whether they violate Fermat’s theorem.
>          If the result of calling `check_fermat` is `False`, this function
>          should print "Holy smokes, Fermat was wrong!".  Otherwise, it should
>          print "No, that doesn't work."
> 
> 1. If you are given three sticks, you may or may not be able to arrange
>    them in a triangle. For example, if one of the sticks is 12 inches
>    long and the other two are one inch long, it is clear that you will
>    not be able to get the short sticks to meet in the middle. For any
>    three lengths, there is a simple test to see if it is possible to form
>    a triangle:
> 
>     If any of the three lengths is greater than the sum of the other
>     two, then you cannot form a triangle. Otherwise, you can.
> 
>        a.  Write a function named `is_triangle` that takes three integers as
>            arguments, and that returns `True` or `False`, depending on
>            whether you can or cannot form a triangle from sticks with the
>            given lengths.
>        
>        b.  Write a function that prompts the user to input three stick
>            lengths, converts them to integers, and uses `is_triangle` to
>            check whether sticks with the given lengths can form a triangle.

<!-- end of chapter -->

