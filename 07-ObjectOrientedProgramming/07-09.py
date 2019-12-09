'''Poniższa klasa zawarta w pliku message.py opisuje dowolny komunikat tekstowy.

Uzupełnij definicję metody set_message(), aby w momencie ustawiania treści komunikatu
jego pierwsza litera została zamieniona na wielką, a pozostałe na małe. Ponadto na końcu
komunikatu dodaj zwrot pożegnalny BYE.
Następnie utwórz dwie klasy pochodne, każdą w oddzielnym pliku: SMS oraz Email. Klasa
SMS powinna zawierać właściwość opisującą nr telefonu nadawcy oraz odbiorcy,
natomiast klasa Email powinna zawierać właściwości: adres nadawcy, adres odbiorcy oraz
temat listu. W obydwu klasach zdefiniuj metodę send(), która służy do wysyłania
wiadomości. Wysłanie wiadomości polega na wyświetleniu danych charakterystycznych dla
danego typu wiadomości oraz jej treści, np.:
Wysyłanie emaila...
Od: nowak@onet.pl
Do: kowalski@gmail.com
Temat: Spotkanie w czwartek
Treść: Informuję, że nasze czwartkowe spotkanie zostało
odwołane. BYE.
W pliku communication.py utwórz program, w którym wyślij jeden email oraz jeden SMS.'''

class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
