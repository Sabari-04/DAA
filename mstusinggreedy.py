graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 1), (3, 1)],
    2: [(0, 3), (1, 1), (3, 3)],
    3: [(1, 1), (2, 3)]
}
n = len(graph)
visited = [False] * n
mst_cost = 0
mst_edges = []
min_cost = [float('inf')] * n
min_cost[0] = 0
parent = [-1] * n
for _ in range(n):
    u = -1
    for i in range(n):
        if not visited[i] and (u == -1 or min_cost[i] < min_cost[u]):
            u = i
    visited[u] = True
    mst_cost += min_cost[u]
    for v, cost in graph[u]:
        if not visited[v] and cost < min_cost[v]:
            min_cost[v] = cost
            parent[v] = u
for i in range(1, n):
    mst_edges.append((parent[i], i))
print("Minimum Spanning Tree Cost:", mst_cost)
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)
