import re
komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
cyfry=[int(x) for x in cyfry]
śr=sum(cyfry)/len(cyfry)
print('Średnia temperatur w tych dniach wynosi:',śr)