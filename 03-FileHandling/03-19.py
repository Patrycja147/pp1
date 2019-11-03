univ =[]
with open("C:/Users/admin/Desktop/universities.txt","r") as f:
    for line in f:
        univ.append(line)
    
univ.sort()
stringus=""
for x in univ:
      stringus=stringus+x
print(stringus)
with open("C:/Users/admin/Desktop/pp1/03-FileHandling/universities.txt","w") as f:
    f.write(stringus)
    