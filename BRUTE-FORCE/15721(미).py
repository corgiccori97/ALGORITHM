people = int(input())
target_cnt = int(input())
bundaegi = int(input())

arr = [0, 1, 0, 1, 0, 0, 1, 1]
arr = arr*((people * target_cnt // 8)+1)
cnt = 0
plus = 0

for a in arr:
    if bundaegi == a:
        cnt += 1
    if target_cnt == cnt:
        if plus <= people:
            print(plus)
        else:
            print(plus % people)
        break
    plus += 1
