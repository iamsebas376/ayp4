# Contar cuántas veces se repite un carácter en un texto

def contar_caracteres(s, c):
    contador = 0
    if len(s) == 0:
        return 0
    cuenta = 1 if s[0] == c else 0
    return cuenta + contar_caracteres(s[1:], c)

print(contar_caracteres("Holaa", "a"))