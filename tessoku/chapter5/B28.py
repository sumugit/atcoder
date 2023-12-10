import numpy as np

N = int(input())

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

A = np.array([[1, 1], [1, 0]])
ans = matrix_power(A, N-1, 1000000007, 60)
print(int(sum(ans[1])%1000000007))
