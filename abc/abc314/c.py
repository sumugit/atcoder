from collections import Counter, deque, defaultdict

N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

dict_M = defaultdict(lambda: [])
for i in range(N):
    dict_M[C[i]].append(i)

ans_lst = ['0'] * N
for i in range(1, M+1):
    idx_lst = dict_M[i]
    for j in range(-1, len(idx_lst)-1):
        ans_lst[idx_lst[j+1]] = S[idx_lst[j]]

print(*ans_lst, sep='')