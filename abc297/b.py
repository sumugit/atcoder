S = input()
bs = []
rs = []
k = -1
for i, s in enumerate(S):
    if s == 'B':
        bs.append(i+1)
    elif s == 'R':
        rs.append(i+1)
    elif s == 'K':
        k = i+1
# sub1
if (sum(bs)%2 == 1) and (rs[0] <= k <= rs[1]):
    print('Yes')
else:
    print('No')