import numpy as np

N = int(input())
abc = []
for _ in range(N):
    _abc = list(map(int, input().split()))
    abc.append(_abc)
ans = -np.Inf
for i in range(N):
    a1, b1, c1 = abc[i]
    for j in range(N):
        if i==j: continue
        a2, b2, c2 = abc[j]
        if abs(a1*b2 - a2*b1) > 0:
            x = (b2*c1-b1*c2)/(a1*b2-a2*b1)
            y = (a1*c2-a2*c1)/(a1*b2-a2*b1)
            flag = True
            for k in range(N):
                ak, bk, ck = abc[k]
                if ak*x+bk*y > ck:
                    flag = False
                    break
            if flag:
                ans = max(ans, x+y)
print(ans)
