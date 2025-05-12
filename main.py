# main.py - Główny moduł aplikacji z tekstowym interfejsem użytkownika (CLI)

import json
import logging
import warnings
import tracemalloc
import pdb

from trip_app import logging_setup, api
from trip_app.exceptions import TripError, ParticipantExistsError, ParticipantNotFoundError
from trip_app.trip import Trip
from trip_app.input_validation import parse_date
from trip_app.context import FileTransaction

def main():
    logger = logging_setup.setup_logging()
    warnings.filterwarnings("always", category=UserWarning)
    trips = []  # lista wycieczek

    while True:
        print("\n=== Aplikacja organizacji wyjazdów grupowych ===")
        print("1. Utwórz nową wycieczkę")
        print("2. Wyświetl wszystkie wycieczki")
        print("3. Usuń wycieczkę")
        print("4. Dodaj uczestnika do wybranej wycieczki")
        print("5. Usuń uczestnika z wybranej wycieczki")
        print("6. Wyświetl uczestników wybranej wycieczki")
        print("7. Zapisz wycieczkę do pliku")
        print("8. Wczytaj wycieczkę z pliku")
        print("9. Geokoduj adres wybranej wycieczki")
        print("10. Debug (uruchom pdb)")
        print("11. Profiluj pamięć (tracemalloc)")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ").strip()

        try:
            if choice == '0':
                print("Koniec programu.")
                break

            elif choice == '1':
                dest = input("Podaj cel podróży: ").strip()
                date_str = input("Podaj datę wyjazdu (RRRR-MM-DD): ").strip()
                date = parse_date(date_str)
                trip = Trip(dest, date)
                trips.append(trip)
                print(f"Utworzono wycieczkę: {dest} ({date})")
                logger.info(f"Utworzono wycieczkę: {dest} ({date})")

            elif choice == '2':
                if not trips:
                    print("Brak wycieczek.")
                else:
                    print("Lista wycieczek:")
                    for idx, t in enumerate(trips, 1):
                        print(f" {idx}. {t.destination} ({t.date}) - uczestników: {len(t.participants)}")

            elif choice == '3':
                if not trips:
                    print("Brak wycieczek do usunięcia.")
                else:
                    print("Wybierz wycieczkę do usunięcia:")
                    for idx, t in enumerate(trips, 1):
                        print(f" {idx}. {t.destination} ({t.date})")
                    sel = int(input("Numer: ").strip())
                    if 1 <= sel <= len(trips):
                        rem = trips.pop(sel-1)
                        print(f"Usunięto wycieczkę: {rem.destination}")
                        logger.info(f"Usunięto wycieczkę: {rem.destination} ({rem.date})")
                    else:
                        print("Nieprawidłowy numer.")

            elif choice == '4':
                if not trips:
                    print("Brak wycieczek. Utwórz najpierw wycieczkę.")
                else:
                    print("Wybierz wycieczkę:")
                    for idx, t in enumerate(trips, 1):
                        print(f" {idx}. {t.destination} ({t.date})")
                    sel = int(input("Numer: ").strip())
                    if not (1 <= sel <= len(trips)):
                        print("Nieprawidłowy wybór.")
                    else:
                        t = trips[sel-1]
                        name = input("Imię i nazwisko: ").strip()
                        email = input("Email: ").strip()
                        t.add_participant(name, email)
                        print(f"Dodano uczestnika {name} <{email}> do '{t.destination}'")
                        logger.info(f"Dodano uczestnika {email} do wycieczki '{t.destination}'")

            elif choice == '5':
                if not trips:
                    print("Brak wycieczek.")
                else:
                    print("Wybierz wycieczkę:")
                    for idx, t in enumerate(trips,1):
                        print(f" {idx}. {t.destination} ({t.date})")
                    sel = int(input("Numer: ").strip())
                    if not (1 <= sel <= len(trips)):
                        print("Nieprawidłowy wybór.")
                    else:
                        t = trips[sel-1]
                        if not t.participants:
                            print("Brak uczestników.")
                        else:
                            print("Uczestnicy:")
                            for p in t.participants:
                                print(f" - {p['name']} <{p['email']}>")
                            email = input("Podaj email: ").strip()
                            t.remove_participant(email)
                            print(f"Usunięto uczestnika o email {email} z '{t.destination}'")
                            logger.info(f"Usunięto {email} z '{t.destination}'")

            elif choice == '6':
                if not trips:
                    print("Brak wycieczek.")
                else:
                    print("Wybierz wycieczkę:")
                    for idx, t in enumerate(trips,1):
                        print(f" {idx}. {t.destination} ({t.date})")
                    sel = int(input("Numer: ").strip())
                    if not (1 <= sel <= len(trips)):
                        print("Nieprawidłowy wybór.")
                    else:
                        t = trips[sel-1]
                        print(f"Uczestnicy '{t.destination}':")
                        if not t.participants:
                            print(" (brak uczestników)")
                        else:
                            for p in t.participants:
                                print(f" - {p['name']} <{p['email']}>")

            elif choice == '7':
                if not trips:
                    print("Brak wycieczek.")
                else:
                    print("Wybierz wycieczkę do zapisu:")
                    for idx, t in enumerate(trips,1):
                        print(f" {idx}. {t.destination} ({t.date})")
                    sel = int(input("Numer: ").strip())
                    if not (1 <= sel <= len(trips)):
                        print("Nieprawidłowy wybór.")
                    else:
                        t = trips[sel-1]
                        filename = input("Nazwa pliku (np. dane.json): ").strip()
                        data = json.dumps(t.to_dict(), ensure_ascii=False, indent=4)
                        with FileTransaction(filename) as f:
                            f.write(data)
                        print(f"Zapisano do {filename}.")
                        logger.info(f"Zapisano '{t.destination}' do pliku {filename}")

            elif choice == '8':
                filename = input("Nazwa pliku do wczytania: ").strip()
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                t = Trip.from_dict(data)
                trips.append(t)
                print(f"Wczytano wycieczkę '{t.destination}' ({t.date})")
                logger.info(f"Wczytano wycieczkę z pliku {filename}")

            elif choice == '9':
                if not trips:
                    print("Brak wycieczek.")
                else:
                    print("Wybierz wycieczkę do geokodowania:")
                    for idx, t in enumerate(trips,1):
                        print(f" {idx}. {t.destination} ({t.date})")
                    sel = int(input("Numer: ").strip())
                    if not (1 <= sel <= len(trips)):
                        print("Nieprawidłowy wybór.")
                    else:
                        t = trips[sel-1]
                        try:
                            coords = api.geocode(t.destination)
                            print(f"Współrzędne: {coords}")
                            logger.info(f"Geokodowano '{t.destination}' -> {coords}")
                        except TripError as e:
                            warnings.warn("Geokodowanie nie powiodło się.", UserWarning)
                            print(f"Nie udało się geokodować: {e}")

            elif choice == '10':
                print("Wejście do debuggera PDB")
                pdb.set_trace()

            elif choice == '11':
                print("Profilowanie pamięci...")
                tracemalloc.start()
                big_list = [x**2 for x in range(100000)]
                current, peak = tracemalloc.get_traced_memory()
                print(f"Zużycie: {current/1024:.2f}KB; szczyt: {peak/1024:.2f}KB")
                snapshot = tracemalloc.take_snapshot()
                stats = snapshot.statistics('lineno')[:3]
                for s in stats:
                    print(s)
                tracemalloc.stop()
                del big_list

            else:
                print("Nieznana opcja.")

        except TripError as e:
            logger.error(f"Błąd aplikacji: {e}", exc_info=True)
            print(f"[Błąd] {e}")
        except ParticipantExistsError as e:
            logger.error(f"Duplikat uczestnika: {e}", exc_info=True)
            print(f"[Błąd] {e}")
        except ParticipantNotFoundError as e:
            logger.error(f"Brak uczestnika: {e}", exc_info=True)
            print(f"[Błąd] {e}")
        except Exception as e:
            logger.exception("Nieoczekiwany błąd")
            print(f"[Nieoczekiwany błąd] {e}")

if __name__ == "__main__":
    main()
