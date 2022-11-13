from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, M = map(int, input().split())
A = list(map(int, input().split()))

a = sorted(A)
b = [a[0]]
now_sum = a[0]
for i in range(1, len(a)):
    now_sum += a[i]
    b.append(now_sum)
u_a = list(set(a))

# 数字の連続が途切れる手前 index を抽出
split_idx = []
cnt_start = -1
now = a[0]
for i in range(1, len(a)):
    if a[i] >= M:
        split_idx.append(i-1)
        cnt_start = i
        break
    if a[i] != now + 1 and a[i] != now:
        split_idx.append(i-1)
    if i == len(a) - 1:
        split_idx.append(i)
    now = a[i]
if len(split_idx) == 0:
    split_idx.append(0)

# a[i] < M の時
ans_list1 = [b[split_idx[0]]]
for i in range(1, len(split_idx)):
    ans_list1.append(b[split_idx[i]] - b[split_idx[i-1]])
if a[split_idx[-1]] == M-1 and a[0] == 0 and max(ans_list1) != b[-1]:
    ans_list1.append(ans_list1[0] + ans_list1[-1])

# a[i] >= M の時
ans_list2 = []
if cnt_start >= 0:
    a_dict = defaultdict(lambda: 0)
    for val in a[cnt_start:]:
        a_dict[val] += 1
    for key, val in a_dict.items():
        ans_list2.append(key*val)

# print(a)
# print(split_idx)
# print(ans_list1)
# print(ans_list2)
ans = max(ans_list1+ans_list2)
print(b[-1]-ans)