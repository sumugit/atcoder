import numpy as np
K, N = map(int, input().split())
A = np.array([
    [1, 1],
    [1, 0]
])
C = np.array([
    [0, 3],
    [1, 0]
])
mod = 1000000007

def matrix_power(A: np.array, n: int, mod: int, lim: int) -> np.array:
    """ A^n を繰り返し二乗法で計算 """
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

if K == 2:
    B = matrix_power(A, N-1, mod, 60)
    print((2*B[1,0]+B[1,1])%mod)
elif K == 3:
    B = matrix_power(C, N-1, mod, 60)
    print((3*B[1,1])%mod)
