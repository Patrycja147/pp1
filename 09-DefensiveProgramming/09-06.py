a = 5.5
b = 7
assert b!=0, 'Wartość b równa 0!'
assert type(a) == int, 'Wartość a jest niecałkowita!'
assert type(b) == int, 'Wartość b jest niecałkowita!'
print(f'{a}/{b} = {a/b}')