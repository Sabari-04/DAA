def min_max_sequence(nums):
    for num_list in nums:
        if not num_list:
            print("Empty list")
            continue
        min_num = min(num_list)
        max_num = max(num_list)
        min_sequence = [min_num] * len(num_list)
        max_sequence = [max_num] * len(num_list)
        print(f"Input list: {num_list}")
        print(f"Minimum value sequence: {min_sequence}")
        print(f"Maximum value sequence: {max_sequence}\n")
nums = [[3, 1, 4, 2, 5, 9]]
min_max_sequence(nums)
