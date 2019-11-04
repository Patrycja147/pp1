tablica=[4,3,7,1,3]
def suma(tablica):
    total = 0
    for x in tablica:
        total += x
    return total
print('Tablica:',tablica)
print('Suma wartości:',suma(tablica))