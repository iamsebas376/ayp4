"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 3: RELACIONES ENTRE CONJUNTOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Relaciones:
- Subconjunto (⊆): todos los elementos de A están en B
- Subconjunto propio (⊂): A ⊆ B y A ≠ B
- Superconjunto (⊇): B contiene todos los elementos de A
- Igualdad (=): A y B tienen exactamente los mismos elementos
- Disjuntos: A y B no tienen elementos en común
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. SUBCONJUNTO (A ⊆ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("1. SUBCONJUNTO (A ⊆ B)")
print("   Todos los elementos de A están en B")
print("=" * 60)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# Método 1: operador <=
print(f"A = {A}")
print(f"B = {B}")
print(f"A <= B (A es subconjunto de B): {A <= B}")  # True

# Método 2: issubset()
print(f"A.issubset(B): {A.issubset(B)}")  # True

# Un conjunto es subconjunto de sí mismo
print(f"\nA <= A: {A <= A}")  # True
print(f"A <= C: {A <= C}")  # True (son iguales)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. SUBCONJUNTO PROPIO (A ⊂ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("2. SUBCONJUNTO PROPIO (A ⊂ B)")
print("   A ⊆ B y A ≠ B (B tiene al menos un elemento más)")
print("=" * 60)

# Operador < (subconjunto propio)
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"\nA < B (A es subconjunto propio de B): {A < B}")  # True
print(f"A < C (A es subconjunto propio de C): {A < C}")  # False (son iguales)
print(f"A < A: {A < A}")  # False


# ═══════════════════════════════════════════════════════════════════════════════
# 3. SUPERCONJUNTO (A ⊇ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("3. SUPERCONJUNTO (A ⊇ B)")
print("   A contiene todos los elementos de B")
print("=" * 60)

# Operador >= o issuperset()
print(f"B >= A (B es superconjunto de A): {B >= A}")  # True
print(f"B.issuperset(A): {B.issuperset(A)}")  # True

# Superconjunto propio
print(f"B > A (B es superconjunto propio de A): {B > A}")  # True


# ═══════════════════════════════════════════════════════════════════════════════
# 4. IGUALDAD (A = B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. IGUALDAD (A = B)")
print("   A y B tienen exactamente los mismos elementos")
print("=" * 60)

X = {1, 2, 3}
Y = {3, 2, 1}  # Mismo contenido, diferente orden
Z = {1, 2, 3, 4}

print(f"X = {X}")
print(f"Y = {Y}")
print(f"Z = {Z}")
print(f"\nX == Y: {X == Y}")  # True (el orden no importa)
print(f"X == Z: {X == Z}")  # False

# Equivalencia: A == B si y solo si A ⊆ B y B ⊆ A
print(f"\n(X <= Y) and (Y <= X): {(X <= Y) and (Y <= X)}")  # True


# ═══════════════════════════════════════════════════════════════════════════════
# 5. CONJUNTOS DISJUNTOS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("5. CONJUNTOS DISJUNTOS")
print("   A y B no tienen elementos en común (A ∩ B = ∅)")
print("=" * 60)

pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}
primos = {2, 3, 5, 7}

print(f"pares = {pares}")
print(f"impares = {impares}")
print(f"primos = {primos}")

# Método isdisjoint()
print(f"\npares.isdisjoint(impares): {pares.isdisjoint(impares)}")  # True
print(f"pares.isdisjoint(primos): {pares.isdisjoint(primos)}")  # False (2 en común)
print(f"impares.isdisjoint(primos): {impares.isdisjoint(primos)}")  # False


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Resumen de operadores de relación
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("RESUMEN DE RELACIONES")
print("=" * 60)
print("""
┌─────────────────────┬──────────┬─────────────────┐
│ Relación            │ Operador │ Método          │
├─────────────────────┼──────────┼─────────────────┤
│ Subconjunto         │    <=    │ .issubset()     │
│ Subconjunto propio  │    <     │ (no hay)        │
│ Superconjunto       │    >=    │ .issuperset()   │
│ Superconjunto propio│    >     │ (no hay)        │
│ Igualdad            │    ==    │ (no hay)        │
│ Disjuntos           │   (no)   │ .isdisjoint()   │
└─────────────────────┴──────────┴─────────────────┘
""")
