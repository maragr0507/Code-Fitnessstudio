"""
mitglied.py 

Ein Mitglied hat:
- alle Eigenschaften einer Person
- eine Mitgliedsnummer
- eine Mitgliedschaft
- eine Liste gebuchter Kurse
- eine Liste reservierter Geraete

"""

from fitnessstudioexception import FitnessstudioException
from person import Person


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

    def kurs_buchen(self, kurs) -> str:
        """Bucht einen Kurs für das Mitglied."""

        # Pruefen, ob die Mitgliedschaft die Leistung erlaubt
        if not self.mitgliedschaft.hat_leistung(kurs.benoetigte_leistung):
            raise FitnessstudioException("Diese Mitgliedschaft erlaubt keine Kursbuchung.")
        
        # Mitglied zum Kurs hinzufuegen
        meldung = kurs.mitglied_hinzufuegen(self)
        # Nur hinzufuegen, wenn das Mitglied tatsaechlich Teilnehmer geworden ist
        if self in kurs.teilnehmer and kurs not in self.gebuchte_kurse:
            self.gebuchte_kurse.append(kurs)
        
        return meldung
    def kurs_stornieren(self, kurs)-> str:
        """Storniert einen bereits gebuchten Kurs."""

        # Pruefen, ob der Kurs ueberhaupt gebucht wurde
        if kurs not in self.gebuchte_kurse:
            raise FitnessstudioException("Dieser Kurs wurde nicht gebucht.")

        # Mitglied aus dem Kurs entfernen
        meldung = kurs.mitglied_entfernen(self)

        # Kurs aus der Liste der gebuchten Kurse entfernen
        self.gebuchte_kurse.remove(kurs)

        # Erfolgsmeldung zurückgeben
        return meldung
    
    def geraet_reservieren(self, geraet)-> str:
        """Reserviert ein Geraet fuer das Mitglied"""
        # Pruefen, ob die Mitgliedschaft die Leistung erlaubt
        if not self.mitgliedschaft.hat_leistung("geraet_reservieren"):
            raise FitnessstudioException("Diese Mitgliedschaft erlaubt keine Geräte-Reservierung.")

        # Geraet reservieren
        meldung = geraet.reservieren(self)

        # Geraet in die Liste der reservierten Geraete aufnehmen
        if geraet not in self.reservierte_geraete:
            self.reservierte_geraete.append(geraet)

        # Erfolgsmeldung zurueckgeben
        return meldung
    
    def geraet_freigeben(self, geraet)-> str:
        """Gibt ein reserviertes Geraet wieder frei"""

        # Pruefen, ob das Geraet ueberhaupt reserviert wurde
        if geraet not in self.reservierte_geraete:
            raise FitnessstudioException("Dieses Gerät wurde nicht von diesem Mitglied reserviert.")

        # Geraet freigeben
        meldung = geraet.freigeben()

        # Geraet aus der Reservierungsliste entfernen
        self.reservierte_geraete.remove(geraet)

        # Erfolgsmeldung zurueckgeben
        return meldung
