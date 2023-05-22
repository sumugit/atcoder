from itertools import combinations

N = int(input())
S = input()

def f(t):
    ft = ''
    for i in range(len(t)):
        if t[len(t)-i-1] == 'd':
            ft += 'p'
        else:
            ft += 'd'
    return ft


ans = S
for l in range(N):
    if S[l] == 'p':
        break
if l == N-1:
    if S[l] == 'p':
        print('d'*len(S))
    else:
        print(S)
else:
    for r in range(l+1, N+1):  # r=N の時, S[l:r]は l から N-1 まで
        s_new = S[:l] + f(S[l:r]) + S[r:]
        if s_new < ans:
            ans = s_new
    print(ans)

# これだと全体で O(N^3)
"""
for v in combinations(range(N), 2): # O (N^2)
    s_new = S[:v[0]] + f(S[v[0]:v[1]]) + S[v[1]:] # O(N)
    # O(N)
    if s_new < ans:
        ans = s_new
print(ans)
"""
