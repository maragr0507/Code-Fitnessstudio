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
    def __init__( self,name, alter,geburtsdatum,telefon,email,personalnummer, fachgebiet):
       
       # Eigenschaften von der Klasse Person werden uebernommen
       super().__init__(name,alter,geburtsdatum,telefon,email )

       # Eindeutige Personalnummer
       self.personalnummer=personalnummer
       
       # Fachgebiet des Trainers
       self.fachgebiet=fachgebiet

       # Liste aller Kurse, die der Trainer betreut
       self.kurse=[]

    def kurs_uebernehmen(self,kurs):
        """Fuegt einen Kurs zur Liste hinzu."""
        self.kurse.append(kurs)
    def kurs_entfernen(self,kurs):
        """Entfernt einen Kurs aus der Liste."""
        self.kurse.remove(kurs)

