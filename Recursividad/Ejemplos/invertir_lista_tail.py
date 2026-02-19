def invertir_lista_tail(lista, acumulador=None):
    if acumulador is None:
        acumulador = []
    if len(lista) == 0:
        return acumulador
    return invertir_lista_tail(lista[1:], [lista[0]] + acumulador)

lista = [1, 2, 3]
print(invertir_lista_tail(lista))