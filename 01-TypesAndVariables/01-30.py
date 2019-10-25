tablica=[12,6,4,9,3]
import random
for x in range(0,len(tablica)):
    gwiazdeczka =""
    for y in range(0,tablica[x]):
        gwiazdeczka =gwiazdeczka+"*"
    print(str(tablica[x])+": "+gwiazdeczka)