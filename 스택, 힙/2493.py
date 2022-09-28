# 으악또시간초과!!

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(len(arr) - 1, -1, -1):
    if i == 0:
        result.append(0)
    else:
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                result.append(j + 1)
                break
            if j == 0:
                result.append(0)

print(*(reversed(result)))
