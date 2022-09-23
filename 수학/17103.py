# 시간초과(소수를 하나하나 구해서 그런가보다. 입력받은 arr의 최대값까지 소수를 미리 구해놓고 할 것)
#  import sys

# def gold(num):
#     cnt = 0
#     for i in range(2, (num // 2) + 1):
#         if sosu(i) == True and sosu(num - i) == True:
#             cnt += 1
#     print(cnt)

# def sosu(num):
#     for i in range(2, (int(num ** 1/2) + 1)):
#         if num % i == 0:
#             return
#     return True

# T = int(sys.stdin.readline())
# arr = [0] * T

# for i in range(T):
#     n = int(sys.stdin.readline())
#     arr[i] = n

# for a in arr:
#     gold(a)

# 아니 이거도 시간초과나는데..? ㅠ
import sys

T = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(T)]
all_nums = [0 for _ in range(max(arr) + 1)]
all_nums[0] = all_nums[1] = 1

for i in range(2, (int(len(all_nums) ** 1/2)) + 1):
    if all_nums[i] == 0:
        for j in range(i + i, len(all_nums), i):
            all_nums[j] = 1

for num in arr:
    cnt = 0
    for n in range(2, (num // 2) + 1):
        if all_nums[n] == 0 and all_nums[num - n] == 0:
            cnt += 1
    print(cnt)