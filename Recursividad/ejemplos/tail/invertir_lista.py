def invertir_lista(lista):
    if not lista:
        return lista
    return invertir_lista(lista[1:]) + [lista[0]]

lista = [1, 2, 3]
print(invertir_lista(lista))