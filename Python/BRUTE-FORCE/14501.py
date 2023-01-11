def sol(N, arr, money):
    while N != 0:
        max_pay_idx = arr.index(max(arr[1] for _ in arr))
        print(max_pay_idx)
        if arr[max_pay_idx][0] <= N:
            money += arr[max_pay_idx][1]
            N -= arr[max_pay_idx][0]
            del arr[max_pay_idx]
            sol(N, arr, money)
        else:
            del arr[max_pay_idx]
        print(money)
    return money

N = int(input())
money = 0
for _ in range(N):
    arr=[list(map(int, input().split()))]
print(sol(N,arr,money))


