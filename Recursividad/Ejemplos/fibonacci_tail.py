import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)

actual1 = time.time()
print(fibonacci(30))
print("Tiempo de ejecución 1: ", time.time() - actual1)

def fibonacci_tail(n, anterior = 0, actual= 1):
    if n == 0:
        return anterior
    elif n == 1:
        return actual
    else:
        return fibonacci_tail(n-1, actual, anterior + actual)   

actual2 = time.time()
print(fibonacci_tail(30))
print("Tiempo de ejecución 2: ", time.time() - actual2)