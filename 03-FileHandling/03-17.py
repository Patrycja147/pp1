import re
komunikat = 'To be, or not to be, that is the question'
cyfry = re.findall('[aeiou]',komunikat)
print('Liczba samogłosek w tekście:',len(cyfry))