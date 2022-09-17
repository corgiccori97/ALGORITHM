import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
temp = []

def dfs():
    if len(temp) == M:
        print(*temp)
        return
    for a in arr:
        if a not in temp:
            temp.append(a)
            dfs()
            temp.pop()


dfs()
