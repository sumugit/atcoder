N, X, Y = map(int, input().split())

ans = 0

def ope1(n, num):
    global ans
    if n == 1:
        return
    else:
        ope1(n-1, num)
        ope2(n, num*X)

def ope2(n, num):
    global ans
    if n == 1:
        ans += num
    else:
        ope1(n-1, num)
        ope2(n-1, num*Y)

ope1(N, 1)
print(ans)