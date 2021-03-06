*******
Strings
*******

In this chapter, we dive into a bit more depth on strings.

Traversal with a ``while`` loop
-------------------------------

There are a number of situations in which a string must be processed one
character at a time. We've already done this with ``for`` loops, but
``while`` loops give us some additional flexibility. Often, we start at
the beginning, select each character in turn, do something to it, and
continue until the end. This pattern of processing is called a
**traversal**. For example:

.. code-block:: python

    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print letter
        index += 1

This loop traverses the string and displays each letter on a line by
itself. The loop condition is ``index < len(fruit)``, so when ``index``
is equal to the length of the string, the condition is false, and the
body of the loop is not executed. The last character accessed is the one
with the index ``len(fruit)-1``, which is the last character in the
string.

    **Examples**

    1. Write a function that takes a string as an argument and displays
       the letters backward, one per line.

    2. Write a function that takes a string as an argument and displays
       the letters backward, all on the same line. (A space between
       letters is ok.)

    3. Write a function that takes a string as a parameter and returns
       the number of ``'x'``\ s that appear before the first ``'z'`` in
       the string. For example, calling the function with the string
       ``'xaxxyz! x?'`` should yield the count 3, since there are 3
       ``'x'``\ s that appear before the ``'z'`` in the string.

The following example shows how to use concatenation (string addition)
and a ``for`` loop to generate an abecedarian series (that is, in
alphabetical order). In Robert McCloskey’s book *Make Way for
Ducklings*, the names of the ducklings are Jack, Kack, Lack, Mack, Nack,
Ouack, Pack, and Quack. This loop outputs these names in order:

.. code-block:: python

    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        print letter + suffix

The output is:

::

    Jack
    Kack
    Lack
    Mack
    Nack
    Oack
    Pack
    Qack

Of course, that’s not quite right because “Ouack” and “Quack” are
misspelled.

    **Examples**:

    1. Modify the program to fix this error.

    2. Modify the program to use a ``while`` loop instead of a ``for``
       loop.

String slices
-------------

A segment of a string is called a **slice**. Selecting a slice is
similar to selecting a character:

.. code-block:: python

    >>> s = 'Monty Python'
    >>> print s[0:5]
    Monty
    >>> print s[6:12]
    Python

The operator ``[n:m]`` returns the part of the string from the "n-eth"
character to the "m-eth" character, including the first but excluding
the last. This behavior is counterintuitive, but it might help to
imagine the indices pointing *between* the characters, as in the
following diagram:

.. figure:: figs/banana.png
   :align: center
   :alt: image

If you omit the first index (before the colon), the slice starts at the
beginning of the string. If you omit the second index, the slice goes to
the end of the string:

.. code-block:: python

    >>> fruit = 'banana'
    >>> fruit[:3]
    'ban'
    >>> fruit[3:]
    'ana'

If the first index is greater than or equal to the second the result is
an **empty string**, represented by two quotation marks:

.. code-block:: python

    >>> fruit = 'banana'
    >>> fruit[3:3]
    ''

An empty string contains no characters and has length 0, but other than
that, it is the same as any other string.

Another way to slice a string is to use *three* indices. The third value
is referred to as the ``step``:

.. code-block:: python

    >>> fruit = 'banana'
    >>> fruit[0:5:2]
    'bnn'    

The three slice indices work similarly to the three arguments to the
``range`` function. In fact, you can think of the three slice parameters
as being used in a ``range`` function call to *generate* the indices of
values to be extracted ("sliced out") from the string. ``range(0,5,2)``
would give the list ``[0, 2, 4]``, so the slice yields a string composed
of the characters at indices 0, 2, and 4.

    **Example**:

    1. Given that ``fruit`` is a string, what does ``fruit[:]`` mean?

    2. Can you construct a string slice that will return a reversed copy
       of the string?

Strings are immutable
---------------------

It is tempting to use the ``[]`` operator on the left side of an
assignment, with the intention of changing a character in a string. For
example:

.. code-block:: python

    >>> greeting = 'Hello, world!'
    >>> greeting[0] = 'J'
    TypeError: object does not support item assignment

The "object" in this case is the string and the "item" is the character
you tried to assign. For now, an **object** is the same thing as a
value, but we will refine that definition later. An **item** is one of
the values in a sequence.

The reason for the error is that strings are **immutable**, which means
you can’t change an existing string. The best you can do is create a new
string that is a variation on the original:

.. code-block:: python

    >>> greeting = 'Hello, world!'
    >>> new_greeting = 'J' + greeting[1:]
    >>> print new_greeting
    Jello, world!

This example concatenates a new first letter onto a slice of
``greeting``. It has no effect on the original string.

Searching
---------

What does the following function do? Read the function carefully before
moving on. If it helps, you can trace the operation of two different
calls to this function: ``find('magic', 'i')`` and
``find('magic', 'z')``.

.. code-block:: python

    def find(word, letter):
        index = 0
        while index < len(word):
            if word[index] == letter:
                return index
            index = index + 1
        return -1

In a sense, ``find`` is the opposite of the ``[]`` operator. Instead of
taking an index and extracting the corresponding character, it takes a
character and finds the index where that character appears. If the
character is not found, the function returns ``-1``.

This is the first example we have seen of a ``return`` statement inside
a loop. If ``word[index] == letter``, the function breaks out of the
loop and returns immediately.

If the character doesn’t appear in the string, the program exits the
loop normally and returns ``-1``.

This pattern of computation—traversing a sequence and returning when we
find what we are looking for—is called a **search**.

    **Examples**:

    1. Modify ``find`` so that it has a third parameter, the index in
       ``word`` where it should start looking.

    2. Write a function named ``findall`` that takes a character to
       search for and a string, and returns a list of indices where the
       character is found in the string.

Looping and counting
--------------------

The following program counts the number of times the letter ``a``
appears in a string:

.. code-block:: python

    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print count

This program demonstrates another pattern of computation called a
**counter**. The variable ``count`` is initialized to 0 and then
incremented each time an ``a`` is found. When the loop exits, ``count``
contains the result—the total number of ``a``\ ’s.

    **Examples**:

    1. Encapsulate this code in a function named ``count``, and
       generalize it so that it accepts the string and the letter as
       arguments.

    2. Rewrite this function so that instead of traversing the string,
       it uses the three-parameter version of ``find`` from the previous
       section.

    3. Rewrite the function so that instead of passing a single
       character as a parameter, another string can be passed to the
       function. Try to generalize the function so that it works for any
       length of substring.

``string`` methods
------------------

A **method** is similar to a function ---it takes arguments and returns
a value---but the syntax is different. For example, the method ``upper``
takes a string and returns a new string with all uppercase letters:

Instead of the function syntax ``upper(word)``, it uses the method
syntax ``word.upper()``.

.. code-block:: python

    >>> word = 'banana'
    >>> new_word = word.upper()
    >>> print new_word
    BANANA

This form of dot notation specifies the name of the method, ``upper``,
and the name of the string to apply the method to, ``word``. The empty
parentheses indicate that this method takes no argument.

A method call is called an **invocation**; in this case, we would say
that we are invoking ``upper`` on the ``word``.

As it turns out, there is a string method named ``find`` that is
remarkably similar to the function we wrote:

.. code-block:: python

    >>> word = 'banana'
    >>> index = word.find('a')
    >>> print index
    1

In this example, we invoke ``find`` on ``word`` and pass the letter we
are looking for as a parameter.

Actually, the ``find`` method is more general than our function; it can
find substrings, not just characters:

.. code-block:: python

    >>> word.find('na')
    2

It can take as a second argument the index where it should start:

.. code-block:: python

    >>> word.find('na', 3)
    4

And as a third argument the index where it should stop:

.. code-block:: python

    >>> name = 'bob'
    >>> name.find('b', 1, 2)
    -1

This search fails because ``b`` does not appear in the index range from
``1`` to ``2`` (not including ``2``).

    **Example**:

    1. There is a string method called ``count`` that is similar to the
       function in the previous exercise. Read the documentation of this
       method and write an invocation that counts the number of ``a``\ s
       in ``'banana'``.

There are quite a few string methods, and you'll probably want to take a
look at the documentation:
http://docs.python.org/library/stdtypes.html#string-methods. Below, we
review several of the useful methods:

+-------------------------+---------------------------------------------------------+
| **method**              | **description**                                         |
+=========================+=========================================================+
| ``upper``               | Return an upper-cased copy of the string.               |
+-------------------------+---------------------------------------------------------+
| ``lower``               | Return a lower-cased copy of the string.                |
+-------------------------+---------------------------------------------------------+
| ``capitalize``          | Return a copy of the string with the first character    |
|                         | capitalized.                                            |
+-------------------------+---------------------------------------------------------+
| ``count(s)``            | Return the number of non-overlapping occurrences        |
|                         | of the substring ``s`` in the string.                   |
+-------------------------+---------------------------------------------------------+
| ``replace(old, new)``   | Return a copy of the string with all occurrences of     |
|                         | ``old`` replaced by ``new``.                            |
+-------------------------+---------------------------------------------------------+
| ``strip``               | Return a copy of the string with leading and trailing   |
|                         | "whitespace" characters removed (spaces, tabs, and      |
|                         | newline characters).                                    |
+-------------------------+---------------------------------------------------------+
| ``split``               | Return a list of words in the string, separating the    |
|                         | string by any whitespace characters.                    |
+-------------------------+---------------------------------------------------------+

Note that several of the methods above can take optional parameters,
which modify the behavior of the method. Refer to the Python
documentation for details on the various string methods.

Character-numeric duality
-------------------------

Internal to a computer, *all* data are represented *numerically*:
images, sounds, videos, strings, and characters. Sometimes it is useful
to be able to process characters *numerically* instead of as
single-character strings.
Python includes two built-in functions to help with this: ``ord`` and
``chr``.

``ord(ch)`` returns the numeric, or *ordinal* value of a character.
``chr(n)`` returns the character corresponding to a given number ``n``.
For example:

.. code-block:: python

    >>> ord('A')
    65
    >>> ord('B')
    66
    >>> ord('C')
    67
    >>> ord('a')
    97
    >>> ord('b')
    98
    >>> chr(99)
    'c'
    >>> chr(100)
    'd'

As you can see above, upper case letters and lower case letters are each
organized sequentially. Upper case letters start at the ordinal value
65, and lower case letters start at 97. Knowing these specific numbers
is not important; it is useful to observe, however, that they're
organized sequentially.

The mappings between characters and their numeric equivalents is defined
by several standards. The most historically relevant one is the American
Standard Code for Information Interchange, or ASCII:
http://en.wikipedia.org/wiki/Ascii. Unfortunately, ASCII, as the name
suggests, is United States (and English) centric and cannot accommodate
character sets from other languages such as Chinese, Russian, or Korean.
The Unicode standard was developed to accommodate international
character sets. Unicode is beyond the scope of this class, but if you're
interested, you can read more on Wikipedia:
http://en.wikipedia.org/wiki/Unicode.

String comparison and ordering
------------------------------

As we've already seen, the relational operators work on strings.
However, Python does not handle uppercase and lowercase letters the same
way that people do. All the uppercase letters come before all the
lowercase letters, so ``'Pineapple'`` comes before ``'banana'``.

A common way to address this problem is to convert strings to a standard
format, such as all lowercase, before performing the comparison. Keep
that in mind in case you have to defend yourself against a man armed
with a Pineapple.

Debugging
---------

When you use indices to traverse the values in a sequence, it is tricky
to get the beginning and end of the traversal right. Here is a function
that is supposed to compare two words and return ``True`` if one of the
words is the reverse of the other, but it contains two errors:

.. code-block:: python

    def is_reverse(word1, word2):
        if len(word1) != len(word2):
            return False

        i = 0
        j = len(word2)

        while j > 0:
            if word1[i] != word2[j]:
                return False
            i = i+1
            j = j-1

        return True

The first ``if`` statement checks whether the words are the same length.
If not, we can return ``False`` immediately and then, for the rest of
the function, we can assume that the words are the same length.

``i`` and ``j`` are indices: ``i`` traverses ``word1`` forward while
``j`` traverses ``word2`` backward. If we find two letters that don’t
match, we can return ``False`` immediately. If we get through the whole
loop and all the letters match, we return ``True``.

If we test this function with the words "pots" and "stop", we expect the
return value ``True``, but we get an IndexError:

.. code-block:: python

    >>> is_reverse('pots', 'stop')
    ...
      File "reverse.py", line 15, in is_reverse
        if word1[i] != word2[j]:
    IndexError: string index out of range

For debugging this kind of error, my first move is to print the values
of the indices immediately before the line where the error appears.

.. code-block:: python

        while j > 0:
            print i, j        # print here

            if word1[i] != word2[j]:
                return False
            i = i+1
            j = j-1

Now when I run the program again, I get more information:

.. code-block:: python

    >>> is_reverse('pots', 'stop')
    0 4
    ...
    IndexError: string index out of range

The first time through the loop, the value of ``j`` is 4, which is out
of range for the string ``'pots'``. The index of the last character is
3, so the initial value for ``j`` should be ``len(word2)-1``.

If I fix that error and run the program again, I get:

.. code-block:: python

    >>> is_reverse('pots', 'stop')
    0 3
    1 2
    2 1
    True

This time we get the right answer, but it looks like the loop only ran
three times, which is suspicious. To get a better idea of what is
happening, it is useful to draw a state diagram. During the first
iteration, the frame for ``is_reverse`` looks like this:

.. figure:: figs/state4.png
   :align: center
   :alt: State diagram for ``is_reverse`` example.

   State diagram for ``is_reverse`` example.

I took a little license by arranging the variables in the frame and
adding dotted lines to show that the values of ``i`` and ``j`` indicate
characters in ``word1`` and ``word2``.

    **Example**:

    1. Starting with this diagram, execute the program on paper,
       changing the values of ``i`` and ``j`` during each iteration.
       Find and fix the second error in this function.

Glossary
--------

object:
    Something a variable can refer to. For now, you can use "object" and
    "value" interchangeably.

sequence:
    An ordered set; that is, a set of values where each value is
    identified by an integer index.

item:
    One of the values in a sequence.

index:
    An integer value used to select an item in a sequence, such as a
    character in a string.

slice:
    A part of a string specified by a range of indices.

empty string:
    A string with no characters and length 0, represented by two
    quotation marks.

immutable:
    The property of a sequence whose items cannot be assigned.

traverse:
    To iterate through the items in a sequence, performing a similar
    operation on each.

search:
    A pattern of traversal that stops when it finds what it is looking
    for.

counter:
    A variable used to count something, usually initialized to zero and
    then incremented.

method:
    A function that is associated with an object and called using dot
    notation.

invocation:
    A statement that calls a method.


.. rubric:: Exercises

1. Write a function named ``inboth`` that takes two strings as
   parameters, and returns a list of all the characters that are
   contained in both strings. Write the function in a case-sensitive
   way.

2. Rewrite the ``inboth`` function to work in a case-insensitive
   way.

3. The following functions are all *intended* to check whether a
   string contains any lowercase letters, but at least some of them
   are wrong. For each function, describe what the function actually
   does (assuming that the parameter is a string).

.. code-block:: python

   def any_lowercase1(s):
      for c in s:
          if c.islower():
              return True
          else:
              return False

   def any_lowercase2(s):
       for c in s:
           if 'c'.islower():
               return 'True'
           else:
               return 'False'

   def any_lowercase3(s):
       for c in s:
           flag = c.islower()
       return flag

   def any_lowercase4(s):
       flag = False
       for c in s:
           flag = flag or c.islower()
       return flag

   def any_lowercase5(s):
       for c in s:
           if not c.islower():
               return False
       return True

4. ROT13 is a weak form of encryption that involves "rotating" each
   letter in a word by 13 places [1]_. To rotate a letter means to
   shift it through the alphabet, wrapping around to the beginning
   if necessary, so 'A' shifted by 3 is 'D' and 'Z' shifted by 1 is
   'A'.

   Write a function called ``rotate_word`` that takes a string and
   an integer as parameters, and that returns a new string that
   contains the letters from the original string "rotated" by the
   given amount.

   For example, "cheer" rotated by 7 is "jolly" and "melon" rotated
   by -10 is "cubed".

5. Write a program that asks for a phrase, then computes and prints
   the number of words and number of characters in the phrase.

6. Write a program that asks for a phrase, then computes the number
   of upper and lower case letters, and prints the two counts.


.. rubric:: Footnotes

.. [1]
   See http://wikipedia.org/wiki/ROT13.
