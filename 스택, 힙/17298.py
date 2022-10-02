# 스택은 idx를 저장해야 한다..

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1] * N

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
