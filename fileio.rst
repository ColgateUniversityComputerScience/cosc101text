File input and output
*********************

.. todo:: add urllib stuff to this chapter

Reading word lists
------------------

Several of the examples and exercises in this chapter require a (big)
list of English words. There are many of word lists available on the
Internet, but the one most suitable for our purpose is one of the word
lists collected and contributed to the public domain by Grady Ward as
part of the Moby lexicon project [1]_. It includes is a list of 117,969
official crosswords; that is, words that are considered valid in
crossword puzzles and other word games. I've extracted and posted this
list at: http://cs.colgate.edu/~jsommers/cosc101/words.txt

This file is in *plain text* (as the suffix ``.txt`` suggests), so you
can open it with a text editor, but you can also read it from Python.
The built-in function ``open`` takes the name of the file as a parameter
and returns a **file object** you can use to read the file.

.. code-block:: python

    >>> fin = open('words.txt')
    >>> print fin
    <open file 'words.txt', mode 'r' at 0xb7f4b380>

``fin`` is a common name for a file object used for input ("*f*\ ile
*in*\ put"). Mode ``'r'`` indicates that this file is open for reading
(as opposed to ``'w'`` for writing).

The file object provides several methods for reading, including
``readline``, which reads characters from the file until it gets to a
newline and returns the result as a string:

.. code-block:: python

    >>> fin.readline()
    'aa\r\n'

The first word in this particular list is "aa," which is a kind of lava.
The sequence ``\r\n`` represents two whitespace characters, a carriage
return (``\r``) and a newline (``\n``), that separate this word from the
next.

The file object keeps track of where it is in the file, so if you call
``readline`` again, you get the next word:

.. code-block:: python

    >>> fin.readline()
    'aah\r\n'

The next word is "aah," which is a perfectly legitimate word, so stop
looking at me like that. If it's the whitespace that’s bothering you, we
can get rid of it with the string method ``strip``:

.. code-block:: python

    >>> line = fin.readline()
    >>> word = line.strip()
    >>> print word
    aahed

You can also use a file object as part of a ``for`` loop. This program
reads ``words.txt`` and prints each word, one per line:

.. code-block:: python

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        print word
    fin.close()

The above program also includes a call to the ``close`` method as the
last statement. You should always remember to close files when you're
done with them!

    **Example**:

    1. Write a program that reads ``words.txt`` and prints only the
       words with more than 20 characters (not counting whitespace). At
       the end of your program, you should also print out the number of
       words that are longer than 20 characters (not including
       whitespace).

Practice exercises
------------------

There are solutions to these exercises in the next section. You should
at least attempt each one before you read the solutions.

    1. In 1939 Ernest Vincent Wright published a 50,000 word novel
       called *Gadsby* that does not contain the letter "e." Since 'e'
       is the most common letter in English, that’s not easy to do.

       In fact, it is difficult to construct a solitary thought without
       using that most common symbol. It is slow going at first, but
       with caution and hours of training you can gradually gain
       facility.

       All right, I’ll stop now.

       Write a function called ``has_no_e`` that returns ``True`` if the
       given word doesn't have the letter 'e' in it.

    2. Write a program that uses your ``has_no_e`` function to print
       only the words in ``words.txt`` that have no ``e``. You should
       also compute and print the percentage of words in the file that
       have no 'e'.

    3. Write a function named ``avoids`` that takes a word and a string
       of forbidden letters, and that returns ``True`` if the word
       doesn't use any of the forbidden letters.

    4. Write a program to prompt the user to enter a string of forbidden
       letters and print the number of words in ``words.txt`` that do
       not contain any of them.

       Fun challenge: can you find a combination of 5 forbidden letters
       that excludes the *smallest* number of words?

    5. Write a function named ``uses_only`` that takes a word and a
       string of letters, and that returns ``True`` if the word contains
       only letters in the list.

       Fun challenge: can you make a sentence using only the letters
       ``acefhlo``? Other than "Hoe alfalfa?"

    6. Write a function named ``uses_all`` that takes a word and a
       string of required letters, and that returns ``True`` if the word
       uses all the required letters at least once. How many words are
       there that use all the vowels ``aeiou``? How about ``aeiouy``?

    7. Write a function called ``is_abecedarian`` that returns ``True``
       if the letters in a word appear in alphabetical order (double
       letters are ok). How many abecedarian words are there?

Search
------

All of the exercises in the previous section have something in common;
they can be solved with the search pattern we previously saw with the
``find`` function we wrote in the strings chapter. The simplest example
is:

.. code-block:: python

    def has_no_e(word):
        for letter in word:
            if letter == 'e':
                return False
        return True

The ``for`` loop traverses the characters in ``word``. If we find the
letter “e”, we can immediately return ``False``; otherwise we have to go
to the next letter. If we exit the loop normally, that means we didn’t
find an “e”, so we return ``True``.

``avoids`` is a more general version of ``has_no_e`` but it has the same
structure:

.. code-block:: python

    def avoids(word, forbidden):
        for letter in word:
            if letter in forbidden:
                return False
        return True

We can return ``False`` as soon as we find a forbidden letter; if we get
to the end of the loop, we return ``True``.

``uses_only`` is similar except that the sense of the condition is
reversed:

.. code-block:: python

    def uses_only(word, available):
        for letter in word: 
            if letter not in available:
                return False
        return True

Instead of a list of forbidden letters, we have a list of available
letters. If we find a letter in ``word`` that is not in ``available``,
we can return ``False``.

``uses_all`` is similar except that we reverse the role of the word and
the string of letters:

.. code-block:: python

    def uses_all(word, required):
        for letter in required: 
            if letter not in word:
                return False
        return True

Instead of traversing the letters in ``word``, the loop traverses the
required letters. If any of the required letters do not appear in the
word, we can return ``False``.

If you were really thinking like a computer scientist, you would have
recognized that ``uses_all`` was an instance of a previously-solved
problem, and you would have written:

.. code-block:: python

    def uses_all(word, required):
        return uses_only(required, word)

This is an example of a program development method called **problem
recognition**, which means that you recognize the problem you are
working on as an instance of a previously-solved problem, and apply a
previously-developed solution.

Looping with indices
--------------------

I wrote the functions in the previous section with ``for`` loops because
I only needed the characters in the strings; I didn’t have to do
anything with the indices.

For ``is_abecedarian`` we have to compare adjacent letters, which is a
little tricky with a ``for`` loop:

.. code-block:: python

    def is_abecedarian(word):
        previous = word[0]
        for c in word:
            if c < previous:
                return False
            previous = c
        return True

An alternative is to use recursion:

.. code-block:: python

    def is_abecedarian(word):
        if len(word) <= 1:
            return True
        if word[0] > word[1]:
            return False
        return is_abecedarian(word[1:])

Another option is to use a ``while`` loop:

.. code-block:: python

    def is_abecedarian(word):
        i = 0
        while i < len(word)-1:
            if word[i+1] < word[i]:
                return False
            i = i+1
        return True

The loop starts at ``i=0`` and ends when ``i=len(word)-1``. Each time
through the loop, it compares the :math:`i`\ th character (which you can
think of as the current character) to the :math:`i+1`\ th character
(which you can think of as the next).

If the next character is less than (alphabetically before) the current
one, then we have discovered a break in the abecedarian trend, and we
return ``False``.

If we get to the end of the loop without finding a fault, then the word
passes the test. To convince yourself that the loop ends correctly,
consider an example like ``'flossy'``. The length of the word is 6, so
the last time the loop runs is when ``i`` is 4, which is the index of
the second-to-last character. On the last iteration, it compares the
second-to-last character to the last, which is what we want.

Here is a version of ``is_palindrome`` that uses two indices; one starts
at the beginning and goes up; the other starts at the end and goes down.

.. code-block:: python

    def is_palindrome(word):
        i = 0
        j = len(word)-1

        while i<j:
            if word[i] != word[j]:
                return False
            i = i+1
            j = j-1

        return True

Or, if you noticed that this is an instance of a previously-solved
problem, you might have written:

.. code-block:: python

    def is_palindrome(word):
        return is_reverse(word, word)

.. raw:: html

   <!--

   ## Persistence

   Most of the programs we have seen so far are transient in the sense that
   they run for a short time and produce some output, but when they end,
   their data disappears. If you run the program again, it starts with a
   clean slate.

   Other programs are **persistent**: they run for a long time (or all the
   time); they keep at least some of their data in permanent storage (a
   hard drive, for example); and if they shut down and restart, they pick
   up where they left off.

   Examples of persistent programs are operating systems, which run pretty
   much whenever a computer is on, and web servers, which run all the time,
   waiting for requests to come in on the network.

   One of the simplest ways for programs to maintain their data is by
   reading and writing text files. We have already seen programs that read
   text files; in this chapter we will see programs that write them.

   An alternative is to store the state of the program in a database. In
   this chapter I will present a simple database and a module, `pickle`,
   that makes it easy to store program data.

   -->

Reading and writing
-------------------

A text file is a sequence of characters stored on a permanent medium
like a hard drive, flash memory, or CD-ROM. `We saw how to open and read
a file earlier <#sec:wordlist>`_.

To write a file, you have to open it with mode ``'w'`` as a second
parameter:

.. code-block:: python

    >>> fout = open('output.txt', 'w')
    >>> print fout
    <open file 'output.txt', mode 'w' at 0xb7eb2410>

If the file already exists, opening it in write mode clears out the old
data and starts fresh, so be careful! If the file doesn’t exist, a new
one is created.

The ``write`` method puts data into the file.

.. code-block:: python

    >>> line1 = "This here's the wattle,\n"
    >>> fout.write(line1)

Again, the file object keeps track of where it is, so if you call
``write`` again, it adds the new data to the end.

.. code-block:: python

    >>> line2 = "the emblem of our land.\n"
    >>> fout.write(line2)

As we saw with reading, when you are done writing, you should close the
file.

.. code-block:: python

    >>> fout.close()

The ``format`` method for strings
---------------------------------

The argument of ``write`` has to be a string, so if we want to put other
values in a file, we have to convert them to strings. The easiest way to
do that is with the ``str`` conversion function:

.. code-block:: python

    >>> x = 52
    >>> f.write(str(x))

An alternative is to use the **``format`` method** on strings. The
string on which the format method is called should contain **replacement
fields** surrounded by curly braces (``{}``). Arguments to the
``format`` method are inserted in the replacement fields, in order.

Here are some examples:

.. code-block:: python

    "My name is {}!".format('Tim!')

which results in the string ``'My name is Tim!'``

.. code-block:: python

   '''{} is the answer to life, 
      the universe, 
      and something else, maybe'''.format(41)

which results in:

::

    '41 is the answer to life, the universe, and something else, maybe'

Within the curly braces, you can specify *how* the replacement item
should be formatted. For example, you can specify that replacement items
should be centered, left justified, or right justified within some
column width, or that a floating point number be shown with a certain
number of decimal places:

.. code-block:: python

    'I am {:d} years old in dog years'.format(age * 7)

Assuming ``age`` is defined, this will convert ``age * 7`` to a
decimal integer (that's the ``d`` in the replacement field). If
``age`` is 2, the resulting string is just
``'I am 14 years old in dog years'``

.. code-block:: python

    'Center this: {:^30}'.format('my string')

In this example, the caret character (``^``) means to center the
replacement item, and the value 30 is the field width. So the
string ``my string`` is centered in a 30-character width. In
addition to ``^``, you can use ``<`` to left-justify an item,
and ``>`` to right-justify an item.

.. code-block:: python

    'PI to 3 decimal places is {:.3f}'.format(math.pi)

In this example, we specify that we want to convert the
replacement item to a floating point number (the ``f``), and
show 3 decimal places (the ``.3`` preceding the ``f``).

.. code-block:: python

    coords = [4.2, 5.532]
    'x,y = {:.1f},{:.1f}'.format(coords[0], coords[1])

In this example, we have two replacement fields, each with
floating point format specifiers. Because we have two
replacement fields, we need two replacement items as arguments
to the ``format`` method.

The ``format`` method is useful, but the replacement field syntax is a
bit complex and we won't go into any more depth here. For full details,
please refer to the Python documentation:
http://docs.python.org/library/string.html#formatstrings. (Finally, note
that if you're using a version of Python less than 2.7, the format
method works a bit differently. Please ensure that you're using Python
2.7.)

Advanced files: filenames and paths
-----------------------------------

Files are organized into **directories** (also called "folders"). Every
running program has a "current directory," which is the default
directory for most operations. For example, when you open a file for
reading, Python looks for it in the current directory.

The ``os`` module provides functions for working with files and
directories ("os" stands for "operating system"). ``os.getcwd`` returns
the name of the current directory:

.. code-block:: python

    >>> import os
    >>> cwd = os.getcwd()
    >>> print cwd
    /Users/jsommers

``cwd`` stands for “current working directory.” The result in this
example is ``/Users/jsommers``, which is the home directory of a user
named ``jsommers``.

A string like ``cwd`` that identifies a file is called a **path**. A
**relative path** starts from the current directory; an **absolute
path** starts from the topmost directory in the file system.

The paths we have seen so far are simple filenames, so they are relative
to the current directory. To find the absolute path to a file, you can
use ``os.path.abspath``:

.. code-block:: python

    >>> os.path.abspath('memo.txt')
    '/Users/jsommers/memo.txt'

``os.path.exists`` checks whether a file or directory exists:

.. code-block:: python

    >>> os.path.exists('memo.txt')
    True

If it exists, ``os.path.isdir`` checks whether it’s a directory:

.. code-block:: python

    >>> os.path.isdir('memo.txt')
    False
    >>> os.path.isdir('music')
    True

Similarly, ``os.path.isfile`` checks whether it’s a file.

``os.listdir`` returns a list of the files (and other directories) in
the given directory:

.. code-block:: python

    >>> os.listdir(cwd)
    ['music', 'photos', 'memo.txt']

To demonstrate these functions, the following example "walks" through a
directory, prints the names of all the files, and calls itself
recursively on all the directories.

.. code-block:: python

    def walk(dir):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)

            if os.path.isfile(path):
                print path
            else:
                walk(path)

``os.path.join`` takes a directory and a file name and joins them into a
complete path.

    **Exercise**

    1. Modify ``walk`` so that instead of printing the names of the
       files, it returns a list of names.

       The ``os`` module provides a function called ``walk`` that is
       similar to this one but more versatile. Read the documentation
       and use it to print the names of the files in a given directory
       and its subdirectories.

Catching exceptions
-------------------

A lot of things can go wrong when you try to read and write files. If
you try to open a file that doesn’t exist, you get an ``IOError``:

.. code-block:: python

    >>> fin = open('bad_file')
    IOError: [Errno 2] No such file or directory: 'bad_file'

If you don’t have permission to access a file:

.. code-block:: python

    >>> fout = open('/etc/passwd', 'w')
    IOError: [Errno 13] Permission denied: '/etc/passwd'

And if you try to open a directory for reading, you get

.. code-block:: python

    >>> fin = open('/Users')
    IOError: [Errno 21] Is a directory

To avoid these errors, you could use functions like ``os.path.exists``
and ``os.path.isfile``, but it would take a lot of time and code to
check all the possibilities (if "``Errno 21``\ " is any indication,
there are at least 21 things that can go wrong).

It is better to go ahead and try, and deal with problems if they happen,
which is exactly what the ``try`` statement does. The syntax is similar
to an ``if`` statement:

.. code-block:: python

    try:    
        fin = open('bad_file')
        for line in fin:
            print line
        fin.close()
    except:
        print 'Something went wrong.'

Python starts by executing the ``try`` clause. If all goes well, it
skips the ``except`` clause and proceeds. If an exception occurs, it
jumps out of the ``try`` clause and executes the ``except`` clause.

Handling an exception with a ``try`` statement is called **catching** an
exception. In this example, the ``except`` clause prints an error
message that is not very helpful. In general, catching an exception
gives you a chance to fix the problem, or try again, or at least end the
program gracefully.

Case study 1: retrieving and processing files available on the internet
-----------------------------------------------------------------------

The ``urllib2`` module provides methods for manipulating URLs and
downloading files from the internet. Interestingly, opening a URL on the
internet using this module is very similar to opening a file stored on
your own computer.

At the beginning of this chapter, we saw that a copy of the
``words.txt`` file is stored at
http://cs.colgate.edu/~jsommers/cosc101/words.txt. Using the ``urllib2``
module, we can open and process the file, even though it isn't locally
stored!

.. code-block:: python

    import urllib2

    connection = urllib2.urlopen("http://cs.colgate.edu/~jsommers/cosc101/words.txt")
    for line in connection:
        print line
    connection.close()

The only difference between this program and an equivalent program that
reads a locally stored file is how the file is opened! (And, of course,
we need to import the ``urllib2`` module). Note that if you run the
above program, you'll see each word in the ``words.txt`` file, followed
by a blank line. Make sure you understand *why* that's the case, and
that you know how to modify the above program to *only* print each word
on a line (and not the blank lines).

Writing modules
---------------

Any file that contains Python code can be imported as a module. For
example, suppose you have a file named ``wc.py`` with the following
code:

.. code-block:: python

    def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count

    print linecount('wc.py')

If you run this program, it reads itself and prints the number of lines
in the file, which is 7. You can also import it like this:

.. code-block:: python

    >>> import wc
    7

Now you have a module object ``wc``:

.. code-block:: python

    >>> print wc
    <module 'wc' from 'wc.py'>

That provides a function called ``linecount``:

.. code-block:: python

    >>> wc.linecount('wc.py')
    7

So that’s how you write modules in Python.

The only problem with this example is that when you import the module it
executes the test code at the bottom. Normally when you import a module,
it defines new functions but it doesn’t execute them.

Programs that will be imported as modules often use the following idiom:

.. code-block:: python

    if __name__ == '__main__':
        print linecount('wc.py')

``__name__`` is a built-in variable that is set when the program starts.
If the program is running as a script, ``__name__`` has the value
``__main__``; in that case, the test code is executed. Otherwise, if the
module is being imported, the test code is skipped.

    **Example**:

    1. Type this example into a file named ``wc.py`` and run it as a
       script. Then run the Python interpreter and ``import wc``. What
       is the value of ``__name__`` when the module is being imported?

    Warning: If you import a module that has already been imported,
    Python does nothing. It does not re-read the file, even if it has
    changed.

    If you want to reload a module, you can use the built-in function
    ``reload``, but it can be tricky, so the safest thing to do is
    restart the interpreter and then import the module again.

Debugging
---------

When you are reading and writing files, you might run into problems with
whitespace. These errors can be hard to debug because spaces, tabs and
newlines are normally invisible:

.. code-block:: python

    >>> s = '1 2\t 3\n 4'
    >>> print s
    1 2  3
     4

The built-in function ``repr`` can help. It takes any object as an
argument and returns a string representation of the object. For strings,
it represents whitespace characters with backslash sequences:

.. code-block:: python

    >>> print repr(s)
    '1 2\t 3\n 4'

This can be helpful for debugging.

One other problem you might run into is that different systems use
different characters to indicate the end of a line. Some systems use a
newline, represented ``\n``. Others use a return character, represented
``\r``. Some use both. If you move files between different systems,
these inconsistencies might cause problems.

For most systems, there are applications to convert from one format to
another. You can find them (and read more about this issue) at
http://wikipedia.org/wiki/Newline. Or, of course, you could write one
yourself.

Glossary
--------

file object:
    A value that represents an open file.

.. raw:: html

   <!--
   problem recognition:
     ~ A way of solving a problem by expressing it as an instance of a
       previously-solved problem.

   special case:
     ~ A test case that is atypical or non-obvious (and less likely to be
       handled correctly).
   -->

format string:
    A string, used with the format method, that contains replacement
    fields.

replacement field:
    A sequence of characters in a format string, like ``{:d}``, or
    ``{:.2f}``, or even just ``{}``, that specifies how a replacement
    item should be formatted.

text file:
    A sequence of characters stored in permanent storage like a hard
    drive.

directory:
    A named collection of files, also called a folder.

path:
    A string that identifies a file.

relative path:
    A path that starts from the current directory.

absolute path:
    A path that starts from the topmost directory in the file system.

catch:
    To prevent an exception from terminating a program using the ``try``
    and ``except`` statements.

.. rubric:: Exercises

1. This question is based on a Puzzler that was broadcast on the
   radio program *Car Talk*\  [2]_:

   Give me a word with three consecutive double letters. I’ll give
   you a couple of words that almost qualify, but don’t. For
   example, the word committee, c-o-m-m-i-t-t-e-e. It would be great
   except for the ‘i’ that sneaks in there. Or Mississippi:
   M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would
   work. But there is a word that has three consecutive pairs of
   letters and to the best of my knowledge this may be the only
   word. Of course there are probably 500 more but I can only think
   of one. What is the word?

   Write a program to find it.

2. Here’s another *Car Talk* Puzzler [3]_:

   "I was driving on the highway the other day and I happened to
   notice my odometer. Like most odometers, it shows six digits, in
   whole miles only. So, if my car had 300,000 miles, for example,
   I’d see 3-0-0-0-0-0.

   "Now, what I saw that day was very interesting. I noticed that
   the last 4 digits were palindromic; that is, they read the same
   forward as backward. For example, 5-4-4-5 is a palindrome, so my
   odometer could have read 3-1-5-4-4-5.

   "One mile later, the last 5 numbers were palindromic. For
   example, it could have read 3-6-5-4-5-6. One mile after that, the
   middle 4 out of 6 numbers were palindromic. And you ready for
   this? One mile later, all 6 were palindromic!

   "The question is, what was on the odometer when I first looked?"

   Write a Python program that tests all the six-digit numbers and
   prints any numbers that satisfy these requirements.

3. Here’s another *Car Talk* Puzzler you can solve with a
   search [4]_:

   "Recently I had a visit with my mom and we realized that the two
   digits that make up my age when reversed resulted in her age. For
   example, if she’s 73, I’m 37. We wondered how often this has
   happened over the years but we got sidetracked with other topics
   and we never came up with an answer.

   "When I got home I figured out that the digits of our ages have
   been reversible six times so far. I also figured out that if
   we’re lucky it would happen again in a few years, and if we’re
   really lucky it would happen one more time after that. In other
   words, it would have happened 8 times over all. So the question
   is, how old am I now?"

   Write a Python program that searches for solutions to this
   Puzzler. Hint: you might find the string method ``zfill`` useful.

4. The website http://www.uszip.com provides information about every
   zip code in the country. For example, the URL
   http://www.uszip.com/zip/13346 provides information about
   Hamilton, NY, including population, longitude and latitude, etc.

   Using the ``urllib2`` module, write a program that prompts the
   user for a zip code and prints the name and population of the
   corresponding town.

   Note: the text you get from uszip.com is in HTML, the language
   most web pages are written in. Even if you don't know HTML, you
   should be able to extract the information you are looking for.

   By the way, your program is an example of a "screen scraper." You
   can read more about this term at
   http://wikipedia.org/wiki/Screen_scraping.

5. In a large collection of MP3 files, there may be more than one
   copy of the same song, stored in different directories or with
   different file names. The goal of this exercise is to search for
   these duplicates.

   a. Write a program that searches a directory and all of its
      subdirectories, recursively, and returns a list of complete
      paths for all files with a given suffix (like ``.mp3``). Hint:
      ``os.path`` provides several useful functions for manipulating
      file and path names.

   b. To recognize duplicates, you can use a hash function that
      reads the file and generates a short summary of the contents.
      For example, MD5 (Message-Digest algorithm 5) takes an
      arbitrarily-long "message" and returns a 128-bit "checksum."
      The probability is very small that two files with different
      contents will return the same checksum. You can read about MD5
      at http://wikipedia.org/wiki/Md5.

      To obtain the MD5 checksum on the contents of a file, you can
      use the ``hashlib`` module, built in to Python:

      ::

          >>> import hashlib
          >>> csum = hashlib.md5()
          >>> csum.update("Nobody inspects the spammish repetition.")
          >>> csum.hexdigest()
          'dc6480df97e6f16ec0aa18c96522aee6'

      With the ``update`` method on the ``csum`` object, you can
      update the checksum by adding new strings (or file contents).
      When you're done processing the contents of a file, you can
      use the ``hexdigest`` method to obtain the final checksum in
      hexadecimal form.

.. rubric:: Footnotes


.. [1]
   http://wikipedia.org/wiki/Moby_Project.

.. [2]
   http://www.cartalk.com/content/puzzler/transcripts/200725

.. [3]
   http://www.cartalk.com/content/puzzler/transcripts/200803

.. [4]
   http://www.cartalk.com/content/puzzler/transcripts/200813
