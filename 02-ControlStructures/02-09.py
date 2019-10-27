a=int(input("Wprowadż dane: "))
if a>0 and a%2!=0:
    print("Liczba {} jest dodatnia i nieparzysta".format(a))
else:
    print("Liczba {} jest ujemna lub parzysta".format(a))