"""
EJERCICIOS DE EXPRESIONES REGULARES - NIVEL 2: GRUPOS Y REFERENCIAS
-------------------------------------------------------------------
En este archivo practicaremos:
- Grupos de captura: ( )
- Grupos de NO captura: (?: )
- Grupos con nombre: (?P<nombre> )
- Referencias hacia atrás (Backreferences): \1, \2, \k<nombre>
"""

import re

# 1. EJERCICIO: Validar una etiqueta HTML básica completa y balanceada:
# - Ejemplo válido: "<div>Hola</div>", "<span>Texto</span>"
# - Ejemplo no válido: "<div>Hola</span>", "<span>Texto</div>"
# Se asume que no hay atributos ni etiquetas anidadas para simplificar.
def validar_etiqueta_balanceada(t):
    # Usamos \1 para referenciar el primer grupo capturado (el nombre de la etiqueta abrir)
    patron = r"^<([a-z0-9]+)>.*?</\1>$"
    return bool(re.match(patron, t))

# 2. EJERCICIO: Extraer información de una URL con grupos con nombre.
# - Formato: https://dominio.com/ruta1/ruta2
# - Queremos extraer: protocolo, dominio y ruta completa.
def parsear_url(url):
    patron = r"^(?P<protocol>\w+)://(?P<domain>[\w\.]+)(?P<path>/.*)?$"
    match = re.match(patron, url)
    if match:
        return match.groupdict()
    return None

# 3. EJERCICIO: Detectar palabras duplicadas consecutivas en un texto.
# - Ejemplo: "El el perro corre" -> ["El el"]
def detectar_duplicados(texto):
    # \b es límite de palabra, \W+ es cualquier espacio/puntuación
    # ignorecase para "El el"
    patron = r"\b(\w+)\W+\1\b"
    return re.findall(patron, texto, flags=re.IGNORECASE)

# 4. EJERCICIO: Extraer año, mes y día de una fecha en formato AAAA-MM-DD
# usando grupos de captura básicos.
def extraer_fecha_componentes(fecha):
    # Formato: 2024-04-15
    patron = r"^(\d{4})-(\d{2})-(\d{2})$"
    match = re.search(patron, fecha)
    if match:
        return {
            "año": match.group(1),
            "mes": match.group(2),
            "dia": match.group(3)
        }
    return None

# 5. EJERCICIO: Validar una fecha con el mismo delimitador al principio y al final.
# - Delimitadores permitidos: / o -
# - Ejemplo válido: 15/04/2024, 15-04-2024
# - Ejemplo no válido: 15/04-2024, 15-04/2024
def validar_fecha_delimitador(f):
    patron = r"^\d{2}([/-])\d{2}\1\d{4}$"
    return bool(re.match(patron, f))

if __name__ == "__main__":
    print("\n--- Probando Grupos y Referencias ---")
    
    # Test 1
    assert validar_etiqueta_balanceada("<div>contenido</div>") == True
    assert validar_etiqueta_balanceada("<div>contenido</span>") == False
    
    # Test 2
    url_info = parsear_url("https://www.google.com/search?q=regex")
    print(f"Info de URL: {url_info}")
    
    # Test 3
    texto_duplicado = "La la casa casa es roja roja"
    # Nota: findall con grupos devuelve solo el grupo si hay uno, o una tupla de grupos si hay varios.
    # Para obtener el match entero se usa finditer.
    duplicados = [m.group(0) for m in re.finditer(r"\b(\w+)\W+\1\b", texto_duplicado, flags=re.IGNORECASE)]
    print(f"Palabras duplicadas: {duplicados}")
    
    # Test 4
    fecha_info = extraer_fecha_componentes("2026-04-04")
    assert fecha_info["mes"] == "04"
    
    # Test 5
    assert validar_fecha_delimitador("15/04/2024") == True
    assert validar_fecha_delimitador("15-04-2024") == True
    assert validar_fecha_delimitador("15/04-2024") == False

    print("¡Todos los tests de grupos pasaron!")
