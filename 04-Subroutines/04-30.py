def lrandom():
    import random
    x=random.randint(1,50)
    return x

par=[]
niepar=[]
for i in range(1,1001):
    if lrandom%2==0:
        par.append(lrandom)
    else:
        niepar.append(lrandom)