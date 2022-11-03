import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    visited[i][j] = 1

    q = deque()
    q.append((i, j))
    num_sum = graph[i][j]
    location = [(i, j)]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    count += 1
                    num_sum += graph[nx][ny]
                    location.append((nx, ny))

    for (x, y) in location:
        graph[x][y] = int(num_sum / count)

    return count


n, l, r = map(int, input().split())
graph = []
visited = [[0] * (n + 1) for _ in range(n + 1)]
answer = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if bfs(i, j) != 1:
            answer += 1

print(graph, answer)
