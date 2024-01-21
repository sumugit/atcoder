N = 100
A = [list(map(int, input().split())) for _ in range(N)]

XYH = []
for i in range(N):
    for j in range(N):
        pnt = A[i][j]
        judge = [False, False, False, False]
        if i-1 >= 0:
            judge[0] = True
        elif i+1 < N:
            judge[1] = True
        elif j-1 >= 0:
            judge[2] = True
        elif j+1 < N:
            judge[3] = True
        flag = True
        for k in range(4):
            if judge[k]:
                if k == 0 and A[i-1][j] != pnt-1:
                    flag = False
                elif k == 1 and A[i+1][j] != pnt-1:
                    flag = False
                elif k == 2 and A[i][j-1] != pnt-1:
                    flag = False
                elif k == 3 and A[i][j+1] != pnt-1:
                    flag = False
        if flag:
            XYH.append([j, i, pnt])                    

Q = len(XYH)
print(Q)
for i in range(Q):
    print(*XYH[i])