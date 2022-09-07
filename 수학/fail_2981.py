import sys

nums = []
result = []
n = int(sys.stdin.readline())
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

for i in range(2, (max(nums) + 1)):
    m = nums[0] % i
    for j in range(1, n):
        if nums[j] % i != m: 
            break
        if j == n - 1: result.append(i)

print(*result)

