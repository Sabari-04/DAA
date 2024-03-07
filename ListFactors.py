def get_factors(n, i=1, factors=[]):
    if i > n:
        return factors
    if n % i == 0:
        factors.append(i)
    return get_factors(n, i + 1, factors)
number = int(input("Enter a number: "))
result = get_factors(number)
print(f"Factors of {number}: {result}")
