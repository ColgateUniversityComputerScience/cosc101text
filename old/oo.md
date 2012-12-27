
# Classes and objects

We have used many of Python’s built-in types, like integers, strings,
lists, and dictionaries.  Each instance of a type in Python (e.g., a
specific string, integer, or list) is called an **object**.  Although
the term "object" sounds generic, it has a very specific meaning in
software design.  In fact, what we'll be learning about in this chapter
is a style of programming and program design called **object-oriented
programming**, or OOP.  Before we get into designing an object-oriented
program, we will first learn about how new types --- and new types of 
objects --- can be defined and created.

## User-defined types

As an initial example, we'll create a new type called `Point` that
represents a point in two-dimensional space. In mathematical notation,
points are often written in parentheses with a comma separating the
coordinates. For example, $(0, 0)$ represents the origin, and $(x, y)$
represents the point $x$ units to the right and $y$ units up from the
origin.

There are several ways we might represent points in Python:

 - We could store the coordinates separately in two variables, `x` and
   `y`.

 - We could store the coordinates as elements in a list or tuple.
 
 - We could create a dictionary that has two keys, `x` and `y`, with
   corresponding values.

 - We could create a *new type* to represent points as objects.  
   (Woo-hoo! Pick me!  Pick me!)

Creating a new type is (a little bit) more complicated than the other
options, but it has advantages that will be apparent soon.

Every type in Python is defined by the type's **class**.  You can think
of a class as a blueprint or model from which objects can be created.  A
minimal class definition looks like this:

    class Point(object):
        """represents a point in 2-D space"""

This header indicates that the new class is a `Point`, which is a kind
of `object`, which is a built-in type.

The body is a docstring that explains the purpose of the class. 
Normally, you will also define functions and variables inside a class
definition; we will get to that shortly.

Defining a class named `Point` creates a class object.

    >>> print Point
    <class '__main__.Point'>

Because `Point` is defined at the top level, its "full name" is
`__main__.Point`.

Besides being like a blueprint, the class object is also like a factory
for creating objects.  To create a Point, you call `Point` as if it were
a function.

    >>> blank = Point()
    >>> print blank
    <__main__.Point instance at 0xb7e9d3ac>

The return value is a reference to a Point object, which we assign to
`blank`.  Creating a new object is called **instantiation**, and the
object is an **instance** of the class.

When you print an instance, Python tells you what class it belongs to
and where it is stored in memory (the string starting `0x` is a memory
location in hexadecimal format---base 16).

Even though it might feel a little strange using the class name as a
function, you can construct any built-in Python type using the same
syntax:

    >>> mylist = list()
    >>> print list
    []
    
Using the class/type name as a function works for *any* type in Python:
`int`, `str`, `list`, `dict`, `tuple`, etc.  And although printing the
`list` object looks a little prettier than our `Point` object, we'll
make the `Point` look better soon.

## Attributes and Methods

We've just made a `Point` class from which we can construct `Point`
instances, or `Point` objects.  Objects, in the peculiar programming
language sense, can have **attributes** and **methods** associated with
them.

 * You can think of the **attributes** as data, or information, stored
   inside an object.  In object-oriented programming languages, attributes
   are also referred to as **instance variables**.

 * We've already used **methods** on objects.  These are functions that
   are, in a sense, *attached* to an object.  In Python, a method is
   invoked by using the dot notation syntax:
   
        >>> # object.method(parameters)
        >>> s = "aabbcc"
        >>> s.count('b')
        2
 
In the above example with the string object `s`, we invoke the `count`
method on the object, passing the string `b` as a parameter.  You can
think of the attributes for the string object as being the sequence of
characters that make up the string.

### Adding attributes

You can assign new attributes to an instance using dot notation and the
assignment operator:

    >>> blank = Point()
    >>> blank.x = 3.0
    >>> blank.y = 4.0

The following diagram shows the result of these assignments. A state
diagram that shows an object and its attributes is called an **object
diagram**:

![Class diagram of a `point` object.](figs/point.png) 

The variable `blank` refers to a Point object, which contains two
attributes.  Each attribute refers to a floating-point number.

You can read the value of an attribute using the same syntax:

    >>> print blank.y
    4.0
    >>> x = blank.x
    >>> print x
    3.0

The expression `blank.x` means, "Go to the object `blank` refers to and
get the value of `x`."  In this case, we assign that value to a variable
named `x`. There is no conflict between the variable `x` and the
attribute `x`.

Interestingly (and usefully), *objects are mutable* --- we can change the
values of attributes:

    >>> blank.x = 5.5
    >>> blank.y = blank.x * 2

### Adding methods

Methods are semantically the same as functions, but there are two
syntactic differences:

 - Methods are defined inside a class definition in order to make the
   relationship between the class and the method explicit.  As with
   functions, we use the `def` keyword to define methods, but the method
   `def` header needs to be indented inside the class definition.

 - The syntax for invoking a method is different from the syntax for
   calling a function.
  
Let's get started writing a method to set the `x` and `y` attributes in
the object to new values:
   
    class Point(object):
        '''represents a point in 2-D space'''
        
        def setXY(point, x, y):
            '''Set values for x and y attributes.
               Parameters:
                  point is the object we're invoking this method on.
                  x is the new value for the x attribute.
                  y is the new value for the y attribute.
               There's no return value.'''
            point.x = x
            point.y = y

We might use our `Point` class to create an object and set its `x` and
`y` attributes using the `setXY` method as follows:

    >>> p = Point()
    >>> p.setXY(8.0, 7.5)
    >>> print p.x
    8.0
    >>> print p.y
    7.5

On line 2 of the above code, `setXY` is the name of the method, and `p`
is the object on which the method is invoked, which is also called the
**subject**.  Just as the subject of a sentence is what the sentence is
about, the subject of a method invocation is what the method is about.

Inside the `setXY` method, the subject is assigned to the first
parameter, so in this case `p` is assigned to `point`.

By convention in Python, the first parameter of a method is called
`self`, so the Pythonically correct way to write `setXY` would be:

    class Point(object):
        '''represents a point in 2-D space'''
        
        def setXY(self, x, y):
            '''Set values for x and y attributes.'''
            self.x = x
            self.y = y

### The init method

Instead of making a `setXY` method to initialize the attributes of our
`Point` class, a more conventional way to set initial attribute values
is to create a special method called the **constructor**, **c'tor**, or
**initializer**.  The method name for the constructor is *always*
`__init__` in Python, and it is automatically invoked when an object is
instantiated.  Constructors are used for initializing attributes in an
object, and to perform any other initialization that might be required
when a new instance is created.

Let's modify our `Point` class to include an `__init__` method that
accepts two parameters for initializing our `x` and `y` coordinates. 
We'll still retain the `setXY` method, too.

    class Point(object):
        '''represents a point in 2-D space'''
        
        def __init__(self, x, y):
            '''Point constructor: takes initial x,y values'''
            self.x = x
            self.y = y
            
        def setXY(self, x, y):
            self.x = x
            self.y = y
            
To create a new `Point` object, we have to change our call to `Point` to pass
in initial values for `x` and `y`:

    >>> p = Point(3.2, 8.9)
    >>> print p.x
    3.2
    >>> print p.y
    8.9
    
Since `__init__` and `setXY` are nearly identical, we could even refine
our code a bit to reduce redundancy:

    class Point(object):
        '''represents a point in 2-D space'''
        
        def __init__(self, x, y):
            '''Point constructor: sets initial x,y values'''
            self.setXY(x, y)
            
        def setXY(self, x, y):
            self.x = x
            self.y = y

The optimization isn't particularly large in this example, but it is 
still a good idea to avoid repeating the same code.  Also, if we add
any new attributes, we only have to specify their initialization
in *one* place.

### Additional `Point` methods

Let's add to our `Point` class by writing two more methods:
 
 * A `getXY` method that doesn't take any parameters and returns
   a tuple consisting of the `x` and `y` coordinates, and
   
 * a `distance` method that takes another `Point` object as a parameter
   and computes and returns the Euclidean distance between the *subject*
   `Point` (the `Point` object on which the `distance` method is called)
   and the `Point` object passed as the parameter.
   
First, the `getXY` method:

    class Point(object):
    
        # ... other methods defined in Point
        
        def getXY(self):
            ''' return the x,y coordinates
                as a tuple.'''
            return (self.x, self.y)

Although we said about that the `getXY` method doesn't take any
parameters, *all* methods must *always* take at least one parameter: the
subject, or `self` object.  Inside the method, we simply return a tuple
consisting of the `x` and `y` components.

In a program, we might use the `getXY` method as follows:

    >>> p = Point(5,2)
    >>> coord_tuple = p.getXY()
    >>> print coord_tuple
    (5,2)    

Now, for the `distance` method:

    import math
    
    class Point(object):
    
        # ... other methods defined in Point
        
        def distance(self, other):
            ''' compute and return the Euclidean
                distance between this point and another.'''
            d = (self.x - other.x)**2 + (self.y - other.y)**2
            return math.sqrt(d)

In a program, we might use the `distance` method as follows:

    >>> p1 = Point(5,1)
    >>> p2 = Point(3,7)
    >>> d = p1.distance(p2)
    >>> print d
    6.324555320336759


### Printing objects

`__str__` is a special method, like `__init__`, that is supposed to
return a string representation of an object.   For the `Point` class, we
might write the `__str__` method as follows:

    class Point(object):
    
        # ... other methods defined in Point

        def __str__(self):
            return "Point ({:.1f},{:.1f})".format(self.x, self.y)
            

When you `print` an object, Python automatically and implicitly invokes
the `__str__` method:

    >>> print p1
    'Point (5.0,1.0)'
    >>> print p2
    Point (3.0,7.0)

When you write a new class, a good idea is to start by writing
`__init__`, which makes it easier to instantiate objects, and `__str__`,
which is useful for debugging.

Note that any method names that are prefixed and suffixed with `__` are
called **magic methods** in Python.  They're "magic" because they're
invoked automatically and implicitly by Python: a programmer generally
never explicitly invokes these methods.

### The full `Point` class

Putting all our work together, here is the full definition of the
`Point` class that we created:

    import math
    
    class Point(object):
        '''represents a point in 2-D space'''
        
        def __init__(self, x, y):
            '''Point constructor: takes initial x,y values'''
            self.x = x
            self.y = y
            
        def setXY(self, x, y):
            '''Set x and y coordinates to new values.'''
            self.x = x
            self.y = y
    
        def getXY(self):
            ''' return the x,y coordinates as a tuple.'''
            return (self.x, self.y)
    
        def distance(self, other):
            ''' compute and return the Euclidean
                distance between this point and another.'''
            d = (self.x - other.x)**2 + (self.y - other.y)**2
            return math.sqrt(d)
                
        def __str__(self):
            return "Point ({:.1f},{:.1f})".format(self.x, self.y)

## Object-oriented program design

Python is an **object-oriented programming language**, which means that
it provides features that support object-oriented programming.

It is not easy to define object-oriented programming, but we have
already seen some of its characteristics:

 - Programs are made up of object definitions and function definitions,
   and most of the computation is expressed in terms of operations on
   objects.

 - Each object definition corresponds to some object or concept in the
   real world, and the functions that operate on that object correspond
   to the ways real-world objects interact.

For example, the `Point` class defined above corresponds to the
mathematical concept of a point.

For solving problems in an object-oriented programming style, the main
idea is to model the entities or concepts in the problem domain,
including *attributes* that are stored by the entity, and *actions*, or
*methods* that can be performed by the entities.   Our goal in this
course is for you to get your feet wet with OOP ideas; later courses
go into more depth on OOP design.

## A `Rectangle` class

Let's try to test our knowledge so far by designing a class that models
a rectangle.

Sometimes it is obvious what the attributes of an object should be, but
other times you have to make decisions.  For the rectangle class we're
designing, what attributes would you use to specify the location and
size of a rectangle?  You can ignore angle; to keep things simple, assume
that the rectangle is either vertical or horizontal.

There are at least two possibilities:

 -  You could specify one corner of the rectangle (or the center), the
    width, and the height.

 -  You could specify two opposing corners.

At this point it is hard to say whether either is better than the other,
so we’ll implement the first one, just as an example.

Here is the class definition, starting with `__init__` and `__str__`:

    class Rectangle(object):
        """represent a rectangle. 
           attributes: width, height, corner.
        """
        
        def __init__(self, width, height, corner):
            self.width = width
            self.height = height
            self.corner = corner
            
        def __str__(self):
            return "Rectangle lower-left: ({:.1f},{:.1f}) "
                   "upper-right: ({:.1f},{:.1f})".format(self.corner.x, 
                   self.corner.y, self.corner.x + self.width, 
                   self.corner.y+self.height)

Once we create the `Rectangle` class, we might use the two methods we've
written to construct and print a rectangle object:

    >>> r = Rectangle(100.0, 200.0, Point(0, 0))
    >>> print r
    Rectangle lower-left: (0.0, 0.0) upper-right: (100.0, 200.0)

The figure shows the state of this object:

![Diagram of a `rectangle` object that refers to a `point` object.](figs/rectangle.png) 

An object that is an attribute of another object is **embedded**: the
`Point` object that represents the lower-left corner of the rectangle is
*embedded* in the `Rectangle` object.  This sort of relationship is also
referred to as a **HAS-A** relationship in object-oriented programming.
In this case, a `Rectangle` HAS-A `Point`.

> **Examples**:
> 
> 1. Write a method named `move_rectangle` that takes two
>    numbers named `dx` and `dy`.  It should change the location of the
>    rectangle by adding `dx` to the `x` coordinate of `corner` and adding
>    `dy` to the `y` coordinate of `corner`.
>
> 1. Write a method named `perimeter` that computes and returns the
>    perimeter length of the rectangle.
>
> 1. Write a method named `area` that computes and returns the area of
>    the rectangle.
>

## A `Circle` class

Since we've started on shapes, how about making a class to model a
circle.  Our choices for attributes are little simpler than with the
rectangle.  It probably makes sense to have a `Point` attribute that
represents the center of the circle, and a number that holds either the
radius or diameter of the circle.  Before you look carefully at the code
below, see if you can write out the class definition for `Circle`,
including the constructor and `__str__` magic method.

    class Circle(object):
        def __init__(self, center, radius):
            self.center = center
            self.radius = radius
            
        def __str__(self):
            return "Circle ({:.1f},{:.1f}) with radius {:.1f}".format(
                self.center.x, self.center.y, self.radius)

> **Examples**:
>
> 1. Write a method named `move_circle` that takes two
>    numbers named `dx` and `dy`.  It should change the center position of the
>    center by adding `dx` to the `x` coordinate of `center` and adding
>    `dy` to the `y` coordinate of `center`.
>
> 1. Write a method named `perimeter` that computes and returns the
>    circumference of the circle.
>
> 1. Write a method named `area` that computes and returns the area of
>    the circle.
>

## Inheritance

If you've faithfully done the examples above (do them now if you haven't
already!), you may have noticed some similarities in how they are
implemented.  For one, the `move_...` methods are remarkably similar.
Also, even though the `perimeter` and `area` methods for the `Rectangle`
and `Circle` are *implemented* differently, they have the same name, and
(at least in an abstract way) are doing the same things.  This should
not be surprising, since circles and rectangles are both shapes.  

Besides HAS-A relationships in object-oriented programming, there are
also **IS-A** relationships that are often directly supported through
programming language features.  In our `Shape` example, a circle IS-A
shape, and a rectangle IS-A shape.  In object-oriented programming
languages, IS-A relationships are directly supported through a featured
called **inheritance**. Inheritance is the ability to define a new class
that is a modified version of an existing class. It is called
"inheritance" because the new class inherits the methods of the existing
class. Extending this metaphor, the existing class is called the
**parent** and the new class is called the **child**.

In the examples below, we'll design a parent `Shape` class, and refactor
(revise) our `Rectangle` and `Circle` classes so that they inherit from
`Shape`.

### A `Shape` class

Let's first make our amorphous shape class.  Just to make things
somewhat interesting, let's give shapes a name and color.  We'll also
define `area` and `perimeter` methods; they can just return 0.

    def Shape(object):
        '''A generic shape class.'''
        def __init__(self, name, color):
            self.name = name
            self.color = color
            
        def __str__(self):
            return "I am a {} {}.".format(self.color, self.name)
    
        def area(self):
            return 0.0
            
        def perimeter(self):
            return 0.0
                
### Refactoring `Rectangle`

Now, let's modify the `Rectangle` class so that it inherit from `Shape`.
We'll start with  the `__init__` method:

    class Rectangle(Shape):
        def __init__(self, corner, width, height, color):
            Shape.__init__(self, "rectangle", color)
            self.corner = corner
            self.width = width
            self.height = height
            
We can first see that instead of `object` in the class definition, we
use `Shape`.  The class name in parenthesis defines the IS-A
relationship between our new class and some other class.  In this case,
a `Rectangle` IS-A `Shape`.

The `__init__` method is a little hairier now.  First, we've added a
`color` parameter so that we can set the color of the shape.  The first
line within the constructor looks messy, but all we're doing is invoking
the constructor of the `Rectangle`'s *parent* class, which is `Shape`.
We have to explicitly say `Shape.__init__` to identify the method to
call, and we also have to explicitly pass in `self` as the first
parameter.  This is one of the (very) few situations in which you ever
have to invoke a magic method directly.  

When we invoke the `Shape` constructor, our object gets outfitted with a
`name` and `color`.  When we return, we add the `corner`, `width`, and
`height` attributes.

Now the fun begins.  Let's create a `Rectangle` and manipulate it:

    >>> r = Rectangle(Point(3,5), 5, 10, "blue")
    >>> print r
    I am blue rectangle.

How did we get such output when we didn't define a `__str__` method in
`Rectangle`?  Because our `Rectangle` class inherited all the methods of
its parent class, `Shape`!

What if we try to get the `perimeter` and `area` for the `Rectangle`?

    >>> print r.perimeter()
    0.0
    >>> print r.area()
    0.0

Since we inherited the methods from `Shape`, we got zeroes.  To make our
`Rectangle` more useful, what we can do is **override** and redefine how
`area` and `perimeter` should work for a rectangle:

    # inside the Rectangle class definition
    
        def perimeter(self):
            return self.width * 2 + self.height * 2
            
        def area(self):
            return self.width * self.height

Now, when we ask a rectangle to give us its perimeter and area, it
responds appropriately:

    >>> r = Rectangle(Point(3,5), 5, 10, "blue")
    >>> print r.perimeter()
    30
    >>> print r.area()
    50

> **Examples**:
>
> 1. Refactor the `Circle` class so that it inherits from `Shape`.
>

## Copying objects

Aliasing can make a program difficult to read because changes in one
place might have unexpected effects in another place. It is hard to keep
track of all the variables that might refer to a given object.

Copying an object is often an alternative to aliasing. The `copy` module
contains a function called `copy` that can duplicate any object:

    >>> p1 = Point(3.0, 4.0)
    >>> import copy
    >>> p2 = copy.copy(p1)

`p1` and `p2` contain the same data, but they are not the same Point.

    >>> print p1
    Point (3.0, 4.0)
    >>> print p2
    Point (3.0, 4.0)
    >>> p1 is p2
    False
    >>> p1 == p2
    False

The `is` operator indicates that `p1` and `p2` are not the same object,
which is what we expected. But you might have expected `==` to yield
`True` because these points contain the same data. In that case, you
will be disappointed to learn that for instances, the default behavior
of the `==` operator is the same as the `is` operator; it checks object
identity, not object equivalence. This behavior can be changed—we’ll see
how later.

If you use `copy.copy` to duplicate a Rectangle, you will find that it
copies the Rectangle object but not the embedded Point.

    >>> import copy
    >>> box = Rectangle(Point(3, 2), 5, 10)
    >>> box2 = copy.copy(box)
    >>> box2 is box
    False
    >>> box2.corner is box.corner
    True

Here is what the object diagram looks like:

![Two `rectangle` objects that refer to the same `point` object in memory.](figs/rectangle2.png) 

This operation is called a **shallow copy** because it copies the object
and any references it contains, but not the embedded objects.

For most applications, this is not what you want. In this example,
invoking `grow_rectangle` on one of the Rectangles would not affect the
other, but invoking `move_rectangle` on either would affect both! This
behavior is confusing and error-prone.

Fortunately, the `copy` module contains a method named `deepcopy` that
copies not only the object but also the objects it refers to, and the
objects *they* refer to, and so on. You will not be surprised to learn
that this operation is called a **deep copy**.

    >>> box3 = copy.deepcopy(box)
    >>> box3 is box
    False
    >>> box3.corner is box.corner
    False

`box3` and `box` are completely separate objects.

> **Example**:
>
> 1. Write a version of `move_rectangle` that creates and returns a new
>    Rectangle instead of modifying the old one.

## An in-depth example: card games

In this section we will develop classes to represent playing cards,
decks of cards, and poker hands. If you don’t play poker, you can read
about it at <http://wikipedia.org/wiki/Poker>, but you don’t have to; I’ll tell
you what you need to know for the exercises.

If you are not familiar with Anglo-American playing cards, you can read
about them at <http://wikipedia.org/wiki/Playing_cards>.

There are fifty-two cards in a deck, each of which belongs to one of
four suits and one of thirteen ranks. The suits are Spades, Hearts,
Diamonds, and Clubs (in descending order in bridge). The ranks are Ace,
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Depending on the game
that you are playing, an Ace may be higher than King or lower than 2.

If we want to define a new object to represent a playing card, it is
obvious what the attributes should be: `rank` and `suit`. It is not as
obvious what type the attributes should be. One possibility is to use
strings containing words like `'Spade'` for suits and `'Queen'` for
ranks. One problem with this implementation is that it would not be easy
to compare cards to see which had a higher rank or suit.

An alternative is to use integers to **encode** the ranks and suits. In
this context, “encode” means that we are going to define a mapping
between numbers and suits, or between numbers and ranks. This kind of
encoding is not meant to be a secret (that would be “encryption”).

For example, this table shows the suits and the corresponding integer
codes:

> Spades $\mapsto$ 3 \
> Hearts $\mapsto$ 2 \
> Diamonds $\mapsto$ 1 \
> Clubs $\mapsto$ 0

This code makes it easy to compare cards; because higher suits map to
higher numbers, we can compare suits by comparing their codes.

The mapping for ranks is fairly obvious; each of the numerical ranks
maps to the corresponding integer, and for face cards:

> Jack $\mapsto$ 11 \
> Queen $\mapsto$ 12 \
> King $\mapsto$ 13 \

I am using the $\mapsto$ symbol to make it clear that these mappings are
not part of the Python program. They are part of the program design, but
they don’t appear explicitly in the code.

### `Card` class 

The class definition for `Card` looks like this:

    class Card(object):
        """represents a standard playing card."""

        def __init__(self, suit=0, rank=2):
            self.suit = suit
            self.rank = rank

As usual, the init method takes an optional parameter for each
attribute. The default card is the 2 of Clubs.

To create a Card, you call `Card` with the suit and rank of the card you
want.

    queen_of_diamonds = Card(1, 12)

### Class attributes

In order to print Card objects in a way that people can easily read, we
need a mapping from the integer codes to the corresponding ranks and
suits. A natural way to do that is with lists of strings. We assign
these lists to **class attributes**:

    # inside class Card:

        suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King']

        def __str__(self):
            return '%s of %s' % (Card.rank_names[self.rank],
                                 Card.suit_names[self.suit])

Variables like `suit_names` and `rank_names`, which are defined inside a
class but outside of any method, are called class attributes because
they are associated with the class object `Card`.

This term distinguishes them from variables like `suit` and `  rank`,
which are called **instance variables** because they are associated
with a particular instance.

Both kinds of attribute are accessed using dot notation. For example, in
`__str__`, `self` is a Card object, and `self.rank` is its rank.
Similarly, `Card` is a class object, and `Card.rank_names` is a list of
strings associated with the class.

Every card has its own `suit` and `rank`, but there is only one copy of
`suit_names` and `rank_names`.

Putting it all together, the expression `Card.rank_names[self.rank]`
means “use the attribute `rank` from the object `self` as an index into
the list `rank_names` from the class `Card`, and select the appropriate
string.”

The first element of `rank_names` is `None` because there is no card
with rank zero. By including `None` as a place-keeper, we get a mapping
with the nice property that the index 2 maps to the string `'2'`, and so
on. To avoid this tweak, we could have used a dictionary instead of a
list.

With the methods we have so far, we can create and print cards:

    >>> card1 = Card(2, 11)
    >>> print card1
    Jack of Hearts

![Diagram that shows the `Card` class object and one Card instance.](figs/card1.png) 

`Card` is a class object, so it has type `type`. `card1` has type
`Card`. (To save space, I didn’t draw the contents of `suit_names` and
`rank_names`).

### Comparing cards

For built-in types, there are relational operators (`<`, `>`, `==`,
etc.) that compare values and determine when one is greater than, less
than, or equal to another. For user-defined types, we can override the
behavior of the built-in operators by providing a method named
`__cmp__`.

`__cmp__` takes two parameters, `self` and `other`, and returns a
positive number if the first object is greater, a negative number if the
second object is greater, and 0 if they are equal to each other.

The correct ordering for cards is not obvious. For example, which is
better, the 3 of Clubs or the 2 of Diamonds? One has a higher rank, but
the other has a higher suit. In order to compare cards, you have to
decide whether rank or suit is more important.

The answer might depend on what game you are playing, but to keep things
simple, we’ll make the arbitrary choice that suit is more important, so
all of the Spades outrank all of the Diamonds, and so on.

With that decided, we can write `__cmp__`:

    # inside class Card:

        def __cmp__(self, other):
            # check the suits
            if self.suit > other.suit: return 1
            if self.suit < other.suit: return -1

            # suits are the same... check ranks
            if self.rank > other.rank: return 1
            if self.rank < other.rank: return -1

            # ranks are the same... it's a tie
            return 0    

You can write this more concisely using tuple comparison:

    # inside class Card:

        def __cmp__(self, other):
            t1 = self.suit, self.rank
            t2 = other.suit, other.rank
            return cmp(t1, t2)

The built-in function `cmp` has the same interface as the method
`__cmp__`: it takes two values and returns a positive number if the
first is larger, a negative number if the second is larger, and 0 if
they are equal.

### Decks

Now that we have Cards, the next step is to define Decks. Since a deck
is made up of cards, it is natural for each Deck to contain a list of
cards as an attribute.

The following is a class definition for `Deck`. The init method creates
the attribute `cards` and generates the standard set of fifty-two cards:

    class Deck(object):

        def __init__(self):
            self.cards = []
            for suit in range(4):
                for rank in range(1, 14):
                    card = Card(suit, rank)
                    self.cards.append(card)

The easiest way to populate the deck is with a nested loop. The outer
loop enumerates the suits from 0 to 3. The inner loop enumerates the
ranks from 1 to 13. Each iteration creates a new Card with the current
suit and rank, and appends it to `self.cards`.

### Printing the deck

Here is a `__str__` method for `Deck`:

    #inside class Deck:

        def __str__(self):
            res = []
            for card in self.cards:
                res.append(str(card))
            return '\n'.join(res)

This method demonstrates an efficient way to accumulate a large string:
building a list of strings and then using `join`. The built-in function
`str` invokes the `__str__` method on each card and returns the string
representation.

Since we invoke `join` on a newline character, the cards are separated
by newlines. Here’s what the result looks like:

    >>> deck = Deck()
    >>> print deck
    Ace of Clubs
    2 of Clubs
    3 of Clubs
    ...
    10 of Spades
    Jack of Spades
    Queen of Spades
    King of Spades

Even though the result appears on 52 lines, it is one long string that
contains newlines.

### Add, remove, shuffle and sort

To deal cards, we would like a method that removes a card from the deck
and returns it. The list method `pop` provides a convenient way to do
that:

    #inside class Deck:

        def pop_card(self):
            return self.cards.pop()

Since `pop` removes the *last* card in the list, we are dealing from the
bottom of the deck. In real life bottom dealing is frowned upon^[See
<http://wikipedia.org/wiki/Bottom_dealing>], but in this context it’s
ok.

To add a card, we can use the list method `append`:

    #inside class Deck:

        def add_card(self, card):
            self.cards.append(card)

A method like this that uses another function without doing much real
work is sometimes called a **veneer**. The metaphor comes from
woodworking, where it is common to glue a thin layer of good quality
wood to the surface of a cheaper piece of wood.

In this case we are defining a “thin” method that expresses a list
operation in terms that are appropriate for decks.

As another example, we can write a Deck method named `shuffle` using the
function `shuffle` from the `random` module:

    # inside class Deck:
                
        def shuffle(self):
            random.shuffle(self.cards)

Don’t forget to import `random`.

> **Example**:
>
> 1. Write a Deck method named `sort` that uses the list method `sort` to
> sort the cards in a `Deck`. `sort` uses the `__cmp__` method we
> defined to determine sort order.

## `Hand` class

Let's that we now want a class to represent a "hand," that is, the set
of cards held by one player.  A hand is similar to a deck: both are made
up of a set of cards, and both require operations like adding and
removing cards.

A hand is also different from a deck; there are operations we want for
hands that don’t make sense for a deck. For example, in poker we might
compare two hands to see which one wins. In bridge, we might compute a
score for a hand in order to make a bid.

This relationship between classes—similar, but different—lends itself to
inheritance.

The definition of a child class is like other class definitions, but the
name of the parent class appears in parentheses:

    class Hand(Deck):
        """represents a hand of playing cards"""

This definition indicates that `Hand` inherits from `Deck`; that means
we can use methods like `pop_card` and `add_card` for Hands as well as
Decks.

`Hand` also inherits `__init__` from `Deck`, but it doesn’t really do
what we want: instead of populating the hand with 52 new cards, the init
method for Hands should initialize `cards` with an empty list.

If we provide an init method in the `Hand` class, it overrides the one
in the `Deck` class:

    # inside class Hand:

        def __init__(self, label=''):
            self.cards = []
            self.label = label

So when you create a Hand, Python invokes this init method:

    >>> hand = Hand('new hand')
    >>> print hand.cards
    []
    >>> print hand.label
    new hand

But the other methods are inherited from `Deck`, so we can use
`pop_card` and `add_card` to deal a card:

    >>> deck = Deck()
    >>> card = deck.pop_card()
    >>> hand.add_card(card)
    >>> print hand
    King of Spades

A natural next step is to encapsulate this code in a method called
`move_cards`:

    #inside class Deck:

        def move_cards(self, hand, num):
            for i in range(num):
                hand.add_card(self.pop_card())

`move_cards` takes two arguments, a Hand object and the number of cards
to deal. It modifies both `self` and `hand`, and returns `None`.

In some games, cards are moved from one hand to another, or from a hand
back to the deck. You can use `move_cards` for any of these operations:
`self` can be either a Deck or a Hand, and `hand`, despite the name, can
also be a `Deck`.

> **Example**:
>
> 1. Write a Deck method called `deal_hands` that takes two parameters, the
> number of hands and the number of cards per hand, and that creates new
> Hand objects, deals the appropriate number of cards per hand, and
> returns a list of Hand objects.

Inheritance is a useful feature. Some programs that would be repetitive
without inheritance can be written more elegantly with it. Inheritance
can facilitate code reuse, since you can customize the behavior of
parent classes without having to modify them. In some cases, the
inheritance structure reflects the natural structure of the problem,
which makes the program easier to understand.

On the other hand, inheritance can make programs difficult to read. When
a method is invoked, it is sometimes not clear where to find its
definition. The relevant code may be scattered among several modules.
Also, many of the things that can be done using inheritance can be done
as well or better without it.

## Class diagrams

So far we have seen stack diagrams, which show the state of a program,
and object diagrams, which show the attributes of an object and their
values. These diagrams represent a snapshot in the execution of a
program, so they change as the program runs.

They are also highly detailed; for some purposes, too detailed. A class
diagram is a more abstract representation of the structure of a program.
Instead of showing individual objects, it shows classes and the
relationships between them.

There are several kinds of relationship between classes:

 - Objects in one class might contain references to objects in another
   class.  For example, each Rectangle contains a reference to a Point.
   This kind of relationship is called **HAS-A**, as in, "a Rectangle has a
   Point."

 - One class might inherit from another. This relationship is called
   **IS-A**, as in, "A Rectangle is a kind of Shape."

 - One class might depend on another in the sense that changes in one
   class would require changes in the other.

A **class diagram** is a graphical representation of these
relationships^[The diagrams I am using here are similar to UML (see
<http://wikipedia.org/wiki/Unified_Modeling_Language>), with a few
simplifications.].  For example, this diagram shows the relationships
between `Card`, `Deck` and `Hand`. 

![Inheritance diagram for `Point`, `Shape`, and `Rectangle`.](figs/class1.png) 

The arrow with a hollow triangle head represents an IS-A relationship;
in this case it indicates that Rectangle inherits from Shape.

The standard arrow head represents a HAS-A relationship; in this case a
Deck has references to Card objects.

A more detailed diagram might show that a Deck actually contains a
*list* of Cards, but built-in types like list and dict are usually not
included in class diagrams.

## Debugging

When you start working with objects, you are likely to encounter some
new exceptions. If you try to access an attribute that doesn’t exist,
you get an `AttributeError`:

    >>> p = Point()
    >>> print p.z
    AttributeError: Point instance has no attribute 'z'

If you are not sure what type an object is, you can ask:

    >>> type(p)
    <type '__main__.Point'>

\label{sec:hasattr}
<a name="sec:hasattr"></a>

If you are not sure whether an object has a particular attribute, you
can use the built-in function `hasattr`:

    >>> hasattr(p, 'x')
    True
    >>> hasattr(p, 'z')
    False

The first argument can be any object; the second argument is a *string*
that contains the name of the attribute.

It is legal to add attributes to objects at any point in the execution
of a program, but if you are a stickler for type theory, it is a dubious
practice to have objects of the same type with different attribute sets.
It is usually a good idea to initialize all of an objects attributes in
the `__init__` method.

If you are not sure whether an object has a particular attribute, you
can use the built-in function `hasattr` (see [above](#sec:hasattr) ).

Another way to access the attributes of an object is through the special
attribute `__dict__`, which is a dictionary that maps attribute names
(as strings) and values:

    >>> p = Point(3, 4)
    >>> print p.__dict__
    {'y': 4, 'x': 3}

For purposes of debugging, you might find it useful to keep this
function handy:

    def print_attributes(obj):
        for attr in obj.__dict__:
            print attr, getattr(obj, attr)

`print_attributes` traverses the items in the object’s dictionary and
prints each attribute name and its corresponding value.

The built-in function `getattr` takes an object and an attribute name
(as a string) and returns the attribute’s value.

Inheritance can make debugging a challenge because when you invoke a
method on an object, you might not know which method will be invoked.

Suppose you are writing a function that works with Hand objects. You
would like it to work with all kinds of Hands, like PokerHands,
BridgeHands, etc. If you invoke a method like `shuffle`, you might get
the one defined in `Deck`, but if any of the subclasses override this
method, you’ll get that version instead.

Any time you are unsure about the flow of execution through your
program, the simplest solution is to add print statements at the
beginning of the relevant methods. If `Deck.shuffle` prints a message
that says something like `Running Deck.shuffle`, then as the program
runs it traces the flow of execution.

As an alternative, you could use this function, which takes an object
and a method name (as a string) and returns the class that provides the
definition of the method:

    def find_defining_class(obj, meth_name):
        for ty in type(obj).mro():
            if meth_name in ty.__dict__:
                return ty

Here’s an example:

    >>> hand = Hand()
    >>> print find_defining_class(hand, 'shuffle')
    <class 'Card.Deck'>

So the `shuffle` method for this Hand is the one in `Deck`.

`find_defining_class` uses the `mro` method to get the list of class
objects (types) that will be searched for methods. “MRO” stands for
“method resolution order.”

Here’s a program design suggestion:  whenever you override a method, the
interface of the new method should be the same as the old. It should
take the same parameters, return the same type, and obey the same
preconditions and postconditions. If you obey this rule, you will find
that any function designed to work with an instance of a superclass,
like a Deck, will also work with instances of subclasses like a Hand or
PokerHand.

If you violate this rule, your code will collapse like (sorry) a house
of cards.

## Glossary

class:
  ~ A user-defined type. A class definition creates a new class object.

class object:
  ~ An object that contains information about a user-defined type. The
    class object can be used to create instances of the type.

instance:
  ~ An object that belongs to a class.

attribute:
  ~ One of the named values associated with an object.  Also
    referred to as *instance variables*.
   
method:
  ~ A function that is defined inside a class definition and is invoked
    on instances of that class.

object diagram:
  ~ A diagram that shows objects, their attributes, and the values of
    the attributes.

subject:
  ~ The object a method is invoked on.

constructor:
  ~ A special method always named `__init__` that handles initializing
    the values of attributes in an object, and any other setup required
    when a new instance is created.
 
magic methods:
  ~ Method names that begin and end with `__`; they are implicitly and
    automatically invoked by the Python interpreter.    
  
object-oriented language:
  ~ A language that provides features, such as user-defined classes and
    method syntax, that facilitate object-oriented programming.

object-oriented programming:
  ~ A style of programming in which data and the operations that
    manipulate it are organized into classes and methods.  Also
    referred to as OOP.

embedded (object):
  ~ An object that is stored as an attribute of another object.

HAS-A relationship:
  ~ The relationship between two classes where instances of one class
    contain references to instances of the other.

IS-A relationship:
  ~ The relationship between a child class and its parent class.

inheritance:
  ~ The ability to define a new class that is a modified version of a
    previously defined class.

parent class:
  ~ The class from which a child class inherits.

child class:
  ~ A new class created by inheriting from an existing class; also
    called a “subclass.”

shallow copy:
  ~ To copy the contents of an object, including any references to
    embedded objects; implemented by the `copy` function in the `copy`
    module.

deep copy:
  ~ To copy the contents of an object as well as any embedded objects,
    and any objects embedded in them, and so on; implemented by the
    `deepcopy` function in the `copy` module.
 

class attribute:
  ~ An attribute associated with a class object. Class attributes are
    defined inside a class definition but outside any method.

veneer:
  ~ A method or function that provides a different interface to another
    function without doing much computation.

class diagram:
  ~ A diagram that shows the classes in a program and the relationships
    between them.


<!--

operator overloading:
  ~ Changing the behavior of an operator like `==` so it works with a
    user-defined type.

polymorphic:
  ~ Pertaining to a function that can work with more than one type.

multiplicity:
  ~ A notation in a class diagram that shows, for a HAS-A relationship,
    how many references there are to instances of another class.

prototype and patch:
  ~ A development plan that involves writing a rough draft of a program,
    testing, and correcting errors as they are found.

planned development:
  ~ A development plan that involves high-level insight into the problem
    and more planning than incremental development or prototype
    development.

pure function:
  ~ A function that does not modify any of the objects it receives as
    arguments. Most pure functions are fruitful.

modifier:
  ~ A function that changes one or more of the objects it receives as
    arguments. Most modifiers are fruitless.

functional programming style:
  ~ A style of program design in which the majority of functions are
    pure.

 -->


## Exercises

> 1. Write a class definition for a Date object that has attributes
>    `day`, `month` and `year`. Write a function called `increment_date`
>    that takes a Date object, `date` and an integer, `n`, and returns a
>    new Date object that represents the day `n` days after `date`. Hint:
>    "Thirty days hath September..."  Challenge: does your function deal
>    with leap years correctly? See <http://wikipedia.org/wiki/Leap_year>.
>    
> 1. The built in `datetime` module provides `date` and `time` objects, 
>    each with a 
>    rich set of methods and operators.  Read the documentation at
>    <http://docs.python.org/lib/datetime-date.html>.
> 
>     a. Use the `datetime` module to write a program that gets the
>        current date and prints the day of the week.
> 
>     b. Write a program that takes a birthday as input and prints the
>        user’s age and the number of days, hours, minutes and seconds until
>        their next birthday.
> 
> 1.  Write a definition for a class named `Kangaroo` with the following
>     methods:
> 
>       a.  An `__init__` method that initializes an attribute named
>           `pouch_contents` to an empty list.
>       
>       b.  A method named `put_in_pouch` that takes an object of any type
>           and adds it to `pouch_contents`.
>       
>       c.  A `__str__` method that returns a string representation of the
>           Kangaroo object and the contents of the pouch.
> 
>      Test your code by creating two `Kangaroo` objects, assigning them to
>      variables named `kanga` and `roo`, and then adding `roo` to the
>      contents of `kanga`’s pouch.
>     
> 1.  The following code is a solution to the previous problem, except that
>     it contains a nasty bug.  Find, describe, and fix the problem.
> 
>         class Kangaroo(object):
>             """a Kangaroo is a marsupial"""
>             
>             def __init__(self, contents=[]):
>                 """initialize the pouch contents; the default value is
>                 an empty list"""
>                 self.pouch_contents = contents
>         
>             def __str__(self):
>                 """return a string representaion of this Kangaroo and
>                 the contents of the pouch, with one item per line"""
>                 t = [ object.__str__(self) + ' with pouch contents:' ]
>                 for obj in self.pouch_contents:
>                     s = '    ' + object.__str__(obj)
>                     t.append(s)
>                 return '\n'.join(t)
>         
>             def put_in_pouch(self, item):
>                 """add a new item to the pouch contents"""
>                 self.pouch_contents.append(item)
>         
>         kanga = Kangaroo()
>         roo = Kangaroo()
>         kanga.put_in_pouch('wallet')
>         kanga.put_in_pouch('car keys')
>         kanga.put_in_pouch(roo)
>         
>         print kanga
>         
>         # If you run this program as is, it seems to work.
>         # To see the problem, trying printing roo.
> 
> 
> 1.  The table below shows possible hands in poker, in increasing order
>     of value (and decreasing order of probability):
> 
>       -------------------  ------------------------------------------------------------------
>        *pair*               two cards with the same rank 
>       
>        *two pair*           two pairs of cards with the same rank 
>       
>        *three of a kind*    three cards with the same rank
>       
>        *straight*           five cards with ranks in sequence (aces can be high or low, so
>                             `Ace-2-3-4-5` is a straight and so is `10-Jack-Queen-King-Ace`,
>                             but `Queen-King-Ace-2-3` is not.) 
>       
>        *flush*              five cards with the same suit 
>       
>        *full house*         three cards with one rank, two cards with another 
>       
>        *four of a kind*     four cards with the same rank 
>       
>        *straight flush*     five cards in sequence (as defined above) and with the same suit
>       -------------------  ------------------------------------------------------------------
> 
>      The goal of these exercises is to estimate the probability of drawing
>      these various hands.
> 
>      a. Using the `Card`, `Hand`, and `Deck` classes created in this chapter, 
>         create a `PokerHand` class that can hold up to 7 cards at once.
> 
>      a. Write a `main` function that deals cards from a `Deck` object
>         and adds them to a `PokerHand` object.  
>         
>      a. Write a `isStraightFlush` method for the `PokerHand` class that
>         tests whether the hand contains a straight flush.
> 
>      a. Add methods to `PokerHand` named `has_pair`, `has_twopair`,
>         etc. that return True or False according to whether or not the
>         hand meets the relevant criteria. Your code should work correctly
>         for “hands” that contain any number of cards (although 5 and 7 are
>         the most common sizes).
> 
>      a. Write a method named `classify` that figures out the highest-value
>         classification for a hand and sets the `label` attribute
>         accordingly.  For example, a 7-card hand might contain a flush and
>         a pair; it should be labeled "flush".
> 
>      a. When you are convinced that your classification methods are
>         working, the next step is to estimate the probabilities of the
>         various hands.  Write a function that shuffles a deck of cards,
>         divides it into hands, classifies the hands, and counts the number
>         of times various classifications appear.
> 
>      a. Print a table of the classifications and their probabilities.  Run
>         your program with larger and larger numbers of hands until the
>         output values converge to a reasonable degree of accuracy.  Compare
>         your results to the values at <http://wikipedia.org/wiki/Hand_rankings>.
>        
> 1. This exercise uses the `turtle` module.  You will write code that
>    makes Turtles play tag. If you are not familiar with the rules of tag,
>    see <http://wikipedia.org/wiki/Tag_(game)>.
> 
>     a. Type in the following code and run it.  You should
>        see a turtle screen with three turtles that start wandering
>        around the screen at random.
> 
>             '''
>             Wobbler class originally written by Allen Downey.
>             Modified by J. Sommers for use with vanilla turtle rather
>             than TurtleWorld.
>             '''
>         
>             import turtle
>             import random
>             
>             class Wobbler(turtle.Turtle):
>                 """a Wobbler is a kind of turtle with attributes for speed and
>                 clumsiness."""
>             
>                 def __init__(self, speed=1, clumsiness=60, color='red'):
>                     turtle.Turtle.__init__(self)
>                     self.delay = 0
>                     self.speed = speed
>                     self.clumsiness = clumsiness
>                     self.pencolor(color)
>         
>                     # move to the starting position
>                     self.penup() 
>                     self.right(random.randint(0,360))
>                     self.backward(150)
>                     self.pendown()
>         
>                 def step(self):
>                     """step is invoked by the timer function on every Wobbler, once
>                     per time step."""
>                     
>                     self.steer()
>                     self.wobble()
>                     self.move()
>             
>                 def move(self):
>                     """move forward in proportion to self.speed"""
>                     self.forward(self.speed)
>         
>                 def wobble(self):
>                     """make a random turn in proportion to self.clumsiness"""
>                     dir = random.randint(0,self.clumsiness) - random.randint(0,self.clumsiness)
>                     self.right(dir)
>         
>                 def steer(self):
>                     """steer the Wobbler in the general direction it should go.
>                     Postcondition: the Wobbler's heading may be changed, but
>                     its position may not."""
>                     self.right(10)
>         
>         
>             def timerfunction():
>                 for t in turtle.turtles():
>                     t.step()
>                 turtle.ontimer(timerfunction, 100)
>         
>         
>             if __name__ == '__main__':
>             
>                 # make 3 turtles
>                 turtle_colors = ['red','blue','yellow']
>                 i = 1.0
>                 for i in range(3):
>                     w = Wobbler(i, i*30, turtle_colors[i])
>                     i += 0.5
>         
>                 timerfunction()
>                 turtle.mainloop()
> 
>     b. Read the code and make sure you understand how it works.  The
>        `Wobbler` class inherits from `Turtle`, which means that the
>        `Turtle` methods `left`, `right`, `forward` and `backward` work on Wobblers.
> 
>         The `step` method gets invoked by the `timerfunction`.  It
>         invokes `steer`, which turns the Turtle in the desired direction,
>         `wobble`, which makes a random turn in proportion to the Turtle’s
>         clumsiness, and `move`, which moves forward a few pixels,
>         depending on the Turtle’s speed.
> 
>     c. Create a class named `Tagger` that inherits from `Wobbler`.
>        Change the call in `main` to invoke `Tagger` instead of `Wobbler`
>        when creating the turtles.
> 
>     d. Add a `steer` method to `Tagger` to override the one in `Wobbler`.
>        As a starting place, write a version that always points the Turtle
>        toward the origin.  Hint: use the math function `atan2` and the
>        Turtle attributes `x`, `y` and `heading`.
> 
>     e. Modify `steer` so that the Turtles stay on the screen.  
> 
>     f. Modify `steer` so that each Turtle points toward its nearest
>        neighbor.  Hint: Turtles have an attribute, `screen`, that is a
>        reference to the `Screen` they live in, and `Screen` has a method
>        `turtles` that returns a list of all the `Turtle` objects on the
>        screen.
> 
>     g. Modify `steer` so the Turtles play tag. You can add methods to
>        `Tagger` and you can override `steer` and `__init__`, but you may
>        not modify or override `step`, `wobble` or `move`. Also,
>        `steer` is allowed to change the heading of the Turtle but not the
>        position.
> 
>        Adjust the rules and your `steer` method for good quality play;
>        for example, it should be possible for the slow Turtle to tag the
>        faster Turtles eventually.
