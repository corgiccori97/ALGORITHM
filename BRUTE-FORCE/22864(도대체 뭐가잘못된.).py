a, b, c, m = map(int, input().split())
work = 0
p = 0

if a > m:
    print(0)
else:
    for _ in range(24):
        if p + a <= m:
            work += b
            p += a
        else:
            if p - c >= 0:
                p -= c
            else:
                p = 0
print(work)
