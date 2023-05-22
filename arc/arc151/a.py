N = int(input())
S = input()
T = input()

s1 = sum([int(s) for s in list(S)])
t1 = sum([int(t) for t in list(T)])
if abs(s1-t1)%2 != 0:
    print(-1)
else:
    c_idx = []
    ans = list('0'*N)
    if s1 <= t1:
        for i in range(N):
            if S[i] == '0' and T[i] == '1':
                c_idx.append(i)
    else:
        for i in range(N):
            if S[i] == '1' and T[i] == '0':
                c_idx.append(i)
    leftover = abs(s1-t1)
    j = len(c_idx)-1
    while leftover > 0:
        ans[c_idx[j]] = '1'
        j -= 1
        leftover -= 2
    print(''.join(ans))