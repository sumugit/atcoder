N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

# A, Bまとめて処理
max_cnt = 0
for a in range(1, 100+1):
    for b in range(1, 100+1):
        cnt = 0
        for i in range(N):
            A, B = AB[i]
            if a <= A <= a+K and b <= B <= b+K:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
