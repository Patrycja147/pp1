tab=[2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
tab.sort()
x=len(tab)
y=x/2
y=int(y)
a=int(tab[y])
b=int(tab[y+1])
mediana=((a+b)/2)
print('Mediana tych liczb to:',mediana)



def mediana(liczby):
    liczby1=[]
    liczby1=liczby.split(", ")
    liczby1.sort()
    x=len(liczby1)
    y=x/2
    y=int(y)
    a=int(liczby1[y])
    b=int(liczby1[y+1])
    mediana=((a+b)/2)
    print('Mediana tych liczb to:',mediana)
    
mediana('2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4')
