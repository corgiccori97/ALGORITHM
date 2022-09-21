import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * N
temp = []


def dfs():
    if len(temp) == M:
        print(*temp)
        return
    same = 0
    for i in range(N):
        if not visited[i] and same != arr[i]:
            visited[i] = True
            temp.append(arr[i])
            same = arr[i]
            dfs()
            visited[i] = False
            temp.pop()


dfs()
