H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

candidate = []
max_n = -1
# 横方向に見る
for i in range(H):
    cnt_dot = 0
    cnt_o = 0
    for j in range(W):
        if S[i][j] == '.':
            cnt_dot += 1
        elif S[i][j] == 'o':
            cnt_o += 1
        if S[i][j] == 'x' or j == W-1:
            if cnt_dot + cnt_o >= K:
                max_n = max(max_n, cnt_o)
            cnt_dot = 0
            cnt_o = 0

# 縦方向に見る
for j in range(W):
    cnt_dot = 0
    cnt_o = 0
    for i in range(H):
        if S[i][j] == '.':
            cnt_dot += 1
        elif S[i][j] == 'o':
            cnt_o += 1
        if S[i][j] == 'x' or i == H-1:
            if cnt_dot + cnt_o >= K:
                max_n = max(max_n, cnt_o)
            cnt_dot = 0
            cnt_o = 0

if max_n == -1:
    print(-1)
elif max_n > K:
    print(0)
else:
    print(K-max_n)
