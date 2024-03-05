def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes
limit = int(input("Enter the limit: "))
print(f"Prime numbers up to {limit}:")
primes = generate_primes(limit)
for prime in primes:
    print(prime)
