def solution(arr):
    answer = 0
    arr.sort()

    stack = []

    for i in range(len(arr)):
        while stack:
            for j in range(i + 1, len(arr) - 2):
                if sorted(str(arr[j])) == sorted(str(stack[-1])):
                    stack.append(arr[j])
                else:
                    stack.pop()
                    if len(stack) == 0: answer += 1
        stack.append(arr[i])
        print(stack, answer)

    
    return answer

solution([112, 1814, 121, 1481, 1184])