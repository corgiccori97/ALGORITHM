n, k = map(int, input().split())
cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(k) in format(h, '02') or str(k) in format(m, '02') or str(k) in format(s, '02'): 
                cnt += 1

print(cnt)