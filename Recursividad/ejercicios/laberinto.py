def resolver_laberinto(laberinto, fila, col, camino_actual):
    villas = len(laberinto)
    columnas = len(laberinto[0])

    # 1. CASO BASE: ¿Estamos fuera de los límites o en una pared?
    if fila < 0 or fila >= villas or col < 0 or col >= columnas or laberinto[fila][col] == 1:
        return False

    # 2. CASO BASE: ¿Ya pasamos por aquí? (Para evitar bucles infinitos)
    if (fila, col) in camino_actual:
        return False

    # Guardamos la posición actual
    camino_actual.append((fila, col))

    # 3. CASO BASE: ¿Llegamos a la meta? (Marcada con 2)
    if laberinto[fila][col] == 2:
        return True

    # 4. EXPLORACIÓN (Recursión): Intentar mover en las 4 direcciones
    if (resolver_laberinto(laberinto, fila, col + 1, camino_actual) or # Derecha
        resolver_laberinto(laberinto, fila + 1, col, camino_actual) or # Abajo
        resolver_laberinto(laberinto, fila, col - 1, camino_actual) or # Izquierda
        resolver_laberinto(laberinto, fila - 1, col, camino_actual)):   # Arriba
        return True

    # 5. BACKTRACKING: Si ninguna dirección funcionó, retrocedemos
    camino_actual.pop()
    return False

# 0: Camino libre
# 1: Pared
# 2: Meta
laberinto_ejemplo = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 2]
]

camino_solucion = []
if resolver_laberinto(laberinto_ejemplo, 0, 0, camino_solucion):
    print("¡Laberinto resuelto!")
    print("Camino seguido:", camino_solucion)
    
    # Visualización
    for f in range(len(laberinto_ejemplo)):
        for c in range(len(laberinto_ejemplo[0])):
            if (f, c) == (0,0): print("S", end=" ") # Start
            elif (f, c) == (4,4): print("E", end=" ") # End
            elif (f, c) in camino_solucion: print("*", end=" ")
            elif laberinto_ejemplo[f][c] == 1: print("█", end=" ")
            else: print(".", end=" ")
        print()
else:
    print("No hay solución para este laberinto.")
