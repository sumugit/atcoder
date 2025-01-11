N, D = map(int, input().split())
TL = [list(map(int, input().split())) for _ in range(N)]
for k in range(1, D+1):
    crit = [t*(l+k) for t,l in TL]
    print(max(crit))