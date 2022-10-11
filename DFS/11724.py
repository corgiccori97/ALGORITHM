import sys
# 재귀 허용치가 넘어가면 런타임에러 일어나기 때문에 허용 범위 넓혀주기
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)
