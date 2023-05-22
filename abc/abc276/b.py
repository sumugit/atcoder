N, M = map(int, input().split())
g = {i+1: [] for i in range(N)}
for _ in range(M):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)
for i in range(N):
    d = len(g[i+1])
    ans = sorted(g[i+1])
    print(d, *ans)