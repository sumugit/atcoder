import numpy as np

N = int(input())
p = list(map(int, input().split()))

c = np.zeros(N, dtype=int)
for n in range(N):
    c[(p[n]-n-1)%N-1] += 1
    c[(p[n]-n)%N-1] += 1
    c[(p[n]-n+1)%N-1] += 1

print(max(c))

"""
delta_p = np.zeros(N, dtype=int)
for idx, _p in enumerate(p):
    if idx < _p:
        delta_p[_p] = idx-_p
    elif idx == _p:
        delta_p[_p] = 0
    else:
        delta_p[_p] = -1*(N-idx+_p)
temp_sum = -1*sum(abs(delta_p))
ans_num = int((N-temp_sum)/N)-1
delta_p1 = delta_p + ans_num
delta_p2 = delta_p + ans_num - 1
ans1 = 0
ans2 = 0
for i in range(len(delta_p1)):
    if delta_p1[i] in [-1, 0, 1]:
        ans1 += 1
for i in range(len(delta_p2)):
    if delta_p2[i] in [-1, 0, 1]:
        ans2 += 1

ans = max(ans1, ans2)
print(ans)
"""
