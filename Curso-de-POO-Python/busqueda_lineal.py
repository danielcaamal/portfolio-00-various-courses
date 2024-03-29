import random

def busqueda_lineal(lista, objetivo):
    match = False #O(1)

    for elemento in lista: #O(n)
        if elemento == objetivo:
            match = True
            break
    
    return match #O(1)


def run():
    tamano_de_lista = int(input("De qué tamaño es la lista? "))
    objetivo = int(input("Qué número quieres encontrar?"))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')


if __name__ == "__main__":
    run()