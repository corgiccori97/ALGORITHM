import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

com = int(input())
m = int(input())
graph =[[] for _ in range(com + 1)]
visited = [0] * (com + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(i)

dfs(1)
print(count)