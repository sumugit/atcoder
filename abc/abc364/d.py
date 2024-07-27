import bisect

N, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

a.sort()

def find_kth_closest_distance(a, b, k):
    def count_within_distance(x):
        lb = bisect.bisect_left(a, b - x) # b-xに最も近いa
        ub = bisect.bisect_right(a, b + x) # b+xに最も近いa
        return (ub - lb) >= k

    ng = -1
    ok = 2 * 10**8 + 10

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if count_within_distance(mid):
            # upper を下げる
            ok = mid
        else:
            # lower を上げる
            ng = mid

    return ok

results = []
index = 0
for q in range(Q):
    b, k = queries[q]
    result = find_kth_closest_distance(a, b, k)
    results.append(result)

for res in results:
    print(res)
