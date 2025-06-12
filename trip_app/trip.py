from .exceptions import *

class Trip:

    def __init__(self, destination, date):
        self.destination = destination
        self.date = date
        self.participants = []

    def add_participant(self, name, email):
        for p in self.participants:
            if p['email'].lower() == email.lower():
                # Uczestnik już istnieje
                raise ParticipantExistsError(f"Uczestnik o email '{email}' już istnieje na liście.")

        self.participants.append({'name': name, 'email': email})
    def remove_participant(self, email):
        for p in self.participants:
            if p['email'].lower() == email.lower():
                self.participants.remove(p)
                return
        # Jeśli nie znaleziono uczestnika, zgłoś wyjątek
        raise ParticipantNotFoundError(f"Nie znaleziono uczestnika o email: {email}")

    def to_dict(self):
        return {
            "destination": self.destination,
            "date": str(self.date),
            "participants": self.participants
        }
