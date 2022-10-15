n, r = map(int, input().split())


def prod(n: int) -> int:
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def my_conb(n: int, r: int) -> int:
    ans = int(prod(n) / (prod(n-r) * prod(r)))
    return ans

print(my_conb(n, r))