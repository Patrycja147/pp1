def drawSquare(x,y,n):
    import turtle
    window=turtle.Screen()
    turtle.speed(100)
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for a in range(0,4):
        if a!= 0 :
            turtle.bk(n-n/4)
            turtle.rt(90)
            turtle.fd(n/4)
            turtle.lt(90)
        for i in range(0,4):
            if (i!=0):
                turtle.fd((n/4))
            for b in range(0,4):
                turtle.fd(n/4)
                turtle.rt(90)
            
def okrag(r,x,y):
    import turtle
    window=turtle.Screen()
    z = turtle.Turtle()
    z.speed(0)
    z.penup()
    z.setposition(0+x,0+y)
    z.pendown()
    z.circle(r)
    
okrag(100,-100,0)
    
def Trojkat(m,x,y):
    import turtle
    window=turtle.Screen()
    z = turtle.Turtle()
    