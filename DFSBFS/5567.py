import sys
input = sys.stdin.readline

def dfs(v, depth):
    global count
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0 and depth <= 2:
            count += 1
            dfs(i, depth + 1)

n = int(input())
m = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
print(count)