"""Automatisierte Tests fuer das Fitnessstudio-Projekt.

Die Tests pruefen sowohl erfolgreiche Standardablaeufe als auch wichtige
Fehlerfaelle. Sie verwenden nur das in Python enthaltene Modul ``unittest``.
"""

import unittest

from fitnessstudioexception import FitnessstudioException
from fitnessstudiokette import FitnessstudioKette
from geraet import Geraet
from kurs import Kurs
from mitglied import Mitglied
from mitgliedschaft import Mitgliedschaft
from standort import Standort
from trainer import Trainer


class FitnessstudioTest(unittest.TestCase):
    """Testet die wichtigsten Funktionen des Fitnessstudio-Systems."""

    def setUp(self) -> None:
        """Erstellt vor jedem Test neue und voneinander unabhängige Objekte."""

        self.basic = Mitgliedschaft("Basic", 15.99)
        self.plus = Mitgliedschaft(
            "Plus",
            29.99,
            ["kurs_buchen", "geraet_reservieren"],
        )

        self.mitglied1 = Mitglied(
            "Max Mustermann",
            22,
            "10.04.2002",
            "015100000001",
            "max@example.de",
            1001,
            self.plus,
        )
        self.mitglied2 = Mitglied(
            "Anna Musterfrau",
            21,
            "05.07.2003",
            "015100000002",
            "anna@example.de",
            1002,
            self.plus,
        )
        self.basic_mitglied = Mitglied(
            "Lisa Beispiel",
            20,
            "02.06.2004",
            "015100000003",
            "lisa@example.de",
            1003,
            self.basic,
        )

        self.trainer = Trainer(
            "Aileen Baum",
            34,
            "04.07.1992",
            "015200000001",
            "aileen@example.de",
            101,
            "Yoga",
        )
        self.kurs = Kurs("Yoga", self.trainer, 1, "kurs_buchen")
        self.geraet = Geraet("Laufband", 202)

    def test_mitgliedschaft_prueft_erlaubte_leistung(self) -> None:
        """Plus erlaubt Buchungen, Basic dagegen nicht."""

        self.assertTrue(self.plus.hat_leistung("kurs_buchen"))
        self.assertFalse(self.basic.hat_leistung("kurs_buchen"))

    def test_kursbuchung_traegt_mitglied_auf_beiden_seiten_ein(self) -> None:
        """Kurs und Mitglied muessen dieselbe Buchung speichern."""

        self.mitglied1.kurs_buchen(self.kurs)

        self.assertIn(self.mitglied1, self.kurs.teilnehmer)
        self.assertIn(self.kurs, self.mitglied1.gebuchte_kurse)

    def test_doppelte_kursbuchung_wird_verhindert(self) -> None:
        """Ein Mitglied darf nicht zweimal denselben Kurs buchen."""

        self.mitglied1.kurs_buchen(self.kurs)

        with self.assertRaises(FitnessstudioException):
            self.mitglied1.kurs_buchen(self.kurs)

    def test_voller_kurs_verwendet_warteliste(self) -> None:
        """Das zweite Mitglied kommt bei einem vollen Kurs auf die Warteliste."""

        self.mitglied1.kurs_buchen(self.kurs)
        self.mitglied2.kurs_buchen(self.kurs)

        self.assertIn(self.mitglied2, self.kurs.warteliste)
        self.assertNotIn(self.mitglied2, self.kurs.teilnehmer)

    def test_warteliste_rueckt_nach_stornierung_nach(self) -> None:
        """Die erste Person der Warteliste erhaelt den frei gewordenen Platz."""

        self.mitglied1.kurs_buchen(self.kurs)
        self.mitglied2.kurs_buchen(self.kurs)
        self.mitglied1.kurs_stornieren(self.kurs)

        self.assertIn(self.mitglied2, self.kurs.teilnehmer)
        self.assertNotIn(self.mitglied2, self.kurs.warteliste)
        self.assertIn(self.kurs, self.mitglied2.gebuchte_kurse)

    def test_mitgliedschaft_ohne_recht_kann_kurs_nicht_buchen(self) -> None:
        """Eine Basic-Mitgliedschaft ohne Kursrecht wird abgelehnt."""

        with self.assertRaises(FitnessstudioException):
            self.basic_mitglied.kurs_buchen(self.kurs)

    def test_ungueltige_kursgroesse_wird_abgelehnt(self) -> None:
        """Ein Kurs muss mindestens einen Platz besitzen."""

        with self.assertRaises(FitnessstudioException):
            Kurs("Ungueltiger Kurs", max_teilnehmer=0)

    def test_geraet_kann_reserviert_und_freigegeben_werden(self) -> None:
        """Eine normale Reservierung veraendert den Geraetestatus korrekt."""

        self.mitglied1.geraet_reservieren(self.geraet)
        self.assertEqual(self.geraet.status, "reserviert")
        self.assertIs(self.geraet.reserviert_von, self.mitglied1)

        self.mitglied1.geraet_freigeben(self.geraet)
        self.assertTrue(self.geraet.ist_verfuegbar())
        self.assertIsNone(self.geraet.reserviert_von)

    def test_doppelreservierung_wird_verhindert(self) -> None:
        """Ein bereits reserviertes Geraet darf nicht erneut reserviert werden."""

        self.mitglied1.geraet_reservieren(self.geraet)

        with self.assertRaises(FitnessstudioException):
            self.mitglied2.geraet_reservieren(self.geraet)

    def test_geraet_in_wartung_kann_nicht_reserviert_werden(self) -> None:
        """Ein Geraet im Wartungsmodus ist nicht verfuegbar."""

        self.geraet.wartung_starten()

        with self.assertRaises(FitnessstudioException):
            self.mitglied1.geraet_reservieren(self.geraet)

    def test_standort_verhindert_doppelte_eintraege(self) -> None:
        """Dasselbe Objekt wird nur einmal in einem Standort gespeichert."""

        standort = Standort("PrimeClub", "Goethestrasse 10")
        standort.kurs_hinzufuegen(self.kurs)
        standort.kurs_hinzufuegen(self.kurs)

        self.assertEqual(len(standort.kurse), 1)

    def test_fitnessstudiokette_findet_standort(self) -> None:
        """Die Kette findet vorhandene Standorte und liefert sonst None."""

        standort = Standort("PrimeClub", "Goethestrasse 10")
        kette = FitnessstudioKette("PrimeClub")
        kette.standort_hinzufuegen(standort)

        self.assertIs(kette.suche_standort("PrimeClub"), standort)
        self.assertIsNone(kette.suche_standort("Unbekannt"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
