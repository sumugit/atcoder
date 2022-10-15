# PyPy3 (7.3.0)
from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

ans_cnt = 0

for tp in combinations(range(N), 5):
    ans = 0
    for idx in tp:
        ans += A[idx]
    if ans == 1000:
        ans_cnt += 1

print(ans_cnt)

