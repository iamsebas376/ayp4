"""
EJERCICIOS DE EXPRESIONES REGULARES - NIVEL 3: LOOKAROUND Y ANCLAS
------------------------------------------------------------------
En este archivo practícaremos:
- Post-condiciones: Lookahead (?= ), (?! )
- Pre-condiciones: Lookbehind (?<= ), (?<! )
- Anclas de contorno: \b, \B
- Anclas de inicio y fin: ^, $
"""

import re

# 1. EJERCICIO: Validar una contraseña que:
# - Tenga al menos 8 caracteres.
# - Contenga al menos UNA letra minúscula.
# - Contenga al menos UNA letra mayúscula.
# - Contenga al menos UN número.
# No necesitamos consumir los caracteres para verificar cada regla, usamos Lookahead.
def validar_password_fuerte(p):
    # (?=.*[a-z]) -> Hay al menos un char en [a-z] en algún lugar adelante
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return bool(re.match(patron, p))

# 2. EJERCICIO: Extraer precios en dólares que NO incluyan decimales.
# - Ejemplo: "$100" (Válido), "$10.50" (No válido)
# - Se usa Lookahead negativo (?!...) para asegurar que después del número no haya un punto.
def extraer_precios_enteros(texto):
    patron = r"\$\d+\b(?!\.\d+)"
    return re.findall(patron, texto)

# 3. EJERCICIO: Encontrar palabras que estén rodeadas por comillas dobles,
# pero solo extraer el contenido interior usando Lookbehind y Lookahead.
# Ejemplo: '"Hola" mundo' -> ["Hola"]
def extraer_entre_comillas(texto):
    patron = r"(?<=\").*?(?=\")"
    return re.findall(patron, texto)

# 4. EJERCICIO: Validar que un nombre de usuario NO empiece por el prefijo "admin_".
# Usamos Lookahead negativo al principio.
def validar_usuario_no_admin(u):
    patron = r"^(?!admin_)[a-zA-Z0-9_]{5,}$"
    return bool(re.match(patron, u))

# 5. EJERCICIO: Extraer números que estén precedidos por el símbolo de Euro (€)
# pero NO los que estén precedidos por el símbolo de Pesos ($).
def extraer_euros(texto):
    patron = r"(?<=€)\d+"
    return re.findall(patron, texto)

if __name__ == "__main__":
    print("\n--- Probando Lookaround y Anclas ---")
    
    # Test 1
    assert validar_password_fuerte("Abc12345") == True
    assert validar_password_fuerte("abc12345") == False # Falta mayúscula
    
    # Test 2
    texto_precios = "Los precios son $10, $5.99 y $100."
    print(f"Precios enteros: {extraer_precios_enteros(texto_precios)}") # ['$10', '$100']
    
    # Test 3
    texto_comillas = 'Dijo "Hola" y luego "Adiós"'
    print(f"Contenido entre comillas: {extraer_entre_comillas(texto_comillas)}") # ['Hola', 'Adiós']
    
    # Test 4
    assert validar_usuario_no_admin("user_123") == True
    assert validar_usuario_no_admin("admin_sebas") == False
    
    # Test 5
    texto_monedas = "Tengo €50 y debo $20."
    print(f"Euros encontrados: {extraer_euros(texto_monedas)}") # ['50']

    print("¡Todos los tests de lookaround pasaron!")
