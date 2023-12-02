N, Q = map(int, input().split())
P = [list(input()) for _ in range(N)]
precalc = [[0 for i in range(1010)] for _ in range(1010)]

def g(h, w):
    if h <= N and w <= N:
        return precalc[h][w]
    hq, hr = h // N, h % N
    wq, wr = w // N, w % N
    ret = 0
    ret += g(N, N) * hq * wq # (A) の面積
    ret += g(N, wr) * hq # (B) の面積
    ret += g(hr, N) * wq # (C) の面積
    ret += g(hr, wr) # (D) の面積
    return ret

def f(a, b, c, d):
    return g(c, d) - g(a, d) - g(c, b) + g(a, b)

# リスト範囲外参照を防ぐためにダミーの要素を追加
for i in range(1, N+1):
    for j in range(1, N+1):
        # precalc[i][j] = (i, j) までの長方形領域に含まれる黒マスの数
        # 図を書いてみるとわかりやすい
        precalc[i][j] += precalc[i-1][j] + precalc[i][j-1] - precalc[i-1][j-1]
        if P[i-1][j-1] == 'B':
            precalc[i][j] += 1

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(f(a, b, c+1, d+1)) # c+1, d+1 に注意!