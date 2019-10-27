x=["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć","dziesięć"]
y=[]
y.extend(str(input("Podaj dowolną liczbę naturalną: ")))
slownie=" "
for i in range(0,len(y)):
    slownie=slownie+" "+x[int(y[i])]
print(*y,"-",slownie)