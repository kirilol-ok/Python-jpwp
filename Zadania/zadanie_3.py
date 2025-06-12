# Zadanie 3: Dekorator, który loguje wyjątki i ponownie je rzuca
import logging
logger = logging.getLogger("cw")
logging.basicConfig(level=logging.DEBUG)

def loguj_wyjatki(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # TODO: zaloguj traceback z logger.exception
            logger.exception(________________)
            # TODO: ponownie rzuć wyjątek
            ________________________
    return wrapper

@loguj_wyjatki
def dziel(a, b):
    return a / b

if __name__ == "__main__":
    dziel(4, 0)
