from person import Person
class trainer(Person):
    def __init__( self,name, alter,geburtdatum,telefon,email,personalnummer, fachgebiet, kurse):
       super().__init__(name,alter,geburtdatum,telefon,email )

       self.personalnummer=personalnummer
       self.fachgebiet=fachgebiet
       self.kurse=[]

    def kurs_uebernehmen(self,kurs):
        self.kurs.append(kurs)
    def kurs_entfernen(self,kurs):
        self.kurs.remove(kurs)
        
