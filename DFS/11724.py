def dfs(v, depth):
    visited[v] = 1
    for i in range(1, n + 1):
        if graph[v][i] == 0 and visited[i] == 0:
            dfs(v, depth + 1)
            count += 1

n, m = int(input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)
count = 0

dfs()