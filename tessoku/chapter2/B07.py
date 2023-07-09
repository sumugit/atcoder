T = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

imos = [0] * (T+1)
for l, r in LR:
    imos[l] += 1
    imos[r] -= 1
for i in range(T):
    imos[i+1] += imos[i]
for i in range(T):
    print(imos[i])