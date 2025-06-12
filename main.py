import json
import pdb

from trip_app.exceptions import *
from trip_app.input_validation import *
from trip_app.trip import Trip

trips = []  # lista wycieczek


def newTrip():
    dest = input("Podaj cel podróży: ").strip()
    while True:
        try:
            date_str = input("Podaj datę wyjazdu (RRRR-MM-DD): ").strip()
            date = parse_date(date_str)
            break
        except DateError as e:
            print(f"Błąd walidacji daty: {e}")

    trip = Trip(dest, date)
    if trip in trips:
        print(f"Wycieczka do {dest} na {date} już istnieje.")
        return
    trips.append(trip)
    print(f"Utworzono wycieczkę: {dest} ({date})")

def showTrips():
    if not trips:
        raise NoTripsError("Brak wycieczek.")
    else:
        print("Lista wycieczek:")
        for idx, t in enumerate(trips, 1):
            print(f" {idx}. {t.destination} ({t.date}) - uczestników: {len(t.participants)}")

def deleteTrip():
    print("Wybierz wycieczkę do usunięcia:")
    try:
        showTrips()
    except NoTripsError as e:
        print(e, "- nie można usunąć.")
        return

    while True:
        try:
            sel = int(input("Numer: ").strip())
            break
        except ValueError:
            print("Nieprawidłowy numer.")

    if 1 <= sel <= len(trips):
        rem = trips.pop(sel-1)
        print(f"Usunięto wycieczkę: {rem.destination}")
    else:
        print("Nieprawidłowy numer.")
        deleteTrip()
        return

def addParticipantToTrip():
    print("Wybierz wycieczkę")
    try:
        showTrips()
    except NoTripsError as e:
        print(e, "Najpierw utwórz wycieczkę.")
        newTrip()
        addParticipantToTrip()
        return
    while True:
        try:
            sel = int(input("Numer: ").strip())
            break
        except ValueError:
            print("Nieprawidłowy numer.")

    if not (1 <= sel <= len(trips)):
        print("Nieprawidłowy wybór.")
        addParticipantToTrip()
        return
    else:
        t = trips[sel-1]
        name = input("Imię i nazwisko: ").strip()

        while True:
            try:
                email = input("Email: ").strip()
                email = email_validate(email)
                break
            except EmailError as e:
                print(e)
        try:
            t.add_participant(name, email)
            print(f"Dodano uczestnika {name} <{email}> do '{t.destination}'")
        except ParticipantExistsError as e:
            print(f"Błąd dodawania uczestnika: {e}")
            return

def removeParticipantFromTrip():
    try:
        showTrips()
    except NoTripsError as e:
        print(e)
        return
    while True:
        try:
            sel = int(input("Numer: ").strip())
            break
        except ValueError:
            print("Nieprawidłowy numer.")

    if not (1 <= sel <= len(trips)):
        print("Nieprawidłowy wybór.")
        removeParticipantFromTrip()
    else:
        t = trips[sel - 1]
        if not t.participants:
            print("Brak uczestników.")
        else:
            print("Uczestnicy:")
            for p in t.participants:
                print(f" - {p['name']} <{p['email']}>")
            email = input("Podaj email: ").strip()
            try:
                t.remove_participant(email)
            except ParticipantNotFoundError:
                print(f"Nie znaleziono uczestnika o email: {email}")
                return
            print(f"Usunięto uczestnika o email {email} z '{t.destination}'")

def showParticipantsFromTrip():
    try:
        showTrips()
    except NoTripsError as e:
        print(e)
        return

    while True:
        try:
            sel = int(input("Numer: ").strip())
            break
        except ValueError:
            print("Nieprawidłowy numer.")

    if not (1 <= sel <= len(trips)):
        print("Nieprawidłowy wybór.")
        showParticipantsFromTrip()
        return
    else:
        t = trips[sel - 1]
        print(f"Uczestnicy '{t.destination}':")
        if not t.participants:
            print(" (brak uczestników)")
        else:
            for p in t.participants:
                print(f" - {p['name']} <{p['email']}>")

def saveToFile():
    if not trips:
        print("Brak wycieczek do zapisania.")
        return
    while True:
        fileName = input().strip()
        try:
            with open(fileName, "w", encoding="utf-8") as file:
                json.dump([trip.to_dict() for trip in trips], file, ensure_ascii=False, indent=4)
            print(f"Wycieczki zapisano do pliku '{fileName}'.")
            break
        except Exception as e:
            print(f"Wystąpił błąd podczas zapisywania: {e}")

def loadFromFile():
    global trips
    print("Podaj nazwę pliku do wczytania wycieczek:")
    while True:
        fileName = input().strip()
        try:
            with open(fileName, "r", encoding="utf-8") as file:
                data = json.load(file)
                trips = [Trip(d["destination"], d["date"]) for d in data]
                for trip, d in zip(trips, data):
                    trip.participants = d.get("participants", [])
            print(f"Wycieczki wczytano z pliku '{fileName}'.")
            break
        except FileNotFoundError:
            print(f"Plik '{fileName}' nie istnieje.")
        except json.JSONDecodeError:
            print(f"Błąd odczytu danych z pliku '{fileName}'.")
            break
        except Exception as e:
            print(f"Wystąpił błąd podczas wczytywania: {e}")
            break

def main():
    while True:
        print("\n=== Aplikacja organizacji wyjazdów grupowych ===")
        print("1. Utwórz nową wycieczkę")
        print("2. Wyświetl wszystkie wycieczki")
        print("3. Usuń wycieczkę")
        print("4. Dodaj uczestnika do wybranej wycieczki")
        print("5. Usuń uczestnika z wybranej wycieczki")
        print("6. Wyświetl uczestników wybranej wycieczki")
        print("7. Zapisz wycieczki do pliku")
        print("8. Wczytaj wycieczkę z pliku")
        print("9. Debug (pdb)")
        print("0. Wyjście")

        while True:
            try:
                choice = int(input("Wybierz opcję: ").strip())
                break
            except ValueError:
                print("Nie podano liczby.")


        if choice == 0:
            print("Koniec programu.")
            break
        elif choice == 1:
            newTrip()
        elif choice == 2:
            try:
                showTrips()
            except NoTripsError as e:
                print(e)
        elif choice == 3:
            deleteTrip()
        elif choice == 4:
            addParticipantToTrip()
        elif choice == 5:
            removeParticipantFromTrip()
        elif choice == 6:
            showParticipantsFromTrip()
        elif choice == 7:
            saveToFile()
        elif choice == 8:
            loadFromFile()
        elif choice == 9:
            pdb.set_trace()
        else:
            print("Niepoprawna opcja")


if __name__ == "__main__":
    main()