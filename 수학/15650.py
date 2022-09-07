import sys

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n + 1)]
result = []

def dfs(depth, idx, n, m):
    if depth == m:
        return
    else:
        for i in range(1, n + 1):

            dfs(depth + 1, idx + 1, n, m)


dfs(0, 0, n, m)