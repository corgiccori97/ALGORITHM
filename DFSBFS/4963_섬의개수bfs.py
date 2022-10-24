import queue
import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우, 대각)시계방향으로
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        a, b = q.popleft()

        for i in range(8):
            nx, ny = dx[i] + a, dy[i] + b
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    land = 0

    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                land += 1

    print(land)
