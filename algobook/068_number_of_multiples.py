from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def gcd(a: int, b: int) -> int:
    """ 2 数の最大公約数 : ユークリッドの互除法 """
    while a >= 1 and b >= 1:
        if a >= b:
            a = a%b
        else:
            b = b%a
    if a >= 1:
        return a
    return b

def lcm(a: int, b: int) -> int:
    """ 2 数の最小公倍数 : gcd 利用 """
    gcd_num = gcd(a, b)
    return int((a*b)/gcd_num)

def lcm_multi(A: list) -> int:
    """ N (> 1) 個の最小公倍数 """
    lcm_next = lcm(A[0], A[1])
    for i in range(len(A)-2):
        lcm_next = lcm(lcm_next, A[i+2])
    return lcm_next

N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for k in range(1, K+1):
    for v_k in combinations(V, k):
        v_k = list(v_k)
        if len(v_k) > 1:
            v_k_lsm = lcm_multi(v_k)
        else:
            v_k_lsm = v_k[0]
        ans += (-1)**(len(v_k)-1)*(N//v_k_lsm)
print(ans)
