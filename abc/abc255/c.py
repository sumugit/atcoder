x, a, d, n = map(int, input().split())

# 反転処理 (上手い)
if d < 0:
    a = a + d * (n - 1)
    d = -1 * d

min_n = a
max_n = a + d*(n - 1)


if x <= min_n:
    num = min_n - x
    print(num)
elif max_n <= x:
    num = x - max_n
    print(num)
else:
    if d == 0:
        print(0)
    else:
        """
        r_n1 = int((x-a)/d + 1)
        r_n2 = int((x-a)/d)
        a_n1 = a + d * (r_n1 - 1)
        a_n2 = a + d * (r_n2 - 1)
        print(min(abs(a_n1 - x), abs(a_n2 - x)))
        """
        print(min((x-a)%d, d - (x-a)%d))

# 別解
# 2分探索使う.