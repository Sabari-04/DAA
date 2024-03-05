n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
print(f"The largest element in the array is: {largest}")
