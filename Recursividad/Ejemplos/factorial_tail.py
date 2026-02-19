def factorial_tail(n, acumulador=1):
    if n <= 1:
        return acumulador
    return factorial_tail(n -1, n * acumulador)

print(factorial_tail(5))