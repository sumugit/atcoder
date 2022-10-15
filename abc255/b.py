import numpy as np

def dis(x1, y1, x2, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

n, k = map(int, input().split())
a = list(map(int, input().split()))
pos = []
for i in range(n):
    pos.append(list(map(int, input().split())))

# 結局max-min問題
max_dis_r = np.zeros(n)

for _n in range(n):
    min_dis_r = np.inf
    for _k in range(k):
        r = dis(pos[a[_k]-1][0], pos[a[_k]-1][1], pos[_n][0], pos[_n][1])
        if r < min_dis_r:
            min_dis_r = r
    max_dis_r[_n] = min_dis_r


print(max(max_dis_r))


