def menor_diferencia(arr):
    n = len(arr)
    min_diff = float("inf")

    for i in range(n):
        for j in range(n+1, n):
            diff = abs(arr[i] - arr[j])
            min_diff = min(min_diff, diff)

    return min_diff