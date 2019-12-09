'''Dla wygody i czytelności kodu programu możliwe jest
utworzenie tekstowej reprezentacji obiektu w postaci
ciągu znaków. Taki obiekt może być następnie
użyty wszędzie tam, gdzie wymagane są dane typu
łańcuchowego, np. podczas wywołania funkcji print().
W grupach 2-3 osobowych uruchom poniższy program
i dokonaj jego analizy. Zwróć uwagę na zastosowaną
metodę __str__ oraz na wywołanie funkcji print()'''

class University():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name + " is the best!"

my_university = University('UEK Kraków')
print(my_university)