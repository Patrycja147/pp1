def rzucaKostka():
    import random
    z=0
    liczby=[]
    suma=0
    for i in range(1,4):
        z=int(random.randrange(1,7))
        liczby.append(z)
    suma=sum(liczby)
    print("Wyrzucone oczka: ",*liczby,' \nSuma oczek: ',suma)
    
rzucaKostka()