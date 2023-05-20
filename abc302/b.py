H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))

# 横にsnuke
for i in range(H):
    for j in range(W-4):
        if ''.join([S[i][j], S[i][j+1], S[i][j+2], S[i][j+3], S[i][j+4]]) == 'snuke':
            for k in range(5):
                print(i+1, j+k+1)
            exit()
        elif ''.join([S[i][j], S[i][j+1], S[i][j+2], S[i][j+3], S[i][j+4]][::-1]) == 'snuke':
            for k in range(5):
                print(i+1, j+5-k)
            exit()

# 縦にsnuke
for i in range(H-4):
    for j in range(W):
        if ''.join([S[i][j], S[i+1][j], S[i+2][j], S[i+3][j], S[i+4][j]]) == 'snuke':
            for k in range(5):
                print(i+k+1, j+1)
            exit()
        elif ''.join([S[i][j], S[i+1][j], S[i+2][j], S[i+3][j], S[i+4][j]][::-1]) == 'snuke':
            for k in range(5):
                print(i+5-k, j+1)
            exit()

# 右斜めにsnuke
for i in range(H-4):
    for j in range(W-4):
        try:
            if ''.join([S[i][j], S[i+1][j+1], S[i+2][j+2], S[i+3][j+3], S[i+4][j+4]]) == 'snuke':
                for k in range(5):
                    print(i+k+1, j+k+1)
                exit()
            elif ''.join([S[i][j], S[i+1][j+1], S[i+2][j+2], S[i+3][j+3], S[i+4][j+4]][::-1]) == 'snuke':
                for k in range(5):
                    print(i+5-k, j+5-k)
                exit()
        except:
            continue

# 左斜めにsnuke
for i in range(H-4):
    for j in range(4, W):
        try:
            if ''.join([S[i][j], S[i+1][j-1], S[i+2][j-2], S[i+3][j-3], S[i+4][j-4]]) == 'snuke':
                for k in range(5):
                    print(i+k+1, j-k+1)
                exit()
            elif ''.join([S[i][j], S[i+1][j-1], S[i+2][j-2], S[i+3][j-3], S[i+4][j-4]][::-1]) == 'snuke':
                for k in range(5):
                    print(i+5-k, j+1-k)
                exit()
        except:
            continue
