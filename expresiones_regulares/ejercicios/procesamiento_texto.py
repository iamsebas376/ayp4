"""
EJERCICIOS DE EXPRESIONES REGULARES - NIVEL 4: PROCESAMIENTO DE TEXTO
--------------------------------------------------------------------
En este archivo practicaremos:
- re.sub: Reemplazo y limpieza de strings.
- re.split: Dividir textos por patrones complejos.
- re.finditer: Captura rica de información (posición, grupos).
- Funciones lambda en re.sub.
"""

import re

# 1. EJERCICIO: Normalizar un número de teléfono.
# Convertir "(+57) 312-345-6789" a "573123456789" (solo dígitos).
def limpiar_telefono(t):
    # Reemplaza todo lo que NO sea un dígito \D por nada.
    return re.sub(r"\D", "", t)

# 2. EJERCICIO: Ofuscar correos electrónicos para evitar spam.
# - "sebas@google.com" -> "***@google.com"
def ofuscar_email(email):
    # Capturamos el dominio para mantenerlo
    return re.sub(r"^[^@]+", "***", email)

# 3. EJERCICIO: Resaltar palabras clave en un texto envolviéndolas en asteriscos.
# - Palabras: "error", "fallo", "advertencia" (insensible a mayúsculas).
def resaltar_errores(texto):
    palabras = ["error", "fallo", "advertencia"]
    # Unimos con | para crear la alternancia
    patron = rf"\b({'|'.join(palabras)})\b"
    return re.sub(patron, r"*\1*", texto, flags=re.IGNORECASE)

# 4. EJERCICIO: Capitalizar la primera letra de cada palabra en un texto,
# pero SÓLO si la palabra tiene más de 3 letras.
def capitalizar_largas(texto):
    # La función recibe un objeto match
    def repl(m):
        palabra = m.group(0)
        if len(palabra) > 3:
            return palabra.capitalize()
        return palabra

    return re.sub(r"\b\w+\b", repl, texto)

# 5. EJERCICIO: Dividir un string que contiene nombres separados por
# comas, puntos y comas, o múltiples espacios.
def dividir_nombres(lista):
    patron = r"[,\s;]+"
    # Eliminamos espacios en blanco al principio y final si quedan
    nombres = re.split(patron, lista)
    return [n.strip() for n in nombres if n.strip()]

if __name__ == "__main__":
    print("\n--- Probando Procesamiento de Texto ---")
    
    # Test 1
    assert limpiar_telefono("(+57) 312 345-6789") == "573123456789"
    
    # Test 2
    assert ofuscar_email("test_user@gmail.com") == "***@gmail.com"
    
    # Test 3
    log = "Error en el sistema. Hubo un fallo crítico pero no hubo una advertencia previa."
    print(f"Log resaltado: {resaltar_errores(log)}")
    
    # Test 4
    texto_input = "hola pepito soy un gran programador de python"
    print(f"Capitalizado: {capitalizar_largas(texto_input)}")
    
    # Test 5
    nombres = "Juan, Pedro; Maria   Jose, Luis"
    print(f"Nombres divididos: {dividir_nombres(nombres)}") # ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis']

    print("¡Todos los tests de procesamiento pasaron!")
