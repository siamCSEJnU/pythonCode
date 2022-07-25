#draw a 36-axis based wheel using turtle

import turtle

#turtle.shape("turtle")
turtle.color("blue")
turtle.speed(10)
i=0
while i<36:
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)

turtle.exitonclick()