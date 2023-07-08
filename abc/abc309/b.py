N = int(input())
A = [list(list(num) for num in input().split())[0] for _ in range(N)]


B = [['n']*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 0 行目
        if i == 0:
            if j == 0:
                B[i][j] = A[i+1][j]
            else:
                B[i][j] = A[i][j-1]
        # N-1 行目
        elif i == N-1:
            if j == N-1:
                B[i][j] = A[i-1][j]
            else:
                B[i][j] = A[i][j+1]
        # 0 列目
        elif j == 0:
            if i == N-1:
                B[i][j] = A[i][j+1]
            else:
                B[i][j] = A[i+1][j]
        # N-1 列目
        elif j == N-1:
            if i == 0:
                B[i][j] = A[i][j-1]
            else:
                B[i][j] = A[i-1][j]
        else:
            B[i][j] = A[i][j]

for i in range(N):
    print("".join(B[i]))