import sys

n, m = map(int, sys.stdin.readline().split())
v1 = 1
v2 = 1

for n in range(n, n-m, -1):
    v1 *= n

for m in range(2, m + 1):
    v2 *= m

print(v1 // v2)
