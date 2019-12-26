wsp=[]
Delta=[]
def czytajWspolczynniki():
    wsp=[]
    a=float(input('Podaj pierwszy współczynnik:'))
    wsp.append(a)
    b=float(input('Podaj drugi współczynnik:'))
    wsp.append(b)
    c=float(input('Podaj trzeci współczynnik:'))
    wsp.append(c)
    print('Równanie kwadratowe postaci:',int(a),'x2+(',int(b),')x+(',int(c),')')
    return wsp

def obliczDelte(wsp):
    import math
    a=int(wsp[0])
    b=int(wsp[1])
    c=int(wsp[2])
    delta=math.pow(b,2)-(4*a*c)
    print ("\nDelta wynosi:",delta)
    Delta.append(delta)
    return Delta

def obliczPierwiastki(wsp,Delta):
    Delta=Delta[0]
    import math
    pierwiastki=[]
    if Delta<0:
        print('Brak miejsc zerowych')
    elif Delta==0:
        z=(-wsp[1])/(2*wsp[0])
        pierwiastki.append(z)
        print('Miejsce zerowe funkcji to:  x0=',*pierwiastki)
    else:
        y=(-(math.pow(Delta,-1))-wsp[1])/(2*wsp[0])
        z=(-(math.pow(Delta,-1))+wsp[1])/(2*wsp[0])
        print('Miejsca zerowe funkcji to: x1=',y,', x2=',z)