"""
main.py 

Startdatei des Fitnessstudio-Programms.

Hier werden Beispielobjekte erstellt und 
"""

from mitgliedschaft import Mitgliedschaft
from mitglied import Mitglied
from trainer import Trainer 
from kurs import Kurs 
from geraet import Geraet
from standort import Standort
from fitnessstudiokette import FitnessstudioKette
from fitnessstudioexception import FitnessstudioException

def main(): 

    print(" Fitnessstudio-Verwaltung")

    # Mitgliedschaften erstellen 
    basic= Mitgliedschaft("Basic", 15.99 )
    basic.erlaubte_leistungen=[]

    plus= Mitgliedschaft("Plus", 29.99)
    plus.erlaubte_leistungen=["kurs_buchen","geraet_reservieren"]

    # Mitglieder erstellen 
    mitglied1=Mitglied ("Max Mustermann", 22,"10.04.2002","015155555555","maxmust@gmail.de",1001,plus)

    mitglied2=Mitglied("Anna Schuhmacher",20,"05.07.2006","025635725637","annaschuh@web.de",1002,plus)

    mitglied3=Mitglied("Lisa Becker",20,"02.06.2006","01567342542","lisabecker@gmx.de",1003,basic)

    # Trainer erstellen
    trainer1=Trainer("Aileen Baum",34,"04.07.1992","015233425797","aileen@primeclub.de",101,"Yoga")

    trainer2=Trainer("Tom Müller", 25,"28.02.2001","0256745362879","tom@primeclub.de",102,"Extrem Spin Racing")

    # Kurs erstellen
    yoga=Kurs("Yoga",trainer1,15,"kurs_buchen")

    extremspinracing=Kurs("Extrem Spin Racing",trainer2,10,"kurs_buchen")

    trainer1.kurs_uebernehmen(yoga)
    trainer2.kurs_uebernehmen(extremspinracing)

    # Geraete erstellen 
    laufband=Geraet("Laufband",202)
    beinpresse=Geraet("Beinpresse",203)
    stairmaster=Geraet("Stairmaster",204)

    # Standort erstellen 
    standort1=Standort("PrimeClub","Goethestrasse 10")
    standort2=Standort("PrimeClub Mannheim","Maximilianstrasse 20")

    #Zuordnung der Testdaten
    standort1.trainer_hinzufuegen(trainer1)
    standort2.trainer_hinzufuegen(trainer2)

    standort1.mitglied_hinzufuegen(mitglied1)
    standort1.mitglied_hinzufuegen(mitglied3)
    standort2.mitglied_hinzufuegen(mitglied2)

    standort1.kurs_hinzufuegen(yoga)
    standort2.kurs_hinzufuegen(extremspinracing)

    standort1.geraet_hinzufuegen(laufband)
    standort2.geraet_hinzufuegen(beinpresse)
    standort2.geraet_hinzufuegen(stairmaster)

    # Fitnessstudio-Kette
    kette=FitnessstudioKette("PrimeClub")
    kette.standort_hinzufuegen(standort1)
    kette.standort_hinzufuegen(standort2)

    print("Standorte: ")
    kette.zeige_alle_standorte()

    print("Kursbuchungen: ")

    try:
        # Mitglied 1 bucht den Yoga-Kurs
        print(mitglied1.kurs_buchen(yoga))

        # Mitglied 2 bucht den Kurs "Extrem Spin Racing"
        print(mitglied2.kurs_buchen(extremspinracing))

    except FitnessstudioException as fehler: 
        print("Fehler: ", fehler)

    # Teilnehmer im Yoga Kurs anzeigen

    print("Teilnehmer im Yoga-Kurs: ")
    for teilnehmer in yoga.teilnehmer:
        print("-", teilnehmer.name)

    # Teilnehmer des zweiten Kurses anzeigen
    print("Teilnehmer im Kurs 'Extrem Spin Racing':")

    for teilnehmer in extremspinracing.teilnehmer:
        print("-", teilnehmer.name)

    #Fehlerfall testen 
    print("Nicht erlaubte Kursbuchung: ")
    try: 
        print(mitglied3.kurs_buchen(yoga))
    
    except FitnessstudioException as fehler:
        print("Fehler: ",fehler)

    #Geraetereservierung testen
    print("Geratereservierung: ")
    
    try:
        # Mitglied reserviert eein Laufband 
        print(mitglied1.geraet_reservieren(laufband))

        # Zweites Mitglied reserviert die Beinpresse
        print(mitglied2.geraet_reservieren(beinpresse))

    except FitnessstudioException as fehler:
        print("Fehler:", fehler)

    # Geraet wird wieder freigegeben
    try:
        # Mitglied gibt das Laufband wieder frei
        print(mitglied1.geraet_freigeben(laufband))

    except FitnessstudioException as fehler:
        print("Fehler:", fehler)

 
    # Wartungsmodus testen
    print("Geraet in Wartung setzen: ")
    
    try:
        #Stairmaster wird in Wartung gesetzt
        print(stairmaster.wartung_starten())

        #Status des Geraets ausgeben
        print(stairmaster)

    except FitnessstudioException as fehler:
         print("Fehler:", fehler)

    # Mitglieds Daten anzteigen
    print("Mitgliedsdaten:")

    mitglied1.daten_anzeigen()
    mitglied2.daten_anzeigen()
    mitglied3.daten_anzeigen()

    # Programmende
    print("Programm erfolgreich beendet.")


# Startpunkt des Programms
if __name__ == "__main__":
    main()