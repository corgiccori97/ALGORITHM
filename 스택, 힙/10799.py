import sys

arr = list(sys.stdin.readline())
stack = []
cnt = 0

for i in range(len(arr) - 1):
    if arr[i] == '(':
        stack.append('(')
    else:
        if arr[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)