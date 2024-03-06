def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        return reverse_number(n // 10, rev)

number = 12345
print("Original number:", number)
print("Reverse number:", reverse_number(number))
