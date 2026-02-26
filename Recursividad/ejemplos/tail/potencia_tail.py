def potencia_tail(base, exp, total=1):
    if exp == 0:
        return total
    return potencia_tail(base, exp -1, total * base)

print(potencia_tail(5))