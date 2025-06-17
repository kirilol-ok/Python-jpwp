# import logging
# logger = logging.getLogger("cw")
# logging.basicConfig(level=logging.DEBUG)

# def bezpiecznie_loguj(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             # logujemy cały traceback
#             ___________________
#             # ponownie rzucamy wyjątek
#             ___________________
#     return wrapper

# # Przykład użycia:
# @bezpiecznie_loguj
# def dziel(a, b):
#     return a / b

# if __name__ == "__main__":
#     dziel(4, 0)
