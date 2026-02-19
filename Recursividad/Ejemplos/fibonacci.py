def fibonacci_simple(n):
    if n <= 1:
        return n
    else:
        return fibonacci_simple(n-1) + fibonacci_simple(n-2)
    
print(fibonacci_simple(5))