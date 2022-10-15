import numpy as np
N, M = map(int, input().split())
g = np.zeros(shape=(N, N), dtype=int)
for i in range(M):
    U_i, V_i = map(int, input().split())
    g[U_i-1, V_i-1] = 1
    g[V_i-1, U_i-1] = 1

ans = 0

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if g[a, b] == 1 and g[b, c] == 1 and g[c, a] == 1:
                ans += 1

print(ans)
