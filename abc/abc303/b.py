N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
A_bit = [[False for i in range(N)] for _ in range(N)]
for i in range(N):
    A_bit[i][i] = True

for i in range(M):
    for j in range(1, N):
        A_bit[A[i][j-1]-1][A[i][j]-1] = True
        A_bit[A[i][j]-1][A[i][j-1]-1] = True

ans = 0
for i in range(N):
    for j in range(i, N):
        if A_bit[i][j] == False:
            ans += 1

print(ans)