"""
trainer.py

Ein Trainer hat:
- alle Eigenschaften einer Person
- eine Personalnummer
- ein Fachgebiet
- eine Liste der betreuten Kurse
"""

from person import Person

class Trainer(Person):
    """Die Klasse Trainer beschreibt einen Trainer im Fitnessstudio."""
    def __init__( self,name: str, alter: int ,geburtsdatum: str,telefon: str,email: str,personalnummer: int, fachgebiet: str)-> None:
       
       # Eigenschaften von der Klasse Person werden uebernommen
       super().__init__(name,alter,geburtsdatum,telefon,email )

       # Eindeutige Personalnummer
       self.personalnummer=personalnummer
       
       # Fachgebiet des Trainers
       self.fachgebiet=fachgebiet

       # Liste aller Kurse, die der Trainer betreut
       self.kurse=[]

    def kurs_uebernehmen(self,kurs)-> None:
        """Fuegt einen Kurs zur Liste hinzu."""
        if kurs not in self.kurse:
            self.kurse.append(kurs)
        kurs.trainer = self

    def kurs_entfernen(self,kurs)-> None:
        """Entfernt einen Kurs aus der Liste."""
        if kurs not in self.kurse:
            raise ValueError("Der Trainer betreut diesen Kurs nicht.")

        self.kurse.remove(kurs)
        if kurs.trainer is self:
            kurs.trainer = None
