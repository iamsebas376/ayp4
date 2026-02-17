import time

def fibonacci(n):
    if n <= 0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)    
    
def factorial_ciclo(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
    
inicio = time.time()
print(factorial_ciclo(1000))
print(time.time() - inicio)