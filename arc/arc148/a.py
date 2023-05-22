import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

def gcd(a: int, b: int) -> int:
    """ 2 数の最大公約数 : ユークリッドの互除法 """
    while a >= 1 and b >= 1:
        if a >= b:
            a = a%b
        else:
            b = b%a
    if a >= 1:
        return a
    return b

def gcd_multi(A: list) -> int:
    """ N (> 1) 個の最大公約数 """
    gcd_next = gcd(A[0], A[1])
    for i in range(len(A)-2):
        gcd_next = gcd(gcd_next, A[i+2])
    return gcd_next

a = A%2
if len(set(a)) == 1:
    print(1)
else:
    B = np.array([abs(A[i+1]-A[i]) for i in range(len(A)-1)])
    if len(B) == 1:
        if B[0] != 1:
            print(1)
        else:
            print(2)
    else:
        B_gcd_num = gcd_multi(list(B))
        if B_gcd_num != 1:
            print(1)
        else:
            print(2)