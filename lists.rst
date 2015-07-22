*****
Lists
*****

In this chapter, we go into more depth on lists. Lists are an incredibly
useful data structure for solving a variety of problems. Before we dive
in, you may wish to review the earlier section on lists, which appeared
at the beginning of the "iteration" chapter.

List slices
-----------

The slice operator we've used for strings also works on lists:

.. code-block:: python

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> t[1:3]
    ['b', 'c']
    >>> t[:4]
    ['a', 'b', 'c', 'd']
    >>> t[3:]
    ['d', 'e', 'f']

If you omit the first index, the slice starts at the beginning. If you
omit the second, the slice goes to the end. So if you omit both, the
slice is a copy of the whole list.

.. code-block:: python

    >>> t[:]
    ['a', 'b', 'c', 'd', 'e', 'f']

Since lists are mutable, it is often useful to make a copy before
performing operations that fold, spindle, or mutilate lists. [1]_

A slice operator on the left side of an assignment can update multiple
elements:

.. code-block:: python

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> t[1:3] = ['x', 'y']
    >>> print t
    ['a', 'x', 'y', 'd', 'e', 'f']

List methods
------------

Python provides methods that operate on lists. For example, ``append``
adds a new element to the end of a list:

.. code-block:: python

    >>> t = ['a', 'b', 'c']
    >>> t.append('d')
    >>> print t
    ['a', 'b', 'c', 'd']

``extend`` takes a list as an argument and appends all of the elements:

.. code-block:: python

    >>> t1 = ['a', 'b', 'c']
    >>> t2 = ['d', 'e']
    >>> t1.extend(t2)
    >>> print t1
    ['a', 'b', 'c', 'd', 'e']

This example leaves ``t2`` unmodified.

``sort`` arranges the elements of the list from low to high:

.. code-block:: python

    >>> t = ['d', 'c', 'e', 'b', 'a']
    >>> t.sort()
    >>> print t
    ['a', 'b', 'c', 'd', 'e']

Note that the append, extend, and sort methods do not return anything
(except None). So, a statement like:

.. code-block:: python

    t = t.sort()

will result in the list ``t`` reassigned to ``None``.

There is a ``sorted`` *function* built in to Python that takes a list as
a parameter, and returns a new, sorted list. The original list is
unchanged:

.. code-block:: python

    >>> t = ['d', 'c', 'e', 'b', 'a']
    >>> sorted(t)
    ['a', 'b', 'c', 'd', 'e']
    >>> print t
    ['d', 'c', 'e', 'b', 'a']

There is also a ``reverse`` method for lists, and a ``reversed``
*function* that work somewhat similarly to ``sort`` and ``sorted``. The
``reversed`` function, instead of returning a list, returns an
*iterator*. The way to turn the iterator into a list is to compose the
list function with the ``reversed`` function:

.. code-block:: python

    >>> t = ['a', 'b', 'c', 'd', 'e']
    >>> t.reverse()
    >>> print t
    ['e', 'd', 'c', 'b', 'a']
    >>> reversed(t)
    <listreverseiterator object at 0x10f1e56d0>
    >>> list(reversed(t))
    ['a', 'b', 'c', 'd', 'e']
    >>> print t
    ['e', 'd', 'c', 'b', 'a']

The ``count`` method, similar to strings, takes one item as a parameter
and returns an integer count of occurrences of all identical items in
the list:

.. code-block:: python

    >>> t = ['d','c','e','b','a','c','d','c']
    >>> t.count('d')
    2
    >>> t.count('a')
    1
    >>> t.count('x')
    0

The ``index`` method, again, similar to strings, takes up to two
parameters. The first parameter is an item to search for, and the second
(optional) parameter is the starting index to search from. If a second
parameter is not specified, the default value of 0 is used. Importantly,
if an item you search for (i.e., the first parameter to ``index``) is
*not* in the list, you'll get a ``ValueError`` exception. Note that
there is no ``find`` method for lists.

.. code-block:: python

    >>> t.index('c')
    1
    >>> t.index('c',3)
    5
    >>> t.index('x')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 'x' is not in list

Deleting elements
-----------------

There are several ways to delete elements from a list. If you know the
index of the element you want, you can use ``pop``:

.. code-block:: python

    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)
    >>> print t
    ['a', 'c']
    >>> print x
    b

``pop`` modifies the list and returns the element that was removed. If
you don’t provide an index, it deletes and returns the last element.

If you don’t need the removed value, you can use the ``del`` operator:

.. code-block:: python

    >>> t = ['a', 'b', 'c']
    >>> del t[1]
    >>> print t
    ['a', 'c']

If you know the element you want to remove (but not the index), you can
use ``remove``:

.. code-block:: python

    >>> t = ['a', 'b', 'c']
    >>> t.remove('b')
    >>> print t
    ['a', 'c']

The return value from ``remove`` is ``None``.

To remove more than one element, you can use ``del`` with a slice index:

.. code-block:: python

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> del t[1:5]
    >>> print t
    ['a', 'f']

As usual, the slice selects all the elements up to, but not including,
the second index.

Lists and strings
-----------------

A string is a sequence of characters and a list is a sequence of values,
but a list of characters is not the same as a string. To convert from a
string to a list of characters, you can use ``list``:

.. code-block:: python

    >>> s = 'spam'
    >>> t = list(s)
    >>> print t
    ['s', 'p', 'a', 'm']

Because ``list`` is the name of a built-in function, you should avoid
using it as a variable name. I also avoid ``l`` because it looks too
much like ``1``. So that’s why many of the examples in this chapter use
``t``.

The ``list`` function breaks a string into individual letters. If you
want to break a string into words, you can use the ``split`` method, as
we saw in the strings chapter:

.. code-block:: python

    >>> s = 'pining for the fjords'
    >>> t = s.split()
    >>> print t
    ['pining', 'for', 'the', 'fjords']

An optional argument called a **delimiter** specifies which characters
to use as word boundaries. The following example uses a hyphen as a
delimiter:

.. code-block:: python

    >>> s = 'spam-spam-spam'
    >>> delimiter = '-'
    >>> s.split(delimiter)
    ['spam', 'spam', 'spam']

``join`` is the inverse of ``split``. It takes a list of strings and
concatenates the elements. ``join`` is a string method, so you have to
invoke it on the delimiter and pass the list as a parameter:

.. code-block:: python

    >>> t = ['pining', 'for', 'the', 'fjords']
    >>> delimiter = ' '
    >>> delimiter.join(t)
    'pining for the fjords'

In this case the delimiter is a space character, so ``join`` puts a
space between words. To concatenate strings without spaces, you can use
the empty string, ``''``, as a delimiter.

Objects and values
------------------

If we execute these assignment statements:

.. code-block:: python

    a = 'banana'
    b = 'banana'

We know that ``a`` and ``b`` both refer to a string, but we don’t know
whether they refer to the *same* string. There are two possible states:

.. figure:: figs/list1.png
   :align: center
   :alt: Variables referring to different objects, and variables that refer to the same object.

   Variables referring to different objects, and variables that refer to
   the same object.

In one case, ``a`` and ``b`` refer to two different objects that have
the same value. In the second case, they refer to the same object.

To check whether two variables refer to the same object, you can use the
``is`` operator.

.. code-block:: python

    >>> a = 'banana'
    >>> b = 'banana'
    >>> a is b
    True

In this example, Python only created one string object, and both ``a``
and ``b`` refer to it.

But when you create two lists, you get two objects:

.. code-block:: python

    >>> a = [1, 2, 3]
    >>> b = [1, 2, 3]
    >>> a is b
    False

So the state diagram looks like this:

.. figure:: figs/list2.png
   :align: center
   :alt: Variables that refer to two different list objects.

   Variables that refer to two different list objects.

In this case we would say that the two lists are **equivalent**, because
they have the same elements, but not **identical**, because they are not
the same object. If two objects are identical, they are also equivalent,
but if they are equivalent, they are not necessarily identical.

Until now, we have been using “object” and “value” interchangeably, but
it is more precise to say that an object has a value. If you execute
``[1,2,3]``, you get a list object whose value is a sequence of
integers. If another list has the same elements, we say it has the same
value, but it is not the same object.

Aliasing
--------

If ``a`` refers to an object and you assign ``b = a``, then both
variables refer to the same object:

.. code-block:: python

    >>> a = [1, 2, 3]
    >>> b = a
    >>> b is a
    True

The state diagram looks like this:

.. figure:: figs/list3.png
   :align: center
   :alt: Variables that are "aliases" of each other; they refer to the same list object.

   Variables that are "aliases" of each other; they refer to the same
   list object.

The association of a variable with an object is called a **reference**.
In this example, there are two references to the same object.

An object with more than one reference has more than one name, so we say
that the object is **aliased**.

If the aliased object is mutable, changes made with one alias affect the
other:

.. code-block:: python

    >>> b[0] = 17
    >>> print a
    [17, 2, 3]

Although this behavior can be useful, it is error-prone. In general, it
is safer to avoid aliasing when you are working with mutable objects.

For immutable objects like strings, aliasing is not as much of a
problem. In this example:

.. code-block:: python

    a = 'banana'
    b = 'banana'

It almost never makes a difference whether ``a`` and ``b`` refer to the
same string or not.

List arguments
--------------

When you pass a list to a function, the function gets a reference to the
list. If the function modifies a list parameter, the caller sees the
change. For example, ``delete_head`` removes the first element from a
list:

.. code-block:: python

    def delete_head(t):
        del t[0]

Here’s how it is used:

.. code-block:: python

    >>> letters = ['a', 'b', 'c']
    >>> delete_head(letters)
    >>> print letters
    ['b', 'c']

The parameter ``t`` and the variable ``letters`` are aliases for the
same object. The stack diagram looks like this:

.. figure:: figs/stack5.png
   :align: center
   :alt: Variable ``letters`` and parameter variable ``t`` refer to the same list object in memory.

   Variable ``letters`` and parameter variable ``t`` refer to the same
   list object in memory.

Since the list is shared by two frames, I drew it between them.

It is important to distinguish between operations that modify lists and
operations that create new lists. For example, the ``append`` method
modifies a list, but the ``+`` operator creates a new list:

.. code-block:: python

    >>> t1 = [1, 2]
    >>> t2 = t1.append(3)
    >>> print t1
    [1, 2, 3]
    >>> print t2
    None

    >>> t3 = t1 + [3]
    >>> print t3
    [1, 2, 3]
    >>> t2 is t3
    False

This difference is important when you write functions that are supposed
to modify lists. For example, this function *does not* delete the head
of a list:

.. code-block:: python

    def bad_delete_head(t):
        t = t[1:]              # WRONG!

The slice operator creates a new list and the assignment makes ``t``
refer to it, but none of that has any effect on the list that was passed
as an argument.

An alternative is to write a function that creates and returns a new
list. For example, ``tail`` returns all but the first element of a list:

.. code-block:: python

    def tail(t):
        return t[1:]

This function leaves the original list unmodified. Here’s how it is
used:

.. code-block:: python

    >>> letters = ['a', 'b', 'c']
    >>> rest = tail(letters)
    >>> print rest
    ['b', 'c']

**Examples**:

    1. Write a function called ``chop`` that takes a list and modifies
       it, removing the first and last elements, and returns ``None``.

    2. Write a function called ``middle`` that takes a list and returns
       a new list that contains all but the first and last elements.

Searching for items in a list
-----------------------------

Say that we have a very large list of words called ``wordlist``, and we
want to check whether the word ``zyzzy`` is in the list. We have a few
options so far:

1. The ``in`` operator.
2. The list ``count`` method (if the count is greater than zero, the
   word is in the list).
3. The list ``index`` method.
4. A "homegrown" function that searches the list, one word after
   another.

The first two of the four options above just tell us whether the word is
in the list, and the last two can tell us the *location* (index) of the
word in the list. Taking approach 3, if we wanted to write a function
called ``findWord`` that returns the index of the word in the list (or
-1 if the word isn't found), here's how we could do it:

.. code-block:: python

    def findWord(wordlist, word):
        '''
        Check whether word is in the wordlist.  Return
        the index of the word if found, or -1 otherwise.
        '''
        try:
            # The index method causes a ValueError exception
            # if the item we're searching for is not found.
            return wordlist.index(word)
        except:
            # if we get here, we know the word isn't in
            #  the list, so just return -1.
            return -1

**Examples**:

    1. Write a ``findWord2`` function to implement option 4: it
       shouldn't use any list methods while doing the same thing as
       ``findWord``. That is, it should search the wordlist for the word
       and return the index where it occurs. If the word isn't found,
       the function should return -1.

    2. Say we have a list of 100,000 words. If the word we're looking
       for is not in the list, how many comparisons between the word
       we're searching for and a word in the list do we need to make?
       (This is the *worst case* situation for trying to find a word. It
       should be pretty easy to identify the number of comparisons we
       have to make.)

For all four options above, the worst case is pretty ugly: we have to
search the entire list. This search technique is called **linear
search**, because we have to linearly search each and every item in the
list. Even with a fast, modern computer, linearly searching a very large
list is best avoided if possible.

What if we were to simply *sort* the list of words? If the list is in
alphabetical order, we can speed things up with a **bisection search**
(also known as **binary search**), which is similar to what you do when
you look a word up in the dictionary. You start in the middle and check
to see whether the word you are looking for comes before the word in the
middle of the list. If so, then you search the first half of the list
the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list
has 115,000 words, it will take about 17 steps to find the word or
conclude that it’s not there. This is a huge improvement over the worst
case with linear search! Writing a function to perform a binary search
is left as an exercise, and interestingly, binary search lends itself
nicely to a recursive implementation.

You should also know that Python includes a ``bisect`` module that
contains an implementation of binary search. You can check out the
documentation for it here: http://docs.python.org/library/bisect.html.

Map, filter and reduce
----------------------

To add up all the numbers in a list, you can use a loop like this:

.. code-block:: python

    def add_all(t):
        total = 0
        for x in t:
            total += x
        return total

``total`` is initialized to 0. Each time through the loop, ``x`` gets
one element from the list.

As the loop executes, ``total`` accumulates the sum of the elements; a
variable used this way is sometimes called an **accumulator**.

Adding up the elements of a list is such a common operation that Python
provides the built-in function, ``sum``:

.. code-block:: python

    >>> t = [1, 2, 3]
    >>> sum(t)
    6

An operation like this that combines a sequence of elements into a
single value is sometimes called **reduce**.

Sometimes you want to traverse one list while building another. For
example, the following function takes a list of strings and returns a
new list that contains capitalized strings:

.. code-block:: python

    def capitalize_all(t):
        res = []
        for s in t:
            res.append(s.capitalize())
        return res

``res`` is initialized with an empty list; each time through the loop,
we append the next element. So ``res`` is another kind of accumulator.

An operation like ``capitalize_all`` is sometimes called a **map**
because it "maps" a function (in this case the method ``capitalize``)
onto each of the elements in a sequence.

Another common operation is to select some of the elements from a list
and return a sublist. For example, the following function takes a list
of strings and returns a list that contains only the uppercase strings:

.. code-block:: python

    def only_upper(t):
        res = []
        for s in t:
            if s.isupper():
                res.append(s)
        return res

``isupper`` is a string method that returns ``True`` if the string
contains only upper case letters.

An operation like ``only_upper`` is called a **filter** because it
selects some of the elements and filters out the others.

First class functions
~~~~~~~~~~~~~~~~~~~~~

This is an advanced topic, but fits well with the idea of *mapping* and
lists.

Let's say we wanted to generalize the mapping function we wrote above,
to apply different transformations to lists of strings. Our original
example was to produce a new list in which each original string is
capitalized, but we might want to apply different functions, such as
changing all the strings to lower case, to upper case, or to obtain a
list of all the string lengths. What we'd like to avoid is to write
separate functions for each of these tasks.

In Python, functions are objects that can be passed as parameters to
other functions. To generalize the ``capitalize_all`` function, what we
can do is pass in a mapping function as a second parameter to a more
general function we'll call ``mapper``. To each item in the input list,
we'll apply our mapping function, which will produce a new item to be
added onto a result list:

::

    def mapper(input_list, mapping_function):
        result = []
        for value in input_list:
            new_value = mapping_function(value)
            result.append(new_value)
        return result

    def tolower(s):
        return s.lower()

    t = ['apple','banana','kiwi','star fruit']
    lower_list = mapper(t, tolower)

So above, ``tolower`` is our mapping function that gets passed into the
``mapper``. Inside ``mapper``, each item in the original list is
transformed by the mapping function and added on to a new list.

This is great --- we've generalized the idea of mapping. But we can do
even better.

It seems a waste to write a two-line function like ``tolower``, when it
is so simple. To simplify this part of our program, we can use what is
called a **lambda** in Python. Lambdas are short, "anonymous" functions
that can be defined at the point at which they're needed. The syntax for
writing a lambda function is to use the ``lambda`` keyword, followed by
a comma-separated list of parameters, a colon (``:``), and a short (at
most one line) Python expression. Importantly, there is no explicit
return statement in a ``lambda``. Python just uses the result of the
expression as the return value.

For example, here is a function defined with ``lambda`` that takes two
parameters, and returns their sum. We assign the result of the
``lambda`` expression to the variable ``addtwo``. The result is just a
function object, just like any function object that gets created with
``def``:

.. code-block:: python

    >>> addtwo = lambda x, y: x + y
    >>> addtwo
    <function <lambda> at 0x10ca0e938>
    >>> addtwo(3,5)
    8

Now, to modify our example above using a ``lambda`` expression (and
adding on a couple more examples of mapping):

.. code-block:: python

    def mapper(input_list, mapping_function):
        result = []
        for value in input_list:
            new_value = mapping_function(value)
            result.append(new_value)
        return result

    t = ['apple','banana','kiwi','star fruit']
    upper_list = mapper(t, lambda s: s.upper())
    lower_list = mapper(t, lambda s: s.lower())
    len_list = mapper(t, lambda s: len(s))

As you can see, using ``lambda`` makes our mapping code more compact,
and still fairly easy to read and understand.

Debugging
---------

Careless use of lists (and other mutable objects) can lead to long hours
of debugging. Here are some common pitfalls and ways to avoid them:

1. Don’t forget that most list methods modify the argument and return
   ``None``. This is the opposite of the string methods, which return a
   new string and leave the original alone.

   If you are used to writing string code like this::

       word = word.strip()

   It is tempting to write list code like this::

       t = t.sort()           # WRONG!

   Because ``sort`` returns ``None``, the next operation you perform
   with ``t`` is likely to fail.

   Before using list methods and operators, you should read the
   documentation carefully and then test them in interactive mode. The
   methods and operators that lists share with other sequences (like
   strings) are documented at http://docs.python.org/lib/typesseq.html.
   The methods and operators that only apply to mutable sequences are
   documented at http://docs.python.org/lib/typesseq-mutable.html.

2. Pick an idiom and stick with it.

   Part of the problem with lists is that there are too many ways to do
   things. For example, to remove an element from a list, you can use
   ``pop``, ``remove``, ``del``, or even a slice assignment.

   To add an element, you can use the ``append`` method or the ``+``
   operator. Assuming that ``t`` is a list and ``x`` is a list element,
   these are right::

       t.append(x)
       t = t + [x]

   And these are wrong::

       t.append([x])          # WRONG!
       t = t.append(x)        # WRONG!
       t + [x]                # WRONG!
       t = t + x              # WRONG!

   Try out each of these examples in interactive mode to make sure you
   understand what they do. Notice that only the last one causes a
   runtime error; the other three are legal, but they do the wrong
   thing.

3. Make copies to avoid aliasing.

   If you want to use a method like ``sort`` that modifies the argument,
   but you need to keep the original list as well, you can make a copy.

   ::

       orig = t[:]
       t.sort()

   In this example you could also use the built-in function ``sorted``,
   which returns a new, sorted list and leaves the original alone. But
   in that case you should avoid using ``sorted`` as a variable name!

Glossary
--------

list:
    A sequence of values.

element:
    One of the values in a list (or other sequence), also called items.

index:
    An integer value that indicates an element in a list.

nested list:
    A list that is an element of another list.

list traversal:
    The sequential accessing of each element in a list.

mapping:
    A relationship in which each element of one set corresponds to an
    element of another set. For example, a list is a mapping from
    indices to elements.

accumulator:
    A variable used in a loop to add up or accumulate a result.

augmented assignment:
    A statement that updates the value of a variable using an operator
    like ``+=``.

reduce:
    A processing pattern that traverses a sequence and accumulates the
    elements into a single result.

map:
    A processing pattern that traverses a sequence and performs an
    operation on each element.

filter:
    A processing pattern that traverses a list and selects the elements
    that satisfy some criterion.

object:
    Something a variable can refer to. An object has a type and a value.

equivalent:
    Having the same value.

identical:
    Being the same object (which implies equivalence).

reference:
    The association between a variable and its value.

aliasing:
    A circumstance where two or more variables refer to the same object.

delimiter:
    A character or string used to indicate where a string should be
    split.

linear search:
    The approach of searching for an item in a list by inspecting each
    element in the list, one after another.

binary search:
    Also known as *bisection search*. An approach for searching a list
    which assumes the items in the list in sorted order. It proceeds by
    checking the middle element, and deciding whether the item to search
    for is in the first half or second half of the list. The "search
    space" is repeately cut in half by applying this same idea to
    smaller and smaller portions of the list.

.. rubric:: Exercises

1. Write a function called ``is_sorted`` that takes a list as a
   parameter and returns ``True`` if the list is sorted in ascending
   order and ``False`` otherwise. You can assume (as a precondition)
   that the elements of the list can be compared with the relational
   operators ``<``, ``>``, etc.

   For example, ``is_sorted([1,2,2])`` should return ``True`` and
   ``is_sorted(['b','a'])`` should return ``False``.

2. Two words are anagrams if you can rearrange the letters from one
   to spell the other. Write a function called ``is_anagram`` that
   takes two strings and returns ``True`` if they are anagrams.

3. The (so-called) Birthday Paradox:

   Write a function called ``has_duplicates`` that takes a list and
   returns ``True`` if there is any element that appears more than
   once. It should not modify the original list.

   If there are 23 students in your class, what are the chances that
   two of you have the same birthday? You can estimate this
   probability by generating random samples of 23 birthdays and
   checking for matches. Hint: you can generate random birthdays
   with the ``randint`` function in the ``random`` module.

   You can read about this problem at
   http://wikipedia.org/wiki/Birthday_paradox.

4. Write a function called ``remove_duplicates`` that takes a list
   and returns a new list with only the unique elements from the
   original. Hint: they don’t have to be in the same order.

5. Write a function that reads the file ``words.txt`` and builds a
   list with one element per word. Write two versions of this
   function, one using the ``append`` method and the other using the
   idiom ``t = t + [x]``. Which one takes longer to run? Why?

6. Two words are a “reverse pair” if each is the reverse of the
   other. Write a program that finds all the reverse pairs in the
   word list.

7. Two words "interlock" if taking alternating letters from each
   forms a new word [2]_. For example, “shoe” and “cold” interlock
   to form “schooled.”

   a. Write a program that finds all pairs of words that interlock.
      Hint: don’t enumerate all pairs!

   b. Can you find any words that are three-way interlocked; that
      is, every third letter forms a word, starting from the first,
      second or third?

8. Binary search implementation.

   a. Write a function called ``bisect_iterative`` that takes a
      sorted list and a target value and *iteratively* finds and
      returns the index of the value in the list, if it's there, or
      ``None`` if it's not. You should use a ``while`` loop and no
      recursion in this version.

   b. Write a function called ``bisect_recursive`` that takes a
      sorted list and a target value and *recursively* finds and
      returns the index of the value in the list, if it's there, or
      ``None`` if it's not. There should not be any explicit loops
      in your solution.

.. rubric:: Footnotes

.. [1]
   The admonition "Do not fold, spindle, or mutilate" was printed on the
   punch cards that were used by early computers. See
   http://www.alteich.com/tidbits/t042202.htm and
   http://design.osu.edu/carlson/history/PDFs/lubar-hollerith.pdf

.. [2]
   This exercise is inspired by an example at http://puzzlers.org.
