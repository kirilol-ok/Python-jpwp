# exceptions.py - Definicje własnych klas wyjątków dla aplikacji wyjazdów grupowych
# Wszystkie wyjątki dziedziczą po Exception i mogą być używane do sygnalizowania konkretnych błędów domenowych.

class TripError(Exception):
    """Bazowy wyjątek dla błędów w aplikacji wyjazdów grupowych."""
    pass

class ParticipantExistsError(TripError):
    """Wyjątek zgłaszany przy próbie dodania uczestnika, który już istnieje."""
    pass

class ParticipantNotFoundError(TripError):
    """Wyjątek zgłaszany przy próbie usunięcia lub dostępu do nieistniejącego uczestnika."""
    pass
