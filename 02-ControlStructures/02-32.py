y=[]
y.extend(str(input("Podaj dowolny ciąg znaków: ")))
y.reverse()
print("Podane znaki w odwróconej kolejności: ",*y, sep='')