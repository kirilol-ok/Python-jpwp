# api.py - Symulacja zewnętrznego API (np. geokodowania adresu) i obsługa potencjalnych wyjątków sieciowych.
# Tutaj zaimplementowano funkcję geocode, która próbuje "zgeokodować" adres i ilustruje obsługę błędów sieciowych.

import logging
logger = logging.getLogger("trip_app")
from .exceptions import TripError

def geocode(address: str):
    """Symuluje geokodowanie adresu. Zwraca współrzędne (szerokość, długość) lub zgłasza TripError w przypadku błędu sieciowego."""
    logger.info(f"Geokodowanie adresu: {address}")
    # Symulacja: jeśli adres zawiera słowo 'invalid' lub 'fail', symuluj błąd połączenia
    if "invalid" in address.lower() or "fail" in address.lower():
        try:
            # Symulacja wyjątku połączenia (np. requests.ConnectionError)
            raise ConnectionError("Symulowany błąd połączenia przy geokodowaniu")
        except ConnectionError as e:
            # Logujemy szczegóły oryginalnego wyjątku
            logger.error("Błąd sieci przy geokodowaniu adresu.", exc_info=True)
            # Zgłaszamy własny wyjątek aplikacji z dołączeniem oryginalnego (łańcuchowanie)
            raise TripError("Nie udało się połączyć z usługą geokodowania") from e
    # W przypadku "poprawnego" adresu, zwróćmy fikcyjne współrzędne
    return (50.06143, 19.93658)  # np. współrzędne Krakowa
