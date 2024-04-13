from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

L, R = map(int, input().split())


def find_largest_power_of_2_leq_A(A):
    """A 以下の最大の 2 のべき乗を求める"""
    if A < 1:
        return 0, -1
    i = A.bit_length() - 1
    largest_power_of_2 = 1 << i
    return largest_power_of_2, i

S_LR = range(L, R)
ans = 0
ans_lst = []
l_m = L
while l_m  < R:
    tmp = [l_m]
    val, i = find_largest_power_of_2_leq_A(R - l_m)
    j = l_m%(val)
    while j != 0:
        i -= 1
        j = l_m%(2**i)
    l_m = (2**i) * (l_m//(2**i)+1)
    ans += 1
    tmp.append(l_m)
    ans_lst.append(tmp)

print(ans)
for l, r in ans_lst:
    print(l, r)