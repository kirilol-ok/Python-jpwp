import pdb
def example_function():
    x = 10
    y = 20
    pdb.set_trace()  # Debugger starts here
    z = x + y
    print(z)

example_function()

# python3 -m pdb pdb_demo.py

# n (next) – przechodzimy do następnej linijki (pomijając wchodzenie w funkcje).
# s (step) – wchodzimy w głąb funkcji, jeżeli bieżąca linia to wywołanie funkcji.
# c (continue) – kontynuuj wykonanie do następnego breakpointa (lub końca, jeśli brak).
# p <zmienna> – wypisz wartość zmiennej (print). Można też wywoływać dowolne wyrażenia Pythona, by podejrzeć stan programu.
# l (list) – wyświetl fragment kodu wokół bieżącej pozycji, by mieć kontekst.
# q (quit) – wyjście z debuggera i przerwanie programu.