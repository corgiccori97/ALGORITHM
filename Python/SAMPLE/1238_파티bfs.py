import sys
from collections import deque
import copy
input = sys.stdin.readline


def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if i[0] == X: return



N, M, X = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
result = copy(graph)

for _ in range(M):
    first, last, time = map(int, input().split())
    graph[first].append([last, time])

print(graph)

for i in range(1, N + 1):
    print(bfs(i))
