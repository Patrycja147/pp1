import re
suma=0
with open("./land.txt","r") as f:
    su=(re.findall('\d',f.read()))
    for x in su:
        suma+=int(x)
    