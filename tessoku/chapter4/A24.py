from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort

N = int(input())
A = list(map(int, input().split()))
VAL = 100007
VAL2 = 500007

# 最長部分増加列 (LIS)
# dp[i]: 最後の要素が A_i である部分列のうち, 最長のものの長さ
# L[x]: 長さ x の部分増加列の最後の要素の最小値
dp = [None] * VAL
L = []
LEN = 0

for i in range(N):
    # bisect_right だと同じ値があったときに末尾+1を返すので, bisect_left を使う
    pos = bisect_left(L, A[i]) # L[:i] までは単調増加なのでソート不要 (初期値をものすごく大きな値にすれば全範囲にしてもOK)
    dp[i] = pos
    
    if dp[i] >= LEN:
        # L の末尾が更新される時
        L.append(A[i])
        LEN += 1
    else:
        L[pos] = A[i]

print(LEN)
