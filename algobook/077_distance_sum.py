N = int(input())
x = []
y = []
for _ in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)
x = [0] + sorted(x, reverse=True)
y = [0] + sorted(y, reverse=True)
ans = 0
for i in range(1, N+1):
    ans += x[i]*(N-2*i+1) + y[i]*(N-2*i+1)
print(ans)