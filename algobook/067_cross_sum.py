import numpy as np
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

h_sum = [sum(h_lst) for h_lst in A]
w_sum = [sum(w_lst) for w_lst in np.array(A).T.tolist()]
B = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j] = h_sum[i] + w_sum[j] - A[i][j]
    print(*B[i])
