def potega(x,n):
    wynik=1
    while n>=1:
        wynik=wynik*x
        n-=1
    return wynik
    
print(f'5 do potęgi 3 wynosi {potega(5,3)}')