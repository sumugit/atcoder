N, M = map(int, input().split())
P = list(map(int, input().split()))

mod = 998244353

def fact(n):
    ans = 1
    for i in range(n):
        ans *= i+1
        ans %= mod
    return ans

def modpow(a: int, b: int, m: int, lim: int) -> int:
    """ 繰り返し二乗法 O(logb)"""
    p = a
    ans = 1
    for i in range(lim):
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

def comb_cnt(n, r):
    bunshi = fact(n)
    bunbo = fact(n - r) * fact(r)
    ans = bunshi * modpow(bunbo, mod-2, mod, 30) # モジュラ逆数
    return ans

def index(a, n):
    """ a^n """
    ans = 1
    for _ in range(n):
        ans *= a%mod
    return ans

ans = 0
temp = 0
# 先頭の要素から順に全ての組合せを求める
for i in range(N):
    if  M-2*i < 2:
        break
    elif P[i]-1 > i:
        ans += comb_cnt(M-2*i, 2)*index(M, N-2*(i+1)+temp)
    else:
        temp += 1
        ans += comb_cnt(M-2*i+temp, 1)*index(M, N-2*(i+1)+temp)
print(ans)