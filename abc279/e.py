N, M = map(int, input().split())
A = [-1] + list(map(int, input().split()))

k_lst = [k for k in range(1, len(A)+1) if A[k]==1]
for i in range(1, M+1):
    for k in k_lst:
        if i == k:
            