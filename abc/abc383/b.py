from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

H, W, D = map(int, input().split())
S = [list(input().split()) for _ in range(H)]
S = [[char for char in inner_list[0]] for inner_list in S]

floor_mass = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            floor_mass.append([i, j])

ans = 0
for i in range(len(floor_mass)):
    for j in range(i+1, len(floor_mass)):
        cri_1 = floor_mass[i]
        cri_2 = floor_mass[j]
        ans_cri = 0
        for k in range(H):
            for l in range(W):
                if S[k][l] == '.' and (abs(k-cri_1[0]) + abs(l-cri_1[1]) <= D or abs(k-cri_2[0]) + abs(l-cri_2[1]) <= D):
                    ans_cri += 1
        ans = max(ans, ans_cri)
print(ans)