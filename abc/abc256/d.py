import numpy as np

N = int(input())

# imos法で解いてみる.
size = 200010
lr = np.zeros(size, dtype=int)

for n in range(N):
    l, r = map(int, input().split())
    lr[l] += 1
    lr[r] -= 1

# 累積和を求める
for i in range(1, size):
    lr[i] += lr[i-1]

for i in range(1, size):
    if lr[i-1] == 0 and lr[i] != 0:
        print(i, end='')
    elif lr[i-1] != 0 and lr[i] == 0:
        print(f' {i}')
