import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejemplos')))
from conjunto_lista_enlazada import ConjuntoEnlazado, Nodo

"""
EJERCICIO PARA EL EXAMEN: Operaciones Lógicas Recursivas
Tarea: Implementar métodos para comparar dos conjuntos enlazados de manera recursiva.
"""

def es_subconjunto_recursivo(nodo_a, conjunto_b):
    """
    Verifica si todos los elementos que empiezan en nodo_a 
    están dentro del conjunto_b.
    """
    if nodo_a is None:
        return True # El conjunto vacío es subconjunto de cualquiera
    
    # Si el elemento actual NO está en b, ya no es subconjunto
    if not conjunto_b.contiene(nodo_a.dato):
        return False
        
    # Verificar recursivamente con el siguiente
    return es_subconjunto_recursivo(nodo_a.siguiente, conjunto_b)

def son_iguales_recursivo(conjunto_a, conjunto_b):
    """
    Dos conjuntos son iguales si a es subconjunto de b Y 
    tienen el mismo tamaño.
    """
    if conjunto_a.tamano != conjunto_b.tamano:
        return False
    return es_subconjunto_recursivo(conjunto_a.cabeza, conjunto_b)

def ejercicio_testing():
    C1 = ConjuntoEnlazado()
    C2 = ConjuntoEnlazado()
    C3 = ConjuntoEnlazado()

    for x in [10, 20, 30]: C1.agregar(x)
    for x in [10, 20, 30, 40]: C2.agregar(x)
    for x in [30, 10, 20]: C3.agregar(x) # El mismo que C1 pero diferente orden

    print(f"C1: {C1}")
    print(f"C2: {C2}")
    print(f"C3: {C3}")

    print("\n--- PRUEBAS LÓGICAS ---")
    print(f"¿Es C1 subconjunto de C2?: {es_subconjunto_recursivo(C1.cabeza, C2)}") # True
    print(f"¿Es C2 subconjunto de C1?: {es_subconjunto_recursivo(C2.cabeza, C1)}") # False
    print(f"¿Es C1 igual a C3?: {son_iguales_recursivo(C1, C3)}") # True

if __name__ == "__main__":
    ejercicio_testing()
