"""
fitnessstudioexception.py

Eigene Exception-Klasse fuer Fehler im Fitnessstudio-System.
"""
class FitnessstudioException(Exception): 
    """Diese Klasse beschreibt benutzerdefinierte Fehler im Fintnessstudio."""
    def __init__( self,message ):
        # Fehlermeldung wird gespeichert. 
        self.message= message

    def __str__(self):
        """Gibt die Fehlermeldung als Text zurueck."""
        return self.message 
    