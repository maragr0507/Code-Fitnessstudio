"""
mitgliedschaft.py

Die Klasse Mitgliedschaft beschreibt eine Mitgliedschaft im Fitnessstudio.

"""
class Mitgliedschaft: 
    def __init__(self,typ,preis):
        # Typ der Mitgliedschaft
        self.typ=typ

        #Monatlicher Preis der Mitgliedschaft
        self.preis=preis

        # Liste mit allen erlaubten leistungen 
        self.erlaubte_leistungen=[]

        # Prueft, ob eine bestimmte Leistung erlaubt ist
    def hat_leistung(self,leistung):
        """ 
        Rueckgabe:
        True  -> Die Leistung ist enthalten.
        False -> Die Leistung ist nicht enthalten."""
        return leistung in self.erlaubte_leistungen 