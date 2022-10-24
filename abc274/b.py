import numpy as np
H, W = map(int, input().split())
C = []
for _ in range(H):
    ipt = list(input())
    ipt = [1 if val=='#' else 0 for val in ipt]
    C.append(ipt)
C = np.array(C)
ans = []
for w in range(W):
    ans.append(np.sum(C[:,w]))
print(*ans)
