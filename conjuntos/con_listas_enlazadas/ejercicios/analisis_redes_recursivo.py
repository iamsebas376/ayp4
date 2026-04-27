import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejemplos')))
from conjunto_lista_enlazada import ConjuntoEnlazado, Nodo

"""
EJERCICIO: Conjuntos y Recursividad
En este ejercicio, vamos a extender la funcionalidad de nuestra clase 
ConjuntoEnlazado para realizar búsquedas de manera recursiva.

TAREA:
1. Implementar una función recursiva 'buscar_recursivo' fuera o dentro de la clase.
2. Comparar elementos de dos redes sociales para encontrar amigos comunes.
"""

def buscar_recursivo(nodo, valor):
    """
    Función recursiva para verificar si un valor existe en el conjunto.
    Caso Base: Nodo es None -> No encontrado (False).
    Caso Base: Nodo.dato == valor -> Encontrado (True).
    Caso Recursivo: Buscar en el siguiente nodo.
    """
    if nodo is None:
        return False
    if nodo.dato == valor:
        return True
    return buscar_recursivo(nodo.siguiente, valor)

def ejercicio_redes():
    # Creamos dos "círculos de amigos"
    amigos_facebook = ConjuntoEnlazado()
    amigos_instagram = ConjuntoEnlazado()

    for nombre in ["Carlos", "Marta", "Daniel", "Sofia", "Luis"]:
        amigos_facebook.agregar(nombre)
    
    for nombre in ["Sofia", "Luis", "Andres", "Camila", "Carlos"]:
        amigos_instagram.agregar(nombre)

    print("--- ANÁLISIS RECURSIVO DE AMIGOS ---")
    
    # Probando la función recursiva
    print(f"¿Está 'Marta' en Facebook? (Recursivo): {buscar_recursivo(amigos_facebook.cabeza, 'Marta')}")
    print(f"¿Está 'Andres' en Facebook? (Recursivo): {buscar_recursivo(amigos_facebook.cabeza, 'Andres')}")

    # Encontrar amigos en común usando la funcionalidad de la clase
    comunes = amigos_facebook.interseccion(amigos_instagram)
    print(f"\nAmigos que tengo en ambas redes: {comunes}")

if __name__ == "__main__":
    ejercicio_redes()
