"""
kurs.py


Ein Kurs hat:
- einen Namen
- einen Trainer
- eine maximale Teilnehmerzahl
- eine Teilnehmerliste
- eine Warteliste
- eine benoetigte Leistung, z. B. "kurs_buchen"

"""

from fitnessstudioexception import FitnessstudioException


class Kurs:
    """
    Die Klasse Kurs beschreibt einen Fitnesskurs.

    Beispiel:
    yoga = Kurs("Yoga", trainer1, 10, "kurs_buchen")
    """

    def __init__(
        self,
        name: str,
        trainer=None,
        max_teilnehmer: int = 10,
        benoetigte_leistung: str = "kurs_buchen",
    ) -> None:
        if max_teilnehmer <= 0:
            raise FitnessstudioException(
                "Die maximale Teilnehmerzahl muss groesser als 0 sein."
            )
        # Name des Kurses, z. B. "Yoga"
        self.name = name

        # Trainer-Objekt, das den Kurs leitet
        self.trainer = trainer

        # Maximale Anzahl der Mitglieder im Kurs
        self.max_teilnehmer = max_teilnehmer

        # Liste mit Mitgliedern, die schon im Kurs sind
        self.teilnehmer = []

        # Liste mit Mitgliedern, die warten muessen, wenn der Kurs voll ist
        self.warteliste = []

        # Welche Leistung die Mitgliedschaft erlauben muss
        self.benoetigte_leistung = benoetigte_leistung

    def platz_verfuegbar(self) -> bool:
        """
        Prueft, ob im Kurs noch ein Platz frei ist.

        Rueckgabe:
        True  -> Es gibt noch freie Plaetze.
        False -> Der Kurs ist voll.
        """
        return len(self.teilnehmer) < self.max_teilnehmer

    def mitglied_hinzufuegen(self, mitglied)-> str:
        """
        Fuegt ein Mitglied zum Kurs hinzu.

        Wenn der Kurs voll ist, wird das Mitglied nicht direkt eingetragen,
        sondern auf die Warteliste gesetzt.

        Wenn das Mitglied schon im Kurs ist, wird eine Exception ausgeloest.
        """

        # Pruefen, ob das Mitglied bereits im Kurs eingetragen ist
        if mitglied in self.teilnehmer:
            raise FitnessstudioException("Das Mitglied ist bereits fuer diesen Kurs angemeldet.")

        # Pruefen, ob das Mitglied bereits auf der Warteliste steht
        if mitglied in self.warteliste:
            raise FitnessstudioException("Das Mitglied steht bereits auf der Warteliste.")

        # Wenn Platz frei ist, Mitglied in Teilnehmerliste eintragen
        if self.platz_verfuegbar():
            self.teilnehmer.append(mitglied)
            return f"{mitglied.name} wurde zum Kurs {self.name} hinzugefuegt."

        # Wenn kein Platz frei ist, Mitglied auf Warteliste setzen
        self.warteliste_hinzufuegen(mitglied)
        return f"Der Kurs {self.name} ist voll. {mitglied.name} wurde auf die Warteliste gesetzt."

    def mitglied_entfernen(self, mitglied)-> str:
        """
        Entfernt ein Mitglied aus dem Kurs.

        Wenn danach jemand auf der Warteliste steht,
        rueckt die erste Person von der Warteliste automatisch nach.
        """

        # Pruefen, ob das Mitglied ueberhaupt im Kurs ist
        if mitglied not in self.teilnehmer:
            raise FitnessstudioException("Das Mitglied ist nicht in diesem Kurs angemeldet.")

        # Mitglied aus Teilnehmerliste entfernen
        self.teilnehmer.remove(mitglied)

        # Wenn die Warteliste nicht leer ist, rueckt die erste Person nach
        if len(self.warteliste) > 0:
            naechstes_mitglied = self.warteliste.pop(0)
            self.teilnehmer.append(naechstes_mitglied)

            # Auch die persönliche Kursliste des nachgerückten Mitglieds
            # muss aktualisiert werden. Sonst wären die Daten widersprüchlich.
            if self not in naechstes_mitglied.gebuchte_kurse:
                naechstes_mitglied.gebuchte_kurse.append(self)

        return f"{mitglied.name} wurde aus dem Kurs {self.name} entfernt."

    def warteliste_hinzufuegen(self, mitglied)-> None:
        """
        Fuegt ein Mitglied zur Warteliste hinzu.
        """

        # Doppelte Eintraege vermeiden
        if mitglied in self.warteliste:
            raise FitnessstudioException("Das Mitglied steht bereits auf der Warteliste.")

        self.warteliste.append(mitglied)

    def __str__(self)-> str:
        """
        Gibt eine kurze Beschreibung des Kurses zurueck.
        """
        return f"Kurs: {self.name}, Plaetze: {len(self.teilnehmer)}/{self.max_teilnehmer}"
