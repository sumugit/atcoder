import numpy as np
N = int(input())
A = np.array([
    [2, 1],
    [1, 0]
])
mod = 1000000007
def matrix_power(A, n, mod, lim):
    P = A.copy()
    Q = np.zeros(shape=(2,2))
    flag = False
    for i in range(lim):
        if n & (1 << i) != 0:
            if not flag:
                Q = P.copy()
                flag = True
            else:
                Q = (Q@P)%mod
        P = (P@P)%mod
    return Q

B = matrix_power(A, N-1, mod, 60)
print((B[1,0]+B[1,1])%mod)
