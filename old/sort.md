
# Sorting

## The sorting problem and built-in solutions

Remember that binary search requires the elements in its input list to be *in order* (or *sorted*).  However, in Python we can certainly write lists that are not sorted.  If someone gives you a list to search, they might not guarantee that it's sorted; you could use something other than binary search, but, if you're going to search a long list many times, you'll probably want to rearrange the elements so that they're in sorted order.^[If you were just going to search the list *once*, it wouldn't be worth sorting it just to use binary search; even though binary search would be faster, the extra time to sort the list first wouldn't be offset by just a single use of binary search.  We won't worry about a precise analysis of the tradeoffs here, though.]

Thinking back to the chapter on searching, we started with the list of names

> Emily

> Bob

> Charlie

> Deborah

If you were given this, it would be pretty easy to put the names in (alphabetical) order as:

> Bob

> Charlie

> Deborah

> Emily

If, instead of the first list of names, you were given a list of all the people in your year in school, it would probably take you much longer to put the names in order.  Both of these are examples of the *sorting problem*: Given a list and a notion of order (i.e., which element of any pair should come before the other one),^[To be a bit more formal, we assume that there is a *linear order*, also known as a *total order*, on the kinds of things that might appear in the list.  This just means what we've assumed: whenever we're presented with two elements that might appear in the list, we know which one should come first.  For example, the usual less-than relationship provides a linear order for real numbers, and alphabetical ordering provides a linear order for words.  There are lots of other orderings that could be defined on these sets, and you could write a function that sorts using those.  However, the notion of order that's used to sort the list must match the notion of order that's used to search the list; as a somewhat contrived example, you could sort the list `['one','two','three']` using alphabetical order to get `['one','three','two']`, but if you then searched this for `two` using the order "`s` comes before `t` if and only if the number whose string description is `s` is less than the number whose string description is `t`", binary search would falsely tell you that `two` is not in the list.] rearrange the elements so that, if one element appears before another one in the list, the first element is smaller (according to our notion of order) than the second one.^[The resulting order is necessarily unique.]  Our general definition of the sorting problem won't specify whether this should rearrange (in place) the list that was given or produce a new (sorted) list while leaving the original list alone.  (Of course, if you write a sorting function, you should document which of these it does.)

Just like the search problem, the sorting problem can be solved using built-in methods and functions.  Recall the `sort()` method for lists and the built-in `sorted()` function; these can be used to solve the sorting problem (either in place or by creating a new list).  Also just like the search problem, knowing these techniques doesn't tell us how to think about the sorting problem.  We'll now spend some time looking at different sorting algorithms: selection sort, bubble sort, insertion sort, and merge sort.

We can group these into two classes.  The first three algorithms make repeated passes through the input list, with each pass increasing the number of sorted elements at one end of the list; each requires (roughly) $n^2$ operations to sort a list of $n$ elements (we discuss this more precisely later in this chapter), so doubling the length of the list (roughly) quadruples the amount of time it takes to sort it.  The last algorithm, merge sort, is inherently recursive and is able to sort a list of n elements in significantly less time (again, we'll make this more precise later).

## Selection sort

One straightforward way we can sort a list is to go through the entire list and find the smallest value.^[We'll use "smallest" to mean the value that should appear first in the sorted list, even if the list happens to be a list of strings, etc.]  We'll then put it in the first position in the list; to make things easy, we'll do that by simply swapping it with whatever was in the first position in the list.  At that point, the first (one) element is what it should be, and we'll turn our attention to finding the correct second element.  We'll again look through the entire list (although we can skip the first element) and find the smallest remaining element; then we'll swap that element with whatever is currently the second element.  At that point, the first two elements are what they should be, and we'll turn our attention to the third element, and so on.  This sorting algorithm is called *selection sort*---each time through the list, we select the next smallest element and put it in its correct place.

Speaking a bit more generally, after putting the smallest $i-1$ elements of the list in their correct places, we'll look through the rest of the list to find the $i^\text{th}$ smallest element, and then we'll swap it with whatever is currently in the $i^\text{th}$ position.  This means the smallest $i$ elements are now sorted, and we'll keep going through the list. 

Let's work through an example before we write some code.  Suppose we want to sort the list `[4,3,1,5,2]` using selection sort.  (To avoid any ambiguities in our discussion, we've chosen an example whose elements are all distinct.  Our code won't require that, though.)

We start by finding the smallest value in the list---in this case, `1`---and swapping it with whatever is in the leftmost position (index `0`) in the list.  This gives us

    [1,3,4,5,2]

We then look at the elements to the right of the first element---i.e., `3`, `4`, `5`, and `2`---and swap the smallest of these (the second-smallest element in the list) with the current second element in the list.  This gives us

    [1,2,4,5,3]

Continuing on, we successively obtain:

    [1,2,3,5,4]    (after i = 3)
    [1,2,3,4,5]    (after i = 4)
    [1,2,3,4,5]    (after i = 5)

Now let's write code for selection sort.  The general description above gives us a pretty good guide for how to proceed.  We'll let a variable `i` start at the first index (`0`), and we'll find the value that we want to swap into index `i`; we'll then repeat (using a `for` loop) this with increasingly large values of `i`.  The value that we want to swap into index `i` might be at index `i` or anywhere to the right of it (i.e., at a larger index); we'll check all of those indices (we'll call the one we're checking `j`) using another `for` loop.

	def selectionSort(x):
	    '''
	    Sort the list x in place using selection sort.
	    '''
	    # i is the index into which we're putting the
	    # correct element
	    for i in range(len(x)):
	        # curMinInd is the index of the smallest
	        # element we've seen so far that is at,
	        # or to the right of, index i; as we check
	        # the indexes j to the right of i, we'll
	        # update curMinInd as needed
	        curMinInd = i
	        for j in range(i,len(x)):
	            if x[j] < x[curMinInd]:
	                curMinInd = j
	        # At this point, curMinInd is the index of
	        # the smallest element at, or to the right of,
	        # index i; we'll swap the elements
	        x[i],x[curMinInd] = x[curMinInd],x[i]

One other note on selection sort: As you sort a list `x` using the code in the text, what do you know about the element at index `len(x) - 1` after the outer `for` loop has finished executing with `i` equal to `len(x) - 2`?  How could you use this observation to make the code above (slightly) more efficient?  (You might look back at the example using `[4,3,1,5,2]` above.)

## Bubble sort

Our second sorting algorithm, *bubble sort*, also has the effect of putting an element that should be at the end of the list in its correct position, then putting the element that should be next to it in its correct position, etc.  We'll write this in the opposite way from selection sort, though, putting the largest element in the correct position first.  That's just a cosmetic difference, though.  (One of the exercises asks you to rework this to put the smallest element in the correct place first as we did for selection sort.)  A somewhat more important difference is how this is done; bubble sort *doesn't* actually identify what the largest element is, it just performs operations that ensure that it winds up at the end of the list.

How does bubble sort do this?  Bubble sort goes through the list from left to right and compares each adjacent pair of values (the values at indexes `0` and `1`, then the values at indexes `1` and `2`, etc.); if a pair of values is in the wrong order, it swaps them before moving on to the next comparison.  Let's apply this to our example list `[4,3,1,5,2]`.  The first bubbling pass produces the intermediate lists

    [3,4,1,5,2]
    [3,1,4,5,2]
    [3,1,4,5,2]
    [3,1,4,2,5]

After we've gone through the entire list, the largest element is indeed at the end.  As promised, we never identified this specifically as the largest element.  Instead, it "bubbled up" to the end of the list; as we went through the list, we may (or may not) have swapped some elements before we got to the largest one.  (In the example above, we swapped the `3` and the `4` and then the `4` and the `1`; at that point, the `4` ran into the largest element `5`, which then bubbled to the end of the list.)  However, once we got to the largest element, it was larger than the element to its right, so we swapped those two elements; by definition, it was larger than *every* other element in the list, so we kept swapping it with its neighbor on the right until we got to the end of the list, at which point it was in its correct position at the end of the list.

Although we know that the largest element is in the correct position after one pass through the list, we can't say anything about where the other elements are.  (Can you identify property of the original list that would ensure that the second-largest element in a list of more than two elements is at index `0` after the algorithm makes on pass through the list?)  If we repeat the process, the largest element is out of the way, so the second-largest value will bubble up to the end of the list (stopping at the next-to-the-last position, where it belongs in the sorted list).  The full bubble-sort algorithm repeats this bubbling process until all of the elements in the list have been bubbled into their correct positions.

If we continue this process our example from above, the second bubbling pass produces the intermediate lists

    [1,3,4,2,5]
    [1,3,4,2,5]
    [1,3,2,4,5]
    [1,3,2,4,5]

The third bubbling pass produces (now skipping the intermediate steps)

    [1,2,3,4,5]

The fourth and fifth bubbling passes don't change anything; each pair is now in the correct order, so we never do any more swaps.

Let's start to code this up.  We'll use one `for` loop to keep track of which pass through the list we're on, and we'll use another (nested) `for` loop to make the pass through the list.  Let's start with a simple version in which we don't worry too much about the limits of the loop.  Each pass through the list will start by comparing the values at indices `0` and `1` and finish by comparing the values at indices `len(x)-2` and `len(x)-1`; however, some of those comparisons will be superfluous.  (In particular, after we've made `i` passes through the list, we know that the `i` values at indices `len(x)-1`, `len(x)-2`, ..., `len(x)-i` are in their correct positions.  The last comparison that matters on the next pass through the list is the one between the values at indexes `len(x)-i-2` and `len(x)-i-1`.  Keep this in mind for later.)


	def simpleBubbleSort(x):
	    '''
	    Sort the list x in place using simplified bubble sort.
	    '''
	    # Make len(x) passes through the list
	    for i in range(len(x)):
	        # Make a pass through the entire list,
	        # including superfluous comparisons.
	        # We'll compare the indexes j and j+1,
	        # so j shouldn't be bigger than len(x)-2.
	        for j in range(len(x)-1):
	            if x[j] > x[j+1]:
	                x[j],x[j+1] = x[j+1],x[j]

We can now refine this by tweaking the ranges used in the `for` loops.  First, we only need to make `len(x)-1` passes through the list; after that, the largest `len(x)-1` values will be in their correct positions, so the other value (the smallest one) must also be in its correct position.  Second, recall our discussion above.  The first time through the list, when `i` is `0`, we need `j` to go up to `len(x)-2`; when `i` is `1`, we can stop `j` after it's equal to `len(x)-3`; when `i` is `2`, we can stop `j` once it's `len(x)-4`.  In general, for a particular value of `i`, we need `j` to go through the values in `range(len(x)-1-i)`.^[As a check, the largest value of `i` will now be `len(x)-2`; at that point, `j` will go through the values in `range(1)`, i.e., we'll check the values at indexes `0` and `1` and swap them if needed, and that's it.]  Let's update our code to reflect this discussion:

	def bubbleSort(x):
	    '''
	    Sort the list x in place using bubble sort.
	    '''
	    # Make len(x)-1 passes through the list
	    for i in range(len(x)-1):
	        # Make a pass through the part of the list,
	        # that might not be sorted; compare the values
	        # at indexes j and j+1, swapping if out of order
	        for j in range(len(x)-1-i):
	            if x[j] > x[j+1]:
	                x[j],x[j+1] = x[j+1],x[j]


## Insertion sort

Our third sorting algorithm, *insertion sort*, also works by sorting some values at one end of the list and increasing the number of sorted values until the entire list is sorted.  *Unlike* our first two sorting algorithms, it only does this in a *relative* way.  Instead of moving, e.g., the smallest value anywhere in the list to the beginning of the list, insertion sort just looks at the first two elements and makes sure they're in the correct order; the algorithm then looks at the first three elements and puts them in the correct order, then the first four, and so on.  Let's see how this applies to the example `[4,3,1,5,2]` that we've been using. 

Putting the first two elements in the correct relative order produces

    [3,4,1,5,2]

Putting the first three elements in the correct relative order produces

    [1,3,4,5,2]

and putting the first four and five elements in the correct order produces

    [1,3,4,5,2]

(unchanged from before) and then

    [1,2,3,4,5].

We can think of this as letting `i` increase from `1` to `len(x)-1` and, for each value of `i`, moving the value that started at index `i` to its correct position relative to the elements at indexes `0` through `i-1`.  We could write this up as pseudocode:

	<Pseudocode for insertionSort(x)>
	    for i in range(len(x)):
	        Let y be the value at index i
	        Remove y and insert it into the index between 0 and i that puts
	            it in the correct position (in terms of order) relative
	            to the values at indexes 0 through i-1.

There are a couple of things left to do.  We've blithely said that we'll insert the next value under consideration (`y` in the pseudocode) into the "correct" position; we need to figure out how to determine the correct position of this element.  Also, the pseudocode suggests the use of the `pop` (if we use `y = x.pop(i)`) and `insert` list methods to accomplish this.  We could use those to solve the problem; however, like using the `sort` method, those would obscure exactly what's happening in this process.^[Because they'd be used as parts of the sorting algorithm, their use would obscure less than the use of `sort` would, but they'd still hide more than we'd like to hide in this discussion.]

If we're going to move the value at index `i` to a smaller index, we'll need to move other elements to the right in the list.  For example, to move `6` to the correct position (assuming we're considering the index `2`) in the list `[3,8,6]`, we need to put `6` at index `1` *and* put `8` at index `2`.  That's easy---we can just swap the two values.  If our list were `[7,8,6]` instead (and we were again looking at the element at index `2`), we couldn't just swap the `6` and the `7`.  We could use bubbling technique (from bubble sort) and first swap the `6` and the `8` to get `[7,6,8]`; then, we could swap the `6` and the `7` to get `[6,7,8]`, the list we wanted.  However, that results in some wasted effort; starting with `[7,8,6]`, it would be slightly faster to do "half" a swap and move the `8` to where the `6` is (after first saving the value `6` elsewhere) to get `[7,8,8]`.  We could then do "half" of the second swap, copying the value `7` to index `1` and obtaining `[7,7,8]`.  At this point, everything that needs to be moved has been moved (in the bubbling version, we didn't do any additional swaps), so we'll finally put the value `6` back into the list to get `[6,7,8]`.

We'll take this approach, but, as we move values to the right before inserting the value we took out of index `i`, we need to know when to stop moving values and insert the value from index `i`.  We can take advantage of the fact that the values in indexes `0` through `i-1` are already sorted---we can stop moving values to the right when we encounter one that's smaller than the value that was at index `i`.  Let's update our pseudocode:

	<Revised pseudocode for insertionSort(x)>
	    for i in range(1,len(x)):
	        Let y be the value at index i
	        Let j = i
	        As long as the value at index j-1 is larger than y:
	            Copy the value at index j-1 to index j
	            Decrease j by 1 (exit the loop if j becomes 0)
	        Put the value y at index j

The range for `i` now starts at `1` instead of `0` to ensure that `j-1` is always in range.  This is very close to actual code, so we can go ahead and write that now.

	def insertionSort(x):
	    '''
	    Sort the list x in place using insertion sort.
	    '''
	    for i in range(1,len(x)):
	        y = x[i]
	        j = i
	        while j > 0 and x[j-1] > y:
	            x[j] = x[j-1]
	            j -= 1
	        x[j] = y

A final note on insertion sort: At the beginning of the chapter, we said that our first three sorting algorithms make repeated passes through the list.  Unlike selection sort and bubble sort, the passes through the list that insertion sort makes get longer, not shorter.

## Merge sort

Merge sort is our last main sorting algorithm (we mention a few others in passing at the end of the chapter).  Unlike our first three sorting algorithms, merge sort is inherently recursive---unlike some recursive examples we've seen, there isn't a reasonable way to write this recursively.

Merge sort resembles binary search in that we'll repeatedly divide the list in half.^[This resemblance carries over to the efficiency analysis of merge sort, which will---like binary search---involve asking how many times we can divide the length of the list by 2 before reaching 1.]  We'll then sort each half of the list separately and combine the two sorted halves.  (This is a bit different from binary search, where we only concerned ourselves with one half of the list.)  Importantly, combining two sorted lists into a longer, sorted list is easy.  With that description, we can easily write pseudocode for merge sort:


	<Pseudocode for mergeSort(x)>
	    Take care of base case(s)
	    Divide x into two halves xLeft and xRight
	    # Assume merge() merges two sorted lists into a new list
	    return merge(mergeSort(xLeft),mergeSort(xRight))

Unlike our earlier implementations of sorting algorithms, this is outlined to produce a new list (which will contain all of the elements of `x`, but in sorted order) instead of sorting `x` in place.  Note the comment in the pseudocode; we've assumed that we have a helper function to take care of the merging.  Let's think about that in the context of the example that we've used throughout this chapter.

First, splitting the list `[4,3,1,5,2]` into two halves produces

    [4,3]

for `xLeft` and

    [1,5,2]

for `xRight`.  (Here, we'll let `mid` be the length of the list divided by `2` using integer division, and we'll split the list `x` as `x[:mid]` and `x[mid:]`.  In this case, `x[:2]` and `x[2:]` produce the two lists above.)   The recursive calls to mergeSort produce sorted versions of these lists, so the arguments to `merge` are lists `[3,4]` and `[1,2,5]`.

If we're given these two (sorted) lists, how can we merge them (into a new list) as efficiently as possible?  What is the first value that should appear in the new list?  Clearly, it's `1`.  If we'd had a different list as the second input (e.g., if we'd called `merge([3,4],[5,17,42])`), the first value in the merged list would have been `3`.  Is there any choice for the second list that would make the first value in the merged list be `4`?  Of course not---the first element can't be any bigger than `3` when one of the input lists is `[3,4]`.  More generally, we know that the first value in the new list will be the first value in one or the other of the input lists; this means we only need to compare these two values, and we can ignore the rest of the values.  Let's code up the `merge` function.

	def merge(list1,list2):
	    '''
	    Return a new list that is the (sorted)
	    merge of the two sorted input lists.
	    '''
	    newList = []
	    i = 0
	    j = 0
	    while i < len(list1) and j < len(list2):
	        if list1[i] < list2[j]:
	            newList.append(list1[i])
	            i += 1
	        else:
	            newList.append(list2[j])
	            j += 1
	    # One of the lists being concatenated onto newList
	    # will be empty
	    newList = newList + list1[i:] + list2[j:]
	    return newList

The `while` loop keeps comparing elements as long as each list has more elements that need to be merged.  Once we exhaust one of the lists (i.e., once we've added all of its elements to `newList`), which is indicated by the failure of the `while`-loop test, we still need to add the remaining elements from the other list.  However, the test failure doesn't tell us which list has elements that we still need to add to `newList`.  We get around that by adding the remaining elements from *both* input lists: `lsit1[i:]` and `list2[j:]`.  We know that one of these is empty, though (because the `while`-loop test failed); we also know that all of the elements remaining in the non-empty one of these are at least as large as all of the elements that we've already added on to `newList` (another benefit of having sorted lists as the inputs), so these can safely be concatenated onto the end of `newList`.

With the `merge` function in hand, let's return to writing the `mergeSort` function.  What should our base case be?  As with any sorting algorithm, if the input list has at most one element, then we're automatically done.  Does this mean that we can simply write

	    if len(x) <= 1:
	        return x

We need to be careful here.  We mentioned above that we were going to write our `mergeSort` function to return a *new* list, and we've written our `merge` function to do that.  Thus, we should make sure that we *always* return a new list.  If we used the code above for our base case, someone who called our function using the code

    y = [17]
    z = mergeSort(x)

would change `y` when they changed `z`.  Instead, we can return `x[:]`; remember that this will create a fresh copy of `x`, which we can return while keeping our promise to the user to give her a new list.  We can now update convert our pseudocode for `mergeSort` to actual code as follows:

	def mergeSort(x):
	    '''
	    Use merge sort to produce a new list containing the values of x in sorted order.
	    '''
	    if len(x) <= 1:
	        return x[:]
	    mid = len(x)//2
	    xLeft = x[:mid]
	    xRight = x[mid:]
	    return merge(mergeSort(xLeft),mergeSort(xRight))
	    

## Comparison of sorting algorithms

### Analyzing quadratic sorting algorithms

Let's compare the various sorting algorithms that we've studied so far.  We'll just focus on the number of comparison operations that each of these algorithms does (as we've coded them above); this will give us a good enough idea of the total number of operations that each algorithm requires.  Throughout this subsection, we'll use `n` for the value `len(x)`.

Our `selectionSort` function does one comparison for each distinct pair of values (`i`,`j`) (i.e., it does one comparison when `i` is `0` and `j` is `0`, another comparison when `i` is `0` and `j` is `1`, and so on).  How many such pairs are there?  For each value of `i`, `j` takes on the values `i`, `i+1`, ..., `len(x)-1` (so `n-i` different values for `j`).  When `i` is `0`, the algorithm does `n` comparisons; when `i` is `1`, the algorithm does `n-1` comparisons, etc.  The total number of comparisons is thus `n` + `n-1` + `n-2` + ... + `1`; this is known to equal `(n*n + n)/2`.

What about bubble sort?  Our `bubbleSort` function also does one comparison for each distinct pair of values (`i`,`j`).  The variable `i` starts at `0` and goes up to `n-2`; for a fixed value of `i`, `j` takes on `n-1-i` values.  Thus, when `i` is `0`, the algorithm does `n-1` comparisons; when `i` is `1`, it does `n-2` comparisons, and this continues until `i` is `n-2`, when the algorithm does `1` comparison.  The total number of comparisons is `n` + `n-1` + ... + `1`, which equals `(n*n - n)/2`.   (To see this, note that this sum is `n` less than the sum for `selectionSort`.)

Now we'll turn to `insertionSort`; this may do *two* comparisons for each distinct pair (`i`,`j`), but our analysis will be pretty similar to that for the previous to algorithms.  The variable `i` takes the values `1`, ..., `n-1`; for a particular value of `i`, `j` starts at `i` and decreases---it could take on all the values down to `0`, or `i+1` different values.  This means there are `2` pairs of values when `i` is `1`, `3` pairs when `i` is `2`, all the way up to `n` pairs when `i` is `n-1`.  This gives us `2` + `3` + ... + `n`, which is just `(n*n + n)/2 - 1` pairs; if every pair gives `2` comparisons, then we have `n*n + n - 2` comparisons.  However, if `j` is `0`, then the first comparison in the `while`-loop test will be `False` and the second comparison won't be done.  This means we've over-counted by one comparison for each value of `i`; subtracting `n` from our previous total, we get `n*n - 2` comparisons.

You might look at this and say that bubble sort must be the best algorithm.  However, our analysis has been pretty rough; we haven't missed any additional factors of `n`, but we haven't worried about factors of `2` or `3` (e.g., to get from the number of comparisons to the total number of operations).  (The approximate nature of our analysis means that we didn't need to worry about the factor of `2` or the over-counting by `n` in our analysis of `insertionSort`.)

What we can say at this point is that all of these algorithms do no worse than a *quadratic* number of operations as a function of the length of the list.  We can't pin down the exact number of operations, but we can say that, if we double the length of the list, then any one of these first three algorithms might take (roughly) *four times* as long to sort it as the algorithm  took to sort the shorter list.^[To recall a bit of mathematics, if the function describing the number of operations is $f(x) = ax^2 + bx + c$, then $f(2n)$ and $f(n)$ differ by roughly a factor of $4$.  This becomes more accurate as the length of the list becomes larger; if you've seen calculus, you'll recognize that $\lim_{n\rightarrow\infty} f(2n)/f(n) = 4$.]

### Analyzing merge sort

We still need to analyze merge sort.  The `mergeSort` function itself doesn't have any comparison operations, so we won't worry about it.^[This decision is the result of thinking about the function and realizing that it won't do more work than is being done by the `merge` function.  The argument for this is discussed a bit more later under the "Extra topics" later in this chapter.]  How many comparisons might `merge` do if it's given lists of length `n1` and `n2` as input?  Each element that's added to `newList` using the `append` method corresponds to three comparisons (two in the `while` test and one in the `if` test).  Depending on the values in the input lists, we could add all but one of the values from the two input lists to `newList` using `append` (we can't add *all* of the elements this way, because one of the input lists must be exhausted first).  Once we've done that, we might still do two more comparisons (if the second input list is the one that is exhausted first, then `while` would test both `i` and `j`).  Taking all of this together, if `m` is the size of the list that `merge` returns (i.e., `m` equals `n1 + n2`), then it could do as many as `3*(m-1) + 2`, or `3*m - 1`, comparisons.  Even if `n1` and `n2` are both `1`, this is at least `m`, and at most `3*m`, comparisons; we'll use `m` to simplify our computations.^[Note that we're not saying that `merge` *always* does `m` comparisons.  Instead, we're saying that the number of comparisons that `merge` *could* do, given the right---or wrong, depending on your perspective---inputs is at least `m`; our concern with this analysis is how bad things *could* be, even if fewer operations are needed in some cases.  Furthermore, if you feel uneasy about the number of comparisons, you can take solace in the fact that `merge` must produce a new list of length `m`, which requires at least `m` operations (although not necessarily comparisons).]

The preceding discussion tells us something about one use of `merge`, but how many comparisons might be done in total by `mergeSort`?  The first time `mergeSort` is called (on a list of length `n`), it uses `merge` to produce a list of length `n`, so there might be `n` comparisons here.  Imagine that this call to `merge` is given lists of lengths `n1` and `n2`; these are the outputs of the recursive calls to `mergeSort`, and we have `n = n1 + n2`.  The call to `mergeSort` that produced a list of length `n1` used `merge` to produce a list of length `n1`, while the call to `mergeSort` that produced a list of length `n2` used `merge` to produce a list of length `n1`.  Thus, the depth-recursive calls might have used a total of `n1 + n2`---i.e., another `n`---comparisons.  Taking this a bit further, the arguments to the call to `merge` that produced the list of length `n1` were outputs of recursive calls to `mergeSort`; its inputs might have been lengths `n11` and `n12` (such that `n1 = n11 + n12`).  By the same argument as before, those depth-two recursive calls to `mergeSort` might require `n11` and `n12` comparisons, or `n1` in total.  At the same time, the depth-two recursive calls to `mergeSort` to produce the lists that were merged to get the list of length `n2` may have required another `n2` comparisons.  In total, then, another `n = n1 + n2` comparisons may have been required at the second level of the recursion.^[Note that we're looking at *all* of the comparisons at this level of the recursion.  Each additional level of the recursion considers shorter lists than the previous version; shorter lists require fewer comparisons to merge, but this effect is offset by the fact that there are more lists at each level of the recursion.]  We can continue this argument; the end result is that, at each level of the recursion, `n` comparisons might be needed.^[More precisely, between `n` and `3*n` might be needed.]

We now know how many comparisons might be done at each level of the recursion.  Once we know how many levels there might be in the recursion, we'll be done.

What happens in the recursion for `mergeSort`?  We divide the input list into halves (or lists whose lengths differ by one if the input list has odd length) and give each half as input to `mergeSort`.  This process keeps going until we get to lists of length `1`.  When will this happen?  We can divide the original list into halves as many times as we can divide the length of the original list by `2` until we get down to `1` or a smaller number.  This is the same as saying that the depth of the recursion is the base-2 logarithm (rounded up) of the length of the original list, which we'll write as `log_2 n` (or $\log_2 n$).  Remember that each level of recursion could contribute `n` (or, a bit more precisely, between `n` and `3*n`) comparisons.  Thus, the total number of comparisons is (roughly) `n log_2 n` (or between `n log_2 n` and `3*n log_2 n`).

At least that's different than the number of comparisons needed for our first three algorithms; is it better?  Yes!  In fact, as `n` gets bigger and bigger, merge sort does better and better in relation to the first three algorithms.  To make this a bit more precise, think about the ratio between the number of comparisons that `mergeSort` needs to do and the number of comparisons that any one of the other three algorithms needs to do.  As `n` gets bigger and bigger, this ratio gets closer and closer to `0`.

Our rough analysis is enough to tell us that merge sort is a more efficient algorithm for long lists.  The level of analysis that we've done here isn't enough to tell us which of the quadratic algorithms would be better, but the principles for determining that are similar once you keep track of enough detail.^[If you wanted to determine which of those algorithms to use, the answer might also depend on the data that you would typically be giving to your function and the particular system it would be run on; for example, the particular system you were using might affect how many addition operations you could do in the time that it takes to do one multiplication operation.]

## Extra topics

### Other sorting algorithms and visualization

The sorting algorithm used by the built-in `sort` method for lists is called "timsort" (written by Tim Peters).  This uses insertion sort for short lists (ones with fewer than 64 elements), and it uses a kind of merge sort for longer lists.  (See <http://svn.python.org/projects/python/trunk/Objects/listsort.txt> for a description of the algorithm by its author.)

Another recursive sorting algorithm is quick sort.  Like merge sort, it recursively sorts two parts of the list.  In contrast to merge sort, it doesn't need to merge the sorted parts; instead, before doing the recursion, quick sort puts all of the elements that need to wind up in the left part of the list into the left part of the list, and it puts all of the elements that need to wind up in the right part of the list into the right part of the list.  It does this by picking an element that will go in the middle; everything less than that element is put to the left of it, everything greater than that element is put to the right of it.  Importantly, the two parts of the list on either side of the special element are *not* sorted in themselves; that's what the recursion takes care of.  This initial work removes the need to do any merging after the recursive calls are finished.

Also in contrast to merge sort, quick sort includes some randomness;^[There are lots of interesting problems and solutions in the area of randomized algorithms.] the special element in the middle is usually chosen *at random* from all of the elements in the list.  When quick sort is analyzed, this randomness must be taken into account, so the analysis talks about the *average* number of operations required to sort a list of length $n$.  That behaves like $n\log n$ (the same result we had for merge sort); however, if the random choices are always the worst possible, then the number of operations required behaves like $n^2$.

The website <http://sortvis.org/> has visualizations of many different sorting algorithms.

### More on comparison of sorting algorithms

In this subsection, we'll use $n$ instead of `n` because that's easer for typing mathematics.

Above, we relied on the fact that $1+2+\cdots+n = \frac{n^2+n}{2}$.  There are a few different ways to see this.  First, you can pair up terms in this sum---the first term ($1$) with the last term ($n$), the second term ($2$) with the penultimate term ($n-1$), etc.; if there are an odd number of terms in the sum, then the middle one (which is equal to $\frac{n+1}{2}$) is in a group by itself.  Now observe that the two terms in each pair (and, if applicable, the one term $\frac{n+1}{2}$) have an average of $\frac{n+1}{2}$.  There are $n$ terms in total; the sum equals the number of terms times the (common) average value, giving us $\frac{n^2+n}{2}$.

You can also visualize this.  Draw $n^2$ dots arranged in a square grid of $n$ rows and $n$ columns.  Make all of the dots on or below the diagonal bigger.  The number of big dots in the different columns ranges from $1$ to $n$, so $1+2+\cdots+n$ equals the total number of big dots in the figure.  How many are there?  If you had $\frac{n^2}{2}$ dots, you'd have all of the dots *below* the diagonal and half of the dots *on* the diagonal (possibly including a half dot if $n$ is odd); to get up to the total number of big dots, you need to add in the remaining half of the dots on the diagonal.  There are $n$ dots on the diagonal, so you're adding $\frac{n}{2}$ to $\frac{n^2}{2}$, giving you the value $\frac{n^2+n}{2}$ that we claimed before.

<!-- Graphic for this? -->

Finally, we mentioned earlier that we were confident that we could ignore the operations in the `mergeSort` function, just focusing on the comparisons in `merge`, for the level of accuracy that we're working with in our analyses here.  If you look back at the the `mergeSort` function, it tests a Boolean condition under the `if` statement (and maybe copies an element to a new list), it computes the length of a list and does an integer division, and it constructs two new lists whose combined length equals the length `n` of the input list `x`.  Because we knew (although we hadn't made the argument yet) that the call to `merge` would also add roughly `n` operations, the operations (in `mergeSort`) that we ignored wouldn't substantially change our analysis.^[That is, they might change a constant factor---perhaps `$4n\log_2 n$ instead of `$3n\log_2 n$ operations---but they wouldn't change something that's roughly $n\log_2 n$ to be, e.g., $n^2$.]

<!-- FIXME

## Debugging

## Glossary

Insertion sort

Selection sort

Bubble sort

Merge sort

-->

## Exercises

> 1. Assume that you have a function `SortInPlace()` that sorts a list in
>    place.  (I.e., it's like the sort method, except it's a function.) 
>    Write a function `NewSortedList()` that takes a single list as an
>    argument and returns a *new* list that's sorted but *does not* change
>    the input list; your function should use the `SortInPlace()` function,
>    but it shouldn't use the `sort()` method or the `sorted()` function.
> 
> 1. Answer the question from the end of the discussion of selection sort.
>    (I.e., how could you make the code slightly more efficient using your
>    observation about the value at index `len(x) - 1`?)
> 
> 1. Rewrite selection sort so that it uses a helper function to find the
>    index of the smallest element to the right of a certain point.  (This is
>    currently the job of the inner `for` loop; your helper function may use
>    a `for` loop, but it should be a separate function.  What should be its
>    argument(s)?  What should it return?)
> 
> 1. Rewrite bubble sort so that the smallest element is bubbled to the
>    beginning of the list, then the second smallest element is bubbled to
>    index `1`, etc.
> 
> 1. Does the number of comparisons done by selection sort depend on order
>    of the elements in the list being sorted?  If so, can you find two lists
>    of the same length that require different numbers of comparisons to sort
>    them?
> 
> 1. Does the number of comparisons done by bubble sort depend on order of
>    the elements in the list being sorted?  If so, can you find two lists of
>    the same length that require different numbers of comparisons to sort
>    them?
> 
> 1. Does the number of comparisons done by insertion sort depend on order
>    of the elements in the list being sorted?  If so, can you find two lists
>    of the same length that require different numbers of comparisons to sort
>    them?
> 
> 1. Write a version of merge sort that sorts a list *in place*.
> 
> 1. If the number of comparisons done by selection, bubble, or insertion
>    sort depends on the input list, analyze the number of comparisons needed
>    for that algorithm as a function of the list length.  (I.e., redo the
>    analysis in the text, but assume that the input list is one that
>    minimizes the number of comparisons.)  Hint: The analyses of these
>    algorithms might give you some ideas about what would minimize the
>    number of comparisons.

