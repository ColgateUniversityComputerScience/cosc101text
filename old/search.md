
# Searching

## The search problem

Imagine that you see a list of the students in your computer science
class, and you want know whether your friend Alice is in the same
lecture section.  If the list looks like

>  ---------
>  Emily
>  Bob
>  Charlie
>  Deborah
>  ---------

it's pretty easy for you to see that Alice is not in the same class. (On
the other hand, you may be pleasantly surprised to learn that your
friend Bob *is* in the class with you.)  Here, the class list is small
enough to look at all at once; you can determine at a glance that Alice
is not in the class but that Bob is.

If the list were for a much larger class (with dozens or hundreds of
people), it would take you a bit more time to answer the question of
whether Alice is in the class.  If the list were much larger still
(and if it were already stored in Python), it would be much more
natural to ask Python to *search* the list for you instead of asking
it to print out the list and then reading it for yourself on the
screen.

This example illustrates the **search problem**: Given a list and a
particular thing that might appear in the list (Alice's name in the
example above), determine whether or not that thing appears in the list
and, if it does appear in the list, where it appears.  (For example, if
we were searching for Bob's name in the list above, we would want to
know that it appears at index 1 when this is viewed as a Python list.) 
An important note is that, if the thing we're searching for appears
multiple times in the list, we will be satisfied (unless otherwise
specified) with knowing *any one* of the places where it appears.

## Built-in solutions

Recall that the `index` method for lists will return the smallest index
where a given element occurs in the list.  Until we study how to handle
the `ValueError` "exception" that this method returns when the element
does not occur in the list, we could first use the `in` operator to
check if the element is in the list.  Thus, one way to code an answer to
the search problem is the following:

	def mySearch(myList,x):
	    '''
	    If x occurs in myList, return an index where x occurs.
	    If x does not occur in myList, return -1.
	    Uses the index method for lists.
	    '''
	    if x not in myList:
	        return -1
	    return myList.index(x)


Knowing how to use built-in methods for searching is very useful.
However, it doesn't tell us how to think about the search problem or
help us understand how to solve it.  Look back at the code for
`mySearch` above; it tells us an index where `x` is (if it's in
`myList`) or that it's not in `myList` (via the returned value `-1`),
but we have no idea how it does this because that information is
locked inside the `index` method.  In order to get a better
understanding of this problem, we'll study two search algorithms:
*linear search* and *binary search*.

## Linear search

Our first search algorithm, **linear search**, formalizes the simplest
way that we might look for something in a list.  We'll simply walk
through the entire list, from beginning to end, checking each element
to see if it's the one we want.  If we find the element we want at
index `i`, we'll return `i`.  If we get to the end of the list without
finding the element we're looking for, then---because we've looked at
every single element in the list---we know that the element doesn't
appear in the list.  At that point, we'll do something to indicate (to
the user or whatever code called our search function) that the element
doesn't appear in the list; in the example below (and throughout this
chapter), we'll return `-1` if the searched-for element doesn't appear
in the list.

Following this discussion, it's straightforward to code up linear
search.  One version is below; this assumes that we are looking for
the element `x` in the list `myList`.

	def linSearch(myList,x):
	    '''
	    If x occurs in myList, return an index where x occurs.
	    If x does not occur in myList, return -1.
	    Uses linear search.
	    '''
	    for i in range(len(myList)):
	        if myList[i] == x:
	            return i
	    # If we haven't returned yet, x isn't in the list
	    return -1

At what point in our search can we be sure that `x` doesn't appear in
the list?  When doing linear search, we only know this after we've
checked *every* element in the list.  This means that we can't return
`-1` (indicating that `x` isn't in the list) until *after* the `for`
loop in the code above; in particular, if we included this as part of
the `for` loop, our function would return `-1` as soon as it
determined that the element at index `0` was not `x`.  (We'll discuss
some more implications of this when we analyze search algorithms later
in the chapter.)

## Binary search

Our second search algorithm, **binary search**, takes a different
approach.  Think about looking up a work in a (paper) dictionary.  If
you were looking up "xylophone," you wouldn't start at the very
beginning of the dictionary (as you would if you were doing a linear
search).  If you open the dictionary to a page near the end, you might
not pick the right page; however, you know whether you should flip
forward or backward in order to find "xylophone."  This relies on the
fact that the words in the dictionary are in alphabetical order;
binary search will also assume that its input is already in order, and
this will make it (as we'll see later in this chapter) faster than
linear search.

The basic approach to binary search is to look at the middle element
of the list (whose elements are in order).  If that element is the one
we're looking for, then we're done.  If it isn't, then---because the
list is in order---we know whether we should look earlier or later in
the list.  We then repeat this process, looking at the midpoint of
elements before (or after, as appropriate) the original midpoint.

As an example, consider the list `[1,3,4,6,17,28,42]`.  Following our
intuitive description of binary search, if we search for `17` in this
list, we would first check the middle value `6`.  This is not `17`, so
we continue; because the value we checked is smaller than the value
we're looking for, we'll continue by looking at the list elements to
the right of `6`.  When we restrict our attention to these
values---`17`, `28`, and `42`---we'll again look at the middle value
(*out of the values to which we've restricted our attention*), namely
`28`.  This is still not `17`, so we'll continue; because the value we
checked is bigger than `17`, we'll now look to its left.
(Importantly, we *don't* consider all of the values to the left of
`28` in the original list; instead, we look only at the values to the
left of `28` that were still under consideration.)  This leaves us
with only the value `17` to consider, which is the value we were
looking for.  We may now return `4`, the index of `17`.  (As we'll see
below, we may need to take some care to make sure that we compute the
correct index.)

What would happen if we used binary search to search for `18` in the
same list (`[1,3,4,6,17,28,42]`)?  Again, the value we're looking for
isn't the middle value (and is bigger than the middle value), so we'd
look at the right part of the list.  We'd then continue by looking at
the left part of *that* list, leaving us with just `17`.  In this
case, however, the value we're looking for *isn't* the middle (only)
value under consideration.  We'll still follow the rule, though, and
look at the values that are to the right of `17` in the remaining
list.  However, *there are no such values!* This tells us that we can
stop (and return `-1` to indicate that `18` isn't in the list)---we
know that if `18` were in the list, it would be to the left of `28`
and to the right of `17`, but there are no such elements.

We'll now code the binary search algorithm in three different ways.
The first one is non-recursive; the second and third are recursive,
but they differ in how they pass the list to the recursive function
call (and, thus, in how they must process the answer returned by the
recursive call).

### Coding binary search non-recursively

Our first approach to binary search is non-recursive.  The search
function takes the list and the element to find as arguments.  It
initially sets the limits (`low` and `high`) on the indices to search
as the first and last indices in the list; after checking the midpoint
(if the midpoint isn't the value we're looking for), it updates one of
these limits to narrow the search window.^[Remember that `//` does
rounded division and produces an `int` if its arguments are `int`s.]
For example, if the value at index `mid` is smaller than the value
we're looking for, then the left limit on the search window (`low`)
will be set to `mid+1`; if `mid` is larger than the value we're
looking for, `high` is set to be `mid-1` instead.  Importantly, this
means---even if the function is only looking at one element (i.e.,
`low` and `high` are the same index)---that the search window gets
*smaller* (not just stays the same) at every step.  In particular, if
the element we're looking for isn't in the list, we'll eventually
reach a point where `high` is less than `low`; once that happens, the
function will return `-1` to indicate that the element isn't in the
list.^[As an example, trace through the execution of
`BinSearch([1,3,4,6,17,28,42],18)` to see how this code implements one
of the examples discussed in the previous subsection.]

	def BinSearch(myList,x):
	    '''
	    If x occurs in myList, return an index where x occurs.
	    If x does not occur in myList, return -1.
	    Uses non-recursive binary search.
	    '''

	    # Initialize left and right indices to search.
	    low = 0
	    high = len(myList) - 1

	    # The indices from low through high are where x might be.
	    # As long as low <= high (and we haven't found x), we'll
	    # keep looking for x.  Note that this takes care of empty
	    # lists---high starts out at -1 in that case---so we don't
	    # need to explicitly check that the list is non-empty.
	    while low <= high:
	        # mid is the index that we'll check
	        mid = (low + high)//2
	        item = myList[mid]
	        if x == item:
	            return mid
	        elif x < item:
	            high = mid - 1
	        else:
	            low = mid + 1

	    # If we haven't returned yet, x isn't in the list; return -1.
	    return -1

Each time through the `while` loop, this function is doing binary
search on a shorter list than before.  That should bring to mind the
basic principles of recursion; it's natural to implement binary search
recursively, which we'll do next.

### Coding binary search recursively

Our first recursive implementation of binary search draws on the
approach used in `BinSearch` above; we'll keep track of a window in
the list where `x` (the element we're looking for) might be and then
search that window.  Instead of narrowing the window each time through
a `while` loop, we'll instead pass the updated limits of the window to
a recursive call to the function.  (We'll also give it the list that
we're search and the element that we're looking for.)

Because we're doing this recursively, we need to figure out what our
base case(s) will be and how we should use the value returned by the
recursive call.  As before, we'll know that we're done when we either
have no more elements to check or we've found an instance of the value
we're looking for.  In the latter case, we'll be returning an index
and not making any more recursive calls, so we don't need to cover it
in a base case.  To put us into the former case, either the list
itself could be empty or we could have `high < low`.  For now, we'll
assume that `low >= 0` and `high <= len(myList) - 1` (where `myList`
is the input list) so, if the list is empty (has length `0`), then
we'll also have `high < low`.  Thus, our base case will simply check
whether `high < low`, and the function will return `-1` if that test
is `True`.

We'll compute `mid` and use it the same way as in the non-recursive
version; here, instead of looping through a `while` loop again, we'll
make a recursive call to the function instead.  What should we do with
the output of the recurve call?  Imagine that we're in one call to the
function (maybe the first call, maybe nested 42 times down) and we get
an output from a recursive call to the function.  If that output is
`-1`, then the value we're looking for doesn't appear in the part of
the list that we searched recursively; by design, that's the only part
of the list where the element we're looking for might appear, so we
can safely return `-1` as well.  If that output is something else
(i.e., it's an index where we can find that value), then that index is
an index *in the same list that we have* where the searched-for value
appears; that means we can safely return this other value as an index
where the searched-for value appears.  Thus, regardless of the output
of the recursive call, we can simply return the value that it
returned.

	def RecBinSrch1(myList,x,low,high):
	    '''
	    If x occurs in myList, return an index where x occurs.
	    If x does not occur in myList, return -1.
	    Uses recursive binary search, with the same list in the
	    recursive call.  Searches between indices low and high, inclusive.
	    Assumes that low >= 0 and high <= len(myList) - 1.
	    '''
	    if high < low:
	        return -1
	    mid = (low + high)//2
	    item = myList[mid]
	    if x == item:
	        return mid
	    elif x < item:
	        high = mid - 1
	    else:
	        low = mid + 1
	    return RecBinSrch1(myList,x,low,high)

We've assumed that the user will only call this with `low >= 0` and
`high <= len(myList) - 1`.  We could drop this assumption if we
checked these values; we'd then want to let the user know what had
gone wrong.  To do that, we probably *wouldn't* want to return `-1`,
because we're using that to mean that the element isn't in the list.
We could instead add something like:

	    # Add this *after* checking whether the list is empty;
	    # that way, if the user calls, e.g.,
	    # myL = []
	    # RecBinSrch1(myL,17,0,len(myL)-1)
	    # we'll respond with -1 instead of -2.
	    #
	    # Check that search window is legal; return -2 if not.
	    if low < 0 or high > len(myList) - 1:
	        return -2

at the beginning of the code.  Of course, we'd then need to update the
docstring so that it accurately describes the revised function's
behavior.^[You might wonder if this causes any problems when returning
the value returned by a recursive call to the function.  The only way
that the function would return `-2` is if `low <= high`---otherwise it
would have returned `-1`---and either `low < 0` or `high > len(myList)
- 1`.  However, if `low <= high`, then the recursive call will be made
with `low` at least as large as it was before and with `high` no
larger than it was before.  This means that the problems this new test
is checking for will be caught by the very first call to the function,
and they could never arise after that point.  As a result, it would
usually be better to keep this test out of the function---where it
might be called many times, all but one of them unnecessarily---and
have the programmer verify that the assumptions `low >= 0` and `high
<= len(myList) -1` hold.]

### Recursive binary search with new lists

If you thought about coding binary search recursively, your first
thought might have been to create a new list containing the part of
the old list that you're continuing to search.  For example, if your
function were called `RecBinSrch2`, then (applying it to the example
above), you might expect

	RecBinSrch2([1,3,4,6,17,28,42],17)

to make the recursive call

	RecBinSrch2([17,28,42],17)

This is completely reasonable, but we'll need to do a bit of work to
make sure the function returns the correct answer.  In particular,
what is the answer that the second call (`RecBinSrch2([17,28,42],17)`)
should return?  Clearly, this function should return `0`, the only
index of `17` in the list `[17,28,42]`.  However, `17` does *not*
occur at index `0` in the original list (`[1,3,4,6,17,28,42]`) from
the first call to `RecBinSrch2`.  That function should return `4`, not
`0`, so we need to figure out how to transform the `0` that we get
back from the recursive call into the `4` that the original function
call is supposed to return.

Look back at these two calls to `RecBinSrch2`; how did we get the
second list from the first one?  We removed the midpoint and
everything to its left.  To determine the index of `17` in the longer
list, we can take its index in the shorter list (`0`, as determined by
the recursive call to `RecBinSrch2`) and add to it the number of
elements from the longer list that originally were to the left of the
shorter list.  (Importantly, if we had made the shorter list by
removing elements from the right of the longer list, then the index of
`17`---or whatever value we were searching for---would be *the same*
in the shorter list and in the longer list.)

Let's code this up:

	def RecBinSrch2(myList,x):
	    '''
	    If x occurs in myList, return an index where x occurs.
	    If x does not occur in myList, return -1.
	    Uses recursive binary search, with a shorter list
	    in the recursive call.
	    '''
	    # Base case is a list of length 0; x is then not in myLis.
	    if len(x) < 1:
	        return -1
	    # Find the index of the midpoint and test the value there
	    mid = (len(myList) - 1) // 2
	    if myList[mid] == x:
	        return mid
	    # If myList has length 1, then x is not in it and we can stop.
	    # This lets us assume that len(myList) > 1, so mid > 0.
	    if len(myList) == 1:
	        return -1
	    # If still searching, how does x compare to the tested value?
	    # If x would be in the left of myList, return the value
	    # returned by the recursive call.
	    if x < myList[mid]:
	        # Remember that mid > 0, so the upper index of the following
	        # slice is not negative; we only get the elements to the left
	        # of index mid.
	        newList = myList[:mid - 1]
	        return RecBinSrch2(newList,x)
	    # 
	    else:
	        newList = myList[mid + 1:]
	        recAns = RecBinSrch2(newList,x)
	        # If recAns is -1, that's what we want to return
	        if recAns == -1:
	            return -1
	        # If recAns is an index, we need to add the number of elements
	        # that we dropped to produce newList before we return our answer.
	        return recAns + mid + 1

## Comparison of search algorithms

We've seen both linear and binary search; we coded the former in just
five lines of code, so you may have wondered why we bothered to learn
a second search algorithm.  As we'll show, binary search is faster
than linear search (for long enough lists), and the relative advantage
of binary search is more significant when used on longer lists.

For both linear search and non-recursive binary search, we'll look at
the number of operations that might possibly be needed to search for a
value in a list of a given length.  Let's start with our example list
`[1,3,4,6,17,28,42]` from before, which has length `7`.  Before going
further, we need to figure out what counts as an `operation`.  It will
suffice to consider the number of equality tests that are evaluated
(we'll discuss this more later).  In `linSearch(myList,x)`, there's
one such test, the line `if myList[i] == x:`.  In
`BinSearch(myList,x)`, there is also one such test, the line `if x ==
item:`.

For the example list that we're using, what is a value `x` that will
require the greatest number of equality tests for linear search?  What
about for binary search?  One example is `18`, a value that's not in
the list.^[Because of the list we chose, *any* value that's not in
this example would cause the maximum number of equality tests to be
evaluated.  However, for some lists, the number of tests could vary by
a very small amount depending on which value not in the list you
searched for.  For example, searching the list `[17,42]` for `16`
would require fewer operations than would searching it for `18`; in
the first case, after checking `17`, `high` is less than `low` and the
function returns `-1`, while in the second case, `low = high` and we
need to test the value `42`.]  When we use `linSearch`, we need to
evaluate the one equality test in this function seven times (one for
each value of `i` in the output of `range`).  When we use `BinSearch`,
we do the tests `18 == 6`, `18 == 28`, and `18 == 17`---just three
tests.

However, that just tells us that linear search is better in this
example (and assuming we only care about equality tests---you've
surely noticed that there's a lot of other code that gets executed in
`BinSearch`; if we counted the `<=` test and the operations `//` and
`=`, we'd get more operations for `BinSearch` than for `linSearch`).
We'll get a clearer understanding of what's happening if we look at a
longer list.

Let's now search the list
`[1,3,4,6,17,28,42,50,51,64,101,216,243,256,343]`.  If we look for the
value `18` in this list (which has 15 elements), `linSearch` will do
15 equality tests; as before, it does one for each value in the list
(because we `18` is not a value in the list, we check every value when
doing linear search).  How many will `BinSearch` do?  It will first
check `18 == 50`, then `18 == 6`, `18 == 28`, and `18 == 17`---four
equality tests.  In roughly doubling the length of the list (going
from seven to 15 elements), we've roughly doubled the number of
equality tests that `linSearch` does, but we've only added 1 to the
number of equality tests that `BinSearch` does.  As you might guess,
this is true more generally; doubling the length of the list another
time will again double the number of equality tests that `linSearch`
must do (in the worst case), but it will only add 1 to the number of
equality tests that `BinSearch` must do (in the worst case).

While there are other operations that are used in these two functions,
an important thing is that each of those operations is done at most
once each time through the loop (the `for` loop in `linSearch` and the
`while` loop in `BinSearch`),^[That is, there aren't loops---or other
things whose number of operations depends on the input---embedded
within these loops.] and the equality test is done each time through
the loop.  That means that the total number of operations (in a more
precise accounting) would be some constant multiple of the number of
equality tests that we've counted.^[We're still ignoring the
operations that are outside the loops, like `low = 0`.  These don't
depend on the input, and right now we're focusing on the effects of
input size on the number of operations.]

The total number of operations, then, is (a constant times) the length
of the list for `linSearch`.  What about for `BinSearch`?  If we start
with a list of length 1 (which is $2^0$), one equality test (and one
pass through the `while` loop) is required; applying the ideas
discussed above, the number of equality tests will not be more than
$k$, if $2^k$ is greater than to the length of the list.  If you
remember logarithms from one of your math classes, this is the same
thing as saying that the number of times through the loop is at most
the base-2 logarithm of the length of the list (rounded up if the
logarithm isn't an integer).

<!-- FIXME 

## Extra topics

### More on comparison of search algorithms

We've only done a rough analysis of the linear- and binary-search
algorithms.  It's been enough to tell us that binary search is clearly
better (for long lists), but it's still been fairly informal.  In this
subsection, we'll make this a bit more formal.

...

Analysis of recursive algorithms

...

If you're interested in the analysis of algorithms, Colgate's COSC 102
course looks more at how to analyze the efficiency of algorithms (and
compare different algorithms that solve a particular problem), and the
COSC 302 course does this even more formally and extensively.  To get
a feel for what that course covers (and to see a more formal
discussion of some of the ideas we've hinted at here), you could look
at the draft version of the book by [Dasgupta, Papadimitriou, and
Vazirani][DPV] that is available online.

[DPV]: http://www.cs.berkeley.edu/~vazirani/algorithms.html

## Debugging

-->

## Glossary

linear search:
  ~ The approach of searching for an item in a list by inspecting
    each element in the list, one after another.

binary search:
  ~ Also known as *bisection search*.   An approach for searching
    a list which assumes the items in the list in sorted order.  It proceeds
    by checking the middle element, and deciding whether the item to
    search for is in the first half or second half of the list.  The
    "search space" is repeately cut in half by applying this same
    idea to smaller and smaller portions of the list.

## Exercises

> 1. Using the function definition in the text, what is the result of
>    calling `linSearch([3,1,4,1],1)`?  More generally, if the list argument
>    contains multiple occurrences of the element being searched for, which
>    index will be returned?  (Having thought about this, what do you think
>    would be a more descriptive docstring to include in the function
>    definition?)
> 
> 1. Implement linear search so that, if the list being searched contains
>    multiple occurrences of the element `x` being searched for, the
>    *largest* index where `x` occurs will be returned.
> 
> 1. Consider the following function:
> 
>            def mystery(x,y):
>                i = 0
>                while i < len(x):
>                    if x[i] == y:
>                        return i
>                    i += 2
>                i = 1
>                while i < len(x):
>                    if x[i] == y:
>                        return i
>                    i += 2
>                return -1
> 
>     a. What is the output of `mystery([3,-1,4,1,1],1)`?
>     a. Briefly describe what this code is doing in general.
> 
> 1. Write an implementation of linear search that, if `x` occurs multiple
>    times in the list being searched, *randomly* chooses an index where `x`
>    occurs and returns that; if `x` does not occur in the list, your
>    function should still return `-1`.  (Note that this still answers the
>    search problem, which only required *an* index of the searched-for
>    element.)
> 
> 1. Write an implementation of linear search that searches for a
>    character `c` in a string `s`.  As with the list version, your function
>    should return an index where `c` occurs (if `c` occurs in `s`) or `-1`
>    (if `c` does not occur in `s`).
> 
