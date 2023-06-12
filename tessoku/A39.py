N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

sorted_LR = sorted(LR, key=lambda x: x[1])
ans = 0
now_time = 0
for i in range(N):
    L, R = sorted_LR[i]
    if now_time <= L:
        ans += 1
        now_time = R
print(ans)