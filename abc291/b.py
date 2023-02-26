N = int(input())
X = list(map(int, input().split()))
X = sorted(X)

a = X[N:-N]
ans = sum(a)/len(a)
print(ans)