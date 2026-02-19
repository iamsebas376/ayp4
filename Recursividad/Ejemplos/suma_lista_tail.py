import time

def suma_lista_tail(lista, total=0):
    if not lista:
        return total
    return suma_lista_tail(lista[1:], total + lista[0])

actual = time.time() 
lista = [1, 2, 3, 4, 5]
print(suma_lista_tail(lista))
print("El tiempo de ejecución es: ", time.time() - actual)