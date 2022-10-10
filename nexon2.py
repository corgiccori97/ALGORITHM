def getMaximumRemovals(order, source, target):
    # Write your code here
    answer = 0
    source = list(source)
    for o in order:
        source.remove(source[o - 1])
        print(source)
        if target in source:
            answer += 1
        else:
            break
    return answer

if __name__ == '__main__':

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    source = input()

    target = input()

    result = getMaximumRemovals(order, source, target)
