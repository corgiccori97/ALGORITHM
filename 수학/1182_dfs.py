import sys

def dfs(idx, sum):
    global cnt
    if idx >= N:
        return
    sum += arr[idx]
    if sum == S:
        cnt += 1
    dfs(idx + 1, sum - arr[idx])
    dfs(idx + 1, sum)

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

dfs(0, 0)
print(cnt)

# 이해가안돼요~!!!!!!!