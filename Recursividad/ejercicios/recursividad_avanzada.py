"""
EJERCICIOS AVANZADOS DE RECURSIVIDAD
------------------------------------
Para practicar lógica pura sin estructuras complejas.
"""

def permutaciones(s):
    """Generar todas las permutaciones de un string."""
    if len(s) == 0: return [""]
    resultado = []
    for i in range(len(s)):
        actual = s[i]
        resto = s[:i] + s[i+1:]
        for p in permutaciones(resto):
            resultado.append(actual + p)
    return resultado

def mochila_recursiva(pesos, valores, capacidad, n):
    """Problema de la mochila (básico)."""
    if n == 0 or capacidad == 0:
        return 0
    
    # Si el peso del objeto i es mayor que la capacidad, no se incluye
    if pesos[n-1] > capacidad:
        return mochila_recursiva(pesos, valores, capacidad, n-1)
    
    # Retornar el máximo entre incluirlo o no
    incluir = valores[n-1] + mochila_recursiva(pesos, valores, capacidad - pesos[n-1], n-1)
    no_incluir = mochila_recursiva(pesos, valores, capacidad, n-1)
    return max(incluir, no_incluir)

def camino_matriz(matriz, x, y):
    """Encontrar si hay un camino de (0,0) a (n,m) con 1s."""
    if x < 0 or y < 0 or x >= len(matriz) or y >= len(matriz[0]) or matriz[x][y] == 0:
        return False
    
    if x == len(matriz) - 1 and y == len(matriz[0]) - 1:
        return True
    
    # Marcar visitado temporalmente para evitar ciclos
    temp = matriz[x][y]
    matriz[x][y] = 0
    
    hay_camino = (camino_matriz(matriz, x + 1, y) or 
                 camino_matriz(matriz, x, y + 1) or 
                 camino_matriz(matriz, x - 1, y) or 
                 camino_matriz(matriz, x, y - 1))
    
    matriz[x][y] = temp
    return hay_camino

if __name__ == "__main__":
    print(f"Permutaciones 'abc': {permutaciones('abc')}")
    
    matriz = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
    print(f"¿Hay camino en matriz?: {camino_matriz(matriz, 0, 0)}")
