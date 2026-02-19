import time

def suma_lista(lst):
    if not lst:
        return 0
    return lst[0] + suma_lista(lst[1:])

actual1 = time.time() 
print(suma_lista([1, 2, 3, 4, 5]))
print("El tiempo de ejecución 1 es: ", time.time() - actual1)