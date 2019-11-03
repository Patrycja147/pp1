with open('C:/Users/admin/Desktop/numbers.txt','r') as file:
    num=[]
    for line in file:
        num.append(int(line))
    x=sum(num)
    print('Suma liczb zawartych w pliku wynosi: ',x)