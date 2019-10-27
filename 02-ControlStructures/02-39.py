num=[0,1]
h=0
for i in range (51):
    h=num[-1]+num[-2]
    num.append(h)
print(num)