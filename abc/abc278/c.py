from collections import Counter, deque, defaultdict

N, Q = map(int, input().split())
tab = []
fol = defaultdict(lambda:defaultdict(lambda: 0))
for i in range(Q):
    tab.append(list(map(int, input().split())))

for tab_val in tab:
    t, a, b = tab_val
    if t == 1:
        if fol[a][b] == 0:
            fol[a][b] = 1
    elif t == 2:
        if fol[a][b] == 1:
            fol[a][b] = 0
    elif t == 3:
        if fol[b][a]==1 and fol[a][b]==1:
            print('Yes')
        else:
            print('No')