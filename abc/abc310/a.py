N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

min_d = min(D)
cr1 = min_d + Q
ans = min(P, cr1)
print(ans)