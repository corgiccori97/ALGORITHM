import sys
input = sys.stdin.readline

def dfs(x, y):
    global gagu
    visited[x][y] = 1
    for nx in range(x, n + 1):
        for ny in range(y, n + 1):
            if graph[nx][ny] and not visited[nx][ny]:
                dfs(nx, ny)
                gagu += 1
    return gagu

n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = graph.copy()
apt = 0
gagu = 0

for i in range(n):
    arr = list(input())
    for j in range(len(arr)):
        if arr[j] == '1':
            graph[i][j] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            apt += 1