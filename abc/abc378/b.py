N = int(input())
qr = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
td = [list(map(int, input().split())) for _ in range(Q)]

for t, d in td:
    q, r = qr[t-1]
    ans = d + (r-d%q)%q
    print(ans)