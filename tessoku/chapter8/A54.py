Q = int(input())
query = [list(input().split()) for _ in range(Q)]

ans_dict = {}
for q in query:
    if len(q) == 3:
        _, x, y = q
        ans_dict[x] = int(y)
    else:
        _, x = q
        print(ans_dict[x])