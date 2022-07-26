#creating a pattern using dot()
import turtle

turtle.color("blue")
turtle.speed(5)
turtle.shape("turtle")
turtle.penup()

row=5
col=5
for i in range(row):
    for j in range(col):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*col)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
turtle.exitonclick()    