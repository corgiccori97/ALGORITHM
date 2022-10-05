# 으악또시간초과!!

# import sys

# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# result = []

# for i in range(len(arr) - 1, -1, -1):
#     if i == 0:
#         result.append(0)
#     else:
#         for j in range(i - 1, -1, -1):
#             if arr[j] > arr[i]:
#                 result.append(j + 1)
#                 break
#             if j == 0:
#                 result.append(0)

# print(*(reversed(result)))

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0] * N

for i in range(N):
    while stack:
        if stack[-1][1] > arr[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, arr[i]])

print(*answer)