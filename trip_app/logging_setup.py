# logging_setup.py - Konfiguracja logowania dla aplikacji
# Tworzy logger zapisujący logi do pliku i na konsolę z odpowiednimi poziomami szczegółowości.
import logging

def setup_logging(log_file: str = "app.log") -> logging.Logger:
    """Konfiguruje logger aplikacji zapisujący logi do pliku (DEBUG) i na konsolę (INFO)."""
    logger = logging.getLogger("trip_app")
    logger.setLevel(logging.DEBUG)
    # Ustawienie formatu logów
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    # Handler do pliku - zapisuje wszystkie poziomy logów
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    # Handler do konsoli - wypisuje logi od poziomu INFO wzwyż
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    # Dodanie handlerów do loggera
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # Wyłączenie propagacji do domyślnego loggera root
    logger.propagate = False
    return logger
