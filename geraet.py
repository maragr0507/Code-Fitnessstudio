"""
geraet.py



Ein Geraet kann drei Status haben:
- "verfuegbar"
- "reserviert"
- "in_wartung"
"""

try:
    # Diese Exception-Datei soll Person 1 erstellen.
    from fitnessstudioexception import FitnessstudioException
except ImportError:
    # Falls exceptions.py noch nicht existiert,
    # kann diese Datei trotzdem einzeln getestet werden.
    class FitnessstudioException(Exception):
        pass


class Geraet:
    """
    Die Klasse Geraet beschreibt ein Fitnessgeraet.

    Beispiel:
    laufband = Geraet("Laufband", 101)
    """

    def __init__(self, name: str, geraetenummer: int)-> None:
        # Name des Geraets, z. B. "Laufband"
        self.name = name

        # Eindeutige Nummer des Geraets
        self.geraetenummer = geraetenummer

        # Startstatus: Das Geraet ist verfuegbar
        self.status = "verfuegbar"

        # Hier wird gespeichert, welches Mitglied das Geraet reserviert hat
        self.reserviert_von = None

    def ist_verfuegbar(self)-> bool:
        """
        Prueft, ob das Geraet verfuegbar ist.

        Rueckgabe:
        True  -> Geraet kann reserviert werden.
        False -> Geraet ist reserviert oder in Wartung.
        """
        return self.status == "verfuegbar"

    def reservieren(self, mitglied)-> str:
        """
        Reserviert das Geraet fuer ein Mitglied.

        Wenn das Geraet schon reserviert ist oder in Wartung ist,
        wird eine Exception ausgeloest.
        """

        # Geraet ist bereits reserviert
        if self.status == "reserviert":
            raise FitnessstudioException("Das Geraet ist bereits reserviert.")

        # Geraet ist in Wartung
        if self.status == "in_wartung":
            raise FitnessstudioException("Das Geraet befindet sich in Wartung.")

        # Geraet reservieren
        self.status = "reserviert"
        self.reserviert_von = mitglied

        return f"{self.name} wurde fuer {mitglied.name} reserviert."

    def freigeben(self)-> str:
        """
        Gibt ein reserviertes Geraet wieder frei.
        """

        # Nur reservierte Geraete koennen freigegeben werden
        if self.status != "reserviert":
            raise FitnessstudioException("Das Geraet ist aktuell nicht reserviert.")

        # Reservierung loeschen
        self.status = "verfuegbar"
        self.reserviert_von = None

        return f"{self.name} ist wieder verfuegbar."

    def wartung_starten(self)-> str:
        """
        Setzt das Geraet in Wartung.

        In Wartung darf das Geraet nicht reserviert werden.
        """

        # Ein reserviertes Geraet sollte zuerst freigegeben werden
        if self.status == "reserviert":
            raise FitnessstudioException("Ein reserviertes Geraet kann nicht direkt in Wartung gesetzt werden.")

        self.status = "in_wartung"
        self.reserviert_von = None

        return f"{self.name} ist jetzt in Wartung."

    def wartung_beenden(self)-> str:
        """
        Beendet die Wartung und macht das Geraet wieder verfuegbar.
        """

        # Pruefen, ob das Geraet wirklich in Wartung ist
        if self.status != "in_wartung":
            raise FitnessstudioException("Das Geraet befindet sich nicht in Wartung.")

        self.status = "verfuegbar"

        return f"{self.name} ist wieder verfuegbar."

    def __str__(self)-> str:
        """
        Gibt eine kurze Beschreibung des Geraets zurueck.
        """
        return f"Geraet: {self.name}, Nummer: {self.geraetenummer}, Status: {self.status}"
