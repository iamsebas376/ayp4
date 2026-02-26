import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)

actual1 = time.time()
print(fibonacci(30))
print("Tiempo de ejecución 1: ", time.time() - actual1)

def fibonacci_tail(n, actual = 0, siguiente= 1):
    if n == 0:
        return actual
    else:
        return fibonacci_tail(n-1, siguiente, actual + siguiente)   

actual2 = time.time()
print(fibonacci_tail(30))
print("Tiempo de ejecución 2: ", time.time() - actual2)