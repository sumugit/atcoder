N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(len(A)):
    ans.append(A[i])
    if i == K-1:
        ans.append(X)
print(*ans)