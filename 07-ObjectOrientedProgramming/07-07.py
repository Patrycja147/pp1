'''Student posiada imię, nazwisko, nr albumu oraz kierunek studiów. Wszyscy studenci
studiują na tej samej uczelni (UEK Kraków). Utwórz klasę opisującą studenta, która
zawierać będzie wymienione cechy. Numer albumu powinien być nadawany
automatycznie, jako kolejna liczba naturalna począwszy od 100000. W tym celu utwórz
zmienną klasową, w której przechowuj ostatnio nadany numer albumu. Tworząc nowego
studenta (obiekt), zwiększ wartość tej zmiennej, a następnie użyj jej jako numer albumu
dla tworzonego studenta. Następnie napisz program, który utworzy 3 różnych studentów i
wyświetli ich dane personalne w formacie, jak poniżej. Wykorzystaj metodę __str__
Wacław POTOCKI (100001), Informatyka stosowana, UEK Kraków'''

class Student():
    nr=100000
    uczelnia='UEK Kraków'
    def __init__(self,imie,nazwisko,kierunek):
        self.imie=imie
        self.nazwisko=nazwisko
        self.album=Student.nr
        self.kierunek=kierunek
        Student.nr+=1
        
    def __str__(self):
        return f'{self.imie}, {self.nazwisko}, {self.album}, {self.kierunek}, {Student.uczelnia}'
    
print(Student('Patrycja','Żółkiewska','Informatyka Stosowana'))
print(Student('Wiktoria','Mroczko','Informatyka Stosowana'))
