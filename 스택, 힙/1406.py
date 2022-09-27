# 시간초과: append() : O(1), pop() : O(1), insert() : O(N) 
# append와 pop을 쓰는 방향으로 가야됨

# import sys

# before = list(sys.stdin.readline())
# before.pop()
# after = before.copy()

# M = int(sys.stdin.readline())
# arr = []
# for _ in range(M):
#     arr.append(sys.stdin.readline().split())

# current = len(before)
# for a in arr:
#     if a[0] == 'L' and current != 0:
#         current -= 1
#     elif a[0] == 'D' and current != len(after):
#         current += 1
#     elif a[0] == 'B' and current != 0:
#         after.remove(after[current - 1])
#         current -= 1
#     elif a[0] == 'P':
#         after.insert(current, a[1])
#         current += 1

# print(''.join(after))

# 다른 사람 코드
# 커서를 기준으로 스택을 두 개 만들어서 푸는 방법..(ㅁㅊ다)

import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = []

for _ in range(int(sys.stdin.readline())):
    arr = list(sys.stdin.readline().split())
    if arr[0] == 'L' and len(s1) != 0:
        s2.append(s1.pop())
    elif arr[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif arr[0] == 'B' and len(s1) != 0:
        s1.pop()
    elif arr[0] == 'P':
        s1.append(arr[1])

s1.extend(reversed(s2))
print(''.join(s1))

        