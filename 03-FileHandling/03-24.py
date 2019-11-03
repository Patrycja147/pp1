import csv
first = ['imie','nazwisko','adres']
typical = [['Marek','Zelnik','zzelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
with open('mails.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(first)
    writer.writerows(typical)