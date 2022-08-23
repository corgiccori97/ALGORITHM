import sys

## < 시간 초과 >

# def fibo(num):
#     if num == 0: return 0
#     elif num == 1: return 1
#     else:
#         return fibo(num - 1) + fibo(num - 2)

n = int(sys.stdin.readline())
arr = []

for i in range(n + 1):
    if i == 0: a = 0
    elif i <= 2: a = 1
    else: a = arr[-1] + arr[-2]
    arr.append(a)

print(arr[-1])