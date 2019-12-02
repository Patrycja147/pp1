class TV(): 
    def __init__(self):
        self.is_on= False
        self.channel_no='Telewizor niezaprogramowany, brak dostępnych kanałów.'
        self.channels=[]
        
    def on(self):
        self.is_on= True
        
    def off(self):
        self.is_on= False
        
    def show_status(self):
        if self.is_on==True:
            print('Telewizor jest włączony, kanał',self.channel_no)
        else:
            print('Telewizor jest wyłączony.')
            
    def set_status(self,changed):
        self.is_on=changed
        
    def set_channel(self, new_channel_no):
        self.channel_no=new_channel_no
        
    def set_channels(channels_list):
        
    def show_channels():
        
    
p=TV()
p.show_status()

y=TV()
y.set_status(True)
y.show_status()
y.set_channel(5)
y.show_status()

z=TV()
z.set_status(False)
z.show_status()