x=int(input("Podaj limit prędkości (km/h): "))
y=int(input("Podaj prędkość pojazdu (km/h): "))
if y-x<0:
    print("Pojazd nie przekroczył prędkości.")
elif y-x>0 and y-x<10:
    print("Mandat (zł): ",5*(y-z))
else:
    print("Mandat (zł):",5*10+15*(y-x-10))