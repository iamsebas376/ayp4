def ordenamiento_rapido(arr):
    """
    Ordenamiento Rápido (Quick Sort)
    Algoritmo divide y vencerás. Selecciona un elemento 'pivote' y divide los 
    elementos restantes en dos sub-arreglos, según si son menores o mayores al pivote.
    Complejidad de Tiempo: O(n log n) en promedio, O(n^2) en el peor caso.
    """
    # Caso base: arreglos de longitud 0 o 1 ya están ordenados
    if len(arr) <= 1:
        return arr
    else:
        # Elegimos el elemento central como pivote
        pivote = arr[len(arr) // 2]
        
        # Elementos menores que el pivote
        izquierda = [x for x in arr if x < pivote]
        
        # Elementos iguales al pivote (maneja duplicados)
        medio = [x for x in arr if x == pivote]
        
        # Elementos mayores que el pivote
        derecha = [x for x in arr if x > pivote]
        
        # Unimos las partes ordenando de forma recursiva la izquierda y derecha
        return ordenamiento_rapido(izquierda) + medio + ordenamiento_rapido(derecha)

# Bloque de prueba
if __name__ == "__main__":
    arreglo_prueba = [64, 34, 25, 12, 22, 11, 90, 45, 3]
    print("--- Ordenamiento Rápido ---")
    print(f"Arreglo original: {arreglo_prueba}")
    arreglo_ordenado = ordenamiento_rapido(arreglo_prueba.copy())
    print(f"Arreglo ordenado: {arreglo_ordenado}")
