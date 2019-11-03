with open('numbers.txt','r') as file:
    with open('evennumbers.txt','w') as secondfile:
        num=[]
        even=[]
        for line in file:
            num.append(int(line))
        for i in num:
            if i%2==0:
                secondfile.write(str(i)+'\n')