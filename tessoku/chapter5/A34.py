N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
NUM = 100009
grundy = [0] * NUM

for i in range(100000+1):
    # grundy[i]の値の候補
    trainsit = [False, False, False]
    if i >= X:
        trainsit[grundy[i-X]] = True
    if i >= Y:
        trainsit[grundy[i-Y]] = True
    if trainsit[0] == False:
        grundy[i] = 0
    elif trainsit[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

A_grundy = [grundy[A[i]] for i in range(N)]
nim_sum = 0
for i in range(N):
    nim_sum ^= A_grundy[i]
if nim_sum == 0:
    print('Second')
else:
    print('First')