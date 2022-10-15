"""
n, x = map(int, input().split())
l= []
a = []
for i in range(n):
    l_a = list(map(int, input().split()))
    l.append(l_a[0])
    a.append(l_a[1:])

product = 1
j = 0

for i in range(n):
    product *= a[i][j]
    if product > x:
        j += 1
# end for

print(product) 
"""

import itertools

# 標準入力を受け付ける。
N, X = map(int, input().split())

# 袋の中に入っている、ボール情報を格納する。
baggages = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    baggages.append(tmp[1:])

# 参考 : https://note.nkmk.me/python-itertools-product/
product_list = itertools.product(*baggages)
ans = 0
for product in product_list:
    value = 1
    for p in product:
        if value > X:
            break
        value *= p

    if X == value:
        ans += 1

print(ans)

