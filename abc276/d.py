N = int(input())
a = list(map(int, input().split()))

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

ans = 0
# 事前に最大公約数で割れば, 処理後はすべて 1 になる
a_gcd = gcd_multi(a)
for i in range(N):
    a[i] //= a_gcd
    while a[i]%2 == 0:
        a[i] //= 2
        ans += 1
    while a[i]%3 == 0:
        a[i] //= 3
        ans += 1
    if a[i] != 1:
        print(-1)
        exit()
print(ans)