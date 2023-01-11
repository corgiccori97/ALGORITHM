import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global gagu
        gagu += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
        
n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = graph.copy()
apt = 0
gagu = 0
gagus = []

for i in range(n):
    arr = list(input())
    for j in range(len(arr)):
        if arr[j] == '1':
            graph[i][j] = 1

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            gagus.append(gagu)
            apt += 1
            gagu = 0

print(apt)
[print(gagu) for gagu in sorted(gagus)]