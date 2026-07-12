from person import Person
from fitnessstudioexception import FitnessstudioException
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

    def kurs_buchen(self,kurs)-> str:
     """Bucht einen Kurs für das Mitglied."""

        # Prüfen, ob die Mitgliedschaft die Leistung erlaubt
     if not self.mitgliedschaft.hat_leistung(kurs.benoetigte_leistung):
        raise FitnessstudioException("Diese Mitgliedschaft erlaubt keine Kursbuchung.")
        
        # Mitglied zum Kurs hinzufügen
     meldung = kurs.mitglied_hinzufuegen(self)
        # Nur hinzufügen, wenn das Mitglied tatsächlich Teilnehmer geworden ist
     if self in kurs.teilnehmer:
        self.gebuchte_kurse.append(kurs)

     return meldung
    def kurs_stornieren(self, kurs)-> None:
        """Storniert einen bereits gebuchten Kurs."""

        # Prüfen, ob der Kurs überhaupt gebucht wurde
        if kurs not in self.gebuchte_kurse:
            raise FitnessstudioException("Dieser Kurs wurde nicht gebucht.")

        # Mitglied aus dem Kurs entfernen
        meldung = kurs.mitglied_entfernen(self)

        # Kurs aus der Liste der gebuchten Kurse entfernen
        self.gebuchte_kurse.remove(kurs)

        # Erfolgsmeldung zurückgeben
        return meldung
    def geraet_reservieren(self, geraet)-> None:
        """Reserviert ein Geraet fuer das Mitglied"""
            # Prüfen, ob die Mitgliedschaft die Leistung erlaubt
        if not self.mitgliedschaft.hat_leistung("geraet_reservieren"):
            raise FitnessstudioException("Diese Mitgliedschaft erlaubt keine Geräte-Reservierung.")

        # Gerät reservieren
        meldung = geraet.reservieren(self)

        # Gerät in die Liste der reservierten Geräte aufnehmen
        self.reservierte_geraete.append(geraet)

        # Erfolgsmeldung zurückgeben
        return meldung
    
    def geraet_freigeben(self, geraet)-> None:
        """Gibt ein reserviertes Geraet wieder frei"""

        # Prüfen, ob das Gerät überhaupt reserviert wurde
        if geraet not in self.reservierte_geraete:
            raise FitnessstudioException("Dieses Gerät wurde nicht von diesem Mitglied reserviert.")

        # Gerät freigeben
        meldung = geraet.freigeben()

        # Gerät aus der Reservierungsliste entfernen
        self.reservierte_geraete.remove(geraet)

        # Erfolgsmeldung zurückgeben
        return meldung