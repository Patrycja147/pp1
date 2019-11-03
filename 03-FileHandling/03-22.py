import re
studenci = []
with open("./students.txt","r") as f:
    for line in f:
        studenci.append(line.split(","))
for i in studenci:
        if (i[2] != 'age' and int(i[2])<30):
            print(i[0]+"  "+i[1]+"  "+i[4])
