def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
input = int(input("Enter a number: "))
result = sum_of_digits(input)
print("Sum of digits (single digit):", result)
