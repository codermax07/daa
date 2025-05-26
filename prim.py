import heapq

def prims(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * n
    min_heap = [(0, 0)]  # cost, vertex
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return total_cost

n, m = map(int, input("Enter vertices and edges: ").split())
edges = [tuple(map(int, input("Enter u v w: ").split())) for _ in range(m)]

print("MST Cost:", prims(n, edges))
