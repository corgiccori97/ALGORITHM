import sys


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return
    return True


def add_sosu(a, b):
    if is_prime(a) and is_prime(b):
        print(n, '=', a, '+', b)
        return
    elif a > b:
        print("Goldbach's conjecture is wrong.")
        return
    else:
        return add_sosu(a+1, b-1)


nums = []
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    else:
        nums.append(num)

for n in nums:
    a = 3
    b = n - a
    add_sosu(a, b)
