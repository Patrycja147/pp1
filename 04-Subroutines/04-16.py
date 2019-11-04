liczby=[]
y=0
def czytajliczbe():
    x=int(input('Podaj liczbę: '))
    return x
for y in range(0,2):
    liczby.append(czytajliczbe())
    y+=1
print('Suma tych liczb to:',sum(liczby))