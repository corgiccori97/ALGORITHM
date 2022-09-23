import sys

N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
A = 1
for a in arr1:
    A *= a

M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
B = 1
for b in arr2:
    B *= b

if len(arr1) == 1:
    print(arr1[0])
elif len(arr2) == 1:
    print(arr2[0])
else:
    