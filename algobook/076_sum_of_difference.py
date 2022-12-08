N = int(input())
A = list(map(int, input().split()))

A = [0] + sorted(A, reverse=True)
ans = 0
for i in range(1, N+1):
    ans += A[i]*(N-2*i+1)
print(ans)