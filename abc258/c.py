N, Q = map(int, input().split())
S = input()
query = []
for q in range(Q):
    query.append(list(map(int, input().split())))


x_num = 0
for quy in query:
    if quy[0] == 1:
        x_num += quy[1]
    else:
        # 引き算の余り注意
        ans = ((quy[1]-1) - (x_num) + N)%N
        print(S[ans])