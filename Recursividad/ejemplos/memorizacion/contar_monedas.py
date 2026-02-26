# Algoritmo que sume las diferentes permutaciones hasta que sume el valor indicado, y retorne la combinación de monedas menor
# y la lista de monedas a usar

def contar_monedas(cantidad, monedas):
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')
    
    min_monedas = float('inf')
    
    for moneda in monedas:
        resultado = contar_monedas(cantidad - moneda, monedas)
        min_monedas = min(resultado + 1, min_monedas)
    
    return min_monedas


# Ejemplo de uso
monedas = [1, 2, 5, 25]
cantidad = 30
resultado = contar_monedas(cantidad, monedas)
print(f"Cantidad: {cantidad}, Monedas: {monedas}, Mínimo de monedas necesarias: {resultado}")

def contar_monedas_memo(cantidad, monedas, memo={}):
    if cantidad in memo:
        return memo[cantidad]
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')
    
    min_monedas = float('inf')
    
    for moneda in monedas:
        resultado = contar_monedas_memo(cantidad - moneda, monedas, memo)
        min_monedas = min(resultado + 1, min_monedas)
    
    memo[cantidad] = min_monedas
    return min_monedas

# Ejemplo de uso con memorización
monedas = [1, 2, 5, 25]
cantidad = 30
resultado = contar_monedas_memo(cantidad, monedas)
print(f"Cantidad: {cantidad}, Monedas: {monedas}, Mínimo de monedas necesarias con memorización: {resultado}")
