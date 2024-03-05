def find_max_min(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    if right - left == 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
    mid = (left + right) // 2
    left_max, left_min = find_max_min(arr, left, mid)
    right_max, right_min = find_max_min(arr, mid + 1, right)
    return max(left_max, right_max), min(left_min, right_min)
arr = [3, 6, 8, 2, 10, 5]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
