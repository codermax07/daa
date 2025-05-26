def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[yroot] < rank[xroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0]*n

    result = 0
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            result += w
            union(parent, rank, u, v)
    return result

n, m = map(int, input("Enter vertices and edges: ").split())
edges = [tuple(map(int, input("Enter u v w: ").split())) for _ in range(m)]

print("MST Cost:", kruskal(n, edges))
