A, B = map(int, input().split())

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

ans = gcd(A, B)
print(ans)