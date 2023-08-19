h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

# 行と列の文字の出現回数を別々に管理するのがポイント
x = [[0] * 26 for _ in range(h)]
y = [[0] * 26 for _ in range(w)]

for i in range(h):
    for j in range(w):
        x[i][ord(c[i][j]) - ord('a')] += 1 # 行ごとに文字の出現回数をカウント
        y[j][ord(c[i][j]) - ord('a')] += 1 # 列ごとに文字の出現回数をカウント

hc, wc = h, w # 残っている行と列の数
fx = [False] * h # 削除済みの行を管理
fy = [False] * w # 削除済みの列を管理

while True:
    is_update = False
    ux = []
    uy = []

    for i in range(h):
        if fx[i]:
            continue
        for j in range(26):
            if x[i][j] == wc and wc >= 2:
                is_update = True
                ux.append((i, j)) # 削除する行と文字を記録

    for i in range(w):
        if fy[i]:
            continue
        for j in range(26):
            if y[i][j] == hc and hc >= 2:
                is_update = True
                uy.append((i, j)) # 削除する列と文字を記録

    if not is_update:
        break
    
    for i, j in ux:
        # i: 行番号, j: 文字番号
        fx[i] = True
        for k in range(w):
            y[k][j] -= 1 # 列の文字カウントから削除する文字を引く
        hc -= 1

    for i, j in uy:
        # i: 列番号, j: 文字番号
        fy[i] = True
        for k in range(h):
            x[k][j] -= 1 # 行の文字カウントから削除する文字を引く
        wc -= 1

print(hc * wc)