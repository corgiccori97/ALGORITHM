import sys
import statistics

num, length = map(int, sys.stdin.readline().split())

arr = []
result = []
hamming_distance = 0

for _ in range(num):
    arr.append(sys.stdin.readline())

for idx in range(length):
    # idx번째 글자 넣어두는 리스트, idx 바뀔 때마다 초기화
    find_alpha = []
    for a in arr:
        find_alpha.append(a[idx])

    # find_alpha를 정렬한 다음 max값 append
    find_alpha.sort()
    max_alpha = statistics.mode(find_alpha)
    result.append(max_alpha)

    # hamming_distance
    for chk in find_alpha:
        if result[idx] != chk:
            hamming_distance += 1

print(''.join(result))
print(hamming_distance)
