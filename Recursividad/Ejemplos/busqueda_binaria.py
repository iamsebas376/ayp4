def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


lista = [1, 5, 7, 12, 15]
numero = binary_search(lista, 0, 5, 12)

if numero != -1:
    print("El número está en la posición: ", str(numero))
else:
    print("El número no está en la lista")
