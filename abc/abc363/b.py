N, T, P = map(int, input().split())
L = list(map(int, input().split()))

L = sorted(L, reverse=True)
ans = max(0, T-L[P-1])
print(ans)
