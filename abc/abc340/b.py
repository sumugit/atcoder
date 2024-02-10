Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

A = []
for num, val in query:
    if num == 1:
        A.append(val)
    elif num == 2:
        print(A[-val])
