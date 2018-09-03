************************************
Case study: data structure selection
************************************

Word frequency analysis
=======================

As usual, you should at least attempt the following exercises before you
read the sections that follow.

    **Examples**:

    1. Write a program that reads a file, breaks each line into words,
       strips whitespace and punctuation from the words, and converts
       them to lowercase.

       Hint: The ``string`` module provides strings named
       ``whitespace``, which contains space, tab, newline, etc., and
       ``punctuation`` which contains the punctuation characters. Let’s
       see if we can make Python swear::

           >>> import string
           >>> print string.punctuation
           !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

       Also, you might consider using the string methods ``strip``,
       ``replace`` and ``translate``.

    2. Go to Project Gutenberg (http://gutenberg.org) and download your
       favorite out-of-copyright book in plain text format.

       Modify your program from the previous exercise to read the book
       you downloaded, skip over the header information at the beginning
       of the file, and process the rest of the words as before.

    3. Then modify the program to count the total number of words in the
       book, and the number of times each word is used.

    4. Print the number of different words used in the book. Compare
       different books by different authors, written in different eras.
       Which author uses the most extensive vocabulary?

    5. Modify the program from the previous exercise to print the 20
       most frequently-used words in the book.

    6. Modify the previous program to read a word list and then print
       all the words in the book that are not in the word list. How many
       of them are typos? How many of them are common words that
       *should* be in the word list, and how many of them are really
       obscure?

    7. Write a function named ``choose_from_hist`` that takes a
       histogram as defined `in the dictionary
       chapter <#sec:histogram>`_ and returns a random value from the
       histogram, chosen with probability in proportion to frequency.
       For example, for this histogram::

           >>> t = ['a', 'a', 'b']
           >>> h = histogram(t)
           >>> print h
           {'a': 2, 'b': 1}

       your function should ``'a'`` with probability :math:`2/3` and
       ``'b'`` with probability :math:`1/3`.

       You will probably find the ``random.choice`` function in the
       ``random`` module helpful for this exercise. This function takes
       a list as a parameter, and returns one of the items from the
       list, chosen uniformly at random.

Word histogram
==============

Here is a program that reads a file and builds a histogram of the words
in the file:

.. code-block:: python

    import string

    def process_file(filename):
        h = dict()
        fp = open(filename)
        for line in fp:
            process_line(line, h)
        return h

    def process_line(line, h):
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()

            h[word] = h.get(word, 0) + 1

    hist = process_file('emma.txt')

This program reads ``emma.txt``, which contains the text of \* Emma\* by
Jane Austen.

``process_file`` loops through the lines of the file, passing them one
at a time to ``process_line``. The histogram ``h`` is being used as an
accumulator.

``process_line`` uses the string method ``replace`` to replace hyphens
with spaces before using ``split`` to break the line into a list of
strings. It traverses the list of words and uses ``strip`` and ``lower``
to remove punctuation and convert to lower case. (It is a shorthand to
say that strings are “converted;” remember that string are immutable, so
methods like ``strip`` and ``lower`` return new strings.)

Finally, ``process_line`` updates the histogram by creating a new item
or incrementing an existing one.

To count the total number of words in the file, we can add up the
frequencies in the histogram:

.. code-block:: python

    def total_words(h):
        return sum(h.values())

The number of different words is just the number of items in the
dictionary:

.. code-block:: python

    def different_words(h):
        return len(h)

Here is some code to print the results:

.. code-block:: python

    print 'Total number of words:', total_words(hist)
    print 'Number of different words:', different_words(hist)

And the results:

.. code-block:: python

    Total number of words: 161073
    Number of different words: 7212

Most common words
=================

To find the most common words, we can apply the DSU pattern;
``most_common`` takes a histogram and returns a list of word-frequency
tuples, sorted in reverse order by frequency:

.. code-block:: python

    def most_common(h):
        t = []
        for key, value in h.items():
            t.append((value, key))

        t.sort(reverse=True)
        return t

Here is a loop that prints the ten most common words:

.. code-block:: python

    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[0:10]:
        print word, '\t', freq

And here are the results from *Emma*:

.. code-block:: python

    The most common words are:
    to      5242
    the     5204
    and     4897
    of      4293
    i       3191
    a       3130
    it      2529
    her     2483
    was     2400
    she     2364

Optional parameters
===================

We have seen built-in functions and methods that take a variable number
of arguments. It is possible to write user-defined functions with
optional arguments, too. For example, here is a function that prints the
most common words in a histogram

.. code-block:: python

    def print_most_common(hist, num=10)
        t = most_common(hist)
        print 'The most common words are:'
        for freq, word in t[0:num]:
            print word, '\t', freq

The first parameter is required; the second is optional. The **default
value** of ``num`` is 10.

If you only provide one argument:

.. code-block:: python

    print_most_common(hist)

``num`` gets the default value. If you provide two arguments:

.. code-block:: python

    print_most_common(hist, 20)

``num`` gets the value of the argument instead. In other words, the
optional argument **overrides** the default value.

If a function has both required and optional parameters, all the
required parameters have to come first, followed by the optional ones.

Dictionary subtraction
======================

Finding the words from the book that are not in the word list from
``words.txt`` is a problem you might recognize as set subtraction; that
is, we want to find all the words from one set (the words in the book)
that are not in another set (the words in the list).

``subtract`` takes dictionaries ``d1`` and ``d2`` and returns a new
dictionary that contains all the keys from ``d1`` that are not in
``d2``. Since we don’t really care about the values, we set them all to
None.

.. code-block:: python

    def subtract(d1, d2):
        res = dict()
        for key in d1:
            if key not in d2:
                res[key] = None
        return res

To find the words in the book that are not in ``words.txt``, we can use
``process_file`` to build a histogram for ``words.txt``, and then
subtract:

.. code-block:: python

    words = process_file('words.txt')
    diff = subtract(hist, words)

    print "The words in the book that aren't in the word list are:"
    for word in diff.keys():
        print word,

Here are some of the results from *Emma*:

::

    The words in the book that aren't in the word list are:
     rencontre jane's blanche woodhouses disingenuousness 
    friend's venice apartment ...

Some of these words are names and possessives. Others, like “rencontre,”
are no longer in common use. But a few are common words that should
really be in the list!

    **Example**:

    1. Python provides a data structure called ``set`` that provides
       many common set operations. Read the documentation at
       http://docs.python.org/lib/types-set.html and write a program
       that uses set subtraction to find words in the book that are not
       in the word list.

Random words
============

To choose a random word from the histogram, the simplest algorithm is to
build a list with multiple copies of each word, according to the
observed frequency, and then choose from the list:

.. code-block:: python

    def random_word(h):
        t = []
        for word, freq in h.items():
            t.extend([word] * freq)

        return random.choice(t)

The expression ``[word] * freq`` creates a list with ``freq`` copies of
the string ``word``. The ``extend`` method is similar to ``append``
except that the argument is a sequence.

    **Example**:

    1. This algorithm works, but it is not very efficient; each time you
       choose a random word, it rebuilds the list, which is as big as
       the original book. An obvious improvement is to build the list
       once and then make multiple selections, but the list is still
       big.

       An alternative is:

       a. Use ``keys`` to get a list of the words in the book.

       b. Build a list that contains the cumulative sum of the word
          frequencies. The last item in this list is the total number of
          words in the book, :math:`n`.

       c. Choose a random number from 1 to :math:`n`. Use a bisection
          search to find the index where the random number would be
          inserted in the cumulative sum.

       d. Use the index to find the corresponding word in the word list.

       Write a program that uses this algorithm to choose a random word
       from the book.

Markov analysis
===============

If you choose words from the book at random, you can get a sense of the
vocabulary, you probably won’t get a sentence:

        this the small regard harriet which knightley's it most things

A series of random words seldom makes sense because there is no
relationship between successive words. For example, in a real sentence
you would expect an article like "the" to be followed by an adjective or
a noun, and probably not a verb or adverb.

One way to measure these kinds of relationships is Markov analysis [1]_,
which characterizes, for a given sequence of words, the probability of
the word that comes next. For example, the song *Eric, the Half a Bee*
begins:

    Half a bee, philosophically,
    Must, ipso facto, half not be.
    But half the bee has got to be
    Vis a vis, its entity. D’you see?
    But can a bee be said to be
    Or not to be an entire bee
    When half the bee is not a bee
    Due to some ancient injury?

In this text, the phrase "half the" is always followed by the word
"bee," but the phrase "the bee" might be followed by either "has" or
"is".

The result of Markov analysis is a mapping from each prefix (like "half
the" and "the bee") to all possible suffixes (like "has" and "is").

Given this mapping, you can generate a random text by starting with any
prefix and choosing at random from the possible suffixes. Next, you can
combine the end of the prefix and the new suffix to form the next
prefix, and repeat.

For example, if you start with the prefix “Half a,” then the next word
has to be “bee,” because the prefix only appears once in the text. The
next prefix is “a bee,” so the next suffix might be “philosophically,”
“be” or “due.”

In this example the length of the prefix is always two, but you can do
Markov analysis with any prefix length. The length of the prefix is
called the “order” of the analysis.

    Markov analysis:

    1. Write a program to read a text from a file and perform Markov
       analysis. The result should be a dictionary that maps from
       prefixes to a collection of possible suffixes. The collection
       might be a list, tuple, or dictionary; it is up to you to make an
       appropriate choice. You can test your program with prefix length
       two, but you should write the program in a way that makes it easy
       to try other lengths.

    2. Add a function to the previous program to generate random text
       based on the Markov analysis. Here is an example from *Emma* with
       prefix length 2:

           He was very clever, be it sweetness or be angry, ashamed or
           only amused, at such a stroke. She had never thought of
           Hannah till you were never meant for me?" "I cannot make
           speeches, Emma:" he soon cut it all himself.

       For this example, I left the punctuation attached to the words.
       The result is almost syntactically correct, but not quite.
       Semantically, it almost makes sense, but not quite.

       What happens if you increase the prefix length? Does the random
       text make more sense?

    3. Once your program is working, you might want to try a mash-up: if
       you analyze text from two or more books, the random text you
       generate will blend the vocabulary and phrases from the sources
       in interesting ways.

Data structures
===============

Using Markov analysis to generate random text is fun, but there is also
a point to this exercise: data structure selection. In your solution to
the previous exercises, you had to choose:

-  How to represent the prefixes.

-  How to represent the collection of possible suffixes.

-  How to represent the mapping from each prefix to the collection of
   possible suffixes.

Ok, the last one is the easy; the only mapping type we have seen is a
dictionary, so it is the natural choice.

For the prefixes, the most obvious options are string, list of strings,
or tuple of strings. For the suffixes, one option is a list; another is
a histogram (dictionary).

How should you choose? The first step is to think about the operations
you will need to implement for each data structure. For the prefixes, we
need to be able to remove words from the beginning and add to the end.
For example, if the current prefix is “Half a,” and the next word is
“bee,” you need to be able to form the next prefix, “a bee.”

Your first choice might be a list, since it is easy to add and remove
elements, but we also need to be able to use the prefixes as keys in a
dictionary, so that rules out lists. With tuples, you can’t append or
remove, but you can use the addition operator to form a new tuple:

.. code-block:: python

    def shift(prefix, word):
        return prefix[1:] + (word,)

``shift`` takes a tuple of words, ``prefix``, and a string, ``word``,
and forms a new tuple that has all the words in ``prefix`` except the
first, and ``word`` added to the end.

For the collection of suffixes, the operations we need to perform
include adding a new suffix (or increasing the frequency of an existing
one), and choosing a random suffix.

Adding a new suffix is equally easy for the list implementation or the
histogram. Choosing a random element from a list is easy; choosing from
a histogram is harder to do efficiently.

So far we have been talking mostly about ease of implementation, but
there are other factors to consider in choosing data structures. One is
run time. Sometimes there is a theoretical reason to expect one data
structure to be faster than other; for example, I mentioned that the
``in`` operator is faster for dictionaries than for lists, at least when
the number of elements is large.

But often you don’t know ahead of time which implementation will be
faster. One option is to implement both of them and see which is better.
This approach is called **benchmarking**. A practical alternative is to
choose the data structure that is easiest to implement, and then see if
it is fast enough for the intended application. If so, there is no need
to go on. If not, there are tools, like the ``profile`` module, that can
identify the places in a program that take the most time.

The other factor to consider is storage space. For example, using a
histogram for the collection of suffixes might take less space because
you only have to store each word once, no matter how many times it
appears in the text. In some cases, saving space can also make your
program run faster, and in the extreme, your program might not run at
all if you run out of memory. But for many applications, space is a
secondary consideration after run time.

One final thought: in this discussion, I have implied that we should use
one data structure for both analysis and generation. But since these are
separate phases, it would also be possible to use one structure for
analysis and then convert to another structure for generation. This
would be a net win if the time saved during generation exceeded the time
spent in conversion.

Debugging
=========

When you are debugging a program, and especially if you are working on a
hard bug, there are four things to try:

-  *Reading*:

   -  Examine your code, read it back to yourself, and check that it
      says what you meant to say.

-  *Running*:

   -  Experiment by making changes and running different versions. Often
      if you display the right thing at the right place in the program,
      the problem becomes obvious, but sometimes you have to spend some
      time to build scaffolding.

-  *Ruminating*:

   -  Take some time to think! What kind of error is it: syntax,
      runtime, semantic? What information can you get from the error
      messages, or from the output of the program? What kind of error
      could cause the problem you’re seeing? What did you change last,
      before the problem appeared?

-  *Retreating*:

   -  At some point, the best thing to do is back off, undoing recent
      changes, until you get back to a program that works and that you
      understand. Then you can starting rebuilding.

Beginning programmers sometimes get stuck on one of these activities and
forget the others. Each activity comes with its own failure mode.

For example, reading your code might help if the problem is a
typographical error, but not if the problem is a conceptual
misunderstanding. If you don’t understand what your program does, you
can read it 100 times and never see the error, because the error is in
your head.

Running experiments can help, especially if you run small, simple tests.
But if you run experiments without thinking or reading your code, you
might fall into a pattern I call “random walk programming,” which is the
process of making random changes until the program does the right thing.
Needless to say, random walk programming can take a long time.

You have to take time to think. Debugging is like an experimental
science. You should have at least one hypothesis about what the problem
is. If there are two or more possibilities, try to think of a test that
would eliminate one of them.

Taking a break helps with the thinking. So does talking. If you explain
the problem to someone else (or even yourself), you will sometimes find
the answer before you finish asking the question.

But even the best debugging techniques will fail if there are too many
errors, or if the code you are trying to fix is too big and complicated.
Sometimes the best option is to retreat, simplifying the program until
you get to something that works and that you understand.

Beginning programmers are often reluctant to retreat because they can’t
stand to delete a line of code (even if it’s wrong). If it makes you
feel better, copy your program into another file before you start
stripping it down. Then you can paste the pieces back in a little bit at
a time.

Finding a hard bug requires reading, running, ruminating, and sometimes
retreating. If you get stuck on one of these activities, try the others.

Glossary
========

default value:
    The value given to an optional parameter if no argument is provided.

override:
    To replace a default value with an argument.

benchmarking:
    The process of choosing between data structures by implementing
    alternatives and testing them on a sample of the possible inputs.


.. rubric:: Exercises

1. The "rank" of a word is its position in a list of words sorted by
   frequency: the most common word has rank 1, the second most
   common has rank 2, etc.

   Zipf’s law describes a relationship between the ranks and
   frequencies of words in natural languages [2]_. Specifically, it
   predicts that the frequency, :math:`f`, of the word with rank
   :math:`r` is :math:`f = c r^{-s}` 
   where :math:`s` and :math:`c` are parameters that depend on the
   language and the text. If you take the logarithm of both sides of
   this equation, you get :math:`\log f = \log c - s \log r`.

   So if you plot :math:`\log f` versus :math:`\log r`, you should
   get a straight line with slope :math:`-s` and intercept
   :math:`\log c`.

   Write a program that reads a text from a file, counts word
   frequencies, and prints one line for each word, in descending
   order of frequency, with :math:`\log f` and :math:`\log r`. Use
   the graphing program of your choice to plot the results and check
   whether they form a straight line. Can you estimate the value of
   :math:`s`?

.. rubric:: Footnotes

.. [1]
   This case study is based on an example from Kernighan and Pike, *The
   Practice of Programming*, 1999.

.. [2]
   See http://wikipedia.org/wiki/Zipf's_law.
