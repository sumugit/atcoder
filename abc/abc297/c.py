H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(1, W):
        if S[i][j-1] == 'T' and S[i][j] == 'T':
            S[i][j-1] = 'P'
            S[i][j] = 'C'
    print(*S[i], sep='')