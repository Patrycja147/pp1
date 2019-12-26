def srednie(liczby):
    import statistics
    z=statistics.mean(liczby)
    print(z)
    
def mediana(liczby):
    import statistics
    z=statistics.median(liczby)
    print(z)
    
def odchylenie(liczby):
    import statistics
    z=statistics.stdev(liczby)
    print(z)
    
srednie([21600,4350,3920,5590,3250, 4010])
mediana([21600,4350,3920,5590,3250, 4010])
odchylenie([21600,4350,3920,5590,3250, 4010])
