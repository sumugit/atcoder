from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
B = sorted(list(set(A)))
# A = sorted(A)
a_dict = defaultdict(lambda: 0)
for i in range(N):
    a_dict[A[i]] += 1

b_idx = len(B)-1
k = 0
for i in range(N):
    if k > len(B)-1:
        print(0)
    else:
        print(a_dict[B[b_idx]])
        b_idx -= 1
        k += 1