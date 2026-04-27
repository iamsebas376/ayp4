def ordenamiento_mezcla(arr):
    """
    Ordenamiento por Mezcla (Merge Sort)
    Algoritmo divide y vencerás. Divide el arreglo a la mitad, ordena ambas mitades
    de forma recursiva y luego las mezcla.
    Complejidad de Tiempo: O(n log n) siempre.
    """
    # Caso base: si el arreglo tiene 1 o 0 elementos, ya está ordenado
    if len(arr) > 1:
        # Encontramos el punto medio del arreglo
        medio = len(arr) // 2
        
        # Dividimos el arreglo en dos mitades
        izquierda = arr[:medio]
        derecha = arr[medio:]

        # Llamada recursiva para ordenar ambas mitades
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # Índices para iterar sobre la mitad izquierda (i), derecha (j) y el arreglo principal (k)
        i = j = k = 0

        # Mezclamos ambas mitades temporalmente ordenadas en el arreglo original
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Comprobamos si quedó algún elemento en la mitad izquierda
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        # Comprobamos si quedó algún elemento en la mitad derecha
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1
            
    return arr

# Bloque de prueba
if __name__ == "__main__":
    arreglo_prueba = [64, 34, 25, 12, 22, 11, 90, 45, 3]
    print("--- Ordenamiento por Mezcla ---")
    print(f"Arreglo original: {arreglo_prueba}")
    arreglo_ordenado = ordenamiento_mezcla(arreglo_prueba.copy())
    print(f"Arreglo ordenado: {arreglo_ordenado}")
