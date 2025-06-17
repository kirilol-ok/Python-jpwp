# import json

# # TODO: zdefiniuj własny wyjątek BladDanych
# class BladDanych(__________________):
#     """Błąd wczytywania danych JSON."""
#     pass

# def wczytaj_json(path: str):
#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError as e:
#         # TODO: rzuć BladDanych z przyczyną FileNotFoundError
#         ______________
#     except json.JSONDecodeError as e:
#         # TODO: rzuć BladDanych z przyczyną JSONDecodeError
#         ______________

# if __name__ == "__main__":
#     try:
#         wczytaj_json("brak.json")
#     except BladDanych as bd:
#         print("Złapano:", bd)
