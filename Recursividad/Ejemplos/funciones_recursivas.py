# Algortimo que recibe una lista, y hace un suma de todos los elementos
def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + suma_lista(lista[1:])

# print(suma_lista([1, 2, 3, 4, 5]))

# Algortimo recursivo que recibe una número y hace una suma de los digitos
print (1552 // 10)
print (1552 % 10)

def suma_digitos(n):
    if n == 0:
        return n
    return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1552))
