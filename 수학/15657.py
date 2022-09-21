import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
temp = []


def dfs():
    if len(temp) == M:
        print(*temp)
        return
    else:
        for i in range(N):
            if len(temp) == 0 or arr[i] >= temp[-1]:
                temp.append(arr[i])
                dfs()
                temp.pop()


dfs()
