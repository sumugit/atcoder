from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]

b = [] # 睡眠時間
for i in range(1, N-1, 2):
    b.append(A[i+1] - A[i])
s = [0, b[0]]
for i in range(1, len(b)):
    s.append(b[i] + s[i])

for idx, _lr in enumerate(lr):
    l, r = _lr
    ans = 0
    # A の二分探索木から l 未満の最大値を探す
    a_idx_l  = bisect_left(A, l)
    if A[a_idx_l] == l:
        a_idx_l = a_idx_l + 1
    if a_idx_l%2 == 0:
        b_min_idx = a_idx_l//2
    else:
        b_min_idx = a_idx_l//2
    # A の二分探索木から r 未満の最大値を探す
    a_idx_r = bisect_left(A, r)
    if A[a_idx_r] == r:
        a_idx_r = a_idx_r + 1
    if a_idx_r%2 == 0:
        b_max_idx = a_idx_r//2
    else:
        b_max_idx = a_idx_r//2
    ans += s[b_max_idx] - s[b_min_idx]
    if a_idx_l%2 == 0:
        ans += A[a_idx_l-1+1] - l
    if a_idx_r%2 == 0:
        ans -= A[a_idx_r-1+1] - r
    print(ans)