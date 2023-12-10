H, W = map(int, input().split())
MOD = 10**9+7

def fact(n: int) -> int:
    """ 階乗 """
    ans = 1
    for i in range(1, n+1):
        ans *= i
        ans %= MOD
    return ans

def modpow(a: int, b: int, m: int, lim: int) -> int:
    """ 
    繰り返し二乗法 O(logb)
    a^b を mod で割った余りを出力
    lim : mod で割る数を2進数にした時の桁数 (10^3 ~ 2^10)
    """
    p = a
    ans = 1
    for i in range(lim):
        # bを2進数に変換して, i 桁目が 1 かどうかを判定
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

def division(a: int, b: int, m, lim: int) -> int:
    """
    a÷b mod m を返す関数
    フェルマーの小定理を使う
    """
    return (a*modpow(b, m-2, m, lim))%m

def comb(n: int, r: int) -> int:
    """ 組み合わせ """
    ans = division(fact(n), (fact(r) * fact(n-r))%MOD, MOD, 30)
    return ans

ans = comb(H+W-2, H-1)
print(ans)
