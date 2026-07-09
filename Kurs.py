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

try:
    # Diese Exception-Datei soll Person 1 erstellen.
    from fitnessstudioexception import FitnessstudioException
except ImportError:
    # Falls die Datei exceptions.py noch nicht existiert,
    # kann diese Datei trotzdem getestet werden.
    class FitnessstudioException(Exception):
        pass


class Kurs:
    """
    Die Klasse Kurs beschreibt einen Fitnesskurs.

    Beispiel:
    yoga = Kurs("Yoga", trainer1, 10, "kurs_buchen")
    """

    def __init__(self, name, trainer=None, max_teilnehmer=10, benoetigte_leistung="kurs_buchen"):
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

    def platz_verfuegbar(self):
        """
        Prueft, ob im Kurs noch ein Platz frei ist.

        Rueckgabe:
        True  -> Es gibt noch freie Plaetze.
        False -> Der Kurs ist voll.
        """
        return len(self.teilnehmer) < self.max_teilnehmer

    def mitglied_hinzufuegen(self, mitglied):
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

    def mitglied_entfernen(self, mitglied):
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

        return f"{mitglied.name} wurde aus dem Kurs {self.name} entfernt."

    def warteliste_hinzufuegen(self, mitglied):
        """
        Fuegt ein Mitglied zur Warteliste hinzu.
        """

        # Doppelte Eintraege vermeiden
        if mitglied in self.warteliste:
            raise FitnessstudioException("Das Mitglied steht bereits auf der Warteliste.")

        self.warteliste.append(mitglied)

    def __str__(self):
        """
        Gibt eine kurze Beschreibung des Kurses zurueck.
        """
        return f"Kurs: {self.name}, Plaetze: {len(self.teilnehmer)}/{self.max_teilnehmer}"
