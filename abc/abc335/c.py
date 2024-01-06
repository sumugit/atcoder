N, Q = map(int, input().split())
query = [list(input().split()) for _ in range(Q)]

stack = []

for i in range(N, 0, -1):
    stack.append([i, 0])
head = stack[-1]

for q in query:
    A, B = q
    A = int(A)
    if A == 1:
        if B == 'R':
            stack.append([head[0] + 1, head[1]])
        elif B == 'L':
            stack.append([head[0] - 1, head[1]])
        elif B == 'U':
            stack.append([head[0], head[1] + 1])
        elif B == 'D':
            stack.append([head[0], head[1] - 1])
        head = stack[-1]
    elif A == 2:
        B = int(B)
        print(stack[-B][0], stack[-B][1])