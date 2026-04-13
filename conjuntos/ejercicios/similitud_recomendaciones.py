"""
EJERCICIO: Sistema de Recomendación de Música
Contexto: Queremos recomendar canciones a un usuario basándonos en sus gustos
y los gustos de otros usuarios utilizando el Índice de Jaccard.

Fórmula Jaccard: (A ∩ B) / (A ∪ B)
"""

def calcular_similitud(usuario1, usuario2, gustos1, gustos2):
    # Intersección: Gustos comunes
    comunes = gustos1 & gustos2
    
    # Unión: Todos los gustos únicos de ambos
    todos = gustos1 | gustos2
    
    # Índice de Jaccard
    similitud = len(comunes) / len(todos) if len(todos) > 0 else 0
    
    print(f"Similitud entre {usuario1} y {usuario2}: {similitud:.2f}")
    
    # Recomendación: Elementos en user2 que no están en user1
    recomendaciones = gustos2 - gustos1
    if recomendaciones and similitud > 0.3: # Si son suficientemente parecidos
        print(f"  -> Recomendaciones para {usuario1}: {recomendaciones}")
    else:
        print(f"  -> No hay recomendaciones claras de este usuario.")

# Datos
ana_gustos = {"Rock", "Pop", "Jazz", "Blues"}
pedro_gustos = {"Pop", "Jazz", "Metal", "Classical"}
maria_gustos = {"Rock", "Blues", "Country", "Folk"}

print("--- ANALIZANDO RECOMENDACIONES ---")
calcular_similitud("Ana", "Pedro", ana_gustos, pedro_gustos)
calcular_similitud("Ana", "Maria", ana_gustos, maria_gustos)
