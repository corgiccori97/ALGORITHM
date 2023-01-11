import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if (0 <= rx < m) and (0 <= ry < n):
            if graph[ry][rx] == 1:
                graph[ry][rx] = 0
                dfs(rx, ry)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    answer = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                answer += 1

    print(answer)