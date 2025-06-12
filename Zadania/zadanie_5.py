# Zadanie 5: Uruchomienie pdb.set_trace(), kiedy DEBUG=True
import pdb

DEBUG = True

def podwoj(lista):
    # TODO: jeśli DEBUG, to pdb.set_trace()
    ____________________________
    return [x * 2 for x in lista]

if __name__ == "__main__":
    print(podwoj([1, 2, 3]))
