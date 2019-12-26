def drawSquare(x,y,n):
    import turtle
    turtle.speed(100)
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for z in range(0,4):
        if z != 0 :
            turtle.bk(n-n/4)
            turtle.rt(90)
            turtle.fd(n/4)
            turtle.lt(90)
        for i in range(0,4):
            if (i!=0):
                turtle.fd((n/4))
            for a in range(0,4):
                turtle.fd(n/4)
                turtle.rt(90)
                
            
 
    
    
drawSquare(-300,300,100)