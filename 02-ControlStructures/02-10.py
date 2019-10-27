x=int(input("Podaj dowolną liczbę: "))
if x>0 and x%2!=0:
    print("Liczba jest dodatnia i nieparzaysta.")
elif x<0 and x%2!=0:
    print("Liczba nie jest dodatnia, ale jest nieparzysta.")
else:
    print("Liczba nie jest dodatnia i jest parzysta.")