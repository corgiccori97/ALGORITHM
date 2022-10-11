import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0

    graph = [[] for _ in range(len(arr) + 1)]
    visited = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        temp = arr[i]
        graph[temp].append(i + 1)
        graph[i + 1].append(temp)

    for a in arr:
        if visited[a] == 0:
            dfs(a)
            count += 1

    print(count)
