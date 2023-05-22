from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())
NUMBER = 10**9
# 深さ優先探索
graph = defaultdict(lambda: [])
isvalid = {}
for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    isvalid[A] = False
    isvalid[B] = False

ans = 1
isvalid[1] = True
now = 1
d = deque([now])
while True:
    flag = False
    for ld in graph[now]:
        if not isvalid[ld]:
            flag = True
            break
    if not flag:
        now = d.popleft()
        if len(d) == 0:
            break
    else:
        temp = NUMBER+1
        for key in graph[now]:
            if not isvalid[key]:
                temp = min(temp, key)
        now = temp
        isvalid[now] = True
        ans = max(ans, now)
        d.appendleft(now)
print(ans)