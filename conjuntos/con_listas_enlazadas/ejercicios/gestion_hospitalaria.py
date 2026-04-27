import sys
import os

# Añadir el camino para importar ConjuntoEnlazado si es necesario
# (Asumiendo que el estudiante copiará el código o importará desde el archivo de ejemplo)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejemplos')))
from conjunto_lista_enlazada import ConjuntoEnlazado

"""
EJERCICIO DE SIMULACRO DE EXAMEN: Gestión de Hospital

El hospital 'Salud Total' desea automatizar la gestión de pacientes en sus áreas.
Se tienen dos áreas principales:
- Urgencias
- Consulta Externa

REQUERIMIENTOS:
1. Crear dos conjuntos (basados en listas enlazadas) para almacenar los nombres de los pacientes.
2. Implementar una función 'reporte_pacientes' que reciba ambos conjuntos y muestre:
   a) Pacientes que fueron atendidos en AMBAS áreas el mismo día (Intersección).
   b) Pacientes que SOLO fueron atendidos en Urgencias (Diferencia: Urgencias - Consulta).
   c) La lista total de pacientes únicos atendidos en el hospital (Unión).
3. Verificar si un paciente específico (ej. 'Pedro') fue atendido en cualquier área.
"""

def ejercicio_hospital():
    # 1. Inicialización
    urgencias = ConjuntoEnlazado()
    consulta = ConjuntoEnlazado()

    # Pacientes en Urgencias
    pacientes_urg = ["Maria", "Juan", "Lucas", "Elena", "Pedro"]
    for p in pacientes_urg:
        urgencias.agregar(p)

    # Pacientes en Consulta Externa
    pacientes_con = ["Ana", "Juan", "Elena", "Sofia", "Roberto"]
    for p in pacientes_con:
        consulta.agregar(p)

    print("--- REGISTRO DEL DÍA ---")
    print(f"Pacientes en Urgencias: {urgencias}")
    print(f"Pacientes en Consulta: {consulta}")

    # 2. Operaciones
    ambas_areas = urgencias.interseccion(consulta)
    solo_urgencias = urgencias.diferencia(consulta)
    total_pacientes = urgencias.union(consulta)

    print("\n--- REPORTE DE GESTIÓN ---")
    print(f"a) Pacientes en ambas áreas (Intersección): {ambas_areas}")
    print(f"b) Solo atendidos en Urgencias (Diferencia): {solo_urgencias}")
    print(f"c) Total de pacientes únicos (Unión): {total_pacientes}")

    # 3. Búsqueda específica
    paciente_a_buscar = "Pedro"
    if total_pacientes.contiene(paciente_a_buscar):
        print(f"\nResultado: El paciente {paciente_a_buscar} se encuentra en los registros.")
    else:
        print(f"\nResultado: El paciente {paciente_a_buscar} no fue atendido hoy.")

if __name__ == "__main__":
    ejercicio_hospital()
