N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
    rotated = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[i][j] = A[N-1-j][i]
    flag = True
    for i in range(N):
        for j in range(N):
            if rotated[i][j] == 1 and B[i][j] == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print('Yes')
        exit()
    A = rotated.copy()
print('No')
