N = int(input())
S = [input() for _ in range(N)]

# 各行および各列における'o'の数をカウント
row_counts = [s.count('o') for s in S]
col_counts = [0] * N
for j in range(N):
    for i in range(N):
        if S[i][j] == 'o':
            col_counts[j] += 1

# 答えを計算
ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            # 同じ行および列にある他の'o'の数
            ans += (row_counts[i] - 1) * (col_counts[j] - 1)

print(ans)