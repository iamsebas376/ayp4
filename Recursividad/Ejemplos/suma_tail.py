import time

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

actual1 = time.time() 
print(sum_list([1, 2, 3, 4, 5]))
print("El tiempo de ejecución 1 es: ", time.time() - actual1)

def sum_list_tail(lst, total=0):
    if not lst:
        return total
    return sum_list_tail(lst[1:], total + lst[0])

actual2 = time.time() 
print(sum_list_tail([1, 2, 3, 4, 5]))
print("El tiempo de ejecución 2 es: ", time.time() - actual2)