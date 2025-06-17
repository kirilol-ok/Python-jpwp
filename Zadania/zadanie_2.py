# import copy

# class BezpiecznaLista:
#     def __init__(self, lista: list):
#         self.lista = lista

#     def __enter__(self):
#         # TODO: zapisz kopię listy
#         self._backup = ____________________
#         return self.lista

#     def __exit__(self, typ, val, tb):
#         if typ is not None:
#             # TODO: przywróć stan listy z kopii
#             ________________________________
#             # TODO: zwróć False, żeby wyjątek przebił się dalej
#             _____________________________
#         return True

# if __name__ == "__main__":
#     moja_lista = [1, 2, 3]
#     try:
#         with BezpiecznaLista(moja_lista) as lst:
#             lst.append(4)
#             raise ValueError("test")
#     except ValueError:
#         pass

#     print(moja_lista)  # powinno wydrukować [1, 2, 3]
