# 시간 초과
# def fibo(n):
#     if n == 0: 
#         result.append(0)
#         return 0
#     elif n == 1:
#         result.append(1)
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# T = int(input())
# for _ in range(T):
#     result = []
#     fibo(int(input()))
#     print(result.count(0), result.count(1))
import sys

def fibo(n):
    if n == 0:
        result.append(0)
        return 0
    elif n == 1:
        result.append(1)
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

T = int(sys.stdin.readline())
for _ in range(T):
    result = []
    fibo(int(sys.stdin.readline()))
    print(result.count(0), result.count(1))