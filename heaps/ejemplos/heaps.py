import heapq

def operaciones_basicas_heaps():

    # 1. Crear un heap a partir de una lista de datos
    datos = [5, 3, 8, 1, 2, 9, 4]
    print("Datos originales:", datos)
    heapq.heapify(datos)
    print("Heap creado:", datos)

    # 2. Insertar un nuevo elemento en el heap
    nuevo_elemento = 6
    heapq.heappush(datos, nuevo_elemento)
    print(f"Después de insertar {nuevo_elemento}:", datos)

    # 3. Eliminar el elemento mínimo del heap
    elemento_minimo = heapq.heappop(datos)
    print(f"Elemento mínimo eliminado: {elemento_minimo}")
    print("Heap después de eliminar el mínimo:", datos)

    # 4. Eliminar el elemento máximo del heap (esto no es directo, se necesita encontrar el máximo y luego eliminarlo)
    elemento_maximo = max(datos)
    datos.remove(elemento_maximo)
    heapq.heapify(datos)  # Reorganizar el heap después de eliminar el elemento
    print(f"Elemento máximo eliminado: {elemento_maximo}")
    print("Heap después de eliminar el máximo:", datos)

    # 5. Eliminar un elemento específico del heap (por ejemplo, el número 3)
    elemento_a_eliminar = 3
    if elemento_a_eliminar in datos:
        datos.remove(elemento_a_eliminar)
        heapq.heapify(datos)  # Reorganizar el heap después de eliminar el elemento
        print(f"Después de eliminar {elemento_a_eliminar}:", datos)
    else:
        print(f"Elemento {elemento_a_eliminar} no encontrado en el heap.")

def heaps_con_tuplas():

    # Crear un heap de tuplas (prioridad, valor)
    tareas = [(3, "Tarea A"), (1, "Tarea B"), (2, "Tarea C")]
    print("Tareas originales:", tareas)
    heapq.heapify(tareas)
    print("Heap de tareas:", tareas)

    # Insertar una nueva tarea con prioridad
    nueva_tarea = (0, "Tarea D")
    heapq.heappush(tareas, nueva_tarea)
    print(f"Después de insertar {nueva_tarea}:", tareas)

    # Eliminar la tarea con mayor prioridad (menor número)
    tarea_prioritaria = heapq.heappop(tareas)
    print(f"Tarea con mayor prioridad eliminada: {tarea_prioritaria}")
    print("Heap de tareas después de eliminar la tarea prioritaria:", tareas)

print("--- Operaciones básicas con heaps ---\n")
operaciones_basicas_heaps() 
print("\n--- Heaps con tuplas ---\n")
heaps_con_tuplas()