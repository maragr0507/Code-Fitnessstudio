class Person:
    def __init__(self,name,alter,geburtsdatum,telefon,email):
        self.name= name 
        self.alter = alter
        self.geburtsdatum =geburtsdatum
        self.telefon= telefon
        self.email=email
    
    def daten_anzeigen(self):
        print(self.name, self.alter,self.geburtsdatum,self.telefon,self.email)

    def daten_aendern (self,name,alter,geburtsdatum,telefon,email):
        self.name= name 
        self.alter = alter
        self.geburtsdatum =geburtsdatum
        self.telefon= telefon
        self.email=email
        