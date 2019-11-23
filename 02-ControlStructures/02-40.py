import random
j=0
d=0
t=0
c=0
p=0
s=0
x=0
for i in range(1,101):
    x=random.randrange(1, 7)
    if x==1:
        j+=1
    elif x==2:
        d+=1
    elif x==3:
        t+=1
    elif x==4:
        c+=1
    elif x==5:
        p+=1
    elif x==6:
        s+=1
print("Jedynka: ",j,"\nDwójka: ",d,"\nTrójka: ",t,"\nCzwórka: ",c,"\nPiątka: ",p,"\nSzóstka: ",s)
      