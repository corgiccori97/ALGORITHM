import sys
input = sys.stdin.readline


def dfs(v, depth):
    global count

    if depth == 2:
        return
    
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            count += 1
        dfs(i, depth + 1)

    return count


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
print(len(list(filter(lambda x: x == True, visited))) - 1)
