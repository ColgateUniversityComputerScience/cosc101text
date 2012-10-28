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
