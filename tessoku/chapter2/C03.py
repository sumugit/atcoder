D = int(input())
X = int(input())
A = [X] + [int(input()) for i in range(1, D)]
Q = int(input())
ST = [list(map(int, input().split())) for i in range(Q)]

for i in range(len(A)-1):
    A[i+1] = A[i] + A[i+1]

for i in range(Q):
    S, T = ST[i]
    S -= 1
    T -= 1
    if A[S] > A[T]:
        print(S+1)
    elif A[S] == A[T]:
        print('Same')
    else:
        print(T+1)
