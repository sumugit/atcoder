N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

B = [0] * M
for i in range(N):
    for j in range(M):
        B[j] += X[i][j]

for i in range(M):
    if B[i] < A[i]:
        print('No')
        exit()
print('Yes')