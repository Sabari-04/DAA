def sum_of_subsets(nums, target):
    nums.sort()
    stack = [(0, [], 0)]
    result = []
    while stack:
        start, path, current_sum = stack.pop()
        if current_sum == target:
            result.append(path)
        for i in range(start, len(nums)):
            if current_sum + nums[i] <= target:
                stack.append((i + 1, path + [nums[i]], current_sum + nums[i]))
    return result
nums = [2, 3, 7, 8, 10]
target = 10
print(sum_of_subsets(nums, target))
