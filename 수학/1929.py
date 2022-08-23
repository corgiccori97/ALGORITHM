import sys

## < 시간초과 난 코드 >

# def sosu(num):
#     if num == 1:
#         return 99
#     else:
#         for i in range(2, num+1):   
#             if i == num:
#                 return 1
#             if num % i == 0:
#                 return 99


# m, n = map(int, sys.stdin.readline().split())
# for i in range(m, n+1, 1):
#     if(sosu(i) == 1):
#         print(i)

def sosu(num):
    if num == 1: return
    else:
        for n in range(2, int(num ** (1/2)) + 1):
            if num % n == 0: return
        return True
        
m, n = map(int, sys.stdin.readline().split())
for i in range(m, n+1):
    if(sosu(i)): print(i)
