N, M = map(int, input().split())
PCF = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        P_i, C_i, F_i = PCF[i][0], PCF[i][1], PCF[i][2:]
        P_j, C_j, F_j = PCF[j][0], PCF[j][1], PCF[j][2:]
        flag1, flag2, flag3 = False, False, False
        if P_i >= P_j:
            flag1 = True
        if set(F_i) <= set(F_j):
            flag2 = True
        if P_i > P_j or C_i < C_j:
            flag3 = True
        if flag1 and flag2 and flag3:
            print('Yes')
            exit()
print('No')