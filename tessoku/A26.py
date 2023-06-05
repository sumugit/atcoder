import math

Q = int(input())
# エラトステネスの篩
arrays = [True] * (3*10**5+1)
for i in range(2, int(math.sqrt(3*10**5))+1):
    if arrays[i]:
        for j in range(i*2, 3*10**5+1, i):
            arrays[j] = False
for _ in range(Q):
    X = int(input())
    if arrays[X]:
        print('Yes')
    else:
        print('No')