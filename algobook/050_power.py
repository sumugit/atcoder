def modpow(a: int, b: int, m: int, lim: int) -> int:
    # 繰り返し二乗法
    p = a
    ans = 1
    for i in range(lim):
        if b & (1 << i) != 0:
            ans *= p
            ans %= m
        p *= p
        p %= m
    return ans

a, b = map(int, input().split())
mod = 1000000007
print(modpow(a, b, mod, 30))

