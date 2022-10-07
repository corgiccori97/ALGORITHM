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

zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    if n >= len(zero):
        for i in range(len(zero), n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[n], one[n])


T = int(sys.stdin.readline())
for _ in range(T):
    fibo(int(sys.stdin.readline()))