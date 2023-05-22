import numpy as np
MAX = np.inf
ans = MAX
N, M = map(int, input().split())

# a < b としても一般性を失わない
for a in range(1, N+1):
    b = (M+a-1)//a
    if b <= N:
        ans = min(ans, a*b)
        if a > b:
            break
if ans == MAX:
    print(-1)
else:
    print(ans)