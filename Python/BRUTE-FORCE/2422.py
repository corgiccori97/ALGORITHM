from itertools import combinations
import sys
icecream, donotmix = map(int, sys.stdin.readline().split())
nomixlist = []

for _ in range(donotmix):
    nomixlist.append(sys.stdin.readline())
nomixlist = [nomix.split() for nomix in nomixlist]

# 그냥 icecream(1,2,3,4,5)로 3가지의 모든 경우의 수를 만들어 놓고 삭제하는 식으로 진행하는 게 더 빠를 거 같음
l = [str(i) for i in range(1, icecream + 1)]
all_list = list(combinations(l, 3))

print(nomixlist)
print(all_list)

for all in all_list:
    chk = False
    for nomix in nomixlist:
        for no in nomix:
            all_list.remove(all)

print(all_list)
