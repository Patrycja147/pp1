Wzrost=int(input("Podaj wzrost w cm: "))
Masa=float(input("Podaj wagę w kg: "))
Wzrost=Wzrost/100
BMI=Masa/(Wzrost**2)
if BMI<16:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza wygłodzenie. Twoje życie jest zagrożone.")
elif 16<BMI and BMI<16.99:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza wychudzenie.")
elif 17<BMI and BMI<18.45:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza niedowagę.")
elif 18.5<BMI and BMI<24.99:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza wagę prawidłową.")
elif 25<BMI and BMI<29.99:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza nadwagę.")
elif 30<BMI and BMI<34.99:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza I stopień otyłości.")
elif 35<BMI and BMI<39.99:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza II stopień otyłości.")
else:
    print("Twój wskaźnik BMI wynosi",round(BMI,2),"i oznacza skrajną otyłość. Twoje życie jest zagrożone.")