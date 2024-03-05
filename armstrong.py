num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum_of_digits = 0
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** order
    temp //= 10
if sum_of_digits == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
