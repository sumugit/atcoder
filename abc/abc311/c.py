from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]  # 0-indexedにする

    visited = [False] * N
    cycle = []
    i = 0
    while True:
        if visited[i]:
            cycle = cycle[cycle.index(i):]  # 閉路部分だけを取り出す
            break
        else:
            visited[i] = True
            cycle.append(i)
            i = A[i]

    print(len(cycle))
    print(' '.join(map(str, [x+1 for x in cycle])))  # 1-indexedに戻して出力

solve()
