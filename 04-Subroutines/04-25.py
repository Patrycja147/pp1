def jestimie(imie,imiona):
    print('Imiona:',imiona)
    print('Imię:',imie)
    listaimion=[]
    listaimion=imiona.split(" ")
    if imie in listaimion:
        print('Rezultat: imię zawarte jest w wykazie imion.')
    else:
        print('Rezultat: imię nie jest zawarte w wykazie imion')
jestimie('Wojtek','Janek Ania Wojtek Zosia')