"""
fitnessstudio_kette.py
Die FitnessstudioKette ist die oberste Verwaltung.
Sie enthaelt mehrere Standorte.
"""


class FitnessstudioKette:
    """
    Die Klasse FitnessstudioKette beschreibt die gesamte Fitnessstudio-Kette.

    Beispiel:
    kette = FitnessstudioKette("FitPlus")
    """

    def __init__(self, name):
        # Name der Fitnessstudio-Kette
        self.name = name

        # Liste aller Standorte
        self.standorte = []

    def standort_hinzufuegen(self, standort):
        """
        Fuegt einen Standort zur Fitnessstudio-Kette hinzu.
        """

        # Doppelte Standorte vermeiden
        if standort not in self.standorte:
            self.standorte.append(standort)

    def zeige_alle_standorte(self):
        """
        Gibt alle Standorte als Liste von Namen zurueck.
        """

        standortnamen = []

        for standort in self.standorte:
            standortnamen.append(standort.name)

        return standortnamen

    def suche_standort(self, name):
        """
        Sucht einen Standort nach seinem Namen.

        Rueckgabe:
        - Standort-Objekt, wenn der Standort gefunden wurde
        - None, wenn kein Standort gefunden wurde
        """

        for standort in self.standorte:
            if standort.name == name:
                return standort

        return None

    def __str__(self):
        """
        Gibt eine kurze Beschreibung der Fitnessstudio-Kette zurueck.
        """
        return f"Fitnessstudio-Kette: {self.name}, Anzahl Standorte: {len(self.standorte)}"
