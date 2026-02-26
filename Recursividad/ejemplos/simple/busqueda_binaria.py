def busqueda_binaria(lista, inicio, final, n):
    if final >= inicio:
        mitad = (inicio + final) // 2
        if lista[mitad] == n:
            return mitad
        elif lista[mitad] > n:
            return busqueda_binaria(lista, inicio, mitad - 1, n)
        else:
            return busqueda_binaria(lista, mitad + 1, final, n)
    else:
        return -1


lista = [1, 5, 7, 12, 15]
numero = busqueda_binaria(lista, 0, 5, 12)

if numero != -1:
    print("El número está en la posición: ", str(numero + 1))
else:
    print("El número no está en la lista")
