x=int(input("Podaj x: "))
y=int(input("Podaj y: "))
print("x=",x,"\ny=",y)
if x>0 and y>0:
    print("Punkt P(",x,",",y,") znajduje się w pierwszej ćwiartce układu współrzędnych.")
elif x<0 and y>0:
    print("Punkt P(",x,",",y,") znajduje się w drugiej ćwiartce układu współrzędnych.")
elif x<0 and y>0:
    print("Punkt P(",x,",",y,") znajduje się w trzeciej ćwiartce układu współrzędnych.")
elif x>0 and y<0:
    print("Punkt P(",x,",",y,") znajduje się w czwartej ćwiartce układu współrzędnych.")
elif x==0 and y==0:
    print("Punkt P(",x,",",y,") znajduje się w centrum układu współrzędnych.")
elif x==0 and y!=0:
    print("Punkt P(",x,",",y,") znajduje się na osi y.")
else:
    print("Punkt P(",x,",",y,") znajduje się na osi x.")