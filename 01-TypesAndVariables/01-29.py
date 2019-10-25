import random
a=random.randint(1,6)
b=int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
print("Komputer wyrzucił",a,"oczek")
if a==b:
    print("Zgadłeś: TRUE")
else:
    print("Zgadłeś: FALSE")
