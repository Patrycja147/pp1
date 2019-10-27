a=int(input("Podaj liczbę a: "))
b=int(input("Podaj liczbę b: "))
c=int(input("Podaj liczbę c: "))
import math
if a==b==c==0:
    print("Brak równania")
else:
    if a!=0:
        print("Równanie kwadratowe.")
        delta=b**2-(4*a*c)
        if delta<0:
            print("Delta mniejsza od 0. Równanie nie ma pierwiastków")
        elif delta==0:
            x0=(b**2/4*a)
            print("Delta jest równa 0. Pierwiastek równania to",x0)
        else:
            from math import sqrt
            x1=(b**2+sqrt(delta)/2*a)
            x2=(b**2-sqrt(delta)/2*a)
            print("Delta większa od 0. Pierwiastki równania to: ",x1,",",x2)
    elif a==0:
        x3=(-c/b)
        print("Funkcja liniowa. Miejsce zerowe to :",x3)