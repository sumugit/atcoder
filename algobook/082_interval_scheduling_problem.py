N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
lr_sorted = sorted(LR, key=lambda x : x[1])
ans = 1
start = lr_sorted[0][1]
for lr in lr_sorted[1:]:
    l, r = lr
    if start <= l:
        ans += 1
        start = r
print(ans)
