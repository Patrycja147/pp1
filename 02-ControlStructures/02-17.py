x=1
wynikN=0
wynikP=0
while x<50:
    if x%2!=0:
        wynikN=wynikN+x
    else:
        wynikP=wynikP+x
    x=x+1
print("Suma liczb parzystych to:",wynikP,".","Suma liczb nieparzystych to: ",wynikN,".")