# Zadanie 2: Bezpieczna aktualizacja słownika z rollbackiem przy błędzie
import copy

class BezpiecznaAktualizacja:
    def __init__(self, data: dict):
        self.data = data

    def __enter__(self):
        # TODO: zachowaj kopię słownika
        self._backup = ____________________
        return self.data

    def __exit__(self, typ, val, tb):
        if typ is not None:
            # TODO: przywróć stan słownika z kopii
            ________________________________
            return False
        return True

# Przykład:
if __name__ == "__main__":
    d = {"x": 1}
    try:
        with BezpiecznaAktualizacja(d) as dd:
            dd["y"] = 2
            raise RuntimeError("test")
    except RuntimeError:
        pass
    print(d)  # powinno być {'x': 1}
