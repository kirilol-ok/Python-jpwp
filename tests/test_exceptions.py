# test_exceptions.py - Testy jednostkowe sprawdzające obsługę wyjątków
# Uruchomienie: np. `python -m unittest test_exceptions.py` lub za pomocą narzędzia pytest.

import unittest
from trip_app.exceptions import TripError, ParticipantExistsError, ParticipantNotFoundError
from trip_app.trip import Trip
from trip_app.input_validation import parse_date


class ExceptionHandlingTests(unittest.TestCase):
    def test_duplicate_participant(self):
        # Przygotowanie obiektu Trip z prawidłową datą
        trip = Trip("Test", parse_date("2100-01-01"))
        # Dodanie uczestnika pierwszy raz - powinno przejść bez wyjątku
        trip.add_participant("Jan Kowalski", "jan@example.com")
        # Dodanie tego samego uczestnika ponownie powinno zgłosić ParticipantExistsError
        with self.assertRaises(ParticipantExistsError):
            trip.add_participant("Jan Kowalski", "jan@example.com")

    def test_invalid_date(self):
        # Niepoprawny format daty (ukośniki zamiast myślników)
        with self.assertRaises(TripError):
            parse_date("2025/12/31")
        # Data z przeszłości
        with self.assertRaises(TripError):
            parse_date("2000-01-01")

    def test_remove_nonexistent_participant(self):
        trip = Trip("Test", parse_date("2100-01-01"))
        # Próba usunięcia nieistniejącego uczestnika -> oczekiwany ParticipantNotFoundError
        with self.assertRaises(ParticipantNotFoundError):
            trip.remove_participant("abc@xyz.com")


if __name__ == '__main__':
    unittest.main()
