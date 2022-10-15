# 런타임에러. 왜지?
# setrecursionlimit 10000에서 10**7로 바꾸니까 해결됨 ㅠ
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    for i in graph[v]: 
        if visited[i] == 0:
            visited[i] = 1
            result.append([i, v])
            dfs(i)

n = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
result = []

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for r in sorted(result):
    print(r[1])