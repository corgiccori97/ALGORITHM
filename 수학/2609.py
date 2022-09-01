import sys

def gcd(a, b):
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return gcd(b, remainder)


def lcm(a, b):
    return a * b // gcd(a, b)


a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print(a*b // gcd(a, b))