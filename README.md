# Fitnessstudio-Kette in Python

Dieses Projekt simuliert die Verwaltung einer Fitnessstudio-Kette mit mehreren
Standorten. Mitglieder können Kurse buchen und Geräte reservieren. Das System
prüft dabei unter anderem Mitgliedschaftsrechte, freie Kursplätze,
Wartelistenplätze und den Status der Geräte.

## Funktionen

- Verwaltung mehrerer Fitnessstudio-Standorte
- Verwaltung von Mitgliedern, Trainern, Kursen und Geräten
- Mitgliedschaften mit unterschiedlichen Leistungen
- Kursbuchung mit begrenzter Teilnehmerzahl
- automatische Warteliste bei einem vollen Kurs
- automatisches Nachrücken nach einer Stornierung
- Reservierung und Freigabe von Geräten
- Wartungsmodus für Geräte
- eigene Exceptions für ungültige Aktionen
- automatisierte Tests für normale Abläufe und Fehlerfälle

## Projektstruktur

| Datei | Aufgabe |
|---|---|
| `person.py` | gemeinsame Personendaten |
| `mitglied.py` | Kursbuchungen und Gerätereservierungen |
| `trainer.py` | Verwaltung der betreuten Kurse |
| `mitgliedschaft.py` | Prüfung erlaubter Leistungen |
| `kurs.py` | Teilnehmer und Warteliste |
| `geraet.py` | Reservierung und Wartungsstatus |
| `standort.py` | Verwaltung eines einzelnen Standorts |
| `fitnessstudiokette.py` | Verwaltung aller Standorte |
| `fitnessstudioexception.py` | eigene Fehlerklasse |
| `main.py` | ausführbares Beispielprogramm |
| `test_fitnessstudio.py` | automatisierte Tests |

## Voraussetzungen

- Python 3.10 oder neuer
- keine externen Python-Pakete erforderlich

## Installation

Repository herunterladen oder klonen und anschließend in den Projektordner
wechseln:

```bash
git clone <GITHUB-LINK-DES-PROJEKTS>
cd Code-Fitnessstudio
```

Optional kann die `requirements.txt` ausgeführt werden. Da das Projekt keine
externen Pakete benötigt, wird dabei nichts zusätzlich installiert:

```bash
python3 -m pip install -r requirements.txt
```

## Programm starten

```bash
python3 main.py
```

Das Beispielprogramm erstellt zwei Standorte, drei Mitglieder, zwei Trainer,
zwei Kurse und drei Geräte. Danach werden erfolgreiche Aktionen und bewusst
ausgelöste Fehlerfälle demonstriert.

## Automatisierte Tests starten

```bash
python3 -m unittest -v
```

Alternativ kann nur die Testdatei ausgeführt werden:

```bash
python3 test_fitnessstudio.py
```

Bei erfolgreicher Ausführung erscheint am Ende:

```text
Ran 12 tests
OK
```

## Wichtige Testfälle

- erfolgreiche Kursbuchung
- doppelte Kursbuchung
- voller Kurs und Warteliste
- automatisches Nachrücken
- fehlende Mitgliedschaftsrechte
- erfolgreiche Gerätereservierung
- Doppelreservierung
- Gerät im Wartungsmodus
- ungültige maximale Teilnehmerzahl
- Standortverwaltung und Standortsuche

## Verwendete Python-Prinzipien

- objektorientierte Programmierung
- Vererbung: `Person` wird von `Mitglied` und `Trainer` erweitert
- klare Verantwortlichkeit jeder Klasse
- Type Hints
- Docstrings und erklärende Kommentare
- eigene Exception-Klasse
- aussagekräftige Variablen- und Methodennamen
- automatisierte Tests mit `unittest`
