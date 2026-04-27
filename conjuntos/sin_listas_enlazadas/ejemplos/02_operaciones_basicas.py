"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 2: OPERACIONES BÁSICAS ENTRE CONJUNTOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Operaciones fundamentales:
- Unión (∪): elementos en A o en B
- Intersección (∩): elementos en A y en B
- Diferencia (-): elementos en A que no están en B
- Diferencia simétrica (△): elementos en A o B, pero no en ambos
"""

# ═══════════════════════════════════════════════════════════════════════════════
# Conjuntos de ejemplo
# ═══════════════════════════════════════════════════════════════════════════════

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("=" * 60)
print("Conjuntos de trabajo")
print("=" * 60)
print(f"A = {A}")
print(f"B = {B}")


# ═══════════════════════════════════════════════════════════════════════════════
# 1. UNIÓN (A ∪ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("1. UNIÓN (A ∪ B)")
print("   Elementos que están en A o en B (o en ambos)")
print("=" * 60)

# Método 1: operador |
union1 = A | B
print(f"A | B = {union1}")

# Método 2: método union()
union2 = A.union(B)
print(f"A.union(B) = {union2}")

# Visualización
print("""
    ┌─────────────────────────────┐
    │    A         B              │
    │  ┌─────┬─────┬─────┐        │
    │  │ 1,2,│ 4,5 │ 6,7,│        │
    │  │  3  │     │  8  │        │
    │  └─────┴─────┴─────┘        │
    │  ←───── UNIÓN ─────→        │
    └─────────────────────────────┘
""")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. INTERSECCIÓN (A ∩ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("2. INTERSECCIÓN (A ∩ B)")
print("   Elementos que están en A y en B")
print("=" * 60)

# Método 1: operador &
interseccion1 = A & B
print(f"A & B = {interseccion1}")

# Método 2: método intersection()
interseccion2 = A.intersection(B)
print(f"A.intersection(B) = {interseccion2}")

# Visualización
print("""
    ┌─────────────────────────────┐
    │    A         B              │
    │  ┌─────┬─────┬─────┐        │
    │  │     │ 4,5 │     │        │
    │  │     │ ^^^ │     │        │
    │  └─────┴─────┴─────┘        │
    │       INTERSECCIÓN          │
    └─────────────────────────────┘
""")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. DIFERENCIA (A - B)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("3. DIFERENCIA (A - B)")
print("   Elementos en A que NO están en B")
print("=" * 60)

# Método 1: operador -
diferencia1 = A - B
print(f"A - B = {diferencia1}")

# Método 2: método difference()
diferencia2 = A.difference(B)
print(f"A.difference(B) = {diferencia2}")

# La diferencia NO es conmutativa
print(f"\nB - A = {B - A}")
print("Nota: A - B ≠ B - A")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. DIFERENCIA SIMÉTRICA (A △ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. DIFERENCIA SIMÉTRICA (A △ B)")
print("   Elementos en A o B, pero NO en ambos")
print("=" * 60)

# Método 1: operador ^
simetrica1 = A ^ B
print(f"A ^ B = {simetrica1}")

# Método 2: método symmetric_difference()
simetrica2 = A.symmetric_difference(B)
print(f"A.symmetric_difference(B) = {simetrica2}")

# Equivalencia: (A - B) ∪ (B - A)
equivalente = (A - B) | (B - A)
print(f"(A - B) | (B - A) = {equivalente}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Resumen de operadores
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("RESUMEN DE OPERADORES")
print("=" * 60)
print("""
┌────────────────────┬──────────┬─────────────────────────┐
│ Operación          │ Operador │ Método                  │
├────────────────────┼──────────┼─────────────────────────┤
│ Unión              │    |     │ .union()                │
│ Intersección       │    &     │ .intersection()         │
│ Diferencia         │    -     │ .difference()           │
│ Diferencia simét.  │    ^     │ .symmetric_difference() │
└────────────────────┴──────────┴─────────────────────────┘
""")
