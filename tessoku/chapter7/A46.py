import math
import random
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
XY_copy = XY[:]

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def calc_dist(lst):
    ans = 0
    for i in range(N-1):
        x1, y1 = XY[lst[i]]
        x2, y2 = XY[lst[i+1]]
        ans += dist(x1, y1, x2, y2)
    return ans

# Phase 1
ans = []
x1, y1 = XY[0]
ans.append(0)
XY_copy[0] = None
while len(ans) < N:
    min_dist = 10**9
    min_idx = -1
    next_x, next_y = -1, -1
    for idx, xy in enumerate(XY_copy):
        if xy is None:
            continue
        x2, y2 = xy
        tmp = dist(x1, y1, x2, y2)
        if tmp < min_dist:
            min_dist = tmp
            min_idx = idx
            next_x, next_y = x2, y2
    ans.append(min_idx)
    XY_copy[min_idx] = None
    x1, y1 = next_x, next_y
ans.append(0)

# Phase 2 and 3
score = calc_dist(ans)
# print(score)
T = 30
for i in range(1, 400001):
    if i == 50000:
        T = 23
    elif i == 100000:
        T = 16
    elif i == 150000:
        T = 0.2
    l = random.randint(1, N-2)
    r = random.randint(l+1, N-1)
    # [l, r] の区間を反転
    ans_tmp = ans[:]
    ans_tmp[l:r+1] = ans_tmp[l:r+1][::-1]
    score_tmp = calc_dist(ans_tmp)
    if score_tmp < score:
        ans = ans_tmp
        score = score_tmp
    else:
        # 焼きなまし法
        prob = math.exp(-abs(score_tmp - score) / T)
        if random.random() < prob:
            ans = ans_tmp
            score = score_tmp

# print(score)

for a in ans:
    print(a+1)

