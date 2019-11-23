def podatek(dochod):
    print('Podaj dochód:',dochod)
    if dochod<=5000:
        x=dochod*0.17
    else:
        x=5000*0.17+(dochod-5000)*0.32
    print('Podatek należny:',x)
        
podatek(6000)