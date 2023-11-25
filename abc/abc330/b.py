N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    if A[i] < L:
        Y = L
    elif A[i] > R:
        Y = R
    else:
        Y = A[i]
    ans.append(Y)
print(*ans)