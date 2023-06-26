D = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
imos_D = [0] * (D+1)
# いもす法
for i in range(N):
    l, r = LR[i]
    imos_D[l] += 1
    if r+1 < D+1:
        imos_D[r+1] -= 1
# 累積和
for i in range(1, D+1):
    imos_D[i] += imos_D[i-1]
    print(imos_D[i])
