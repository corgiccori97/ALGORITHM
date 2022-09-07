import sys

N = int(sys.stdin.readline())
sum = 0
num = 1

while sum != N:
    if sum > N:
        num -= 1
        break
    sum += num
    num += 1

print(num - 1)
