import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejemplos')))
from conjunto_lista_enlazada import ConjuntoEnlazado

"""
EJERCICIO: Gestión de Aerolínea
Contexto: Una aerolínea quiere identificar sus pasajeros más leales.
Se tiene la lista de pasajeros de tres vuelos diferentes.
"""

def encontrar_fieles(vuelo1, vuelo2, vuelo3):
    # Pasajeros que estuvieron en todos los vuelos (Triple Intersección)
    # C1 ∩ C2 ∩ C3
    inter_1_2 = vuelo1.interseccion(vuelo2)
    fieles_totales = inter_1_2.interseccion(vuelo3)
    return fieles_totales

def encontrar_unicos(vuelo1, vuelo2, vuelo3):
    # Pasajeros que solo volaron en el vuelo 1 y en ningún otro
    # C1 - (C2 ∪ C3)
    otros_vuelos = vuelo2.union(vuelo3)
    solo_vuelo1 = vuelo1.diferencia(otros_vuelos)
    return solo_vuelo1

# Simulación
v1 = ConjuntoEnlazado()
v2 = ConjuntoEnlazado()
v3 = ConjuntoEnlazado()

for p in ["Juan", "Maria", "Pedro", "Ana"]: v1.agregar(p)
for p in ["Maria", "Ana", "Luis", "Carlos"]: v2.agregar(p)
for p in ["Sofia", "Maria", "Ana", "David"]: v3.agregar(p)

print(f"Vuelo 1: {v1}")
print(f"Vuelo 2: {v2}")
print(f"Vuelo 3: {v3}")

print(f"\nPasajeros frecuentes (Estuvieron en los 3): {encontrar_fieles(v1, v2, v3)}")
print(f"Pasajeros exclusivos del Vuelo 1: {encontrar_unicos(v1, v2, v3)}")
