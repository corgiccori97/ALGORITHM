import sys
from collections import deque
import copy

input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    current = graph[i][j]
    graph[i][j] = 0

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == current:
                graph[nx][ny] = 0
                q.append((nx, ny))

    return current


n = int(input())
count = 0
rg_count = 0

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

# deep copy(내부 객체들까지 새롭게 copy)
# 얕은 복사시 bfs 돌아간 후에 temp도 전부 0 되므로 미리 딥카피해놓음!
temp = copy.deepcopy(graph)

# bfs
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            bfs(i, j)
            count += 1

# 적록색약 그래프
graph = temp
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            bfs(i, j)
            rg_count += 1

print(count, rg_count)
