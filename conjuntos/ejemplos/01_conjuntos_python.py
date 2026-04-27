"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 1: CONJUNTOS EN PYTHON (set)
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Un CONJUNTO es una colección de elementos:
- Sin duplicados (cada elemento aparece una sola vez)
- Sin orden específico
- Los elementos deben ser inmutables (no listas ni diccionarios)

Python tiene el tipo 'set' incorporado que usaremos para entender
los conceptos antes de implementar nuestra propia estructura.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. Crear conjuntos
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("1. Crear conjuntos")
print("=" * 60)

# Con llaves {}
frutas = {"manzana", "naranja", "pera"}
print(f"Frutas: {frutas}")

# Con set() a partir de una lista
numeros = set([1, 2, 3, 2, 1, 4])  # Duplicados se eliminan
print(f"Números (sin duplicados): {numeros}")

# Conjunto vacío (NO usar {}, eso es diccionario vacío)
vacio = set()
print(f"Conjunto vacío: {vacio}")
print(f"Tipo de {{}}: {type({})}")  # dict
print(f"Tipo de set(): {type(set())}")  # set


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Características de los conjuntos
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("2. Características")
print("=" * 60)

# No hay duplicados
letras = set("mississippi")
print(f"set('mississippi'): {letras}")  # Solo m, i, s, p

# No hay orden garantizado
numeros = {5, 2, 8, 1, 9}
print(f"Conjunto: {numeros}")  # El orden puede variar

# Cardinalidad (tamaño)
print(f"Cardinalidad: {len(numeros)}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Pertenencia (membership)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("3. Pertenencia")
print("=" * 60)

colores = {"rojo", "verde", "azul"}

# Verificar si un elemento está en el conjunto
print(f"'rojo' in colores: {'rojo' in colores}")      # True
print(f"'amarillo' in colores: {'amarillo' in colores}")  # False
print(f"'rojo' not in colores: {'rojo' not in colores}")  # False


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Agregar y eliminar elementos
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. Agregar y eliminar")
print("=" * 60)

animales = {"perro", "gato"}
print(f"Original: {animales}")

# Agregar un elemento
animales.add("pájaro")
print(f"Después de add('pájaro'): {animales}")

# Agregar duplicado (no hace nada)
animales.add("perro")
print(f"Después de add('perro'): {animales}")  # Sin cambio

# Eliminar elemento (error si no existe)
animales.remove("gato")
print(f"Después de remove('gato'): {animales}")

# Eliminar elemento (sin error si no existe)
animales.discard("elefante")  # No lanza error
print(f"Después de discard('elefante'): {animales}")

# Eliminar y retornar elemento arbitrario
elemento = animales.pop()
print(f"pop() retornó: {elemento}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Iterar sobre un conjunto
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("5. Iterar")
print("=" * 60)

numeros = {10, 20, 30, 40, 50}

print("Elementos del conjunto:")
for num in numeros:
    print(f"  - {num}")

# Convertir a lista si necesitas orden
lista_ordenada = sorted(numeros)
print(f"Ordenados: {lista_ordenada}")
