N = int(input())
mod = 1000000007

# 4^0 + 4^1 + ... + 4^N = (4^(N+1)-1)/3
"""
save = 1
ans = save
for i in range(1, N+1):
    save = (save*4)%mod
    ans = (ans+save)%mod
print(ans)
"""
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

def division(a, b, m, lim):
    """ a÷b mod m を返す関数 """
    return (a*modpow(b, m-2, m, lim))%m

bunshi = modpow(4, N+1, mod, 60)-1
ans = division(bunshi, 3, mod, 60)
print(ans)