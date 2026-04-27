"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 4: APLICACIONES PRÁCTICAS DE CONJUNTOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Los conjuntos son útiles para:
- Eliminar duplicados
- Verificar pertenencia rápidamente
- Encontrar elementos comunes o diferentes
- Sistemas de etiquetas/tags
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. Eliminar duplicados de una lista
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("1. Eliminar duplicados")
print("=" * 60)

lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
sin_duplicados = list(set(lista_con_duplicados))

print(f"Original: {lista_con_duplicados}")
print(f"Sin duplicados: {sin_duplicados}")

# Con strings
palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
palabras_unicas = set(palabras)
print(f"\nPalabras únicas: {palabras_unicas}")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Encontrar elementos comunes (amigos en común)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("2. Amigos en común (intersección)")
print("=" * 60)

amigos_juan = {"María", "Pedro", "Ana", "Carlos", "Laura"}
amigos_maria = {"Pedro", "Laura", "Sofia", "Diego", "Ana"}

amigos_comunes = amigos_juan & amigos_maria
print(f"Amigos de Juan: {amigos_juan}")
print(f"Amigos de María: {amigos_maria}")
print(f"Amigos en común: {amigos_comunes}")

# Sugerencias de amistad (amigos de amigos que no conoces)
sugerencias_juan = amigos_maria - amigos_juan
print(f"Sugerencias para Juan: {sugerencias_juan}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Sistema de etiquetas (tags)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("3. Sistema de etiquetas")
print("=" * 60)

# Artículos con sus etiquetas
articulo1 = {"python", "programación", "tutorial", "principiantes"}
articulo2 = {"python", "web", "django", "backend"}
articulo3 = {"javascript", "web", "frontend", "react"}

print(f"Artículo 1: {articulo1}")
print(f"Artículo 2: {articulo2}")
print(f"Artículo 3: {articulo3}")

# Artículos relacionados (tienen etiquetas en común)
print(f"\nEtiquetas comunes 1-2: {articulo1 & articulo2}")
print(f"Etiquetas comunes 2-3: {articulo2 & articulo3}")
print(f"Etiquetas comunes 1-3: {articulo1 & articulo3}")

# Todas las etiquetas usadas
todas_etiquetas = articulo1 | articulo2 | articulo3
print(f"\nTodas las etiquetas: {todas_etiquetas}")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Verificar requisitos (permisos)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. Sistema de permisos")
print("=" * 60)

permisos_admin = {"leer", "escribir", "eliminar", "crear_usuarios", "ver_logs"}
permisos_editor = {"leer", "escribir"}
permisos_usuario = {"leer"}

def tiene_permisos(usuario_permisos, permisos_requeridos):
    """Verifica si el usuario tiene todos los permisos requeridos"""
    return permisos_requeridos <= usuario_permisos

# Verificar acceso
accion_editar = {"leer", "escribir"}
accion_admin = {"crear_usuarios", "ver_logs"}

print(f"¿Editor puede editar? {tiene_permisos(permisos_editor, accion_editar)}")
print(f"¿Editor puede administrar? {tiene_permisos(permisos_editor, accion_admin)}")
print(f"¿Admin puede administrar? {tiene_permisos(permisos_admin, accion_admin)}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Análisis de texto
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("5. Análisis de texto")
print("=" * 60)

texto1 = "python es un lenguaje de programación"
texto2 = "java es otro lenguaje de programación"

palabras1 = set(texto1.lower().split())
palabras2 = set(texto2.lower().split())

print(f"Texto 1: {texto1}")
print(f"Texto 2: {texto2}")
print(f"\nPalabras en común: {palabras1 & palabras2}")
print(f"Solo en texto 1: {palabras1 - palabras2}")
print(f"Solo en texto 2: {palabras2 - palabras1}")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Búsqueda eficiente
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("6. Búsqueda eficiente")
print("=" * 60)

# Lista vs Set para búsqueda
import time

# Crear datos
datos_lista = list(range(100000))
datos_set = set(range(100000))

# Buscar elemento
elemento = 99999

# Búsqueda en lista
inicio = time.time()
for _ in range(1000):
    _ = elemento in datos_lista
tiempo_lista = time.time() - inicio

# Búsqueda en set
inicio = time.time()
for _ in range(1000):
    _ = elemento in datos_set
tiempo_set = time.time() - inicio

print(f"Tiempo búsqueda en lista: {tiempo_lista:.4f}s")
print(f"Tiempo búsqueda en set: {tiempo_set:.4f}s")
print(f"Set es {tiempo_lista/tiempo_set:.0f}x más rápido")
