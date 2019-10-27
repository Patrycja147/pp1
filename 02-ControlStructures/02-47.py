x=int(input("Podaj kwotę w zł: "))
p=0
d=0
j=0
while x>0:
    if x<5:
        if x<2:
            if x==1:
                j+=1
                x-=1
            else:
                print()
        else:
            d+=1
            x-=2
    else:
        p+=1
        x-=5
print("5zł:",p,"\n2zł;",d,"\n1zł:",j)