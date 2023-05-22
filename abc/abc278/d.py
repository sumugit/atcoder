N = int(input())
A = [0] + list(map(int, input().split()))
S = [[a, 0] for a in A] # S[i][0] は query1 の値に対する差分
x = [0, 0]
Q = int(input())
query = []
for q in range(Q):
    query.append(list(map(int, input().split())))
for i in range(Q):
    if query[i][0] == 1:
        x = [query[i][1], i+1]
    elif query[i][0] == 2:
        a_i, ti= S[query[i][1]]
        xv, xt = x
        if ti < xt:
            S[query[i][1]] = [query[i][2], i+1]
        else:
            S[query[i][1]] = [S[query[i][1]][0]+query[i][2], i+1]
    elif query[i][0] == 3:
        a_i, ti= S[query[i][1]]
        xv, xt = x
        if ti < xt:
            print(xv)
        else:
            print(S[query[i][1]][0]+xv)