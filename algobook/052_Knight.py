X, Y = map(int, input().split())
"""
DP だと O(XY) となり, 実行時間内に計算が終わらない.
dp = [[0]*(Y+1) for _ in range(X+1)]
dp[0][0] = 1
for i in range(X+1):
    for j in range(Y+1):
        if i >= 2 and j >= 2:
            dp[i][j] = (dp[i-1][j-2] + dp[i-2][j-1])%(10**9+7)
        elif i >= 1 and j >= 2:
            dp[i][j] = dp[i-1][j-2]%(10**9+7)
        elif i >= 2 and j >= 1:
            dp[i][j] = dp[i-2][j-1]%(10**9+7)
print(dp[X][Y])
"""

def fact(n):
    ans = 1
    for i in range(n):
        ans *= i+1
        ans %= (10**9+7)
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
    ans = bunshi * modpow(bunbo, 10**9+7-2, 10**9+7, 30) # モジュラ逆数
    return ans


if (2*Y-X)%3 != 0 or (2*X-Y)%3 != 0:
    print(0)
elif 2*Y-X < 0 or 2*X-Y < 0:
    print(0)
else:
    num = int((X+Y)/3)
    num_a = int((2*Y-X)/3)
    print(comb_cnt(num, num_a)%(10**9+7))