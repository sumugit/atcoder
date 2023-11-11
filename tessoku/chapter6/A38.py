D, N = map(int, input().split())
LRH = [list(map(int, input().split())) for _ in range(N)]

scd = [24 for _ in range(D+1)]
for i in range(N):
    L, R, H = LRH[i]
    for j in range(L, R+1):
        scd[j] = min(scd[j], H)
ans = sum(scd[1:])
print(ans)
