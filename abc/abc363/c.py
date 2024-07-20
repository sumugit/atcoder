from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from sortedcontainers import SortedList, SortedDict, SortedSet
from itertools import accumulate, product, permutations, combinations

# 考え方もプログラムも正しい
N, K = map(int, input().split())
S = input()
memo_s = defaultdict(lambda: False)

ans = 0
for v in permutations(S):
    if memo_s[str(v)]:
        continue
    flag = True
    for i in range(len(S)-K+1):
        v_tmp = v[i:i+K]
        if v_tmp == v_tmp[::-1]:
            flag = False
            break
    if flag:
        memo_s[str(v)] = True
        ans += 1
print(ans)

