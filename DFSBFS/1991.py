import sys
input = sys.stdin.readline

def dfs(v):
    visited1[v] = 1
    print(chr(v + 65), end='')
    for i in graph[v]:
        if visited1[i] == 0:
            visited1[i] = 1
            dfs(i)
        
n = int(input())
graph = [[] * (n) for _ in range(n)]
visited1 = [0] * (n)
for i in range(n):
    arr = list(map(lambda x:x - 65 if x - 65 >= 0 else '', list(map(ord, input().split()))))
    for i in range(1, 3):
        if arr[i] != '':
            graph[arr[0]].append(arr[i])
            graph[arr[i]].append(arr[0])
print(graph)
dfs(0)
print()