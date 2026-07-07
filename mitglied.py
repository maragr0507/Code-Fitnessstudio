from person import Person
class Mitglied (Person):
    def __init__(self,name, alter,geburtdatum,telefon,email, mitgliedsnummer, mitgliedschaft, gebuchte_kurse,reservierte_geraete):
        super().__init__(name,alter,geburtdatum,telefon,email )

        self.mitliedsnummer=mitgliedsnummer
        self.mitgliedschaft=mitgliedschaft
        #"""Ein Mitglied kann mehrere Kurse buchen und mehrere Geräte reservieren. Dafür eignet sich eine Liste."""
        self.gebuchte_kurse = []
        self.reservierte_geraete = []

    def kurs_buchen(self,kurs):
            self.gebuchte_kurse.append(kurs)
    def kurs_stornieren(self, kurs):
            self.gebuchte_kurse.remove(kurs)
    def geraet_reservieren(self, geraet):
            self.reservierte_geraete.append(geraet)
    def geraet_freigeben(self, geraet):
            self.reservierte_geraet.remove(geraet)

