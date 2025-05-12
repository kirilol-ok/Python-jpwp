# trip.py - Definicje klas i logiki biznesowej dla wyjazdu grupowego (Trip, Participant)
# Klasa Trip przechowuje informacje o wyjeździe i uczestnikach oraz zapewnia metody do modyfikacji tych danych z odpowiednią walidacją.

from .exceptions import TripError, ParticipantExistsError, ParticipantNotFoundError
from .input_validation import parse_date

class Trip:
    """Reprezentuje wyjazd grupowy z listą uczestników."""
    def __init__(self, destination: str, date):
        self.destination = destination
        self.date = date  # oczekujemy obiektu datetime.date
        self.participants = []  # lista słowników z kluczami 'name' i 'email'
    
    def add_participant(self, name: str, email: str):
        """Dodaje uczestnika do wyjazdu.
        Zgłasza ParticipantExistsError, jeśli uczestnik o podanym email już jest na liście."""
        # Sprawdzamy duplikat po adresie email (ignorujemy wielkość liter)
        for p in self.participants:
            if p['email'].lower() == email.lower():
                # Znaleziono uczestnika o takim samym email
                raise ParticipantExistsError(f"Uczestnik o email '{email}' już istnieje na liście.")
        # Jeśli nie ma duplikatu, dodajemy do listy
        self.participants.append({'name': name, 'email': email})
    
    def remove_participant(self, email: str):
        """Usuwa uczestnika o podanym email z listy uczestników.
        Zgłasza ParticipantNotFoundError, jeśli takiego uczestnika nie ma na liście."""
        for p in self.participants:
            if p['email'].lower() == email.lower():
                self.participants.remove(p)
                return
        # Jeśli nie znaleziono uczestnika, zgłoś wyjątek
        raise ParticipantNotFoundError(f"Nie znaleziono uczestnika o email: {email}")
    
    def to_dict(self):
        """Zwraca słownik z danymi wyjazdu do łatwego zapisania (np. do pliku JSON)."""
        return {
            'destination': self.destination,
            'date': self.date.strftime("%Y-%m-%d"),  # zapisujemy datę jako tekst
            'participants': list(self.participants)   # lista uczestników (kopiujemy listę słowników)
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Tworzy instancję Trip na podstawie słownika (np. odczytanego z pliku JSON)."""
        dest = data.get('destination')
        date_str = data.get('date')
        participants = data.get('participants', [])
        if not dest or not date_str:
            # Brak kluczowych danych wyjazdu
            raise TripError("Brak wymaganych informacji o wyjeździe w danych.")
        # Walidacja i konwersja daty (parse_date może zgłosić TripError)
        date = parse_date(date_str)
        trip = cls(dest, date)
        # Dodaj uczestników z listy (zakładamy brak duplikatów w danych wejściowych)
        for p in participants:
            try:
                trip.add_participant(p['name'], p['email'])
            except ParticipantExistsError:
                # Jeśli duplikat jednak wystąpi (np. błędne dane), pomijamy go
                continue
        return trip
