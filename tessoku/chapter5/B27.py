A, B = map(int, input().split())

def gcd(a: int, b: int) -> int:
    """ 2 数の最大公約数 : ユークリッドの互除法 """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """ 2 数の最小公倍数 : gcd 利用 """
    return a // gcd(a, b) * b

ans = lcm(A, B)
print(ans)
