miesiace=[]
def miesiac(n):
    if n==1:
        return 'Styczeń'
    elif n>12:
        return 'Nie ma takiego miesiąca'
    elif n==2:
        return 'Luty'
    elif n==3:
        return 'Marzec'
    elif n==4:
        return 'Kwiecień'
    elif n==5:
        return 'Maj'
    elif n==6:
        return 'Czerwiec'
    elif n==7:
        return 'Lipiec'
    elif n==8:
        return 'Sierpień'
    elif n==9:
        return 'Wrzesień'
    elif n==10:
        return 'Październik'
    elif n==1:
        return 'Listopad'
    else:
        return 'Grudzień'
    
    
print(miesiac(7))
print(miesiac(9))
miesiace.append(miesiac(7))
miesiace.append(miesiac(9))