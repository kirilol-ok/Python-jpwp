# context.py - Kontekstowe zarządzanie zasobami (np. operacje na plikach z mechanizmem rollback)
# Definiuje menedżera kontekstu do bezpiecznego zapisu danych do pliku z możliwością przywrócenia poprzedniej zawartości w razie błędu.

import os
import logging
logger = logging.getLogger("trip_app")

class FileTransaction:
    """Menedżer kontekstu dla operacji zapisu pliku z obsługą rollback w przypadku błędów."""
    def __init__(self, filename: str):
        self.filename = filename
        self.backup_path = None
        self.file = None

    def __enter__(self):
        # Jeżeli plik istnieje, tworzymy kopię zapasową
        if os.path.exists(self.filename):
            self.backup_path = self.filename + ".bak"
            try:
                # Kopia zapasowa istniejącego pliku (zmiana nazwy pliku na *.bak)
                os.replace(self.filename, self.backup_path)
            except Exception as e:
                logger.error("Nie udało się utworzyć kopii zapasowej pliku.", exc_info=True)
                raise
        # Otwieramy plik do zapisu (tworząc nowy lub nadpisując istniejący)
        try:
            self.file = open(self.filename, 'w', encoding='utf-8')
        except Exception as e:
            # Jeżeli otwarcie pliku nie powiodło się, przywróć kopię i przekaż wyjątek dalej
            if self.backup_path and os.path.exists(self.backup_path):
                try:
                    os.replace(self.backup_path, self.filename)
                except Exception as re:
                    logger.error("Nie udało się przywrócić pliku z kopii zapasowej.", exc_info=True)
            raise  # ponownie zgłaszamy wyjątek (będzie obsłużony wyżej)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Zamykamy plik jeśli jest otwarty
        if self.file:
            try:
                self.file.close()
            except Exception as e:
                logger.error("Błąd przy zamykaniu pliku.", exc_info=True)
        # Jeśli wystąpił wyjątek w bloku with:
        if exc_type is not None:
            # Przywracamy oryginalny plik z kopii zapasowej, jeśli istniał
            if self.backup_path:
                try:
                    os.replace(self.backup_path, self.filename)
                    logger.error("Wystąpił błąd podczas zapisu - przywrócono poprzednią wersję pliku.")
                except Exception as e:
                    logger.error("Nie udało się przywrócić poprzedniej wersji pliku!", exc_info=True)
            else:
                # Plik był nowy (nie istniał przed zapisem) -> usuwamy niedokończony plik
                try:
                    os.remove(self.filename)
                except OSError:
                    pass
        else:
            # Jeśli wyjątku nie było, usuwamy kopię zapasową (zapis zakończony pomyślnie)
            if self.backup_path:
                try:
                    os.remove(self.backup_path)
                except OSError:
                    pass
        # False -> nie tłumi wyjątku; jeśli wystąpił, zostanie propagowany dalej
        return False
