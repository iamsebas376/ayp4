def ordenamiento_seleccion(arr):
    """
    Ordenamiento por Selección (Selection Sort)
    Busca el elemento más pequeño del arreglo no ordenado y lo intercambia 
    con el primer elemento no ordenado.
    Complejidad de Tiempo: O(n^2) siempre.
    """
    n = len(arr)
    # Iteramos por todo el arreglo
    for i in range(n):
        # Encontramos el índice del elemento mínimo en la parte no ordenada
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Intercambiamos el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Bloque de prueba
if __name__ == "__main__":
    arreglo_prueba = [64, 34, 25, 12, 22, 11, 90, 45, 3]
    print("--- Ordenamiento por Selección ---")
    print(f"Arreglo original: {arreglo_prueba}")
    arreglo_ordenado = ordenamiento_seleccion(arreglo_prueba.copy())
    print(f"Arreglo ordenado: {arreglo_ordenado}")
