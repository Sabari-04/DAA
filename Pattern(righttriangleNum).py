def print_pattern(n, i=1):
    if i > n: return
    print(*range(1, i + 1))
    print_pattern(n, i + 1)
print_pattern(4)
