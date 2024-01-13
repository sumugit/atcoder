N = int(input())
A = list(map(int, input().split()))

cnt = [0] * 100
for a in A:
    cnt[a%100] += 1

ans = 0
for i in range(100):
    for j in range(i, 100):
        if (i + j)%100 == 0:
            if i == j:
                ans += cnt[i] * (cnt[i] - 1) // 2
            else:
                ans += cnt[i] * cnt[j]
print(ans)