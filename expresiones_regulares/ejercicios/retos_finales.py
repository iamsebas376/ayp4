"""
EJERCICIOS DE EXPRESIONES REGULARES - NIVEL 5: RETOS FINALES
-----------------------------------------------------------
En este archivo pondremos a prueba todo lo aprendido con casos complejos:
- Análisis de archivos CSV con campos entrecomillados.
- Extracción de metadata de código fuente.
- Validaciones de lógica de negocio profunda.
- Manejo de ambigüedad (Greedy vs Non-greedy).
"""

import re

# 1. RETO: Parsear una línea de CSV que puede tener comas dentro de comillas.
# Ejemplo: '1, "Sebas, Londoño", 25, "Medellín, Colombia"'
# Queremos obtener una lista: ['1', '"Sebas, Londoño"', '25', '"Medellín, Colombia"']
def parsear_csv_seguro(linea):
    # Buscamos o bien un texto entre comillas, o bien lo que haya entre comas.
    # Explicación: ("[^"]*"|[^,]+)
    patron = r'("[^"]*"|[^,]+)'
    matches = re.findall(patron, linea)
    # Limpiamos espacios laterales sobrantes
    return [m.strip() for m in matches]

# 2. RETO: Scraper de funciones Python.
# Extraer el nombre de la función y la lista de sus argumentos de un string de código.
# Ejemplo: "def calcular_area(radio, pi=3.14):" -> ("calcular_area", "radio, pi=3.14")
def extraer_info_funcion(linea_codigo):
    patron = r"def\s+(?P<name>\w+)\s*\((?P<args>.*?)\):"
    match = re.search(patron, linea_codigo)
    if match:
        return match.group("name"), match.group("args")
    return None

# 3. RETO: Validar una fecha FEBRERO que considere años bisiestos (Simplified logic).
# Validar formato DD/MM/AAAA donde MM es 02.
# Si el año termina en 00, 04, 08, 12, etc, el día puede ser hasta 29.
# Si no, el día puede ser hasta 28. (Nota: Esto es complejo con puras regex).
# Haremos una versión que valide que si es 29/02, el año sea múltiplo de 4.
def validar_bisiesto_simple(fecha):
    # ^(29/02/(\d{2}([02468][048]|[13579][26])))|((0[1-9]|1[0-9]|2[0-8])/02/\d{4})$
    # Explicación: Parte 1 para el 29 de febrero, Parte 2 para 01-28 de febrero.
    patron = r"^(29/02/(\d{2}([02468][048]|[13579][26])))|((0[1-9]|1[0-9]|2[0-8])/02/\d{4})$"
    return bool(re.match(patron, fecha))

# 4. RETO: Extraer contenido entre etiquetas de comentarios XML/HTML multilínea.
# <!-- Comentario 
#      multilínea -->
# Queremos extraer el contenido sin los delimitadores, usando re.DOTALL.
def extraer_comentario_multilinea(html):
    # .*? -> Non-greedy para no saltar entre múltiples comentarios.
    patron = r"<!--(.*?)-->"
    return re.findall(patron, html, flags=re.DOTALL)

# 5. RETO: Validar números de teléfono internacionales con el formato +X (YYY) ZZZ-ZZZZ
# El +X es opcional (1 a 3 dígitos). YYY son 3 dígitos. ZZZ-ZZZZ son 3 y 4 dígitos.
def validar_tel_internacional(tel):
    patron = r"^(\+\d{1,3}\s)?\(\d{3}\)\s\d{3}-\d{4}$"
    return bool(re.match(patron, tel))

if __name__ == "__main__":
    print("\n--- Probando Retos Finales ---")
    
    # Test 1
    linea = '1, "Londoño, Sebas", 25, "Antioquia, Medellín"'
    print(f"CSV Parseado: {parsear_csv_seguro(linea)}")
    
    # Test 2
    codigo = "def actualizar_perfil(usuario_id, token, activo=True):"
    print(f"Info Función: {extraer_info_funcion(codigo)}")
    
    # Test 3
    assert validar_bisiesto_simple("29/02/2024") == True # 2024 es bisiesto
    assert validar_bisiesto_simple("29/02/2023") == False # 2023 no es bisiesto
    assert validar_bisiesto_simple("28/02/2023") == True
    
    # Test 4
    html_doc = """
    <div>
        <!-- Este es un
             comentario largo -->
        <p>Hola</p>
        <!-- Comentario corto -->
    </div>
    """
    comentarios = extraer_comentario_multilinea(html_doc)
    print(f"Comentarios extraídos: {[c.strip() for c in comentarios]}")
    
    # Test 5
    assert validar_tel_internacional("+57 (312) 345-6789") == True
    assert validar_tel_internacional("(312) 345-6789") == True
    assert validar_tel_internacional("312 345 6789") == False

    print("¡Todos los retos finales fueron completados!")
