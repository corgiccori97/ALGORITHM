def triangle(num):
    arr = [1, 1, 1, 2, 2]
    if num >= len(arr):
        current = arr[0]
        i = 0
        while len(arr) != num:
            if current == arr[i]:
                arr.append(current + arr[-1])
            else:
                current = arr[i]
                arr.append(current + arr[-1])
            i += 1
    print(arr[num - 1])

N = int(input())
for _ in range(N):
    triangle(int(input()))