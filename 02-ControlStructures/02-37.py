x=int(input("Podaj pierwszą liczbę: "))
y=int(input("Podaj drugą liczbę: "))
z=int(input("Podaj trzecią liczbę: "))
list=[x,y,z]
list.sort()
print("Mediana tych liczb to: ",list[1])