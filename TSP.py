import sys

def tsp(graph):
    n = len(graph)
    memo = [[-1] * (1 << n) for _ in range(n)]

    def dfs(node, visited):
        if visited == (1 << n) - 1:  # Base case: all nodes visited
            return graph[node][0]     # Return to the starting node

        if memo[node][visited] != -1:
            return memo[node][visited]

        min_dist = sys.maxsize

        for next_node in range(n):
            if not (visited & (1 << next_node)):
                dist = graph[node][next_node] + dfs(next_node, visited | (1 << next_node))
                min_dist = min(min_dist, dist)

        memo[node][visited] = min_dist
        return min_dist

    return dfs(0, 1)

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Minimum distance for TSP:", tsp(graph))
