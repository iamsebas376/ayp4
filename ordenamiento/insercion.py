def ordenamiento_insercion(arr):
    """
    Ordenamiento por Inserción (Insertion Sort)
    Construye el arreglo ordenado de a un elemento a la vez, tomando cada elemento
    y moviéndolo a su posición correcta en la parte del arreglo que ya está ordenada.
    Complejidad de Tiempo: O(n^2) en el peor de los casos, O(n) si ya está ordenado.
    """
    # Empezamos desde el segundo elemento (índice 1)
    for i in range(1, len(arr)):
        clave = arr[i] # El elemento actual que queremos insertar
        j = i - 1
        
        # Movemos los elementos de arr[0..i-1] que son mayores que la clave, 
        # una posición hacia adelante de su posición actual
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Colocamos la clave en su posición correcta
        arr[j + 1] = clave
    return arr

def ordenamiento_insercion_alfabetico(arr):
    """
    Ordenamiento por Inserción (Insertion Sort) adaptado para cadenas de texto.
    Ordena una lista de nombres o palabras alfabéticamente de manera case-insensitive
    (ignorando mayúsculas y minúsculas).
    """
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        
        # Movemos los elementos mayores hacia adelante, comparando en minúsculas
        while j >= 0 and clave.lower() < arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = clave
    return arr

# Bloque de prueba
if __name__ == "__main__":
    # Prueba 1: Arreglo de números
    arreglo_prueba = [64, 34, 25, 12, 22, 11, 90, 45, 3]
    print("--- 1. Ordenamiento por Inserción (Números) ---")
    print(f"Arreglo original: {arreglo_prueba}")
    arreglo_ordenado = ordenamiento_insercion(arreglo_prueba.copy())
    print(f"Arreglo ordenado: {arreglo_ordenado}\n")

    # Prueba 2: Arreglo de nombres alfabéticamente
    nombres_prueba = ["Zaragoza", "alberto", "Carlos", "ana", "Beto"]
    print("--- 2. Ordenamiento por Inserción (Nombres Alfabéticamente) ---")
    print(f"Arreglo original: {nombres_prueba}")
    nombres_ordenados = ordenamiento_insercion_alfabetico(nombres_prueba.copy())
    print(f"Arreglo ordenado: {nombres_ordenados}")
