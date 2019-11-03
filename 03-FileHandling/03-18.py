lista=[]
text = open('./numbers.txt').read()
lista.append(text)
lista=[text.replace('\n',' ') for i in lista]
lista=[i.split(' ') for i in lista]
intlist=[]
for x in lista[0]:
    intlist.append(int(x))
intlist.sort()
suma = sum(intlist)