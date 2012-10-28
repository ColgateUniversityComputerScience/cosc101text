'''
Wobbler class originally written by Allen Downey.
Modified by J. Sommers for use with vanilla turtle rather
than TurtleWorld.
'''

import turtle
import random

class Wobbler(turtle.Turtle):
    """a Wobbler is a kind of turtle with attributes for speed and
    clumsiness."""

    def __init__(self, speed=1, clumsiness=60, color='red'):
        turtle.Turtle.__init__(self)
        self.delay = 0
        self.speed = speed
        self.clumsiness = clumsiness
        self.pencolor(color)

        # move to the starting position
        self.penup() 
        self.right(random.randint(0,360))
        self.backward(150)
        self.pendown()

    def step(self):
        """step is invoked by the timer function on every Wobbler, once
        per time step."""
        
        self.steer()
        self.wobble()
        self.move()

    def move(self):
        """move forward in proportion to self.speed"""
        self.forward(self.speed)

    def wobble(self):
        """make a random turn in proportion to self.clumsiness"""
        dir = random.randint(0,self.clumsiness) - random.randint(0,self.clumsiness)
        self.right(dir)

    def steer(self):
        """steer the Wobbler in the general direction it should go.
        Postcondition: the Wobbler's heading may be changed, but
        its position may not."""
        self.right(10)


def timerfunction():
    for t in turtle.turtles():
        t.step()
    turtle.ontimer(timerfunction, 100)


if __name__ == '__main__':

    # make 3 turtles
    turtle_colors = ['red','blue','yellow']
    i = 1.0
    for i in range(3):
        w = Wobbler(i, i*30, turtle_colors[i])
        i += 0.5

    timerfunction()
    turtle.mainloop()
