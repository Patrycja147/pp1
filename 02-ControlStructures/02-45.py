b=int(input("Podaj liczbę: "))
p=[]
for i in range(0,b):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            p.append(i)
print("Liczby pierwsze: ",p)