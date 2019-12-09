class Muzyka():
    def __init__(self,wykonawca,utwor,album,rok):
        self.wykonawca=wykonawca
        self.utwor=utwor
        self.album=album
        self.rok=rok
    
    def __str__(self):
        return f'Wykonawca: {self.wykonawca} \nUtwór: {self.utwor}\nAlbum: {self.album}\nRok: {self.rok}'

muzyka=Muzyka("Dawid Podsiadło","Nie ma fal","Małomiasteczkowy","2018")    
print(muzyka)