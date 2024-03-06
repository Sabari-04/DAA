import sys

def optimal_bst(keys, freq):
    n = len(keys)
    
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = sys.maxsize

            for r in range(i, j + 1):
                c = sum(freq[i:j+1])
                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]
                cost[i][j] = min(cost[i][j], c)

    return cost[0][n - 1]

keys = [10, 12, 20, 25]
freq = [34, 8, 50, 10]
print("Optimal Cost:", optimal_bst(keys, freq))
