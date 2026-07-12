"""
fitnessstudioexception.py

Eigene Exception-Klasse fuer Fehler im Fitnessstudio-System.
"""
class FitnessstudioException(Exception):
    """Diese Klasse beschreibt benutzerdefinierte Fehler im Fintnessstudio."""
    def __init__(self, message: str) -> None:
        # Die Basisklasse Exception speichert die Fehlermeldung ebenfalls.
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """Gibt die Fehlermeldung als Text zurueck."""
        return self.message
    
