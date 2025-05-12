# input_validation.py - Funkcje do walidacji danych wejściowych (np. daty)
# Zawiera walidację formatu i zakresu daty wyjazdu oraz inne funkcje walidujące.
import datetime
from .exceptions import TripError

def parse_date(date_str: str) -> datetime.date:
    """Parsuje tekstową datę w formacie RRRR-MM-DD do obiektu datetime.date.
    Zgłasza TripError, jeśli format jest niepoprawny lub data jest z przeszłości."""
    try:
        # Próba przetworzenia napisu daty w formacie RRRR-MM-DD
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        # Jeśli data nie pasuje do formatu, zgłoś wyjątek TripError z oryginalnym wyjątkiem (łańcuchowanie)
        raise TripError(f"Niepoprawny format daty '{date_str}'. Wprowadź w formacie RRRR-MM-DD.") from e
    # Sprawdzenie czy data nie jest wcześniejsza niż dzisiejsza
    if date < datetime.date.today():
        raise TripError("Data wyjazdu nie może być z przeszłości.")
    return date
