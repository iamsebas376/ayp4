def permutaciones(lista):
    if len(lista) <= 1:
        return [lista[:]]
    
    resultado = []

    for i in range(len(lista)):
        elemento = lista[i]
        resto = lista[:1] + lista[i+1:]

        for perm in permutaciones(resto):
            resultado.append[(elemento + perm)]

    return resultado

lista = [1, 3, 5]
print(permutaciones(lista))