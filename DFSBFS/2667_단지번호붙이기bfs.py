import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    gagu = 0

    graph[x][y] = 0
    while q:
        a, b = q.popleft()
        gagu += 1

        for i in range(4):
            nx, ny = dx[i] + a, dy[i] + b
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
    return gagu

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
        if graph[i][j] == 1:
            gagus.append(bfs(i, j))
            apt += 1

print(apt)
[print(gagu) for gagu in sorted(gagus)]