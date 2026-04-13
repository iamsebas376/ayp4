# Operaciones de conjuntos

# Crear conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)

# 1. Unión - todos los elementos de ambos conjuntos
union = conjunto_a | conjunto_b
print("\nUnión (A | B):", union)

# 2. Intersección - elementos comunes
interseccion = conjunto_a & conjunto_b
print("Intersección (A & B):", interseccion)

# 3. Diferencia - elementos en A que no están en B
diferencia = conjunto_a - conjunto_b
print("Diferencia (A - B):", diferencia)

# 4. Diferencia simétrica - elementos que están en A o B pero no en ambos
diferencia_simetrica = conjunto_a ^ conjunto_b
print("Diferencia simétrica (A ^ B):", diferencia_simetrica)

# 5. Subconjunto - si A está contenido en B
es_subconjunto = conjunto_a <= conjunto_b
print("\n¿A es subconjunto de B? (A <= B):", es_subconjunto)

# 6. Superconjunto - si A contiene a B
es_superconjunto = conjunto_a >= conjunto_b
print("¿A es superconjunto de B? (A >= B):", es_superconjunto)

# 7. Conjuntos disjuntos - sin elementos en común
son_disjuntos = conjunto_a.isdisjoint(conjunto_b)
print("¿A y B son disjuntos?:", son_disjuntos)

# Métodos alternativos
print("\n--- Métodos alternativos ---")
print("Union:", conjunto_a.union(conjunto_b))
print("Intersección:", conjunto_a.intersection(conjunto_b))
print("Diferencia:", conjunto_a.difference(conjunto_b))
print("Diferencia simétrica:", conjunto_a.symmetric_difference(conjunto_b))