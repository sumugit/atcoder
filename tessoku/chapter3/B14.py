from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))

# ビット全探索
def Enumerate(A):
	SumList = []
	for i in range(2 ** len(A)):
		sum = 0 # 現在の合計値
		for j in range(len(A)):
			wari = (2 ** j)
			if (i // wari) % 2 == 1:
				sum += A[j]
		SumList.append(sum)
	return SumList

# 半分に分ける！
A1 = A[:N//2]
A2 = A[N//2:]

sum1 = Enumerate(A1) # O(2**(N/2)) まで減る
sum2 = Enumerate(A2)
sum1 = sorted(sum1)
sum2 = sorted(sum2)

for a1 in sum1:
    idx = bisect_left(sum2, K - a1)
    if idx < len(sum2) and a1 + sum2[idx] == K:
        print("Yes")
        exit()
print("No")