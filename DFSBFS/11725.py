# 런타임에러. 왜지?
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in graph[v]: 
        if visited[i] == 0:
            visited[i] = 1
            result[i] = v
            dfs(i)

n = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
result = {}

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for r in sorted(result.items()):
    print(r[1])