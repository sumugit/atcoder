N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = N*M*B
for i in range(N):
    ans += A[i]*M
for i in range(M):
    ans += C[i]*N
print(ans)