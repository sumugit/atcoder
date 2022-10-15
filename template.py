import math

def isprime(n: int) -> bool:
    """ 素数判定 """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0: return False
    return True

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

def lcm(a: int, b: int) -> int:
    """ 2 数の最小公倍数 : gcd 利用 """
    gcd_num = gcd(a, b)
    return int((a*b)/gcd_num)

def lcm_multi(A: list) -> int:
    """ N (> 1) 個の最小公倍数 """
    lcm_next = lcm(A[0], A[1])
    for i in range(len(A)-2):
        lcm_next = lcm(lcm_next, A[i+2])
    return lcm_next

def eratosthenes(N: int) -> list:
    """ N 以下の素数を全て求める (エラトステネスの篩) """
    P = [True] * N
    P[0] = False
    for i in range(2, int(math.sqrt(N)+1)):
        for j in range(i+1, N+1): 
            if j%i == 0:
                P[j-1] = False
    ans = []
    for i in range(1, len(P)):
        if P[i]:
            ans.append(i+1)
    return ans

def modpow(a: int, b: int, m: int, lim: int) -> int:
    """ 
    繰り返し二乗法 O(logb)
    lim : mod で割る数を2進数にした時の桁数 (10^3 ~ 2^10)
    """
    p = a
    ans = 1
    for i in range(lim):
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

def division(a: int, b: int, m, lim) -> int:
    """
    a÷b mod m を返す関数
    フェルマーの小定理を使う
    """
    return (a*modpow(b, m-2, m, lim))%m

class UnionFind:
    """ Union Find Tree """
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n  # 根は -1*(集合のノード数)

    def find(self, x):
        """ 根を参照するまで再帰 """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """ 木の連結 """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        # 大きい集合に小さい集合を merge
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """ ノード数の取得 """
        return -self.parents[self.find(x)]

### code ###
N = int(input())
a = list(map(int, input().split()))
print(lcm_multi(a))