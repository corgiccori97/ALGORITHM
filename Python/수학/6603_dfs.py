import sys

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end='')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
while True:
    s = list(map(int, sys.stdin.readline().split()))
