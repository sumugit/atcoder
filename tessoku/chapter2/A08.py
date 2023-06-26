H, W = map(int, input().split())
A = [[0] * (W+1)] + [[0] + list(map(int, input().split())) for _ in range(H)]
Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

sum_H = [[0] * (W+1) for _ in range(H+1)]
# 横方向の累積和
for i in range(1, H+1):
    for j in range(1, W+1):
        sum_H[i][j] = A[i][j] + sum_H[i][j-1]

# 縦方向の累積和
for i in range(1, H+1):
    for j in range(1, W+1):
        sum_H[i][j] += sum_H[i-1][j]


for i in range(Q):
    a, b, c, d = ABCD[i]
    # 二次元累積和の計算
    ans = sum_H[c][d] - sum_H[a-1][d] - sum_H[c][b-1] + sum_H[a-1][b-1]
    print(ans)