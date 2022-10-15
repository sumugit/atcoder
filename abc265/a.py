X, Y, N = map(int, input().split())

if 3*X <= Y:
    ans = X * N
else:
    ans = Y * (N//3) + X * (N%3)

print(int(ans))