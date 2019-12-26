import turtle
window=turtle.Screen()
turtle.speed(10)
turtle.pensize(5)

turtle.penup()
turtle.setposition(-100,100)
turtle.pendown()
for i in range(0,4):
    turtle.fd(100)
    turtle.rt(90)