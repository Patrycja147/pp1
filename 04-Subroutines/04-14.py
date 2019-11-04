tablica=[15,38,7,23,14]
liczba=23
def wystepuje(liczba, tablica):
    if liczba in tablica:
        print('Rezultat: Podana liczba występuje w tablicy')
    else:
        print('Rezultat: Podana liczba nie występuje w tablicy')
print('Liczba:',liczba,'\nTablica:',tablica)
wystepuje(liczba,tablica)