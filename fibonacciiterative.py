def fibonacci_iterative(n):
    if n <= 1:
        return n

    first, second = 0, 1

    for _ in range(2, n + 1):
        next = first + second
        first, second = second, next

    return second
result_iterative = fibonacci_iterative(5)
print(result_iterative)
