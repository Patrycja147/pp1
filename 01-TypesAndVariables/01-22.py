a=int(input("Podaj bok a: "))
b=int(input("Podaj bok b: "))
c=int(input("Podaj bok c: "))
boki=[a,b,c]
p=sum(boki)/2
d=max(boki)
boki.remove(max(boki))
if d<sum(boki):
    print("Pole trójkąta wynosi: ",(p*(p-a)*(p-b)*(p-c))**(1/2))
else:
    print("Z tych boków nie można stworzyć trójkąta.")