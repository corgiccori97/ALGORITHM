# x, y좌표가 왜 이렇게 헷갈리지 !!!
import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
graph = []
count = 0
visited = [[0] * (m) for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

bfs(0, 0)
print(visited[n - 1][m - 1] + 1)