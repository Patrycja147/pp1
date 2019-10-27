x=int(input("Podaj liczbę: "))
list=[]
list.append(x)
while x!=0:
    x=int(input("Podaj liczbę: "))
    if x!=0:
        list.append(x)
    else:
        print()
s=sum(list)
aryt=s/len(list)
print("REZULTAT: Liczb=",len(list)," Suma=",s," Średnia=",aryt)