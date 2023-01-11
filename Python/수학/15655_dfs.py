# 출력 초과

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

visited = [False] * (max(arr) + 1)
result = []

def dfs(depth, idx):
    if depth == m:
        print(' '.join(result))
        return
    else:
        for i in range(idx, len(arr)):
            if not visited[i]:
                visited[i] = True
                result.append(str(arr[i]))
                dfs(depth + 1, idx + 1)
                visited[i] = False
                result.pop()

dfs(0, 0)