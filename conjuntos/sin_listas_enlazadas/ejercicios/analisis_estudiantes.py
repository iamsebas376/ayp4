"""
EJERCICIOS DE CONJUNTOS (SETS)
-----------------------------
Operaciones de pertenencia, unión, intersección y diferencia.
"""

# 1. EJERCICIO: Comparación de Estudiantes
def analizar_cursos(est_python, est_java):
    # a. Estudiantes que están en ambos cursos (Intersección)
    ambos = est_python & est_java
    
    # b. Estudiantes que solo están en Python (Diferencia)
    solo_python = est_python - est_java
    
    # c. Estudiantes que están en al menos uno de los cursos (Unión)
    todos = est_python | est_java
    
    # d. Estudiantes que solo están en uno de los dos cursos (Diferencia Simétrica)
    solo_uno = est_python ^ est_java
    
    return ambos, solo_python, todos, solo_uno

# 2. EJERCICIO: Eliminar Duplicados de una Lista preservando Orden
def eliminar_duplicados_ordenado(lista):
    visto = set()
    resultado = []
    for x in lista:
        if x not in visto:
            resultado.append(x)
            visto.add(x)
    return resultado

# 3. EJERCICIO: Verificación de Subconjuntos
def verificar_correquisitos(estudiantes_visto_calculo, estudiantes_actuales_fisica):
    """Verifica si todos los estudiantes de física ya vieron cálculo."""
    # ¿Física es un subconjunto de Cálculo?
    return estudiantes_actuales_fisica.issubset(estudiantes_visto_calculo)

if __name__ == "__main__":
    python = {"Ana", "Juan", "Pedro", "Maria"}
    java = {"Pedro", "Maria", "Carlos", "Elena"}
    
    amb, solo_py, tod, solo_un = analizar_cursos(python, java)
    print(f"Estudiantes en ambos cursos: {amb}")
    print(f"Estudiantes solo en Python: {solo_py}")
    print(f"Total de estudiantes únicos: {tod}")
    
    duplicados = [1, 2, 2, 3, 1, 4, 2]
    print(f"Lista sin duplicados ordenada: {eliminar_duplicados_ordenado(duplicados)}")
    
    calculo = {"Ana", "Juan", "Pedro", "Maria", "Luis"}
    fisica = {"Ana", "Maria"}
    print(f"¿Todos de física vieron cálculo?: {verificar_correquisitos(calculo, fisica)}")
