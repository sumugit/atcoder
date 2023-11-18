N, Q = map(int, input().split())
A = list(range(1, N+1))

flag = False
for i in range(Q):
    query = list(input().split())
    if len(query) == 3:
        q, x, y = query
        x, y = int(x), int(y)
        x -= 1
        if flag:
            x = N - x - 1
        A[x] = y
    elif len(query) == 2:
        q, x = query
        x = int(x)
        x -= 1
        if flag:
            x = N - x - 1
        print(A[x])
    else:
        flag = not flag