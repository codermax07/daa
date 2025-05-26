import heapq

def dijkstra(n, edges, src):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float('inf')] * n
    dist[src] = 0
    min_heap = [(0, src)]

    while min_heap:
        d, u = heapq.heappop(min_heap)
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(min_heap, (dist[v], v))
    return dist

n, m = map(int, input("Enter vertices and edges: ").split())
edges = [tuple(map(int, input("Enter u v w: ").split())) for _ in range(m)]
src = int(input("Enter source vertex: "))

print("Distances:", dijkstra(n, edges, src))
