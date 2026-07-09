"""
standort.py


Ein Standort verwaltet:
- Kurse
- Geraete
- Trainer
- Mitglieder
"""


class Standort:
    """
    Die Klasse Standort beschreibt ein einzelnes Fitnessstudio-Gebäude.
    """

    def __init__(self, name, adresse):
        # Name des Standortes, z. B. "Fitnessstudio Hanau"
        self.name = name

        # Adresse des Standortes
        self.adresse = adresse

        # Liste aller Kurse an diesem Standort
        self.kurse = []

        # Liste aller Geräte an diesem Standort
        self.geraete = []

        # Liste aller Trainer an diesem Standort
        self.trainer = []

        # Liste aller Mitglieder an diesem Standort
        # Wichtig: hier PLURAL benutzen, also mitglieder
        self.mitglieder = []

    def kurs_hinzufuegen(self, kurs):
        """
        Fügt einen Kurs zum Standort hinzu.
        """

        # Prüft, ob der Kurs noch nicht in der Liste ist
        if kurs not in self.kurse:
            self.kurse.append(kurs)

    def geraet_hinzufuegen(self, geraet):
        """
        Fügt ein Gerät zum Standort hinzu.
        """

        # Prüft, ob das Gerät noch nicht in der Liste ist
        if geraet not in self.geraete:
            self.geraete.append(geraet)

    def trainer_hinzufuegen(self, trainer):
        """
        Fügt einen Trainer zum Standort hinzu.
        """

        # Prüft, ob der Trainer noch nicht in der Liste ist
        if trainer not in self.trainer:
            self.trainer.append(trainer)

    def mitglied_hinzufuegen(self, mitglied):
        """
        Fügt ein Mitglied zum Standort hinzu.
        """

        # Prüft, ob das Mitglied noch nicht in der Liste ist
        if mitglied not in self.mitglieder:
            self.mitglieder.append(mitglied)

    def zeige_kurse(self):
        """
        Gibt alle Kurse des Standortes aus.
        """

        print("Kurse an diesem Standort:")

        for kurs in self.kurse:
            print("-", kurs.name)

    def zeige_geraete(self):
        """
        Gibt alle Geräte des Standortes aus.
        """

        print("Geräte an diesem Standort:")

        for geraet in self.geraete:
            print("-", geraet.name)

    def zeige_trainer(self):
        """
        Gibt alle Trainer des Standortes aus.
        """

        print("Trainer an diesem Standort:")

        for trainer in self.trainer:
            print("-", trainer.name)

    def zeige_mitglieder(self):
        """
        Gibt alle Mitglieder des Standortes aus.
        """

        print("Mitglieder an diesem Standort:")

        for mitglied in self.mitglieder:
            print("-", mitglied.name)

    def __str__(self):
        """
        Gibt eine kurze Beschreibung des Standortes zurück.
        """

        return f"Standort: {self.name}, Adresse: {self.adresse}"