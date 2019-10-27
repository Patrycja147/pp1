x=1
while x<=30:
    if (x%15==0):
        print("BINGO")
    elif (x%5==0):
        print("FIVE")
    elif (x%3==0):
        print("THREE")
    else:
        print(str(x))
    x+=1