from collections import Counter

def elementos_mas_repetidos(vector):
    if not vector:
        return []
    
    contador = Counter(vector)
    max_frecuencia = max(contador.values())
    return [elemento for elemento, frecuencia in contador.items() if frecuencia == max_frecuencia]