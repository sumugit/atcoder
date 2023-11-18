from collections import Counter, deque, defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

candidates = defaultdict(lambda: 0)
candidates[A[0]] = 1
max_candidate = A[0]
max_num = 1
print(max_candidate)
for i in range(1, M):
    candidates[A[i]] += 1
    if max_num < candidates[A[i]]:
        max_candidate = A[i]
        max_num = candidates[A[i]]
        print(max_candidate)
    elif max_num == candidates[A[i]]:
        max_candidate = min(max_candidate, A[i])
        print(max_candidate)
    else:    
        print(max_candidate)