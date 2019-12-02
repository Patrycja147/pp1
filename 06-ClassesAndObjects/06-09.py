class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name=new_name
        
    def print_fullname(self):
        print(self.fullname)
    
    def set_fullname(self, new_fullname):
        self.fullname=new_fullname
        
x=University()
x.print_name()
x.print_fullname()

z=University()
z.set_name('AGH')
z.print_name()
z.set_fullname('Akademia Górniczo-Hutnicza w Krakowie')
z.print_fullname()