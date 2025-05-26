def floyd_warshall(n, graph):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (INF=99999):")
graph = [list(map(int, input().split())) for _ in range(n)]

result = floyd_warshall(n, graph)
print("Shortest distances:")
for row in result:
    print(" ".join(map(str, row)))
