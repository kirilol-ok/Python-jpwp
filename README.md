# README.md – Przewodnik po zadaniach “Zaawansowana obsługa wyjątków i debugowanie”

W tym repozytorium znajdziesz pięć ćwiczeń w formie “uzupełnij kod”. Każde zadanie koncentruje się na innym aspekcie zaawansowanej obsługi wyjątków i debugowania w Pythonie.

## Jak korzystać z zadań

1. **Przejdź do katalogu `tasks/`**:
   ```bash
   cd project_root/Zadania
   ```
2. **Otwórz wybrane zadanie** w edytorze i przeanalizuj komentarz na początku pliku – opisuje cel ćwiczenia.
3. **W miejscach oznaczonych `# TODO`** dopisz brakujące fragmenty kodu.
4. **Testuj działanie** każdego skryptu uruchamiając go bezpośrednio z Pythona:

   ```bash
   python zadanie_X.py
   ```

   gdzie `X` to numer zadania od 1 do 5.

## Opis poszczególnych zadań

### Task 1 – Łańcuchowanie wyjątków

* **Plik:** `zadanie_1.py`
* **Cel:** Po złapaniu `FileNotFoundError` lub `JSONDecodeError` zgłosić własny wyjątek `BladDanych`, używając `raise ... from ...`.

### Task 2 – Bezpieczna aktualizacja listy

* **Plik:** `zadanie_2.py`
* **Cel:** Za pomocą kontekstowego menedżera `BezpiecznaLista` zrobić rollback listy do stanu wyjściowego w razie wystąpienia wyjątku.

### Task 3 – Dekorator @bezpiecznie_loguj

* **Plik:** `zadanie_3.py`
* **Cel:** Stworzyć dekorator `@bezpiecznie_loguj`, który przechwytuje wyjątki z dekorowanej funkcji, loguje pełny traceback przez `logger.exception(...)` i ponownie rzuca wyjątek.

### Task 4 – Ostrzeżenia zamiast wyjątków

* **Plik:** `zadanie_4.py`
* **Cel:** W razie niekrytycznego błędu (np. liczba < 0) wywołać `warnings.warn(...)`, nie przerywając programu.

### Task 5 – Punkt zaczepienia debuggera

* **Plik:** `zadanie_5.py`
* **Cel:** W zależności od flagi `DEBUG` wstawić `pdb.set_trace()` w funkcji, aby zatrzymać wykonanie i debugować.

## Wskazówki

* Zapoznaj się z dokumentacją modułów: `json`, `warnings`, `logging`, `pdb`.
* Uruchamiaj zadania jedno po drugim, by obserwować efekty w miejscu TODO.
* Sprawdź fragmenty z prezentacji dotyczące danej funkcjonalności – znajdziesz tam gotowe wzorce.

##

Powodzenia!
