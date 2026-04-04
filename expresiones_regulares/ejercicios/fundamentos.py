"""
EJERCICIOS DE EXPRESIONES REGULARES - NIVEL 1: FUNDAMENTOS
---------------------------------------------------------
En este archivo practicaremos:
- Metacaracteres: . , ^ , $
- Cuantificadores: * , + , ? , {n} , {n,} , {n,m}
- Clases de caracteres: [abc], [a-z], [^0-9]
- Clases predefinidas: \d, \w, \s, \D, \W, \S
"""

import re

# 1. EJERCICIO: Validar un ID de usuario que:
# - Empiece por una letra minúscula.
# - Tenga entre 5 y 12 caracteres.
# - Solo contenga letras minúsculas y números.
def validar_id_usuario(id_usuario):
    patron = r"^[a-z][a-z0-9]{4,11}$"
    return bool(re.match(patron, id_usuario))

# 2. EJERCICIO: Verificar si un string es un número decimal válido (ej: 12.5, -3.14, 0.5)
# Debe soportar opcionalmente un signo negativo al principio.
def es_decimal(texto):
    patron = r"^-?\d+\.\d+$"
    return bool(re.match(patron, texto))

# 3. EJERCICIO: Validar un código de producto con el formato "XXX-9999"
# Donde X son letras mayúsculas y 9 son dígitos.
def validar_codigo_producto(codigo):
    patron = r"^[A-Z]{3}-\d{4}$"
    return bool(re.match(patron, codigo))

# 4. EJERCICIO: Encontrar todas las palabras que tengan exactamente 4 letras en un texto.
def palabras_de_cuatro_letras(texto):
    # Usamos \b para límites de palabra
    patron = r"\b[a-zA-Z]{4}\b"
    return re.findall(patron, texto)

# 5. EJERCICIO: Validar una dirección IP básica (4 grupos de 1-3 dígitos separados por puntos)
# Nota: Esta versión simple no valida que los números sean < 256.
def validar_ip_basica(ip):
    patron = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    return bool(re.match(patron, ip))

if __name__ == "__main__":
    print("--- Probando Fundamentos ---")
    
    # Test 1
    assert validar_id_usuario("user123") == True
    assert validar_id_usuario("1user") == False
    assert validar_id_usuario("abc") == False
    
    # Test 2
    assert es_decimal("15.20") == True
    assert es_decimal("-0.5") == True
    assert es_decimal("10") == False
    
    # Test 3
    assert validar_codigo_producto("ABC-1234") == True
    assert validar_codigo_producto("AB-1234") == False
    
    # Test 4
    texto = "La casa es azul y el cielo es gris"
    print(f"Palabras de 4 letras: {palabras_de_cuatro_letras(texto)}") # ['casa', 'azul', 'gris']
    
    # Test 5
    assert validar_ip_basica("192.168.1.1") == True
    assert validar_ip_basica("1.1.1") == False

    print("¡Todos los tests de fundamentos pasaron!")
