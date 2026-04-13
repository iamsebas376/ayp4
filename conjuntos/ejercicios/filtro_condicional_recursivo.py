import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejemplos')))
from conjunto_lista_enlazada import ConjuntoEnlazado

"""
EJERCICIO RETO: Eliminación por Condición (Recursivo)
Tarea: Implementar una función que elimine todos los elementos 
de un conjunto enlazado que cumplan cierta condición.
Ejemplo: Eliminar todos los números pares.
"""

def filtrar_recursivo(nodo_actual, condicion_func, conjunto):
    """
    Recorre el conjunto y si un elemento cumple la condición, lo elimina.
    """
    if nodo_actual is None:
        return
    
    # Guardamos el siguiente antes de posiblemente borrar el actual
    siguiente_nodo = nodo_actual.siguiente
    
    # Si cumple la condición (ej. es par), lo eliminamos del conjunto
    if condicion_func(nodo_actual.dato):
        print(f"Eliminando: {nodo_actual.dato}")
        conjunto.eliminar(nodo_actual.dato)
    
    # Llamada recursiva
    filtrar_recursivo(siguiente_nodo, condicion_func, conjunto)

# Ejemplo de uso
def es_par(n):
    return n % 2 == 0

def ejercicio_reto():
    C = ConjuntoEnlazado()
    for i in range(1, 11): C.agregar(i) # Conjunto {1, 2, ..., 10}
    
    print(f"Conjunto original: {C}")
    
    # Filtramos para que solo queden impares
    filtrar_recursivo(C.cabeza, es_par, C)
    
    print(f"Conjunto final (solo impares): {C}")

if __name__ == "__main__":
    ejercicio_reto()
