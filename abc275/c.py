from cmath import isclose
from inspect import iscode
"""
from itertools import combinations
import math
S = [list(input()) for _ in range(9)]
sharp_list = []
for i in range(9):
    for j in range(9):
        if S[i][j]=='#':
            sharp_list.append([i,j])
# 全探索
def dist(x1, y1, x2, y2):
    # 2乗のまま使う
    return abs(x1-x2) + abs(y1-y2)
ans = 0
for v in combinations(sharp_list, 4):
    x1, y1 = v[0][0], v[0][1]
    x2, y2 = v[1][0], v[1][1]
    x3, y3 = v[2][0], v[2][1]
    x4, y4 = v[3][0], v[3][1]
    d1 = dist(x1, y1, x2, y2)
    d2 = dist(x1, y1, x3, y3)
    d3 = dist(x1, y1, x4, y4)
    if math.isclose(d1,d2):
        d4 = dist(x2, y2, x4, y4)
        if math.isclose(d2,d4):
            ans += 1
    elif math.isclose(d2,d3):
        d4 = dist(x2, y2, x4, y4)
        if math.isclose(d2,d4):
            ans += 1
print(ans)
"""
import itertools
S=[input() for _ in range(9)]
ans=0

for i1,j1,i2,j2 in itertools.product(range(9),repeat=4):
    # (i1,j1)から→↓の向きに(i2,j2)がある
    if i2>i1 and j2>=j1 and S[i1][j1]=="#" and S[i2][j2]=="#":
        di=i2-i1
        dj=j2-j1
        i3=i2+dj
        j3=j2-di
        i4=i3-di
        j4=j3-dj
        if 0<=i3<9 and 0<=j3<9 and 0<=i4<9 and 0<=j4<9 and S[i3][j3]=="#" and S[i4][j4]=="#":
            ans+=1
print(ans)
