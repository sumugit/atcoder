N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
XY = sorted([[x, a] for x, a in zip(X, A)], key=lambda x: x[0])
X = [xy[0] for xy in XY]
A = [xy[1] for xy in XY]

cnt = 0
if sum(A) != N or X[0] != 1:
    print(-1)
    exit()

stock = 0
for i in range(M):
    if i < M-1:
        K = X[i + 1] - X[i]
        required_rock = K-1
        stock += A[i]-1
        if stock < required_rock:
            print(-1)
            exit()
        cnt += (K - 1)*K//2
        stock -= required_rock
    else:
        K = N - X[i]
        required_rock = K
        stock += A[i]-1
        if stock < required_rock:
            print(-1)
            exit()
        cnt += (K + 1)*K//2
print(cnt)