import sys


def sosu(num):
    if num == 1:
        return 99
    else:
        for i in range(2, num+1):
            
            if i == num:
                return 1
            if num % i == 0:
                return 99


m, n = map(int, sys.stdin.readline().split())
for i in range(m, n+1, 1):
    if(sosu(i) == 1):
        print(i)
