"""
person.py

Eine Person hat:
- einen Namen 
- ein Alter
- ein Geburtsdatum 
- eine Telefonnummer 
-eine E-mail Adresse
"""

class Person:
    """Die Klasse.beschreibt eine Person im Fitnessstudio"""
    def __init__(self,name,alter,geburtsdatum,telefon,email):
        #Name der Person
        self.name= name 

        # Alter der Person
        self.alter = alter

        #Geburtsdatum der Person 
        self.geburtsdatum =geburtsdatum

        #Telefonnummer der Person 
        self.telefon= telefon

        #Email-Adresse der Person
        self.email=email
     
    
    def daten_anzeigen(self):
        """Gibt alle gespeicherten Daten der Person aus """
        print(self.name, self.alter,self.geburtsdatum,self.telefon,self.email)
     
    
    
    def daten_aendern (self,name,alter,geburtsdatum,telefon,email):
        """Ändert die gespeicherten Daten der Person"""
        #Überschreibt die bisherigen Werte mit den neuen Werten 

        self.name= name 
        self.alter = alter
        self.geburtsdatum =geburtsdatum
        self.telefon= telefon
        self.email=email
        