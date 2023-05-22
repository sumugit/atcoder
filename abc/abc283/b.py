N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = []
for _ in range(Q):
    qu = list(map(int, input().split()))
    query.append(qu)
for qu in query:
    if len(qu) == 3:
        num, k, x = qu[0], qu[1], qu[2]
        A[k-1] = x
    else:
        k = qu[1]
        print(A[k-1])