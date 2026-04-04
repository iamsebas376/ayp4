"""
EJERCICIOS DE HEAPS (COLAS CON PRIORIDAD)
-----------------------------------------
Uso de heapq para gestión de tareas y recursos.
"""

import heapq

# 1. EJERCICIO: Programador de Tareas Médicas (Triage)
def triage_hospital():
    """
    Simular un sistema de urgencias donde:
    - Prioridad 1: Crítico
    - Prioridad 2: Grave
    - Prioridad 3: Estable
    """
    pacientes = []
    
    # Agregar pacientes (Prioridad, Nombre)
    heapq.heappush(pacientes, (2, "Juan Pérez"))
    heapq.heappush(pacientes, (1, "Ana Gómez"))
    heapq.heappush(pacientes, (3, "Luis Sosa"))
    heapq.heappush(pacientes, (1, "Marta Ruiz"))
    
    print("Atendiendo pacientes por orden de prioridad:")
    while pacientes:
        prioridad, nombre = heapq.heappop(pacientes)
        print(f"- Atendiendo a: {nombre} (Prioridad {prioridad})")

# 2. EJERCICIO: K elementos más frecuentes
def k_frecuentes(lista, k):
    """Retorna los K elementos que más se repiten en una lista usando un heap."""
    frecuencias = {}
    for x in lista:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    
    # Creamos un heap invertido (negando la frecuencia para que sea max-heap simulado)
    heap = [(-freq, val) for val, freq in frecuencias.items()]
    heapq.heapify(heap)
    
    resultado = []
    for _ in range(k):
        if heap:
            resultado.append(heapq.heappop(heap)[1])
    return resultado

if __name__ == "__main__":
    print("--- Sistema de Triage ---")
    triage_hospital()
    
    print("\n--- K más frecuentes ---")
    datos = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print(f"2 más frecuentes en {datos}: {k_frecuentes(datos, 2)}")
