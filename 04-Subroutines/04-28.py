def rysujWykres(jezyki,wartosci):
    jezyki1=jezyki.split(" ")
    wartosci1=wartosci.split(" ")
    y=0
    for i in wartosci1:
        x=jezyki1[y]
        i=int(i)
        print(x,': ','#'*i)
        y+=1

rysujWykres('Java Python JavaScript C++ C# Ruby Perl PHP C Android','61 47 37 32 26 18 14 14 9 7')