from person import Person
"""
mitglied.py 

Ein Mitglied hat:
- alle Eigenschaften einer Person
- eine Mitgliedsnummer
- eine Mitgliedschaft
- eine Liste gebuchter Kurse
- eine Liste reservierter Geraete

"""
class Mitglied(Person):
    """Die Klasse Mitglied beschreibt ein Mitglied im Fitnessstudio"""
    def __init__(self,name: str, alter: int,geburtsdatum: str,telefon: str,email: str, mitgliedsnummer: int, mitgliedschaft)-> None:
        # Eigenschaften der Klasse Person 
        super().__init__(name,alter,geburtsdatum,telefon,email )

        # Eindeutige Mitgliedsnummer 
        self.mitgliedsnummer=mitgliedsnummer

        # Mitgliedschaft des Mitglieds 
        self.mitgliedschaft=mitgliedschaft

        # Ein Mitglied kann mehrere Kurse buchen und mehrere Geraete reservieren. Dafuer eignet sich eine Liste.
        self.gebuchte_kurse = []
        self.reservierte_geraete = []

    def kurs_buchen(self,kurs)-> None:
            """Fuegt einen Kurs zu den gebuchten Kursen hinzu. """
            self.gebuchte_kurse.append(kurs)
    def kurs_stornieren(self, kurs)-> None:
            """Entfernt einen Kurs aus den gebuchten Kursen."""
            self.gebuchte_kurse.remove(kurs)
    def geraet_reservieren(self, geraet)-> None:
            """Reserviert ein Geraet fuer das Mitglied"""
            self.reservierte_geraete.append(geraet)
    def geraet_freigeben(self, geraet)-> None:
            """Gibt ein reserviertes Geraet wieder frei"""
            self.reservierte_geraete.remove(geraet)

