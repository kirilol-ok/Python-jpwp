# input_validation.py - Funkcje do walidacji danych wejściowych (np. daty)

import datetime
import re
from .exceptions import TripError, DateError, EmailError


def parse_date(date_str: str) -> datetime.date:
    """Parsuje tekstową datę w formacie RRRR-MM-DD do obiektu datetime.date.
    Zgłasza TripError, jeśli format jest niepoprawny lub data jest z przeszłości."""
    try:
        # Próba przetworzenia napisu daty w formacie RRRR-MM-DD
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise DateError(f"Niepoprawny format daty '{date_str}'. Wprowadź w formacie RRRR-MM-DD.") from e
    if date < datetime.date.today():
        raise DateError("Data wyjazdu nie może być z przeszłości.")
    return date

def email_validate(email):
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.fullmatch(pattern, email):
        raise EmailError("Niepoprawny format adresu email.")
    return email


