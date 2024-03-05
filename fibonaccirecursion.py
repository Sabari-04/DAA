n = int(input("Enter the number of terms for Fibonacci series: "))
def fibonacci_recursive(n, fib_series=[0, 1]):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif len(fib_series) == n:
        return fib_series
    else:
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fibonacci_recursive(n, fib_series)
print(f"Fibonacci series using recursive approach: {fibonacci_recursive(n)}")
