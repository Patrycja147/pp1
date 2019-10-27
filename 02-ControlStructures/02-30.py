x=0
PIN="0805"
while x<3:
    PIN2=str(input("Podaj kod PIN: "))
    if PIN==PIN2:
        print("Kod PIN jest poprawny.")
        break
    elif PIN!=PIN2 and x==2:
        print("Kod PIN jest niepoprawny.\nKarta płatnicza zostaje zablokowana.")
    else:
        print("Kod PIN jest niepoprawny.")
    x+=1