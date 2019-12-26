import csv
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    x=0
    tablica=[]
    for row in reader:
        if x==0:
            row.insert(0,"#")
            x=x+1
        else:
            row.insert(0,x)
            x=x+1
            
        tablica.append(row)
    output=''
    for item in tablica[0]:
        output+=str(item)+' '*10
    output+='\n========================================================'
    out=''
    for item in tablica[1:]:
        out+='\n'
        i=0
        for item2 in item:
            space = len(str(item2))-1
            if i == 0:
                out+=str(item2)+' '*(11-space)
            elif i == 1:
                out+=str(item2)+' '*(14-space)
            elif i == 2:
                out+=str(item2)+' '*(17-space)
            elif i == 3:
                out+=str(item2)+' '*(14-space)
            elif i == 4:
                out+=str(item2)+' '*(14-space)
            i+=1
    num=[]
    for item in tablica[1:]:
        import statistics
        num.append(int(item[3])) 
    z=statistics.mean(num)
print(output,out)
print('\nŚrednia arytmetyczna wieku pracowników to:',z)