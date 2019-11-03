prod=input('Podaj kolejny produkt do listy: ')
with open('shoppinglist.txt','a') as file:
    file.write(prod+'\n')