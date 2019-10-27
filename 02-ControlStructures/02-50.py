b=[]
n=int(input("Podaj liczbę: "))
d=n
while n>0 or n%2==1:
    if n%2==1:
        b.append(1)
        n=(n-1)/2
    else:
        b.append(0)
        n=n/2
list.reverse(b)
print(d,"(10)=",*b,"(2)")
        