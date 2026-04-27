def ordenamiento_burbuja_sencillo(arr):
    """
    Ordenamiento de Burbuja (Bubble Sort) clásico.
    Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
    Complejidad de Tiempo: O(n^2) en el peor de los casos.
    """
    n = len(arr)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        
        if not intercambiado:
            break
    return arr


def ordenamiento_burbuja_diccionarios(arr, clave_diccionario):
    """
    Ordenamiento de Burbuja (Bubble Sort) adaptado para diccionarios.
    Compara elementos adyacentes usando una clave específica del diccionario 
    y los intercambia si están en el orden incorrecto.
    """
    n = len(arr)
    contador_intercambios = 0
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            # Intercambiamos si el valor de la clave en el elemento actual es mayor que en el siguiente
            if arr[j][clave_diccionario] > arr[j + 1][clave_diccionario]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
                contador_intercambios += 1
        
        if not intercambiado:
            break
    return arr, contador_intercambios


# Bloque de prueba
if __name__ == "__main__":
    # Prueba 1: Arreglo sencillo
    arreglo_prueba = [64, 34, 25, 12, 22, 11, 90, 45, 3]
    print("--- 1. Ordenamiento de Burbuja (Arreglo Sencillo) ---")
    print(f"Arreglo original: {arreglo_prueba}")
    arreglo_ordenado = ordenamiento_burbuja_sencillo(arreglo_prueba.copy())
    print(f"Arreglo ordenado: {arreglo_ordenado}\n")

    # Prueba 2: Lista de estudiantes (Diccionarios)
    estudiantes = [
        {"nombre": "Carlos", "calificacion": 85},
        {"nombre": "Ana", "calificacion": 92},
        {"nombre": "Luis", "calificacion": 78},
        {"nombre": "María", "calificacion": 95},
        {"nombre": "Pedro", "calificacion": 60}
    ]
    
    print("--- 2. Ordenamiento de Burbuja (Estudiantes por Calificación) ---")
    print("Lista original:")
    for est in estudiantes:
        print(f"  {est}")
        
    estudiantes_ordenados, num_intercambios = ordenamiento_burbuja_diccionarios(list(estudiantes), "calificacion")
    
    print("\nLista ordenada (de menor a mayor calificación):")
    for est in estudiantes_ordenados:
        print(f"  {est}")
    print(f"\nTotal de intercambios realizados: {num_intercambios}")
