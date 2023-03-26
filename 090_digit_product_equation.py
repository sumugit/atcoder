N, B = map(int, input().split())

def product(m):
    if m == 0:
        return 0
    else:
        ans = 1
        while m != 0:
            val = m%10
            ans *= val
            m = m//10
        return ans

# 各桁の積の候補の集合を返す関数
def func(digit, m):
    if digit == 11:
        return {product(m)}
    # 次の桁を探索
    min_value = m % 10
    ret = set()
    for i in range(min_value, 10):
        r = func(digit + 1, m * 10 + i)
        for j in r:
            ret.add(j)
    return ret

# 各桁の積の候補を列挙
fm_card = func(0, 0)

# m - f(m) = B になるかどうかをチェック
Answer = 0
for fm in fm_card:
    m = fm + B
    prod_m = product(m)
    if m == prod_m + B and m <= N:
        Answer += 1
print(Answer)