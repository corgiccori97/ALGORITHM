import sys
from itertools import combinations

while True:
    s = list(map(int, sys.stdin.readline().split()))
    if s[0] == 0:
        break
    com = list(combinations(s[1:], 6))
    for c in com:
        print(*c)
    print()