def is_perfect_number(n):
    sum_of_divisors = 1  # Start with 1 as all numbers are divisible by 1
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:
                sum_of_divisors += n // i

    return sum_of_divisors == n

def find_perfect_numbers(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

# Example usage:
start_range = 1
end_range = 10000
perfect_numbers = find_perfect_numbers(start_range, end_range)
print("Perfect numbers between", start_range, "and", end_range, ":", perfect_numbers)
