x=int(input("Podaj wiek psa w ludzkich latach: "))
if x<=2:
    print("Pies ma",x*10.5,"lat w psich latach.")
else:
    print("Pies ma",2*10.5+(x-2)*4,"lat w psich latach.")