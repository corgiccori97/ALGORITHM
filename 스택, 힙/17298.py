# 끝까지 stack에 추가하기

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1] * N

for i in range(N - 1):
    stack.append(arr[i + 1])
    while stack:
        if stack[-1] > arr[i]:
            answer[i] = stack[-1]
            break
        else:
            stack.pop()

print(*answer)
