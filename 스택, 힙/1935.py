import sys

N = int(sys.stdin.readline())
string = list(sys.stdin.readline())
string.pop()
nums = [int(sys.stdin.readline()) for _ in range(N)]

stack = []

for s in string:
    if 'A' <= s <= 'Z':
        stack.append(nums[ord(s) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if s == '+':
            stack.append(num1 + num2)
        elif s == '-':
            stack.append(num1 - num2)
        elif s == '*':
            stack.append(num1 * num2)
        elif s == '/':
            stack.append(num1 / num2)

print('%.2f' %stack[0])