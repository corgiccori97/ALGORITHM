import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(1, N+1):
    com = combinations(arr, i)
    for c in list(com):
        if sum(c) == S:
            cnt += 1

print(cnt)