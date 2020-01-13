wzrost=int(input('Podaj wzrost:'))
waga=float(input('Podaj wagę:'))
assert type(wzrost)==int,'Nieprawidłowa wartość'
assert type(waga)==float,'Nieprawidłowa wartość'
assert wzrost>=150 and wzrost<=220,'Wzrost jest nieprawidłowy'
assert waga>=40.0 and waga<=150.0, 'Waga jest nieprawidłowa'
print(f'BMI={waga/((wzrost/100)**2)}')